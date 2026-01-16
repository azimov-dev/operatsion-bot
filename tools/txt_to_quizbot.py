#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re
from pathlib import Path


Q_LINE = re.compile(r"^\?\s+(\d+)\.\s+(.*)$")
OPT_LINE = re.compile(r"^([\+\-])\s+([ABCD])\)\s+(.*)$")


def parse_tests_txt(txt: str):
    questions = []
    cur = None

    for raw in txt.splitlines():
        line = raw.rstrip("\n")
        if not line.strip():
            continue

        qm = Q_LINE.match(line.strip())
        if qm:
            if cur:
                questions.append(cur)
            cur = {
                "n": int(qm.group(1)),
                "text": qm.group(2).strip(),
                "options": [],  # list of {letter,text,is_correct}
            }
            continue

        om = OPT_LINE.match(line.strip())
        if om and cur is not None:
            cur["options"].append(
                {
                    "letter": om.group(2),
                    "text": om.group(3).strip(),
                    "is_correct": om.group(1) == "+",
                }
            )

    if cur:
        questions.append(cur)

    return questions


def to_quizbot_blocks(questions):
    # QuizBot doesn’t support bulk import; this format is optimized for copy/paste while creating a quiz.
    # Each block tells you: question text, options, and which option number is correct.
    out = []
    for q in questions:
        opts = q["options"]
        if not opts:
            continue

        correct_idx = None
        for i, opt in enumerate(opts, start=1):
            if opt["is_correct"]:
                correct_idx = i
                break

        # Fallback: if none marked, set 1
        if correct_idx is None:
            correct_idx = 1

        out.append(f"Q{q['n']}: {q['text']}")
        for i, opt in enumerate(opts, start=1):
            out.append(f"{i}) {opt['text']}")
        out.append(f"Correct option: {correct_idx}")
        out.append("---")

    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Convert generated tests_txt into QuizBot-ready copy/paste blocks")
    ap.add_argument("--in-dir", default="Ma'ruza/tests_txt", help="Input directory with .txt tests")
    ap.add_argument("--out-dir", default="Ma'ruza/telegram_quizbot", help="Output directory for QuizBot-ready files")
    args = ap.parse_args()

    in_dir = Path(args.in_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(in_dir.glob("*.txt"))
    if not files:
        raise SystemExit(f"No .txt files found in {in_dir}")

    for fp in files:
        txt = fp.read_text(encoding="utf-8")
        questions = parse_tests_txt(txt)
        out = to_quizbot_blocks(questions)
        (out_dir / fp.name).write_text(out, encoding="utf-8")

    print(f"Converted {len(files)} files -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
