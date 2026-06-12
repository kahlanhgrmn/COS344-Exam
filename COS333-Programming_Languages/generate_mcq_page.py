#!/usr/bin/env python3
"""
generate_mcq_page.py
Reads chapter *_mcq.json files AND past-paper *_memo.json files and produces
a single self-contained interactive HTML MCQ page.

Usage:
    python3 generate_mcq_page.py
Output:
    COS333_mcq_bank.html  (next to this script)
"""

import json
import os
import glob
import re
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

SCRIPT_DIR  = Path(__file__).parent
OUTPUT_FILE = SCRIPT_DIR / "COS333_mcq_bank.html"

SECTION_META = {
    "Section1": {
        "label":    "Section 1 — Language Evaluation & History",
        "color":    "#7c3aed",
        "color_bg": "#f5f3ff",
        "chapters": ["chapter_01", "chapter_02"],
    },
    "Section2": {
        "label":    "Section 2 — Variables, Types & Functional/Logic",
        "color":    "#0284c7",
        "color_bg": "#f0f9ff",
        "chapters": ["chapter_05", "chapter_06", "chapter_15", "chapter_16"],
    },
    "Section3": {
        "label":    "Section 3 — Expressions, Control & OOP",
        "color":    "#059669",
        "color_bg": "#ecfdf5",
        "chapters": ["chapter_07", "chapter_08", "chapter_09", "chapter_12"],
    },
}

PAST_PAPER_META = [
    {"key": "exam_2022", "label": "Examination 2022", "type": "Exam",  "year": 2022,
     "color": "#b45309", "color_bg": "#fffbeb", "file": "PastPapers/Exams/2022_examination_memo.json"},
    {"key": "exam_2023", "label": "Examination 2023", "type": "Exam",  "year": 2023,
     "color": "#b45309", "color_bg": "#fffbeb", "file": "PastPapers/Exams/2023_examination_memo.json"},
    {"key": "exam_2024", "label": "Examination 2024", "type": "Exam",  "year": 2024,
     "color": "#b45309", "color_bg": "#fffbeb", "file": "PastPapers/Exams/2024_examination_memo.json"},
    {"key": "exam_2025", "label": "Examination 2025", "type": "Exam",  "year": 2025,
     "color": "#b45309", "color_bg": "#fffbeb", "file": "PastPapers/Exams/2025_examination_memo.json"},
    {"key": "st1_2024",  "label": "Semester Test 1 (2024)", "type": "ST1", "year": 2024,
     "color": "#0284c7", "color_bg": "#f0f9ff", "file": "PastPapers/ST1/2024_semester_test_1_memo.json"},
    {"key": "st1_2025",  "label": "Semester Test 1 (2025)", "type": "ST1", "year": 2025,
     "color": "#0284c7", "color_bg": "#f0f9ff", "file": "PastPapers/ST1/2025_semester_test_1_memo.json"},
    {"key": "st2_2024",  "label": "Semester Test 2 (2024)", "type": "ST2", "year": 2024,
     "color": "#7c3aed", "color_bg": "#f5f3ff", "file": "PastPapers/ST2/2024_semester_test_2_memo.json"},
    {"key": "st2_2025",  "label": "Semester Test 2 (2025)", "type": "ST2", "year": 2025,
     "color": "#7c3aed", "color_bg": "#f5f3ff", "file": "PastPapers/ST2/2025_semester_test_2_memo.json"},
]

# ── Load chapter MCQ data ─────────────────────────────────────────────────────

def load_all_mcqs() -> list[dict]:
    chapters = []
    for section_name, smeta in SECTION_META.items():
        for ch_dir in smeta["chapters"]:
            json_path = SCRIPT_DIR / section_name / ch_dir / f"{ch_dir}_mcq.json"
            if not json_path.exists():
                print(f"  [SKIP] {json_path} not found")
                continue
            with open(json_path, encoding="utf-8") as f:
                data = json.load(f)

            questions = []
            for q in data.get("questions", []):
                opts = q.get("options", [])
                answer_text = q.get("answer", "")
                answer_letter = "A"
                for i, o in enumerate(opts):
                    if o == answer_text:
                        answer_letter = "ABCD"[i]
                        break
                questions.append({
                    "q":           q.get("question", ""),
                    "opts":        opts,
                    "answer":      answer_letter,
                    "explanation": q.get("explanation", ""),
                    "topic":       q.get("topic", ""),
                })

            chapters.append({
                "id":           ch_dir.upper().replace("_", ""),
                "chKey":        ch_dir,
                "section":      section_name,
                "sectionLabel": smeta["label"],
                "color":        smeta["color"],
                "colorBg":      smeta["color_bg"],
                "title":        data.get("title", ch_dir),
                "chapter":      data.get("chapter", ""),
                "count":        len(questions),
                "mcqs":         questions,
            })
    return chapters

# ── Load past-paper data ──────────────────────────────────────────────────────

def load_all_past_papers() -> list[dict]:
    papers = []
    for pmeta in PAST_PAPER_META:
        json_path = SCRIPT_DIR / pmeta["file"]
        if not json_path.exists():
            print(f"  [SKIP] {json_path} not found")
            continue
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)

        questions = []
        for q in data.get("questions", []):
            opts    = q.get("options")       # None for non-MCQ
            ans_raw = q.get("answer", "")
            ans_str = str(ans_raw) if not isinstance(ans_raw, dict) else json.dumps(ans_raw)

            LETTERS = "ABCDEFGHIJ"
            if opts and isinstance(ans_raw, str):
                # Single-answer MCQ
                answer_letter = "A"
                for i, o in enumerate(opts):
                    if o == ans_raw:
                        answer_letter = LETTERS[i]
                        break
                questions.append({
                    "type":        "mcq",
                    "q":           q.get("question_text", ""),
                    "opts":        opts,
                    "answer":      answer_letter,
                    "explanation": q.get("explanation", ""),
                    "topic":       q.get("topic", ""),
                    "marks":       q.get("marks", 1),
                    "q_num":       q.get("question", ""),
                })
            elif opts and isinstance(ans_raw, list):
                # Multi-select MCQ
                correct_letters = []
                for a in ans_raw:
                    for i, o in enumerate(opts):
                        if o == a:
                            correct_letters.append(LETTERS[i])
                            break
                questions.append({
                    "type":           "multi",
                    "q":              q.get("question_text", ""),
                    "opts":           opts,
                    "answer_list":    ans_raw,
                    "correct_letters": correct_letters,
                    "explanation":    q.get("explanation", ""),
                    "topic":          q.get("topic", ""),
                    "marks":          q.get("marks", 1),
                    "q_num":          q.get("question", ""),
                })
            else:
                # Short answer or coding (no options)
                qtype = "code" if "\n" in ans_str else "short"
                questions.append({
                    "type":        qtype,
                    "q":           q.get("question_text", ""),
                    "opts":        None,
                    "answer":      ans_raw,
                    "explanation": q.get("explanation", ""),
                    "topic":       q.get("topic", ""),
                    "marks":       q.get("marks", 1),
                    "q_num":       q.get("question", ""),
                })

        mcq_count = sum(1 for q in questions if q["type"] == "mcq")
        papers.append({
            "key":       pmeta["key"],
            "label":     pmeta["label"],
            "type":      pmeta["type"],
            "year":      pmeta["year"],
            "color":     pmeta["color"],
            "colorBg":   pmeta["color_bg"],
            "date":      data.get("date", ""),
            "totalMarks": data.get("total_marks", 0),
            "count":     len(questions),
            "mcqCount":  mcq_count,
            "questions": questions,
        })
    return papers

# ── HTML generator ────────────────────────────────────────────────────────────

CSS = """
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;500;600;700&display=swap');
:root{
  --bg:#f8f9fb;--surface:#fff;--surface2:#f0f2f5;
  --border:#e0e4ea;--border2:#c8cdd6;
  --navy:#1a2035;--navy2:#2c3654;
  --text:#1e2535;--muted:#6b7590;
  --accent:#2563eb;--accent-bg:#eff4ff;
  --accent2:#0ea47a;--accent2-bg:#edfaf5;
  --warn:#d97706;--warn-bg:#fffbeb;
  --danger:#dc2626;--danger-bg:#fef2f2;
  --radius:8px;
  --mono:'JetBrains Mono',monospace;
  --sans:'Inter',system-ui,sans-serif;
  --shadow:0 1px 3px rgba(0,0,0,.08),0 1px 2px rgba(0,0,0,.05);
  --shadow-md:0 4px 12px rgba(0,0,0,.1);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:var(--sans);font-size:15px;line-height:1.7}
h1{font-size:clamp(1.7rem,4vw,2.4rem);font-weight:700;letter-spacing:-.02em;line-height:1.2;color:var(--navy)}
h2{font-size:1.18rem;font-weight:700;color:var(--navy);margin:2rem 0 .75rem;border-bottom:2px solid var(--border);padding-bottom:.4rem}
h3{font-size:1.0rem;font-weight:600;color:var(--navy2);margin:1.25rem 0 .5rem}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
strong{color:var(--navy);font-weight:600}

/* nav */
nav.topnav{background:var(--navy);position:sticky;top:0;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.2)}
.topnav-inner{max-width:1100px;margin:0 auto;padding:.85rem 1.5rem;display:flex;align-items:center;gap:2rem}
.topnav-logo{font-family:var(--mono);font-size:.88rem;font-weight:600;color:#fff;white-space:nowrap}
.topnav-logo span{color:#8892a8;font-weight:400}
.topnav-links{display:flex;gap:1.5rem}
.topnav-links a{color:#8892a8;font-size:.85rem;font-weight:500;transition:color .15s;padding:.2rem 0;border-bottom:2px solid transparent}
.topnav-links a:hover{color:#fff;text-decoration:none}
.topnav-links a.active{color:#fff;border-bottom-color:var(--accent2)}

/* layout */
.page-wrap{max-width:960px;margin:0 auto;padding:0 1.5rem 4rem}

/* hero */
.page-hero{padding:2.5rem 0 1.5rem}
.breadcrumb{font-size:.78rem;color:var(--muted);margin-bottom:.5rem;font-family:var(--mono)}
.breadcrumb a{color:var(--muted)}

/* control panel */
.control-panel{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:1.25rem;margin-bottom:1.5rem;box-shadow:var(--shadow)}
.control-row{display:flex;gap:1rem;flex-wrap:wrap;align-items:flex-end;margin-bottom:.75rem}
.ctrl-group{display:flex;flex-direction:column;gap:.3rem}
.ctrl-label{font-size:.72rem;font-weight:600;color:var(--muted);text-transform:uppercase;
  letter-spacing:.05em;font-family:var(--mono)}
.ctrl-select{padding:.4em .75em;border-radius:5px;border:1.5px solid var(--border);
  background:var(--surface);font-size:.85rem;font-family:var(--sans);color:var(--navy);cursor:pointer;
  min-width:200px}
.ctrl-select:focus{outline:none;border-color:var(--accent)}
.mode-group{display:flex;gap:.4rem}
.mode-btn{padding:.4em .9em;border-radius:4px;border:1.5px solid var(--border);
  background:var(--surface);cursor:pointer;font-size:.78rem;font-weight:600;
  font-family:var(--mono);color:var(--muted);transition:all .15s}
.mode-btn.active{background:var(--navy);border-color:var(--navy);color:#fff}
.score-display{background:var(--navy);color:#fff;border-radius:var(--radius);
  padding:.75rem 1.2rem;display:inline-flex;align-items:center;gap:.6rem;font-size:.85rem}
.score-num{font-family:var(--mono);font-size:1.4rem;font-weight:700;color:var(--accent2)}
.btn{padding:.45em 1em;border-radius:5px;border:1.5px solid var(--border);background:var(--surface);
  cursor:pointer;font-size:.83rem;font-weight:600;font-family:var(--sans);color:var(--navy);transition:all .15s}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.btn-danger{background:var(--danger-bg);border-color:var(--danger);color:var(--danger)}
.btn-danger:hover{background:var(--danger);color:#fff}
.btn-row{display:flex;gap:.6rem;flex-wrap:wrap;margin-bottom:.75rem}
.progress-wrap{height:5px;background:var(--surface2);border-radius:99px;overflow:hidden}
.progress-fill{height:100%;background:var(--accent2);border-radius:99px;transition:width .3s}
.progress-text{font-size:.73rem;color:var(--muted);margin-top:.35rem;font-family:var(--mono)}

/* source toggle */
.source-toggle{display:flex;gap:.4rem;margin-bottom:.75rem;padding-bottom:.75rem;border-bottom:1px solid var(--border)}
.src-btn{padding:.4em 1.1em;border-radius:5px;border:1.5px solid var(--border);background:var(--surface);
  cursor:pointer;font-size:.85rem;font-weight:600;font-family:var(--sans);color:var(--muted);transition:all .15s}
.src-btn.active{background:var(--navy);border-color:var(--navy);color:#fff}
.src-btn:hover:not(.active){border-color:var(--accent);color:var(--accent)}

/* section header */
.section-block{margin-bottom:2rem}
.section-header{display:flex;align-items:center;gap:.75rem;margin-bottom:1rem;
  padding:.6rem 1rem;border-radius:var(--radius);background:var(--surface);
  border:1px solid var(--border);box-shadow:var(--shadow)}
.section-pill{font-family:var(--mono);font-size:.72rem;font-weight:600;padding:.25em .65em;
  border-radius:99px;letter-spacing:.04em}
.section-count{font-size:.8rem;color:var(--muted);font-family:var(--mono);margin-left:auto}

/* chapter block */
.chapter-block{margin-bottom:1.5rem;background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius);box-shadow:var(--shadow);overflow:hidden}
.chapter-header{padding:.9rem 1.2rem;border-bottom:1px solid var(--border);
  display:flex;align-items:center;gap:.75rem;cursor:pointer;user-select:none;
  transition:background .15s}
.chapter-header:hover{background:var(--surface2)}
.ch-badge{font-family:var(--mono);font-size:.7rem;font-weight:600;padding:.2em .6em;
  border-radius:99px;white-space:nowrap}
.ch-title{font-size:.95rem;font-weight:600;color:var(--navy)}
.ch-meta{font-size:.75rem;color:var(--muted);font-family:var(--mono);margin-left:auto;white-space:nowrap}
.ch-chevron{color:var(--muted);font-size:.75rem;transition:transform .2s;margin-left:.5rem}
.chapter-body{padding:1rem 1.2rem}
.chapter-body.collapsed{display:none}

/* MCQ card */
.mcq-block{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:1.1rem 1.25rem;margin-bottom:.75rem;transition:box-shadow .15s}
.mcq-block:hover{box-shadow:var(--shadow-md)}
.mcq-meta{display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem;flex-wrap:wrap}
.mcq-num{font-family:var(--mono);font-size:.68rem;font-weight:600;color:var(--muted);
  text-transform:uppercase;letter-spacing:.04em}
.topic-tag{font-family:var(--mono);font-size:.66rem;padding:.15em .55em;border-radius:99px;
  background:var(--surface2);color:var(--muted);border:1px solid var(--border)}
.mcq-q{font-size:.93rem;font-weight:500;color:var(--navy);margin-bottom:.75rem;line-height:1.55}
.mcq-opts{list-style:none;display:flex;flex-direction:column;gap:.45rem;padding:0}
.mcq-opt{display:flex;align-items:flex-start;gap:.75rem;padding:.65rem .9rem;
  border-radius:6px;border:1.5px solid var(--border);cursor:pointer;
  font-size:.875rem;line-height:1.5;transition:all .15s}
.mcq-opt:hover:not(.locked){background:var(--accent-bg);border-color:var(--accent)}
.mcq-opt.locked{cursor:default}
.mcq-opt.correct{background:var(--accent2-bg);border-color:var(--accent2);color:var(--navy)}
.mcq-opt.wrong{background:var(--danger-bg);border-color:var(--danger)}
.opt-letter{font-family:var(--mono);font-size:.75rem;font-weight:700;min-width:1.1rem;
  color:var(--muted);padding-top:.05em}
.mcq-opt.correct .opt-letter{color:var(--accent2)}
.mcq-opt.wrong .opt-letter{color:var(--danger)}
.mcq-feedback{margin-top:.75rem;padding:.6rem .9rem;border-radius:6px;
  font-size:.83rem;line-height:1.5;display:none}
.mcq-feedback.show{display:block}
.fb-correct{background:var(--accent2-bg);border:1px solid var(--accent2);color:#065f46}
.fb-wrong{background:var(--danger-bg);border:1px solid var(--danger);color:#991b1b}

/* Past-paper badges & reveal cards */
.pp-marks-badge{font-family:var(--mono);font-size:.66rem;font-weight:600;padding:.15em .5em;
  border-radius:99px;background:var(--warn-bg);color:var(--warn);border:1px solid var(--warn);white-space:nowrap}
.pp-type-badge{font-family:var(--mono);font-size:.63rem;padding:.13em .45em;border-radius:99px;
  background:var(--surface2);color:var(--muted);border:1px solid var(--border)}
.pp-reveal-btn{margin-left:auto;padding:.3em .8em;border-radius:4px;border:1.5px solid var(--accent);
  background:var(--accent-bg);color:var(--accent);cursor:pointer;font-size:.75rem;font-weight:600;
  font-family:var(--mono);white-space:nowrap;transition:all .15s;flex-shrink:0}
.pp-reveal-btn:hover{background:var(--accent);color:#fff}
.pp-reveal-btn.revealed{border-color:var(--accent2);background:var(--accent2-bg);color:var(--accent2)}
.pp-reveal-btn.revealed:hover{background:var(--accent2);color:#fff}
.pp-ans-label{font-family:var(--mono);font-size:.66rem;font-weight:700;text-transform:uppercase;
  letter-spacing:.06em;color:var(--accent2);margin-bottom:.35rem}
.pp-ans-text{font-size:.9rem;font-weight:600;color:var(--navy);display:block;margin-bottom:.4rem}
.pp-ans-list{list-style:none;padding:0;margin:0 0 .4rem}
.pp-ans-list li{font-size:.88rem;font-weight:600;color:var(--navy);padding:.15rem 0}
.pp-ans-list li::before{content:"✓ ";color:var(--accent2);font-weight:700}
.pp-ans-code{font-family:var(--mono);font-size:.8rem;background:var(--navy);color:#a8d8a8;
  padding:.75rem 1rem;border-radius:5px;overflow-x:auto;margin-bottom:.4rem;white-space:pre;display:block}
.pp-ans-dict{font-size:.85rem;display:grid;grid-template-columns:auto 1fr;gap:.25rem .75rem;margin-bottom:.4rem}
.pp-ans-dict dt{font-weight:600;color:var(--muted);text-transform:capitalize;white-space:nowrap}
.pp-ans-dict dd{font-weight:600;color:var(--navy)}
.pp-exp{font-size:.82rem;line-height:1.55;color:var(--text);margin-top:.5rem;
  padding-top:.5rem;border-top:1px solid rgba(0,0,0,.07)}

/* Question text markdown rendering */
.q-pre{font-family:var(--mono);font-size:.8rem;background:var(--surface2);border:1px solid var(--border);
  padding:.6rem .85rem;border-radius:5px;overflow-x:auto;margin:.4rem 0;white-space:pre;display:block}
code.q-code{font-family:var(--mono);font-size:.83em;background:var(--surface2);
  padding:.1em .35em;border-radius:3px;border:1px solid var(--border)}

/* empty state */
.empty-state{text-align:center;padding:3rem 1rem;color:var(--muted)}
.empty-state svg{opacity:.3;margin-bottom:1rem}

/* footer */
footer{background:var(--navy);color:#8892a8;padding:1.5rem;margin-top:3rem}
.footer-inner{max-width:1100px;margin:0 auto;display:flex;justify-content:space-between;
  align-items:center;font-size:.8rem;font-family:var(--mono)}
.footer-inner a{color:#8892a8}
.footer-inner a:hover{color:#fff;text-decoration:none}

/* stats strip */
.stats-strip{display:flex;gap:1.5rem;flex-wrap:wrap;margin-bottom:1.2rem}
.stat-chip{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:.5rem .9rem;font-size:.8rem;font-family:var(--mono);color:var(--muted)}
.stat-chip strong{color:var(--navy);font-size:1rem}

/* scroll to top */
#scroll-top{position:fixed;bottom:1.5rem;right:1.5rem;background:var(--navy);color:#fff;
  border:none;border-radius:50%;width:40px;height:40px;cursor:pointer;font-size:1rem;
  opacity:0;transition:opacity .2s;box-shadow:var(--shadow-md);z-index:99}
#scroll-top.visible{opacity:1}
"""


def build_html(chapters: list[dict], papers: list[dict]) -> str:
    total_qs      = sum(c["count"] for c in chapters)
    total_chs     = len(chapters)
    total_pp_qs   = sum(p["count"] for p in papers)
    total_pp_mcq  = sum(p["mcqCount"] for p in papers)
    total_pp      = len(papers)

    data_json = json.dumps(chapters, ensure_ascii=False)
    pp_json   = json.dumps(papers,   ensure_ascii=False)

    section_options = '<option value="all">All Sections</option>'
    for skey, smeta in SECTION_META.items():
        section_options += f'<option value="{skey}">{smeta["label"]}</option>'

    pp_type_options = (
        '<option value="all">All Papers</option>'
        '<option value="Exam">Examinations</option>'
        '<option value="ST1">Semester Test 1</option>'
        '<option value="ST2">Semester Test 2</option>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MCQ Bank &middot; COS 333</title>
<style>{CSS}</style>
</head>
<body>

<nav class="topnav">
  <div class="topnav-inner">
    <div class="topnav-logo">COS333 <span>// MCQ Bank</span></div>
    <div class="topnav-links">
      <a href="#" class="active">Question Bank</a>
    </div>
  </div>
</nav>

<div class="page-wrap">
  <div class="page-hero">
    <div class="breadcrumb">COS 333 &rsaquo; Programming Languages &rsaquo; MCQ Bank</div>
    <h1>MCQ Question Bank</h1>
    <p style="color:var(--muted);font-size:.95rem;margin-top:.4rem">
      {total_qs} chapter MCQs &middot; {total_pp_mcq} past-paper MCQs &middot; {total_pp_qs} total past-paper questions.
      Click an option to check your answer instantly.
    </p>
  </div>

  <!-- Stats strip — swapped by JS based on active source -->
  <div class="stats-strip" id="stats-mcq">
    <div class="stat-chip">Chapters <strong>{total_chs}</strong></div>
    <div class="stat-chip">Chapter MCQs <strong>{total_qs}</strong></div>
    <div class="stat-chip">Per chapter <strong>20</strong></div>
    <div class="stat-chip">Sections <strong>3</strong></div>
  </div>
  <div class="stats-strip" id="stats-pp" style="display:none">
    <div class="stat-chip">Papers <strong>{total_pp}</strong></div>
    <div class="stat-chip">Past-paper MCQs <strong>{total_pp_mcq}</strong></div>
    <div class="stat-chip">Total questions <strong>{total_pp_qs}</strong></div>
    <div class="stat-chip">Exams <strong>4</strong></div>
  </div>

  <!-- Control panel -->
  <div class="control-panel">

    <!-- Source toggle -->
    <div class="source-toggle">
      <button class="src-btn active" id="src-mcq" onclick="setSource('mcq')">Chapter MCQs</button>
      <button class="src-btn"        id="src-pp"  onclick="setSource('pp')">Past Papers</button>
    </div>

    <!-- Chapter-MCQ controls -->
    <div id="mcq-controls">
      <div class="control-row">
        <div class="ctrl-group">
          <span class="ctrl-label">Section</span>
          <select class="ctrl-select" id="section-select" onchange="onSectionChange()">
            {section_options}
          </select>
        </div>
        <div class="ctrl-group">
          <span class="ctrl-label">Chapter</span>
          <select class="ctrl-select" id="chapter-select" onchange="render()">
            <option value="all">All Chapters</option>
          </select>
        </div>
        <div class="ctrl-group">
          <span class="ctrl-label">Sort / View</span>
          <div class="mode-group">
            <button class="mode-btn active" id="mode-grouped" onclick="setMode('grouped')">Grouped</button>
            <button class="mode-btn"        id="mode-flat"    onclick="setMode('flat')">Flat</button>
          </div>
        </div>
        <div style="margin-left:auto;align-self:flex-end">
          <div class="score-display">
            Score&nbsp;<span class="score-num" id="score-num">0/0</span>
          </div>
        </div>
      </div>
      <div class="btn-row">
        <button class="btn btn-danger" onclick="resetAll()">&#8634; Reset All</button>
        <button class="btn" onclick="revealAll()">&#128065; Show All Answers</button>
        <button class="btn" onclick="collapseAll()">&#8722; Collapse All</button>
        <button class="btn" onclick="expandAll()">&#43; Expand All</button>
      </div>
      <div class="progress-wrap">
        <div class="progress-fill" id="progress-fill" style="width:0%"></div>
      </div>
      <div class="progress-text" id="progress-text">0 of {total_qs} answered</div>
    </div>

    <!-- Past-paper controls -->
    <div id="pp-controls" style="display:none">
      <div class="control-row">
        <div class="ctrl-group">
          <span class="ctrl-label">Paper Type</span>
          <select class="ctrl-select" id="pp-type-select" onchange="onPPTypeChange()">
            {pp_type_options}
          </select>
        </div>
        <div class="ctrl-group">
          <span class="ctrl-label">Paper</span>
          <select class="ctrl-select" id="pp-paper-select" onchange="renderPP()">
            <option value="all">All Papers</option>
          </select>
        </div>
        <div style="margin-left:auto;align-self:flex-end">
          <div class="score-display">
            Score&nbsp;<span class="score-num" id="pp-score-num">0/0</span>
          </div>
        </div>
      </div>
      <div class="btn-row">
        <button class="btn btn-danger" onclick="resetAllPP()">&#8634; Reset All</button>
        <button class="btn" onclick="revealAllPP()">&#128065; Show All Answers</button>
        <button class="btn" onclick="collapseAllPP()">&#8722; Collapse All</button>
        <button class="btn" onclick="expandAllPP()">&#43; Expand All</button>
      </div>
      <div class="progress-wrap">
        <div class="progress-fill" id="pp-progress-fill" style="width:0%"></div>
      </div>
      <div class="progress-text" id="pp-progress-text">0 of {total_pp_qs} attempted</div>
    </div>

  </div><!-- /control-panel -->

  <div id="content-area"></div>
</div>

<footer>
  <div class="footer-inner">
    <span>COS 333 &mdash; Programming Languages</span>
    <span id="footer-info">{total_qs} Chapter MCQs &middot; {total_chs} Chapters</span>
  </div>
</footer>

<button id="scroll-top" title="Back to top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">&uarr;</button>

<script>
const DATA    = {data_json};
const PP_DATA = {pp_json};

const SECTION_META = {{
  "Section1": {{ label: "Section 1", color: "#7c3aed", colorBg: "#f5f3ff" }},
  "Section2": {{ label: "Section 2", color: "#0284c7", colorBg: "#f0f9ff" }},
  "Section3": {{ label: "Section 3", color: "#059669", colorBg: "#ecfdf5" }}
}};

let answers   = {{}};
let revealed  = {{}};
let openState = {{}};
let viewMode   = "grouped";
let viewSource = "mcq";

const secSel    = document.getElementById("section-select");
const chSel     = document.getElementById("chapter-select");
const ppTypeSel = document.getElementById("pp-type-select");
const ppPaperSel= document.getElementById("pp-paper-select");

// ── Source toggle ─────────────────────────────────────────────────────────────

function setSource(src) {{
  viewSource = src;
  document.getElementById("src-mcq").classList.toggle("active", src === "mcq");
  document.getElementById("src-pp" ).classList.toggle("active", src === "pp");
  document.getElementById("mcq-controls").style.display = src === "mcq" ? "" : "none";
  document.getElementById("pp-controls" ).style.display = src === "pp"  ? "" : "none";
  document.getElementById("stats-mcq").style.display    = src === "mcq" ? "" : "none";
  document.getElementById("stats-pp" ).style.display    = src === "pp"  ? "" : "none";
  document.getElementById("footer-info").textContent    = src === "mcq"
    ? "{total_qs} Chapter MCQs · {total_chs} Chapters"
    : "{total_pp_qs} Past-paper Questions · {total_pp} Papers";
  if (src === "mcq") render();
  else               renderPP();
}}

// ── Utilities ─────────────────────────────────────────────────────────────────

function escHtml(s) {{
  return String(s)
    .replace(/&/g,"&amp;").replace(/</g,"&lt;")
    .replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}}

// Very light markdown→HTML for question text (handles fenced code, inline code, bold)
function mdToHtml(text) {{
  if (!text) return '';
  const parts = [];
  const re = /```(?:[a-z]*)\\n([\\s\\S]*?)```/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {{
    if (m.index > last) parts.push({{ t:'txt', s: text.slice(last, m.index) }});
    parts.push({{ t:'pre', s: m[1].replace(/\\n$/, '') }});
    last = m.index + m[0].length;
  }}
  if (last < text.length) parts.push({{ t:'txt', s: text.slice(last) }});

  return parts.map(function(seg) {{
    if (seg.t === 'pre') return '<pre class="q-pre">' + escHtml(seg.s) + '</pre>';
    let s = escHtml(seg.s);
    s = s.replace(/`([^`\\n]+)`/g, '<code class="q-code">$1</code>');
    s = s.replace(/\\*\\*([^*\\n]+)\\*\\*/g, '<strong>$1</strong>');
    s = s.replace(/\\n\\n+/g, '<br><br>').replace(/\\n/g, '<br>');
    return s;
  }}).join('');
}}

// ── Chapter MCQ rendering (unchanged) ─────────────────────────────────────────

function onSectionChange() {{
  const sec = secSel.value;
  chSel.innerHTML = '<option value="all">All Chapters</option>';
  const pool = sec === "all" ? DATA : DATA.filter(c => c.section === sec);
  pool.forEach(c => {{
    const opt = document.createElement("option");
    opt.value = c.chKey;
    opt.textContent = c.chapter + " — " + c.title;
    chSel.appendChild(opt);
  }});
  render();
}}

function setMode(m) {{
  viewMode = m;
  ["grouped","flat"].forEach(x => {{
    document.getElementById("mode-"+x).classList.toggle("active", x===m);
  }});
  render();
}}

function getFilteredChapters() {{
  const sec = secSel.value;
  const ch  = chSel.value;
  let pool = sec === "all" ? DATA : DATA.filter(c => c.section === sec);
  if (ch !== "all") pool = pool.filter(c => c.chKey === ch);
  return pool;
}}

function renderMCQ(mcq, key, qNum, total) {{
  const ans = answers[key];
  const isLocked   = ans !== undefined;
  const isRevealed = revealed[key];
  const letters    = ["A","B","C","D","E","F","G","H","I","J"];

  // Use original exam Q number if provided
  const dispNum = mcq.q_num !== undefined ? mcq.q_num : qNum;

  let opts = "";
  mcq.opts.forEach(function(opt, oi) {{
    const letter = letters[oi];
    let cls = "mcq-opt";
    if (isLocked || isRevealed) {{
      cls += " locked";
      if (letter === mcq.answer) cls += " correct";
      else if (ans && ans.chosen === letter) cls += " wrong";
    }}
    opts += '<li class="' + cls + '" data-key="' + escHtml(key) + '" data-oi="' + oi
          + '" data-ans="' + escHtml(mcq.answer) + '" onclick="handlePick(this)">'
          + '<span class="opt-letter">' + letter + '</span><span>' + escHtml(opt) + '</span></li>';
  }});

  let feedback = "";
  if (isLocked || isRevealed) {{
    const correct  = ans ? ans.chosen === mcq.answer : true;
    const cls2     = (isRevealed && !ans) ? "fb-correct" : (correct ? "fb-correct" : "fb-wrong");
    const icon     = (isRevealed && !ans) ? "&#8594;" : (correct ? "&#10003;" : "&#10007;");
    const prefix   = (isRevealed && !ans)
      ? ("Answer: <strong>" + mcq.answer + "</strong>. ")
      : (correct ? "Correct! " : "Answer is <strong>" + mcq.answer + "</strong>. ");
    feedback = '<div class="mcq-feedback show ' + cls2 + '">' + icon + " " + prefix + escHtml(mcq.explanation) + "</div>";
  }}

  const topicTag   = mcq.topic ? '<span class="topic-tag">' + escHtml(mcq.topic) + '</span>' : '';
  const marksBadge = (mcq.marks && mcq.marks > 1)
    ? '<span class="pp-marks-badge">' + mcq.marks + ' marks</span>' : '';

  return '<div class="mcq-block" id="mcq-' + escHtml(key) + '">'
       + '<div class="mcq-meta">'
       + '<span class="mcq-num">Q' + dispNum + ' / ' + total + '</span>'
       + marksBadge
       + topicTag
       + '</div>'
       + '<div class="mcq-q">' + mdToHtml(mcq.q) + '</div>'
       + '<ul class="mcq-opts">' + opts + '</ul>'
       + feedback
       + '</div>';
}}

function handlePick(el) {{
  const key = el.dataset.key;
  const oi  = parseInt(el.dataset.oi);
  const correctAnswer = el.dataset.ans;
  if (answers[key] !== undefined || revealed[key]) return;
  const letters = ["A","B","C","D"];
  answers[key] = {{ chosen: letters[oi], correct: letters[oi] === correctAnswer }};

  const chKey = key.split("__")[0];
  const qi    = parseInt(key.split("__")[1]);

  // Find in chapter data or past-paper data
  const ch = DATA.find(c => c.chKey === chKey);
  let mcq, total;
  if (ch) {{
    mcq   = ch.mcqs[qi];
    total = ch.mcqs.length;
  }} else {{
    const paper = PP_DATA.find(p => p.key === chKey);
    if (!paper) return;
    mcq   = paper.questions[qi];
    total = paper.questions.length;
  }}

  const el2 = document.getElementById("mcq-" + key);
  if (el2) el2.outerHTML = renderMCQ(mcq, key, qi + 1, total);

  if (viewSource === "pp") updatePPScore();
  else                     updateScore();
}}

function renderChapterBlock(ch) {{
  const bodyId = "chbody-" + ch.chKey;
  const isOpen = openState[ch.chKey] !== false;
  const sm     = SECTION_META[ch.section] || {{}};

  let mcqHtml = "";
  ch.mcqs.forEach(function(mcq, qi) {{
    mcqHtml += renderMCQ(mcq, ch.chKey + "__" + qi, qi+1, ch.mcqs.length);
  }});

  return '<div class="chapter-block">'
    + '<div class="chapter-header" data-chkey="' + escHtml(ch.chKey) + '" onclick="toggleChapter(this.dataset.chkey)">'
    + '<span class="ch-badge" style="background:' + escHtml(ch.colorBg) + ';color:' + escHtml(ch.color) + ';border:1px solid ' + escHtml(ch.color) + '20">'
    + escHtml(ch.chapter) + '</span>'
    + '<span class="ch-title">' + escHtml(ch.title) + '</span>'
    + '<span class="ch-meta">' + ch.mcqs.length + ' MCQs</span>'
    + '<span class="ch-chevron" id="chev-' + ch.chKey + '">' + (isOpen ? "&#9650;" : "&#9660;") + '</span>'
    + '</div>'
    + '<div class="chapter-body' + (isOpen ? '' : ' collapsed') + '" id="' + bodyId + '">'
    + mcqHtml
    + '</div></div>';
}}

function toggleChapter(chKey) {{
  const body = document.getElementById("chbody-" + chKey);
  const chev = document.getElementById("chev-"   + chKey);
  if (!body) return;
  body.classList.toggle("collapsed");
  const open = !body.classList.contains("collapsed");
  openState[chKey] = open;
  if (chev) chev.innerHTML = open ? "&#9650;" : "&#9660;";
}}

function render() {{
  const chapters = getFilteredChapters();
  const area     = document.getElementById("content-area");

  if (chapters.length === 0) {{
    area.innerHTML = '<div class="empty-state"><p>No chapters match the selected filters.</p></div>';
    updateScore();
    return;
  }}

  let html = "";
  if (viewMode === "flat") {{
    chapters.forEach(ch => {{ html += renderChapterBlock(ch); }});
  }} else {{
    const seenSections = [];
    chapters.forEach(ch => {{
      if (!seenSections.includes(ch.section)) seenSections.push(ch.section);
    }});
    seenSections.forEach(sec => {{
      const secChs = chapters.filter(c => c.section === sec);
      const sm     = SECTION_META[sec] || {{}};
      const totalInSec = secChs.reduce((a,c) => a + c.mcqs.length, 0);
      html += '<div class="section-block">'
            + '<div class="section-header">'
            + '<span class="section-pill" style="background:' + (sm.colorBg||'var(--surface2)') + ';color:' + (sm.color||'var(--muted)') + ';border:1px solid ' + (sm.color||'var(--border)') + '30">'
            + escHtml(sm.label || sec) + '</span>'
            + '<span class="section-count">' + secChs.length + ' chapters &middot; ' + totalInSec + ' MCQs</span>'
            + '</div>';
      secChs.forEach(ch => {{ html += renderChapterBlock(ch); }});
      html += '</div>';
    }});
  }}

  area.innerHTML = html;
  updateScore();
}}

function updateScore() {{
  const chapters = getFilteredChapters();
  let total = 0, answered = 0, correct = 0;
  chapters.forEach(ch => {{
    ch.mcqs.forEach((_, qi) => {{
      total++;
      const key = ch.chKey + "__" + qi;
      if (answers[key] !== undefined) {{
        answered++;
        if (answers[key].correct) correct++;
      }}
    }});
  }});
  document.getElementById("score-num").textContent = correct + "/" + answered;
  const pct = total > 0 ? (answered / total * 100) : 0;
  document.getElementById("progress-fill").style.width = pct + "%";
  const pctCorrect = answered > 0 ? Math.round(correct/answered*100) : 0;
  document.getElementById("progress-text").textContent =
    answered + " of " + total + " answered · " + correct + " correct (" + pctCorrect + "%)";
}}

function resetAll() {{
  if (!confirm("Reset all answers for the current filter?")) return;
  getFilteredChapters().forEach(ch => {{
    ch.mcqs.forEach((_, qi) => {{
      const key = ch.chKey + "__" + qi;
      delete answers[key];
      delete revealed[key];
    }});
  }});
  render();
}}

function revealAll() {{
  getFilteredChapters().forEach(ch => {{
    ch.mcqs.forEach((_, qi) => {{
      const key = ch.chKey + "__" + qi;
      if (answers[key] === undefined) revealed[key] = true;
    }});
  }});
  render();
}}

function collapseAll() {{
  getFilteredChapters().forEach(ch => {{ openState[ch.chKey] = false; }});
  render();
}}

function expandAll() {{
  getFilteredChapters().forEach(ch => {{ openState[ch.chKey] = true; }});
  render();
}}

// ── Past-paper rendering ──────────────────────────────────────────────────────

function onPPTypeChange() {{
  const t = ppTypeSel.value;
  ppPaperSel.innerHTML = '<option value="all">All Papers</option>';
  const pool = t === "all" ? PP_DATA : PP_DATA.filter(p => p.type === t);
  pool.forEach(p => {{
    const o = document.createElement("option");
    o.value = p.key;
    o.textContent = p.label;
    ppPaperSel.appendChild(o);
  }});
  renderPP();
}}

function getFilteredPapers() {{
  const t = ppTypeSel.value;
  const k = ppPaperSel.value;
  let pool = t === "all" ? PP_DATA : PP_DATA.filter(p => p.type === t);
  if (k !== "all") pool = pool.filter(p => p.key === k);
  return pool;
}}

// Render a reveal card for multi-select, short-answer, or coding questions
function renderRevealCard(q, key) {{
  const isRevealed = revealed[key];
  const letters    = ["A","B","C","D","E","F","G","H","I","J"];

  // ── Build answer display ────────────────────────────────────────────────────
  let ansHtml = "";
  if (isRevealed) {{
    ansHtml += '<div class="pp-ans-label">Answer</div>';

    if (q.type === "code") {{
      ansHtml += '<code class="pp-ans-code">' + escHtml(String(q.answer)) + '</code>';
    }} else if (q.type === "multi") {{
      ansHtml += '<ul class="pp-ans-list">'
        + (q.answer_list || []).map(a => '<li>' + escHtml(a) + '</li>').join('')
        + '</ul>';
    }} else if (q.answer !== null && typeof q.answer === 'object') {{
      // Structured answer dict
      ansHtml += '<dl class="pp-ans-dict">'
        + Object.entries(q.answer).map(([k2,v]) =>
            '<dt>' + escHtml(k2.replace(/_/g,' ')) + '</dt><dd>' + escHtml(String(v)) + '</dd>'
          ).join('')
        + '</dl>';
    }} else {{
      ansHtml += '<span class="pp-ans-text">' + escHtml(String(q.answer)) + '</span>';
    }}

    if (q.explanation) {{
      ansHtml += '<div class="pp-exp">' + escHtml(q.explanation) + '</div>';
    }}
  }}

  // ── Build options (for multi-select, show after reveal) ────────────────────
  let optsHtml = "";
  if (q.type === "multi" && q.opts) {{
    q.opts.forEach(function(opt, oi) {{
      const letter  = letters[oi];
      const correct = isRevealed && q.answer_list && q.answer_list.includes(opt);
      optsHtml += '<li class="mcq-opt locked' + (correct ? ' correct' : '') + '">'
                + '<span class="opt-letter">' + letter + '</span>'
                + '<span>' + escHtml(opt) + '</span></li>';
    }});
  }}

  // ── Type badge ──────────────────────────────────────────────────────────────
  const typeLabel = q.type === "code"  ? "&#128196; Coding"
                  : q.type === "multi" ? "&#9745; Multi-select"
                  :                      "&#9998; Short answer";
  const marksLabel = q.marks === 1 ? "1 mark" : q.marks + " marks";
  const btnClass   = "pp-reveal-btn" + (isRevealed ? " revealed" : "");
  const btnText    = isRevealed ? "&#8593; Hide" : "&#9654; Reveal Answer";

  return '<div class="mcq-block" id="mcq-' + escHtml(key) + '">'
       + '<div class="mcq-meta">'
       + '<span class="mcq-num">Q' + escHtml(String(q.q_num)) + '</span>'
       + '<span class="pp-marks-badge">' + marksLabel + '</span>'
       + '<span class="pp-type-badge">'  + typeLabel  + '</span>'
       + (q.topic ? '<span class="topic-tag">' + escHtml(q.topic) + '</span>' : '')
       + '<button class="' + btnClass + '" data-key="' + escHtml(key) + '" onclick="toggleReveal(this.dataset.key)">'
       + btnText + '</button>'
       + '</div>'
       + '<div class="mcq-q">' + mdToHtml(q.q) + '</div>'
       + (optsHtml ? '<ul class="mcq-opts">' + optsHtml + '</ul>' : '')
       + (isRevealed ? '<div class="mcq-feedback show fb-correct">' + ansHtml + '</div>' : '')
       + '</div>';
}}

function toggleReveal(key) {{
  const chKey = key.split("__")[0];
  const qi    = parseInt(key.split("__")[1]);
  const paper = PP_DATA.find(p => p.key === chKey);
  if (!paper) return;

  if (revealed[key]) delete revealed[key];
  else               revealed[key] = true;

  const q   = paper.questions[qi];
  const el  = document.getElementById("mcq-" + key);
  if (el) el.outerHTML = renderRevealCard(q, key);
  updatePPScore();
}}

function renderPPQuestion(q, key, idx, total) {{
  if (q.type === "mcq") return renderMCQ(q, key, idx + 1, total);
  return renderRevealCard(q, key);
}}

function renderPaperBlock(paper) {{
  const bodyId = "ppbody-" + paper.key;
  const isOpen = openState[paper.key] !== false;

  let qHtml = "";
  paper.questions.forEach(function(q, qi) {{
    qHtml += renderPPQuestion(q, paper.key + "__" + qi, qi, paper.questions.length);
  }});

  const nonMcq = paper.count - paper.mcqCount;
  const metaStr = paper.mcqCount + " MCQ"
    + (nonMcq > 0 ? " &middot; " + nonMcq + " other" : "")
    + " &middot; " + paper.totalMarks + " marks";

  return '<div class="chapter-block">'
    + '<div class="chapter-header" data-chkey="' + escHtml(paper.key) + '" onclick="togglePaper(this.dataset.chkey)">'
    + '<span class="ch-badge" style="background:' + escHtml(paper.colorBg) + ';color:' + escHtml(paper.color) + ';border:1px solid ' + escHtml(paper.color) + '20">'
    + escHtml(paper.type) + ' ' + paper.year + '</span>'
    + '<span class="ch-title">' + escHtml(paper.label) + '</span>'
    + '<span class="ch-meta">' + metaStr + '</span>'
    + '<span class="ch-chevron" id="ppchev-' + paper.key + '">' + (isOpen ? "&#9650;" : "&#9660;") + '</span>'
    + '</div>'
    + '<div class="chapter-body' + (isOpen ? '' : ' collapsed') + '" id="' + bodyId + '">'
    + qHtml
    + '</div></div>';
}}

function togglePaper(pKey) {{
  const body = document.getElementById("ppbody-"  + pKey);
  const chev = document.getElementById("ppchev-"  + pKey);
  if (!body) return;
  body.classList.toggle("collapsed");
  const open = !body.classList.contains("collapsed");
  openState[pKey] = open;
  if (chev) chev.innerHTML = open ? "&#9650;" : "&#9660;";
}}

function renderPP() {{
  const papers = getFilteredPapers();
  const area   = document.getElementById("content-area");

  if (papers.length === 0) {{
    area.innerHTML = '<div class="empty-state"><p>No papers match the selected filters.</p></div>';
    updatePPScore();
    return;
  }}

  let html = "";
  papers.forEach(paper => {{ html += renderPaperBlock(paper); }});
  area.innerHTML = html;
  updatePPScore();
}}

function updatePPScore() {{
  const papers = getFilteredPapers();
  let total = 0, mcqAnswered = 0, mcqCorrect = 0, revealedCount = 0;

  papers.forEach(function(paper) {{
    paper.questions.forEach(function(q, qi) {{
      const key = paper.key + "__" + qi;
      total++;
      if (q.type === "mcq") {{
        if (answers[key] !== undefined) {{
          mcqAnswered++;
          if (answers[key].correct) mcqCorrect++;
        }}
      }} else {{
        if (revealed[key]) revealedCount++;
      }}
    }});
  }});

  document.getElementById("pp-score-num").textContent = mcqCorrect + "/" + mcqAnswered;
  const attempted = mcqAnswered + revealedCount;
  const pct = total > 0 ? (attempted / total * 100) : 0;
  document.getElementById("pp-progress-fill").style.width = pct + "%";
  const pctCorrect = mcqAnswered > 0 ? Math.round(mcqCorrect / mcqAnswered * 100) : 0;
  document.getElementById("pp-progress-text").textContent =
    attempted + " of " + total + " attempted"
    + " · MCQ: " + mcqCorrect + "/" + mcqAnswered + " (" + pctCorrect + "%)"
    + " · Revealed: " + revealedCount;
}}

function resetAllPP() {{
  if (!confirm("Reset all answers for the current filter?")) return;
  getFilteredPapers().forEach(function(paper) {{
    paper.questions.forEach(function(_, qi) {{
      const key = paper.key + "__" + qi;
      delete answers[key];
      delete revealed[key];
    }});
  }});
  renderPP();
}}

function revealAllPP() {{
  getFilteredPapers().forEach(function(paper) {{
    paper.questions.forEach(function(q, qi) {{
      const key = paper.key + "__" + qi;
      if (q.type !== "mcq") revealed[key] = true;
      else if (answers[key] === undefined) revealed[key] = true;
    }});
  }});
  renderPP();
}}

function collapseAllPP() {{
  getFilteredPapers().forEach(function(p) {{ openState[p.key] = false; }});
  renderPP();
}}

function expandAllPP() {{
  getFilteredPapers().forEach(function(p) {{ openState[p.key] = true; }});
  renderPP();
}}

// ── Scroll-to-top ─────────────────────────────────────────────────────────────

window.addEventListener("scroll", () => {{
  document.getElementById("scroll-top").classList.toggle("visible", window.scrollY > 400);
}});

// ── Init ──────────────────────────────────────────────────────────────────────
onSectionChange();  // populates chapter dropdown then calls render()
</script>
</body>
</html>"""


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("Loading chapter MCQ data...")
    chapters = load_all_mcqs()
    total_ch = sum(c["count"] for c in chapters)
    print(f"  {len(chapters)} chapters, {total_ch} MCQs")
    for c in chapters:
        print(f"    {c['section']} / {c['chKey']:20s}  {c['count']:>3} MCQs  —  {c['title']}")

    print("\nLoading past-paper data...")
    papers = load_all_past_papers()
    total_pp = sum(p["count"] for p in papers)
    total_pp_mcq = sum(p["mcqCount"] for p in papers)
    print(f"  {len(papers)} papers, {total_pp} questions ({total_pp_mcq} MCQ)")
    for p in papers:
        non_mcq = p["count"] - p["mcqCount"]
        print(f"    {p['key']:15s}  {p['mcqCount']:>2} MCQ  {non_mcq:>2} other  —  {p['label']}")

    print(f"\nGenerating HTML → {OUTPUT_FILE}")
    html = build_html(chapters, papers)
    OUTPUT_FILE.write_text(html, encoding="utf-8")
    size_kb = OUTPUT_FILE.stat().st_size // 1024
    print(f"  Done. File size: {size_kb} KB")
    print(f"\nOpen in browser:")
    print(f"  open \"{OUTPUT_FILE}\"")


if __name__ == "__main__":
    main()
