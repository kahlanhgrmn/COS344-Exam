#!/usr/bin/env python3
"""
generate_mcq_page.py
Reads all chapter *_mcq.json files and produces a single self-contained
interactive HTML MCQ page in the COS344 study-hub style.

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

# ── Load data ─────────────────────────────────────────────────────────────────

def load_all_mcqs() -> list[dict]:
    """Return a flat list of chapter dicts, each with section metadata."""
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
                # Find letter for correct answer
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
                "id":        ch_dir.upper().replace("_", ""),   # e.g. CHAPTER01
                "chKey":     ch_dir,                            # e.g. chapter_01
                "section":   section_name,                      # e.g. Section1
                "sectionLabel": smeta["label"],
                "color":     smeta["color"],
                "colorBg":   smeta["color_bg"],
                "title":     data.get("title", ch_dir),
                "chapter":   data.get("chapter", ""),
                "count":     len(questions),
                "mcqs":      questions,
            })
    return chapters

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
.mcq-meta{display:flex;align-items:center;gap:.6rem;margin-bottom:.5rem}
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


def build_html(chapters: list[dict]) -> str:
    total_qs    = sum(c["count"] for c in chapters)
    total_chs   = len(chapters)

    # Serialize chapters to JSON for JavaScript
    data_json = json.dumps(chapters, ensure_ascii=False)

    # Section options for filter
    section_options = '<option value="all">All Sections</option>'
    for skey, smeta in SECTION_META.items():
        section_options += f'<option value="{skey}">{smeta["label"]}</option>'

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
      {total_qs} MCQs across {total_chs} chapters and 3 sections.
      Click an option to check your answer instantly.
    </p>
  </div>

  <div class="stats-strip">
    <div class="stat-chip">Chapters <strong>{total_chs}</strong></div>
    <div class="stat-chip">Total MCQs <strong>{total_qs}</strong></div>
    <div class="stat-chip">Per chapter <strong>20</strong></div>
    <div class="stat-chip">Sections <strong>3</strong></div>
  </div>

  <!-- Control panel -->
  <div class="control-panel">
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
          <button class="mode-btn" id="mode-flat" onclick="setMode('flat')">Flat</button>
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

  <div id="content-area"></div>
</div>

<footer>
  <div class="footer-inner">
    <span>COS 333 &mdash; Programming Languages</span>
    <span>{total_qs} MCQs &middot; {total_chs} Chapters</span>
  </div>
</footer>

<button id="scroll-top" title="Back to top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">&uarr;</button>

<script>
const DATA = {data_json};

const SECTION_META = {{
  "Section1": {{ label: "Section 1", color: "#7c3aed", colorBg: "#f5f3ff" }},
  "Section2": {{ label: "Section 2", color: "#0284c7", colorBg: "#f0f9ff" }},
  "Section3": {{ label: "Section 3", color: "#059669", colorBg: "#ecfdf5" }}
}};

let answers  = {{}};
let revealed = {{}};
let openState = {{}};
let viewMode = "grouped";

const secSel = document.getElementById("section-select");
const chSel  = document.getElementById("chapter-select");

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

function escHtml(s) {{
  return String(s)
    .replace(/&/g,"&amp;").replace(/</g,"&lt;")
    .replace(/>/g,"&gt;").replace(/"/g,"&quot;");
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
  const isLocked = ans !== undefined;
  const isRevealed = revealed[key];
  const letters = ["A","B","C","D"];

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
    const correct = ans ? ans.chosen === mcq.answer : true;
    const cls2 = (isRevealed && !ans) ? "fb-correct" : (correct ? "fb-correct" : "fb-wrong");
    const icon = (isRevealed && !ans) ? "&#8594;" : (correct ? "&#10003;" : "&#10007;");
    const prefix = (isRevealed && !ans)
      ? ("Answer: <strong>" + mcq.answer + "</strong>. ")
      : (correct ? "Correct! " : "Answer is <strong>" + mcq.answer + "</strong>. ");
    feedback = '<div class="mcq-feedback show ' + cls2 + '">' + icon + " " + prefix + escHtml(mcq.explanation) + "</div>";
  }}

  const topicTag = mcq.topic ? '<span class="topic-tag">' + escHtml(mcq.topic) + '</span>' : '';

  return '<div class="mcq-block" id="mcq-' + escHtml(key) + '">'
       + '<div class="mcq-meta"><span class="mcq-num">Q' + qNum + ' / ' + total + '</span>' + topicTag + '</div>'
       + '<div class="mcq-q">' + escHtml(mcq.q) + '</div>'
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
  // Find the chapter that owns this key and re-render just that block
  const chKey = key.split("__")[0];
  const ch = DATA.find(c => c.chKey === chKey);
  if (!ch) return;
  const qi = parseInt(key.split("__")[1]);
  const el2 = document.getElementById("mcq-" + key);
  if (el2) el2.outerHTML = renderMCQ(ch.mcqs[qi], key, qi+1, ch.mcqs.length);
  updateScore();
}}

function renderChapterBlock(ch) {{
  const bodyId = "chbody-" + ch.chKey;
  const isOpen = openState[ch.chKey] !== false; // default open
  const sm = SECTION_META[ch.section] || {{}};

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
  const chev = document.getElementById("chev-" + chKey);
  if (!body) return;
  const isNowOpen = body.classList.toggle("collapsed");
  // collapsed class added = now closed; NOT present = open
  const open = !body.classList.contains("collapsed");
  openState[chKey] = open;
  if (chev) chev.innerHTML = open ? "&#9650;" : "&#9660;";
}}

function render() {{
  const chapters = getFilteredChapters();
  const area = document.getElementById("content-area");

  if (chapters.length === 0) {{
    area.innerHTML = '<div class="empty-state"><p>No chapters match the selected filters.</p></div>';
    updateScore();
    return;
  }}

  let html = "";

  if (viewMode === "flat") {{
    // Single flat list, no section grouping
    chapters.forEach(ch => {{ html += renderChapterBlock(ch); }});
  }} else {{
    // Grouped by section
    const seenSections = [];
    chapters.forEach(ch => {{
      if (!seenSections.includes(ch.section)) seenSections.push(ch.section);
    }});
    seenSections.forEach(sec => {{
      const secChs = chapters.filter(c => c.section === sec);
      const sm = SECTION_META[sec] || {{}};
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
  const chapters = getFilteredChapters();
  chapters.forEach(ch => {{
    ch.mcqs.forEach((_, qi) => {{
      const key = ch.chKey + "__" + qi;
      delete answers[key];
      delete revealed[key];
    }});
  }});
  render();
}}

function revealAll() {{
  const chapters = getFilteredChapters();
  chapters.forEach(ch => {{
    ch.mcqs.forEach((_, qi) => {{
      const key = ch.chKey + "__" + qi;
      if (answers[key] === undefined) revealed[key] = true;
    }});
  }});
  render();
}}

function collapseAll() {{
  const chapters = getFilteredChapters();
  chapters.forEach(ch => {{ openState[ch.chKey] = false; }});
  render();
}}

function expandAll() {{
  const chapters = getFilteredChapters();
  chapters.forEach(ch => {{ openState[ch.chKey] = true; }});
  render();
}}

// Scroll-to-top button
window.addEventListener("scroll", () => {{
  document.getElementById("scroll-top").classList.toggle("visible", window.scrollY > 400);
}});

// Initial render
onSectionChange(); // populates chapter dropdown then calls render()
</script>
</body>
</html>"""


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("Loading MCQ data...")
    chapters = load_all_mcqs()

    total = sum(c["count"] for c in chapters)
    print(f"  Loaded {len(chapters)} chapters, {total} questions total")
    for c in chapters:
        print(f"    {c['section']} / {c['chKey']:20s}  {c['count']:>3} MCQs  —  {c['title']}")

    print(f"\nGenerating HTML → {OUTPUT_FILE}")
    html = build_html(chapters)
    OUTPUT_FILE.write_text(html, encoding="utf-8")
    size_kb = OUTPUT_FILE.stat().st_size // 1024
    print(f"  Done. File size: {size_kb} KB")
    print(f"\nOpen in browser:")
    print(f"  open \"{OUTPUT_FILE}\"")


if __name__ == "__main__":
    main()
