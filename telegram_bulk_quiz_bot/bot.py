#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import logging
import os
import random
from pathlib import Path
from typing import List, Optional
from uuid import uuid4

from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ChatAction
from telegram.error import BadRequest, Forbidden
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    PollAnswerHandler,
    filters,
)


logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("bulk-quiz-bot")

# Support both:
# - `python3 -m telegram_bulk_quiz_bot.bot` (package/module run)
# - `python3 telegram_bulk_quiz_bot/bot.py` (file run)
try:
    from telegram_bulk_quiz_bot.parser import QuizQuestion, parse_tests_txt
except ModuleNotFoundError:
    from parser import QuizQuestion, parse_tests_txt


QUIZ_OPEN_PERIOD_SECONDS = 30

# Telegram poll limits (server-enforced)
MAX_POLL_QUESTION_LEN = 300
MAX_POLL_OPTION_LEN = 100


def _truncate(text: str, max_len: int) -> str:
    text = (text or "").strip()
    if max_len <= 0:
        return ""
    if len(text) <= max_len:
        return text
    if max_len <= 1:
        return text[:max_len]
    return text[: max_len - 1].rstrip() + "…"


def _sanitize_poll_payload(question: str, options: List[str]) -> tuple[str, List[str]]:
    q = _truncate(question, MAX_POLL_QUESTION_LEN)
    opts = [_truncate(o, MAX_POLL_OPTION_LEN) for o in (options or [])]
    return q, opts


def _shuffle_options(options: List[str], correct_index: int) -> tuple[List[str], int]:
    if not options:
        return options, 0

    if not isinstance(correct_index, int) or not (0 <= correct_index < len(options)):
        correct_index = 0

    tagged = [(opt, i == correct_index) for i, opt in enumerate(options)]
    random.shuffle(tagged)
    new_options = [t[0] for t in tagged]
    new_correct = 0
    for i, (_, is_correct) in enumerate(tagged):
        if is_correct:
            new_correct = i
            break
    return new_options, new_correct


def _tests_dir() -> Path:
    return Path(os.environ.get("TESTS_DIR", "Ma'ruza/tests_txt"))


def _known_test_names(base_dir: Path) -> set[str]:
    return {p.name for p in list_local_tests(base_dir)}


def _format_test_label(fp: Path) -> str:
    # Keep button labels compact
    label = fp.stem
    return label[:60] + ("…" if len(label) > 60 else "")


async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    base_dir = _tests_dir()
    files = list_local_tests(base_dir)
    if not files:
        await update.effective_message.reply_text(f"Testlar topilmadi: {base_dir}")
        return

    buttons = []
    row = []
    for fp in files:
        row.append(InlineKeyboardButton(_format_test_label(fp), callback_data=f"pick:{fp.name}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    await update.effective_message.reply_text(
        "Test tanlang:",
        reply_markup=InlineKeyboardMarkup(buttons),
    )


def _is_private(update: Update) -> bool:
    chat = update.effective_chat
    return bool(chat and chat.type == "private")


def _get_sessions(context: ContextTypes.DEFAULT_TYPE) -> dict:
    return context.application.bot_data.setdefault("sessions", {})


def _get_active_session_by_user(context: ContextTypes.DEFAULT_TYPE) -> dict:
    return context.application.bot_data.setdefault("active_session_by_user", {})


def _get_polls(context: ContextTypes.DEFAULT_TYPE) -> dict:
    return context.application.bot_data.setdefault("polls", {})


def _cancel_timeout_task(session: dict) -> None:
    task = session.get("timeout_task")
    if task is None:
        return
    try:
        task.cancel()
    except Exception:
        pass
    session["timeout_task"] = None


def _clear_session(context: ContextTypes.DEFAULT_TYPE, session_id: str) -> None:
    sessions = _get_sessions(context)
    session = sessions.get(session_id)
    if not session:
        return
    _cancel_timeout_task(session)
    user_id = session.get("user_id")
    if user_id is not None:
        active = _get_active_session_by_user(context)
        if active.get(user_id) == session_id:
            active.pop(user_id, None)
    sessions.pop(session_id, None)


def _start_new_session(
    context: ContextTypes.DEFAULT_TYPE,
    *,
    user_id: int,
    chat_id: int,
    title: str,
    questions: List[QuizQuestion],
) -> str:
    # Cancel any previous active session for this user
    active = _get_active_session_by_user(context)
    prev = active.get(user_id)
    if prev:
        _clear_session(context, prev)

    session_id = uuid4().hex
    sessions = _get_sessions(context)
    sessions[session_id] = {
        "user_id": user_id,
        "chat_id": chat_id,
        "title": title,
        "questions": questions,
        "i": 0,
        "answers": {},  # qn -> chosen_index | None
        "wrong": {},  # qn -> {chosen, correct}
        "current_poll_id": None,
        "current_message_id": None,
        "timeout_task": None,
        "advance_lock": asyncio.Lock(),
    }
    active[user_id] = session_id
    return session_id


async def _send_final_summary(context: ContextTypes.DEFAULT_TYPE, session_id: str) -> None:
    sessions = _get_sessions(context)
    session = sessions.get(session_id)
    if not session:
        return

    total = len(session.get("questions") or [])
    wrong = session.get("wrong") or {}
    score = total - len(wrong)

    lines = [
        f"Test yakunlandi: {session.get('title')}",
        f"Natija: {score}/{total}",
    ]
    if wrong:
        lines.append("Xatolar:")
        for qn in sorted(wrong.keys()):
            w = wrong[qn]
            lines.append(f"- {qn}) Siz: {w['chosen']} | To‘g‘ri: {w['correct']}")
    else:
        lines.append("Xato yo‘q — zo‘r!")
    lines.append("Qayta ishlash uchun /menu")

    chat_id = session.get("chat_id")
    if chat_id is not None:
        try:
            await context.bot.send_message(chat_id=chat_id, text="\n".join(lines))
        except Forbidden:
            # User blocked the bot; nothing more to do.
            _clear_session(context, session_id)
            return

    _clear_session(context, session_id)


async def _send_next_question(context: ContextTypes.DEFAULT_TYPE, session_id: str) -> None:
    sessions = _get_sessions(context)
    session = sessions.get(session_id)
    if not session:
        return

    chat_id = session.get("chat_id")
    user_id = session.get("user_id")
    questions: List[QuizQuestion] = session.get("questions") or []
    i = int(session.get("i") or 0)

    attempts = 0
    while True:
        if i >= len(questions):
            await _send_final_summary(context, session_id)
            return

        q = questions[i]

        # Shuffle answer options each time a question is sent.
        shuffled_options, shuffled_correct = _shuffle_options(q.options, q.correct_index)
        poll_question, poll_options = _sanitize_poll_payload(f"{q.n}. {q.text}", shuffled_options)

        try:
            msg = await context.bot.send_poll(
                chat_id=chat_id,
                question=poll_question,
                options=poll_options,
                type="quiz",
                correct_option_id=shuffled_correct,
                is_anonymous=False,
                allows_multiple_answers=False,
                open_period=QUIZ_OPEN_PERIOD_SECONDS,
            )
            break
        except Forbidden:
            # User blocked the bot (or removed chat). End session gracefully.
            _clear_session(context, session_id)
            return
        except BadRequest as e:
            # Usually caused by Telegram poll constraints (e.g., option length > 100).
            logger.warning("send_poll BadRequest (will skip question): %s", e)
            attempts += 1
            i += 1
            session["i"] = i
            session["current_poll_id"] = None
            session["current_message_id"] = None
            _cancel_timeout_task(session)
            try:
                await context.bot.send_message(
                    chat_id=chat_id,
                    text="Bitta savol Telegram chekloviga to‘g‘ri kelmadi, keyingisiga o‘tdim.",
                )
            except Forbidden:
                _clear_session(context, session_id)
                return
            except Exception:
                pass

            # Avoid infinite loops if something is seriously wrong.
            if attempts >= 5:
                await _send_final_summary(context, session_id)
                return
            continue

    poll_id = msg.poll.id if msg.poll else None
    session["current_poll_id"] = poll_id
    session["current_message_id"] = msg.message_id

    if poll_id:
        polls = _get_polls(context)
        polls[poll_id] = {
            "session_id": session_id,
            "user_id": user_id,
            "qn": q.n,
            "correct": shuffled_correct,
            "options": poll_options,
            "chat_id": chat_id,
            "message_id": msg.message_id,
        }

        # Schedule timeout using asyncio (no PTB JobQueue dependency)
        _cancel_timeout_task(session)
        session["timeout_task"] = asyncio.create_task(
            _timeout_runner(context, session_id=session_id, poll_id=poll_id)
        )


def list_local_tests(base_dir: Path) -> List[Path]:
    if not base_dir.exists():
        return []
    return sorted(base_dir.glob("*.txt"))


def find_test_file(base_dir: Path, query: str) -> Optional[Path]:
    query = query.strip()
    if not query:
        return None

    # allow passing just stem, or full filename
    candidates = list_local_tests(base_dir)
    for fp in candidates:
        if fp.name == query or fp.stem == query:
            return fp

    # allow numeric prefix like "01" to match "01-..."
    if query.isdigit():
        for fp in candidates:
            if fp.stem.startswith(query + "-") or fp.name.startswith(query + "-"):
                return fp

    # fuzzy contains
    qlow = query.lower()
    for fp in candidates:
        if qlow in fp.stem.lower():
            return fp

    return None


async def start_quiz(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    questions: List[QuizQuestion],
    title: str,
) -> None:
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id if update.effective_user else None
    if user_id is None:
        return

    session_id = _start_new_session(context, user_id=user_id, chat_id=chat_id, title=title, questions=questions)
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"Test boshlandi: {title}\nHar savol uchun {QUIZ_OPEN_PERIOD_SECONDS} soniya.",
    )
    await _send_next_question(context, session_id)


async def _timeout_runner(context: ContextTypes.DEFAULT_TYPE, *, session_id: str, poll_id: str) -> None:
    try:
        await asyncio.sleep(QUIZ_OPEN_PERIOD_SECONDS + 1)
    except asyncio.CancelledError:
        return

    try:
        await _on_timeout(context, session_id=session_id, poll_id=poll_id)
    except Forbidden:
        _clear_session(context, session_id)
    except Exception:
        logger.exception("Unhandled exception in timeout runner")


async def _on_timeout(context: ContextTypes.DEFAULT_TYPE, *, session_id: str, poll_id: str) -> None:

    sessions = _get_sessions(context)
    session = sessions.get(session_id)
    if not session:
        return

    lock: asyncio.Lock = session.get("advance_lock")
    if lock is None:
        lock = asyncio.Lock()
        session["advance_lock"] = lock

    async with lock:
        # Ignore if user already moved on / poll already handled
        if session.get("current_poll_id") != poll_id:
            return

        polls = _get_polls(context)
        meta = polls.get(poll_id)
        if not meta:
            return

        qn = int(meta.get("qn"))
        options = meta.get("options") or []
        correct = meta.get("correct")
        correct_text = options[correct] if isinstance(correct, int) and 0 <= correct < len(options) else "(noma’lum)"

        # Mark unanswered as wrong
        session["answers"][qn] = None
        session["wrong"][qn] = {"chosen": "(javob berilmadi)", "correct": correct_text}

        session["i"] = int(session.get("i") or 0) + 1
        session["current_poll_id"] = None
        session["current_message_id"] = None
        session["timeout_task"] = None

    # Close poll if possible
    try:
        polls = _get_polls(context)
        meta = polls.get(poll_id)
        if meta:
            await context.bot.stop_poll(chat_id=meta.get("chat_id"), message_id=meta.get("message_id"))
    except Forbidden:
        _clear_session(context, session_id)
        return
    except Exception:
        pass

    try:
        await context.bot.send_message(chat_id=session.get("chat_id"), text=f"{qn}-savol: vaqt tugadi.")
    except Forbidden:
        _clear_session(context, session_id)
        return
    except Exception:
        pass

    await _send_next_question(context, session_id)


async def on_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pa = update.poll_answer
    if not pa:
        return

    polls = _get_polls(context)
    meta = polls.get(pa.poll_id)
    if not meta:
        return

    # Only track the user who started this session
    if meta.get("user_id") != pa.user.id:
        return

    session_id = meta.get("session_id")
    sessions = _get_sessions(context)
    session = sessions.get(session_id) if session_id else None
    if not session:
        return

    lock: asyncio.Lock = session.get("advance_lock")
    if lock is None:
        lock = asyncio.Lock()
        session["advance_lock"] = lock

    async with lock:
        # Advance only for the currently active poll
        if session.get("current_poll_id") != pa.poll_id:
            return

        chosen = pa.option_ids[0] if pa.option_ids else None
        correct = meta.get("correct")
        options = meta.get("options") or []

        if chosen is None or correct is None or not options:
            return

        qn = int(meta.get("qn"))
        # Save answer and compute wrong list
        session["answers"][qn] = chosen
        correct_text = options[correct] if 0 <= correct < len(options) else "(noma’lum)"
        chosen_text = options[chosen] if 0 <= chosen < len(options) else "(noma’lum)"

        if chosen == correct:
            text = "Natija: to‘g‘ri."
            session["wrong"].pop(int(qn), None)
        else:
            text = f"Natija: noto‘g‘ri. Siz: {chosen_text}. To‘g‘ri: {correct_text}."
            session["wrong"][int(qn)] = {
                "chosen": chosen_text,
                "correct": correct_text,
            }

        # Mark this poll as handled (prevents timeout/duplicate handling)
        _cancel_timeout_task(session)
        session["i"] = int(session.get("i") or 0) + 1
        session["current_poll_id"] = None
        session["current_message_id"] = None

    # Stop current poll early (outside lock)
    try:
        await context.bot.stop_poll(chat_id=meta.get("chat_id"), message_id=meta.get("message_id"))
    except Forbidden:
        _clear_session(context, session_id)
        return
    except Exception:
        pass

    # PollAnswer event has no chat_id; we DM the user (works after user presses Start at least once).
    try:
        await context.bot.send_message(chat_id=pa.user.id, text=text)
    except Forbidden:
        _clear_session(context, session_id)
        return
    except Exception:
        # Ignore if user hasn't started bot or DMs are blocked.
        return

    await _send_next_question(context, session_id)


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Keep the bot running even if a handler raises.
    try:
        logger.exception("Unhandled error: %s", context.error)
    except Exception:
        pass


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Bu bot .txt test faylini qabul qiladi va avtomatik Telegram quiz-poll savollarini chiqaradi.\n\n"
        "Komandalar:\n"
        "- /menu — test tanlash (tugmalar)\n"
        "- /list — mavjud testlar ro‘yxati (serverdagi)\n"
        "- /send <nom yoki 01> — serverdagi testni boshlash\n\n"
        "- /stop — aktiv testni to‘xtatish\n\n"
        "Eslatma: natija/xatolarni DM’da ko‘rish uchun bot bilan private chatda ishlang."
    )
    await show_menu(update, context)


async def cmd_stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    chat = update.effective_chat
    if not user or not chat:
        return

    active = _get_active_session_by_user(context)
    session_id = active.get(user.id)
    if not session_id:
        await update.effective_message.reply_text("Hozir aktiv test yo‘q. /menu orqali test tanlang.")
        return

    sessions = _get_sessions(context)
    session = sessions.get(session_id)

    # Best-effort: stop current poll if we can.
    poll_id = session.get("current_poll_id") if session else None
    if poll_id:
        polls = _get_polls(context)
        meta = polls.get(poll_id)
        if meta:
            try:
                await context.bot.stop_poll(chat_id=meta.get("chat_id"), message_id=meta.get("message_id"))
            except Forbidden:
                # User blocked bot or chat gone; clear session below.
                pass
            except Exception:
                pass

    _clear_session(context, session_id)
    try:
        await update.effective_message.reply_text("Test to‘xtatildi. Yangi test uchun /menu yoki /send ishlating.")
    except Forbidden:
        return


async def cmd_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await show_menu(update, context)


async def cmd_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    base_dir = _tests_dir()
    files = list_local_tests(base_dir)
    if not files:
        await update.message.reply_text(f"Test fayllar topilmadi: {base_dir}")
        return

    lines = ["Mavjud testlar:"]
    for fp in files:
        lines.append(f"- {fp.name}")
    await update.message.reply_text("\n".join(lines))


async def cmd_send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Foydalanish: /send 01  yoki  /send 01-operatsion-tizim-asosiy-tushunchalar")
        return

    base_dir = _tests_dir()
    query = " ".join(context.args).strip()
    fp = find_test_file(base_dir, query)
    if not fp:
        await update.message.reply_text("Topilmadi. /list bilan tekshiring.")
        return

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    txt = fp.read_text(encoding="utf-8")
    questions = parse_tests_txt(txt)
    if not questions:
        await update.message.reply_text("Fayldan savollar o‘qilmadi.")
        return

    await start_quiz(update, context, questions, title=fp.stem)


async def on_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    doc = update.message.document
    if not doc:
        return

    name = (doc.file_name or "").strip()
    if not name.lower().endswith(".txt"):
        await update.message.reply_text("Iltimos .txt fayl yuboring.")
        return

    # "Only these tests" mode: accept only the known filenames from TESTS_DIR.
    base_dir = _tests_dir()
    known = _known_test_names(base_dir)
    if name not in known:
        await update.message.reply_text("Bu bot faqat tayyor testlar bilan ishlaydi. /list dan tanlang va /send <nom> ishlating.")
        return

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    txt = (base_dir / name).read_text(encoding="utf-8")
    questions = parse_tests_txt(txt)
    if not questions:
        await update.message.reply_text("Serverdagi fayldan savollar o‘qilmadi.")
        return

    await start_quiz(update, context, questions, title=name)


async def on_pick_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    q = update.callback_query
    if not q:
        return
    await q.answer()

    data = q.data or ""
    if not data.startswith("pick:"):
        return

    if not _is_private(update):
        await q.message.reply_text("Natija/xatolar uchun bot bilan private chatda ishlang.")
        return

    name = data.split(":", 1)[1]
    base_dir = _tests_dir()
    fp = base_dir / name
    if not fp.exists():
        await q.message.reply_text("Topilmadi. /menu ni qayta bosing.")
        return

    txt = fp.read_text(encoding="utf-8")
    questions = parse_tests_txt(txt)
    if not questions:
        await q.message.reply_text("Test o‘qilmadi.")
        return

    await start_quiz(update, context, questions, title=fp.stem)


def main() -> int:
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise SystemExit("BOT_TOKEN env var is required")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("menu", cmd_menu))
    app.add_handler(CommandHandler("list", cmd_list))
    app.add_handler(CommandHandler("send", cmd_send))
    app.add_handler(CommandHandler("stop", cmd_stop))
    app.add_handler(PollAnswerHandler(on_poll_answer))
    app.add_handler(CallbackQueryHandler(on_pick_callback))
    app.add_handler(MessageHandler(filters.Document.ALL, on_document))
    app.add_error_handler(on_error)

    logger.info("Bot started")
    app.run_polling(allowed_updates=Update.ALL_TYPES)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
