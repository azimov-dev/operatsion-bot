#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
from pathlib import Path


Q_RE = re.compile(r"^(\d+)\.\s+(.*)$")
OPT_RE = re.compile(r"^-\s*([ABCD])\)\s*(.*)$")
ANS_RE = re.compile(r"^(\d+)\.\s*([ABCD])\s*$")


def parse_answer_key(md_text: str) -> dict[int, str]:
    parts = md_text.split("## Javoblar kaliti")
    if len(parts) < 2:
        raise ValueError("`## Javoblar kaliti` bo‘limi topilmadi")
    key_text = parts[1]

    answers: dict[int, str] = {}
    for line in key_text.splitlines():
        line = line.strip()
        m = ANS_RE.match(line)
        if not m:
            continue
        qn = int(m.group(1))
        answers[qn] = m.group(2)

    if not answers:
        raise ValueError("Javoblar kalitidan hech narsa o‘qilmadi")

    return answers


def parse_questions(md_text: str) -> list[dict]:
    body = md_text.split("## Javoblar kaliti")[0]
    lines = body.splitlines()

    questions = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")
        m = Q_RE.match(line.strip())
        if not m:
            i += 1
            continue

        qn = int(m.group(1))
        qtext = m.group(2).strip()

        # Collect options following the question until next question or heading
        opts = []
        i += 1
        while i < len(lines):
            l = lines[i].rstrip("\n")
            s = l.strip()

            # stop at next question or new section header
            if s.startswith("## "):
                break
            if Q_RE.match(s):
                break

            om = OPT_RE.match(s)
            if om:
                opts.append((om.group(1), om.group(2).strip()))
            i += 1

        questions.append({"n": qn, "text": qtext, "options": opts})
        continue

    return questions


def md_to_txt(md_path: Path, out_path: Path) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    answers = parse_answer_key(md_text)
    questions = parse_questions(md_text)

    # Basic validation
    q_numbers = [q["n"] for q in questions]
    if not q_numbers:
        raise ValueError(f"Savollar topilmadi: {md_path}")

    # Render
    out_lines = []
    for q in questions:
        n = q["n"]
        out_lines.append(f"? {n}. {q['text']}")

        correct = answers.get(n)
        opts = q["options"]
        if not opts:
            # If no options were parsed, still emit a placeholder line
            out_lines.append("- (variantlar topilmadi)")
            out_lines.append("")
            continue

        for letter, text in opts:
            mark = "+" if (correct == letter) else "-"
            out_lines.append(f"{mark} {letter}) {text}")
        out_lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(out_lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Convert OS course Markdown tests to TXT with ? questions and +/- options")
    ap.add_argument("--in-dir", default="Ma'ruza/tests", help="Input directory containing .md test files")
    ap.add_argument("--out-dir", default="Ma'ruza/tests_txt", help="Output directory for .txt files")
    args = ap.parse_args()

    in_dir = Path(args.in_dir)
    out_dir = Path(args.out_dir)

    md_files = sorted(in_dir.glob("*.md"))
    if not md_files:
        raise SystemExit(f"No .md files found in {in_dir}")

    for md_path in md_files:
        out_path = out_dir / (md_path.stem + ".txt")
        md_to_txt(md_path, out_path)

    print(f"Converted {len(md_files)} files -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
