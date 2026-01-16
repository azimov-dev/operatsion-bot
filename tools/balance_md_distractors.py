#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Balance MCQ option lengths in Ma'ruza/tests/*.md.

Goal: reduce the common giveaway where the correct option is much longer.
This script expands *incorrect* options in questions 1-15 using simple heuristics.
It avoids adding explicit cues like "emas"/"noto'g'ri".

Usage:
  python3 tools/balance_md_distractors.py
"""

from __future__ import annotations

import re
from pathlib import Path

TESTS_DIR = Path("Ma'ruza/tests")

MCQ_OPT = re.compile(r"^(?P<prefix>\s*[-*]\s+)(?P<letter>[ABCD])\)\s+(?P<text>.*)\s*$")
KEY_LINE = re.compile(r"^\s*(\d+)\.\s*([ABCD])\s*$")


def _parse_answer_key(md: str) -> dict[int, str]:
    # Find section "Javoblar kaliti" and parse lines like "1. B"
    parts = md.split("## Javoblar kaliti")
    if len(parts) < 2:
        return {}
    tail = parts[1]
    out: dict[int, str] = {}
    for line in tail.splitlines():
        m = KEY_LINE.match(line.strip())
        if not m:
            continue
        out[int(m.group(1))] = m.group(2)
    return out


def _enrich(text: str) -> str:
    t = text.strip()
    low = t.lower()

    # Normalize overly short "Faqat ..." distractors into longer (still narrow) ones.
    if low.startswith("faqat "):
        t = t[6:].strip()
        low = t.lower()

    # Keyword-driven expansions (keep them plausible but still not the full concept).
    add = ""

    if any(k in low for k in ["matn", "hujjat", "muharrir", "office"]):
        add = " va hujjat/taqdimot kabi ofis ilovalari bilan ishlash"
    elif any(k in low for k in ["tarmoq", "paket", "marshrut", "firewall"]):
        add = " va tarmoq trafikini filtrlash/marshrutlash qoidalarini sozlash"
    elif any(k in low for k in ["drayver", "qurilma", "printer", "driver"]):
        add = " va qurilmalarni ulash hamda drayverlarni boshqarish"
    elif any(k in low for k in ["gui", "grafik", "oyna", "interfeys"]):
        add = " va oynali interfeys elementlarini boshqarish"
    elif any(k in low for k in ["bios", "firmware", "uefi"]):
        add = " va firmware (UEFI/BIOS) sozlamalari bilan ishlash"
    elif any(k in low for k in ["antivirus", "virus", "zararli"]):
        add = " va zararli dasturlarni aniqlash/karantin qilish"
    elif any(k in low for k in ["o'yin", "oyin", "multimedia", "media"]):
        add = " va multimedia/kulgi ilovalarini ishga tushirish"
    elif any(k in low for k in ["disk", "sektor", "defrag", "bo'lish"]):
        add = " hamda diskdagi ma'lumotlarni tashkil etish/tekshirish"
    elif any(k in low for k in ["ram", "xotira", "memory"]):
        add = " va xotiradan foydalanishni nazorat qilish"

    # If still too short, append a generic narrow add-on.
    if not add and len(t) < 35:
        add = " va unga yaqin yordamchi vazifalarni bajarish"

    enriched = (t + add).strip()

    # Light trimming to avoid absurdly long options.
    if len(enriched) > 110:
        enriched = enriched[:107].rstrip() + "…"

    # Capitalize first letter if needed.
    if enriched and enriched[0].islower():
        enriched = enriched[0].upper() + enriched[1:]

    return enriched


def balance_file(path: Path) -> bool:
    md = path.read_text(encoding="utf-8")
    key = _parse_answer_key(md)
    if not key:
        return False

    lines = md.splitlines(True)
    out_lines: list[str] = []

    current_q: int | None = None

    # Only balance MCQ options in questions 1-15.
    q_header = re.compile(r"^\s*(\d+)\.\s+.*$")

    for raw in lines:
        mqh = q_header.match(raw.strip())
        if mqh:
            qn = int(mqh.group(1))
            current_q = qn
            out_lines.append(raw)
            continue

        mo = MCQ_OPT.match(raw.rstrip("\n"))
        if mo and current_q is not None and 1 <= current_q <= 15:
            letter = mo.group("letter")
            text = mo.group("text")

            correct = key.get(current_q)
            if correct and letter != correct:
                new_text = _enrich(text)
                raw = f"{mo.group('prefix')}{letter}) {new_text}\n"

        out_lines.append(raw)

    new_md = "".join(out_lines)
    if new_md != md:
        path.write_text(new_md, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = 0
    for fp in sorted(TESTS_DIR.glob("*.md")):
        if balance_file(fp):
            changed += 1
    print(f"Updated files: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
