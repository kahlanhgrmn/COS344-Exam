#!/usr/bin/env python3
"""
enrich_past_papers.py
Parses each past-paper markdown file, extracts the question text and MCQ
options, and writes them back into the corresponding JSON memo file.

Also normalizes answers so they exactly match the option text (fixing
backtick / hyphenation differences between the MD and the memo).

Run once:
    python3 enrich_past_papers.py
"""

import json
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PP_DIR     = SCRIPT_DIR / "PastPapers"

PAIRS = [
    ("Exams/2022_examination.md",       "Exams/2022_examination_memo.json"),
    ("Exams/2023_examination.md",       "Exams/2023_examination_memo.json"),
    ("Exams/2024_examination.md",       "Exams/2024_examination_memo.json"),
    ("Exams/2025_examination.md",       "Exams/2025_examination_memo.json"),
    ("ST1/2024_semester_test_1.md",     "ST1/2024_semester_test_1_memo.json"),
    ("ST1/2025_semester_test_1.md",     "ST1/2025_semester_test_1_memo.json"),
    ("ST2/2024_semester_test_2.md",     "ST2/2024_semester_test_2_memo.json"),
    ("ST2/2025_semester_test_2.md",     "ST2/2025_semester_test_2_memo.json"),
]

# "Did you submit?" checkbox values — different papers use different wording
SUBMIT_VALUES = {'Yes', 'No', 'True', 'False'}

# Answer-placeholder lines to strip from question text
ANSWER_PLACEHOLDER = re.compile(
    r'^\*\*(?:Answer|Ad-hoc binding|Shallow binding|Deep binding'
    r'|Shallow|Deep):\*\*\s*_+\s*$'
)


# ── Option / answer normalization ─────────────────────────────────────────────

def strip_backticks(s: str) -> str:
    return s.replace('`', '')


def normalize_for_match(s: str) -> str:
    """Lose text normalization for fuzzy answer↔option matching."""
    s = strip_backticks(s)
    s = ' '.join(s.split())          # collapse whitespace
    s = s.lower()
    s = s.rstrip('.')                # ignore trailing period differences
    # Normalize inter-word hyphens only: short-circuit → short circuit
    s = re.sub(r'(?<=\w)-(?=\w)', ' ', s)
    return ' '.join(s.split())


def best_matching_option(answer_str: str, options: list[str]) -> str | None:
    """
    Return the option that matches the answer, or None.
    Tries exact match first, then normalised match.
    """
    if answer_str in options:
        return answer_str
    ans_norm = normalize_for_match(answer_str)
    for opt in options:
        if normalize_for_match(opt) == ans_norm:
            return opt
    return None


def fix_answers(data: dict) -> int:
    """
    For each MCQ question (options != None) make the answer(s) match the
    exact option text. Returns count of updated answers.
    """
    fixed = 0
    for q in data['questions']:
        opts = q.get('options')
        if not opts:
            continue
        ans = q.get('answer')
        if isinstance(ans, str):
            matched = best_matching_option(ans, opts)
            if matched and matched != ans:
                q['answer'] = matched
                fixed += 1
        elif isinstance(ans, list):
            new_ans = []
            for a in ans:
                matched = best_matching_option(a, opts)
                if matched and matched != a:
                    fixed += 1
                    new_ans.append(matched)
                else:
                    new_ans.append(a)
            q['answer'] = new_ans
    return fixed


# ── MD parser ─────────────────────────────────────────────────────────────────

def parse_md_questions(md_text: str) -> dict[int, dict]:
    """
    Return {q_num: {"question_text": str, "options": list|None}}
    for every question block in the markdown.
    """
    parsed: dict[int, dict] = {}

    blocks = re.split(r'\n---+\n', md_text)

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        hdr = re.match(r'## Question (\d+) \*\((\d+) points?\)\*', block)
        if not hdr:
            continue

        q_num   = int(hdr.group(1))
        content = block[hdr.end():].strip()

        # ── Options ────────────────────────────────────────────────────────
        raw_opts = re.findall(r'^- \[ \] (.+?)$', content, re.MULTILINE)
        # Strip backtick formatting; exclude submit checkboxes
        real_opts = [
            strip_backticks(o.strip())
            for o in raw_opts
            if o.strip() not in SUBMIT_VALUES
        ]

        # ── Question text ──────────────────────────────────────────────────
        lines      = content.split('\n')
        text_lines = []
        skip_rest  = False

        for line in lines:
            if ('**Did you submit?**' in line
                    or line.strip().startswith('Submit file')):
                skip_rest = True
            if skip_rest:
                continue
            if re.match(r'^- \[ \]', line):
                continue
            if ANSWER_PLACEHOLDER.match(line.strip()):
                continue
            text_lines.append(line)

        question_text = '\n'.join(text_lines).strip()

        parsed[q_num] = {
            'question_text': question_text,
            'options':       real_opts if real_opts else None,
        }

    return parsed


# ── Main enrichment logic ─────────────────────────────────────────────────────

def enrich(md_path: Path, json_path: Path) -> None:
    print(f"\n{md_path.name}  →  {json_path.name}")

    md_parsed = parse_md_questions(md_path.read_text(encoding='utf-8'))
    print(f"  MD: parsed {len(md_parsed)} questions")

    with open(json_path, encoding='utf-8') as fh:
        data = json.load(fh)

    updated, missing = 0, 0
    for q in data['questions']:
        q_num = q.get('question')
        if q_num not in md_parsed:
            print(f"  [WARN] Q{q_num} not found in MD — skipped")
            missing += 1
            continue
        q['question_text'] = md_parsed[q_num]['question_text']
        q['options']       = md_parsed[q_num]['options']
        updated += 1

    fixed = fix_answers(data)

    print(f"  JSON: {updated} questions updated"
          + (f", {missing} not matched" if missing else "")
          + (f", {fixed} answers normalised" if fixed else ""))

    with open(json_path, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)

    print(f"  Saved ✓")


def main() -> None:
    for md_rel, json_rel in PAIRS:
        md_path   = PP_DIR / md_rel
        json_path = PP_DIR / json_rel
        if not md_path.exists():
            print(f"[SKIP] {md_path.name} — not found")
            continue
        if not json_path.exists():
            print(f"[SKIP] {json_path.name} — not found")
            continue
        enrich(md_path, json_path)

    print("\nDone.")


if __name__ == '__main__':
    main()
