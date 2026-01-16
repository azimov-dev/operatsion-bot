#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from dataclasses import dataclass
from typing import List, Optional


Q_LINE = re.compile(r"^\?\s+(\d+)\.\s+(.*)$")
OPT_LINE = re.compile(r"^([\+\-])\s+([ABCD])\)\s+(.*)$")


@dataclass
class QuizQuestion:
    n: int
    text: str
    options: List[str]
    correct_index: int  # 0-based


def parse_tests_txt(txt: str) -> List[QuizQuestion]:
    questions: List[dict] = []
    cur: Optional[dict] = None

    for raw in txt.splitlines():
        line = raw.strip("\n")
        if not line.strip():
            continue

        qm = Q_LINE.match(line.strip())
        if qm:
            if cur:
                questions.append(cur)
            cur = {"n": int(qm.group(1)), "text": qm.group(2).strip(), "opts": []}
            continue

        om = OPT_LINE.match(line.strip())
        if om and cur is not None:
            cur["opts"].append(
                {
                    "is_correct": om.group(1) == "+",
                    "letter": om.group(2),
                    "text": om.group(3).strip(),
                }
            )

    if cur:
        questions.append(cur)

    out: List[QuizQuestion] = []
    for q in questions:
        opts = q["opts"]
        if not opts:
            continue

        correct_idx = None
        for i, opt in enumerate(opts):
            if opt["is_correct"]:
                correct_idx = i
                break
        if correct_idx is None:
            correct_idx = 0

        out.append(
            QuizQuestion(
                n=int(q["n"]),
                text=str(q["text"]),
                options=[o["text"] for o in opts],
                correct_index=int(correct_idx),
            )
        )

    return out
