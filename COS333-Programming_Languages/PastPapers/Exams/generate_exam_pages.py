#!/usr/bin/env python3
"""Generate interactive HTML exam pages from the memo JSON files."""

import json
import html
import re
import os

YEARS = ["2022", "2023", "2024", "2025"]
BASE = os.path.dirname(os.path.abspath(__file__))


def md_inline(text):
    """Convert inline markdown to HTML: bold, italic, code, backtick code."""
    text = html.escape(text)
    # code blocks ``` ... ``` (multi-line) → <pre><code>
    text = re.sub(r'```(\w+)?\n(.*?)```', lambda m: f'<pre><code>{m.group(2)}</code></pre>', text, flags=re.DOTALL)
    # inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # italic (single *)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text


def render_question_text(raw):
    """Convert question_text (markdown) to HTML."""
    raw = raw.replace('\r\n', '\n').replace('\r', '\n')
    lines = raw.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # fenced code block
        if line.strip().startswith('```'):
            lang = line.strip()[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(html.escape(lines[i]))
                i += 1
            out.append(f'<pre><code>{chr(10).join(code_lines)}</code></pre>')
        # bullet list item
        elif line.strip().startswith('- '):
            out.append(f'<li>{md_inline(line.strip()[2:])}</li>')
        # blank line
        elif line.strip() == '':
            out.append('')
        else:
            out.append(f'<p>{md_inline(line)}</p>')
        i += 1
    # wrap consecutive <li> in <ul>
    result = '\n'.join(out)
    result = re.sub(r'((?:<li>.*?</li>\n?)+)', r'<ul>\1</ul>', result, flags=re.DOTALL)
    return result


def detect_type(q):
    """Detect question type: mcq, multiselect, code_scheme, code_prolog, short."""
    topic = q.get("topic", "")
    opts = q.get("options")
    ans = q.get("answer")
    if "Scheme" in topic:
        return "code_scheme"
    if "Prolog" in topic:
        return "code_prolog"
    if opts and isinstance(ans, list):
        return "multiselect"
    if opts:
        return "mcq"
    return "short"


def render_mcq(q, qid):
    letters = "ABCDE"
    opts_html = ""
    correct = q["answer"]
    for idx, opt in enumerate(q["options"]):
        letter = letters[idx]
        escaped = md_inline(opt)
        opts_html += f'''
        <li class="mcq-opt" onclick="checkMCQ(this, '{qid}', {json.dumps(opt == correct)})">
          <span class="opt-letter">{letter}.</span>
          <span>{escaped}</span>
        </li>'''
    exp = html.escape(q.get("explanation", ""))
    return f'''
  <div class="q-block" id="{qid}">
    <div class="q-meta"><span class="q-num-badge">Q{q["question"]}</span> <span class="q-marks">{q["marks"]} mark{"s" if q["marks"]!=1 else ""}</span> <span class="q-topic">{html.escape(q["topic"])}</span></div>
    <div class="q-text">{render_question_text(q["question_text"])}</div>
    <ul class="mcq-opts">{opts_html}
    </ul>
    <div class="q-feedback" id="{qid}-fb"></div>
    <div class="q-explanation hidden" id="{qid}-exp">
      <div class="exp-label">Explanation</div>
      <p>{exp}</p>
    </div>
  </div>'''


def render_multiselect(q, qid):
    letters = "ABCD"
    correct_set = set(q["answer"]) if isinstance(q["answer"], list) else {q["answer"]}
    opts_html = ""
    for idx, opt in enumerate(q["options"]):
        letter = letters[idx]
        escaped = md_inline(opt)
        is_correct = json.dumps(opt in correct_set)
        opts_html += f'''
        <li class="mcq-opt ms-opt" data-correct="{is_correct}" onclick="toggleMS(this, '{qid}')">
          <span class="opt-letter">{letter}.</span>
          <span>{escaped}</span>
        </li>'''
    exp = html.escape(q.get("explanation", ""))
    return f'''
  <div class="q-block" id="{qid}">
    <div class="q-meta"><span class="q-num-badge">Q{q["question"]}</span> <span class="q-marks">{q["marks"]} marks</span> <span class="q-topic">{html.escape(q["topic"])}</span> <span class="q-multi-badge">Select all that apply</span></div>
    <div class="q-text">{render_question_text(q["question_text"])}</div>
    <ul class="mcq-opts">{opts_html}
    </ul>
    <button class="btn-check-ms" onclick="checkMS('{qid}', {json.dumps(list(correct_set))})">Check Selection</button>
    <div class="q-feedback" id="{qid}-fb"></div>
    <div class="q-explanation hidden" id="{qid}-exp">
      <div class="exp-label">Explanation</div>
      <p>{exp}</p>
    </div>
  </div>'''


def render_code(q, qid, lang):
    label = "Scheme" if lang == "scheme" else "Prolog"
    placeholder = "; Write your Scheme function here..." if lang == "scheme" else "% Write your Prolog clauses here..."
    answer_esc = html.escape(q["answer"])
    exp = html.escape(q.get("explanation", ""))
    return f'''
  <div class="q-block code-q" id="{qid}">
    <div class="q-meta"><span class="q-num-badge">Q{q["question"]}</span> <span class="q-marks">{q["marks"]} marks</span> <span class="q-topic">{html.escape(q["topic"])}</span> <span class="lang-badge lang-{lang}">{label}</span></div>
    <div class="q-text">{render_question_text(q["question_text"])}</div>
    <div class="answer-label">Your Answer <span class="lang-tag">{label}</span></div>
    <textarea class="code-editor" id="{qid}-answer" placeholder="{placeholder}"></textarea>
    <div class="code-actions">
      <button class="btn-show-sol" onclick="toggleSol('{qid}')">Show Solution</button>
      <button class="btn-compare" onclick="compareCode('{qid}')">Compare</button>
      <button class="btn-clear" onclick="clearCode('{qid}')">Clear</button>
    </div>
    <div class="solution-block hidden" id="{qid}-sol">
      <div class="sol-label">Memo Solution</div>
      <pre><code>{answer_esc}</code></pre>
      <div class="exp-label">Explanation</div>
      <p>{exp}</p>
    </div>
    <div class="compare-block hidden" id="{qid}-cmp">
      <div class="cmp-grid">
        <div><div class="cmp-label yours">Your Answer</div><div class="compare-code empty" id="{qid}-yours"></div></div>
        <div><div class="cmp-label memo">Memo</div><div class="compare-code"><pre>{answer_esc}</pre></div></div>
      </div>
    </div>
  </div>'''


def render_short(q, qid):
    ans = q["answer"]
    if isinstance(ans, list):
        ans_str = ", ".join(ans)
    else:
        ans_str = str(ans)
    exp = html.escape(q.get("explanation", ""))
    return f'''
  <div class="q-block short-q" id="{qid}">
    <div class="q-meta"><span class="q-num-badge">Q{q["question"]}</span> <span class="q-marks">{q["marks"]} mark{"s" if q["marks"]!=1 else ""}</span> <span class="q-topic">{html.escape(q["topic"])}</span></div>
    <div class="q-text">{render_question_text(q["question_text"])}</div>
    <input type="text" class="short-input" id="{qid}-inp" placeholder="Type your answer...">
    <div class="code-actions">
      <button class="btn-show-sol" onclick="toggleSol('{qid}')">Show Answer</button>
    </div>
    <div class="solution-block hidden" id="{qid}-sol">
      <div class="sol-label">Answer</div>
      <p><strong>{html.escape(ans_str)}</strong></p>
      <div class="exp-label">Explanation</div>
      <p>{exp}</p>
    </div>
  </div>'''


def generate_page(year, data):
    exam_info = f"{data.get('date', year)} · {data.get('duration', '3 hours')} · {data.get('total_marks', 40)} marks"
    questions_html = ""
    mcq_count = 0
    total_mcq = 0
    for q in data["questions"]:
        qid = f"q{q['question']}"
        qtype = detect_type(q)
        if qtype == "mcq":
            questions_html += render_mcq(q, qid)
            total_mcq += 1
        elif qtype == "multiselect":
            questions_html += render_multiselect(q, qid)
        elif qtype == "code_scheme":
            questions_html += render_code(q, qid, "scheme")
        elif qtype == "code_prolog":
            questions_html += render_code(q, qid, "prolog")
        else:
            questions_html += render_short(q, qid)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{year} Examination — COS 333</title>
<link rel="stylesheet" href="../../../../style.css">
<style>
  .q-block {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.3rem 1.4rem;
    margin-bottom: 1.2rem;
    box-shadow: var(--shadow);
  }}
  .q-meta {{
    display: flex;
    align-items: center;
    gap: .6rem;
    flex-wrap: wrap;
    margin-bottom: .9rem;
  }}
  .q-num-badge {{
    font-family: var(--mono);
    font-size: .7rem;
    font-weight: 700;
    background: var(--navy);
    color: #fff;
    border-radius: 4px;
    padding: .2em .65em;
  }}
  .q-marks {{
    font-family: var(--mono);
    font-size: .7rem;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: .2em .55em;
    color: var(--muted);
  }}
  .q-topic {{
    font-size: .78rem;
    color: var(--muted);
    flex: 1;
  }}
  .q-multi-badge {{
    font-family: var(--mono);
    font-size: .65rem;
    font-weight: 600;
    background: var(--warn-bg);
    color: var(--warn);
    border: 1px solid #fcd34d;
    border-radius: 3px;
    padding: .15em .55em;
  }}
  .lang-badge {{
    font-family: var(--mono);
    font-size: .65rem;
    font-weight: 700;
    border-radius: 3px;
    padding: .15em .6em;
    text-transform: uppercase;
    letter-spacing: .04em;
  }}
  .lang-scheme {{ background: var(--accent2-bg); color: var(--accent2); border: 1px solid #6ee7be; }}
  .lang-prolog  {{ background: var(--accent-bg);  color: var(--accent);  border: 1px solid #bfdbfe; }}

  .q-text {{ font-size: .92rem; margin-bottom: .9rem; }}
  .q-text p {{ margin: 0 0 .5rem; }}
  .q-text ul {{ margin: .3rem 0 .6rem; padding-left: 1.3rem; }}
  .q-text pre {{ margin: .6rem 0; }}

  /* MCQ */
  .mcq-opts {{ list-style:none; padding:0; display:flex; flex-direction:column; gap:.35rem; margin:0 0 .75rem; }}
  .mcq-opt {{
    padding:.5rem .85rem; border-radius:5px;
    border:1.5px solid var(--border); background:var(--bg);
    cursor:pointer; font-size:.88rem; transition:all .15s;
    display:flex; gap:.5rem; align-items:flex-start;
  }}
  .mcq-opt:hover:not(.locked) {{ border-color:var(--accent); background:var(--accent-bg); }}
  .mcq-opt.correct {{ border-color:var(--accent2)!important; background:var(--accent2-bg)!important; color:#0a5c43!important; font-weight:500; }}
  .mcq-opt.wrong   {{ border-color:var(--danger)!important;  background:var(--danger-bg)!important;  color:#7f1d1d!important; }}
  .mcq-opt.locked  {{ cursor:default; }}
  .opt-letter {{ font-family:var(--mono); font-weight:700; min-width:1.2rem; color:var(--muted); flex-shrink:0; }}
  .mcq-opt.correct .opt-letter {{ color:var(--accent2); }}
  .mcq-opt.wrong   .opt-letter {{ color:var(--danger); }}

  .q-feedback {{ font-size:.84rem; margin:.4rem 0 .2rem; font-weight:500; }}
  .fb-correct {{ color:var(--accent2); }}
  .fb-wrong   {{ color:var(--danger); }}

  /* Score bar */
  .score-bar {{
    background: var(--navy); color:#fff; border-radius:var(--radius);
    padding:.9rem 1.3rem; margin-bottom:1.5rem;
    display:flex; justify-content:space-between; align-items:center; gap:1rem;
    font-size:.88rem; flex-wrap:wrap;
  }}
  .score-val {{ font-family:var(--mono); font-size:1.3rem; font-weight:700; color:var(--accent2); }}

  /* Multi-select */
  .ms-opt.selected {{ border-color:var(--accent); background:var(--accent-bg); }}
  .btn-check-ms {{
    font-family:var(--sans); font-size:.8rem; font-weight:500;
    padding:.4em .9em; border-radius:6px; border:1px solid var(--accent2);
    background:var(--accent2); color:#fff; cursor:pointer; margin-bottom:.5rem;
    transition:background .15s;
  }}
  .btn-check-ms:hover {{ background:#0b8c68; }}

  /* Code questions */
  .answer-label {{
    font-size:.72rem; text-transform:uppercase; letter-spacing:.08em;
    color:var(--muted); font-weight:600; margin-bottom:.4rem;
    display:flex; align-items:center; gap:.5rem;
  }}
  .lang-tag {{
    background:var(--warn-bg); color:var(--warn);
    border-radius:3px; padding:.1em .45em; font-family:var(--mono);
  }}
  .code-editor {{
    width:100%; min-height:150px;
    background:var(--code-bg); color:var(--code-text);
    font-family:var(--mono); font-size:.82rem; line-height:1.6;
    border:1px solid var(--border2); border-radius:var(--radius);
    padding:.9rem 1.1rem; resize:vertical; outline:none;
    transition:border-color .2s;
  }}
  .code-editor:focus {{ border-color:var(--accent2); }}
  .code-editor::placeholder {{ color:#4a5568; }}
  .code-actions {{
    display:flex; gap:.5rem; flex-wrap:wrap; margin:.6rem 0;
  }}
  .btn-show-sol, .btn-compare, .btn-clear {{
    font-family:var(--sans); font-size:.79rem; font-weight:500;
    padding:.4em .9em; border-radius:6px; border:1px solid; cursor:pointer; transition:all .15s;
  }}
  .btn-show-sol {{ background:var(--accent2); border-color:var(--accent2); color:#fff; }}
  .btn-show-sol:hover {{ background:#0b8c68; }}
  .btn-compare {{ background:var(--accent); border-color:var(--accent); color:#fff; }}
  .btn-compare:hover {{ background:#1d4ed8; }}
  .btn-clear {{ background:transparent; border-color:var(--border2); color:var(--muted); }}
  .btn-clear:hover {{ border-color:var(--danger); color:var(--danger); background:var(--danger-bg); }}

  /* Short answer */
  .short-input {{
    width:100%; font-family:var(--mono); font-size:.88rem;
    padding:.55rem .85rem; border:1.5px solid var(--border2);
    border-radius:var(--radius); outline:none; background:var(--surface2);
    color:var(--text); transition:border-color .2s; margin-bottom:.4rem;
  }}
  .short-input:focus {{ border-color:var(--accent2); }}

  /* Solution / explanation */
  .solution-block {{ margin-top:.75rem; border-top:1px dashed var(--border2); padding-top:.75rem; }}
  .solution-block.hidden, .compare-block.hidden, .q-explanation.hidden {{ display:none; }}
  .sol-label, .exp-label {{
    font-family:var(--mono); font-size:.68rem; font-weight:700;
    text-transform:uppercase; letter-spacing:.08em; margin-bottom:.3rem;
  }}
  .sol-label {{ color:var(--accent2); }}
  .exp-label {{ color:var(--accent); margin-top:.75rem; }}
  .solution-block p, .q-explanation p {{ font-size:.88rem; margin:.2rem 0 0; }}

  /* Compare */
  .cmp-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-top:.6rem; }}
  @media(max-width:680px) {{ .cmp-grid {{ grid-template-columns:1fr; }} }}
  .cmp-label {{
    font-size:.7rem; text-transform:uppercase; letter-spacing:.08em; font-weight:600;
    margin-bottom:.3rem; padding:.2em .6em; border-radius:4px; display:inline-block;
  }}
  .cmp-label.yours {{ background:var(--warn-bg); color:var(--warn); }}
  .cmp-label.memo  {{ background:var(--accent2-bg); color:var(--accent2); }}
  .compare-code {{
    background:var(--code-bg); color:var(--code-text); font-family:var(--mono);
    font-size:.79rem; line-height:1.6; border-radius:var(--radius);
    padding:.9rem 1rem; overflow-x:auto; min-height:100px;
    border:1px solid var(--border2); white-space:pre;
  }}
  .compare-code.empty {{ color:#4a5568; font-style:italic; white-space:normal; }}
  .compare-code pre {{ margin:0; background:none; padding:0; box-shadow:none; color:inherit; }}
</style>
</head>
<body>

<nav class="topnav">
  <div class="topnav-inner">
    <div class="topnav-logo">COS333 <span>// Programming Languages</span></div>
    <div class="topnav-links">
      <a href="../../../../index.html">Home</a>
      <a href="../../PracticeQuestions/scheme_practice_questions.html">Scheme</a>
      <a href="../../PracticeQuestions/prolog_practice_questions.html">Prolog</a>
      <a href="../../PracticeQuestions/scheme_prolog_guide.html">Guide</a>
    </div>
  </div>
</nav>

<div class="hero">
  <div class="hero-inner">
    <div class="hero-eyebrow">COS 333 · Past Paper</div>
    <h1>{year}<br><em>Examination</em></h1>
    <p class="hero-sub">{exam_info}</p>
    <div class="hero-pills">
      <span class="hero-pill"><strong>{len(data["questions"])}</strong> Questions</span>
      <span class="hero-pill"><strong>{data.get("total_marks", 40)}</strong> Marks</span>
      <span class="hero-pill">Click options to check MCQs</span>
    </div>
  </div>
</div>

<div class="page-wrap" style="padding-top:1.5rem;">

  <div class="breadcrumb">
    <a href="../../../../index.html">Home</a>
    <span>›</span>
    <span>Past Papers</span>
    <span>›</span>
    <span>{year} Examination</span>
  </div>

  <div class="score-bar">
    <span>MCQ Score</span>
    <span class="score-val"><span id="score-correct">0</span> / <span id="score-total">0</span></span>
    <span id="score-pct" style="color:#8892a8;font-size:.82rem;"></span>
  </div>

  {questions_html}

  <div style="height:3rem;"></div>
</div>

<script>
  let correct = 0;
  let answered = 0;
  const total = document.getElementById('score-total');
  const scoreEl = document.getElementById('score-correct');
  const pctEl = document.getElementById('score-pct');

  function updateScore() {{
    total.textContent = answered;
    scoreEl.textContent = correct;
    if (answered > 0) {{
      pctEl.textContent = Math.round(correct / answered * 100) + '%';
    }}
  }}

  function checkMCQ(el, qid, isCorrect) {{
    const block = document.getElementById(qid);
    if (block.dataset.answered) return;
    block.dataset.answered = '1';
    answered++;
    const opts = block.querySelectorAll('.mcq-opt');
    opts.forEach(o => o.classList.add('locked'));
    const fb = document.getElementById(qid + '-fb');
    if (isCorrect) {{
      el.classList.add('correct');
      fb.textContent = 'Correct!';
      fb.className = 'q-feedback fb-correct';
      correct++;
    }} else {{
      el.classList.add('wrong');
      fb.textContent = 'Incorrect.';
      fb.className = 'q-feedback fb-wrong';
      // reveal the correct one
      opts.forEach(o => {{
        if (o.onclick && o.onclick.toString().includes('true')) o.classList.add('correct');
      }});
    }}
    document.getElementById(qid + '-exp').classList.remove('hidden');
    updateScore();
  }}

  function toggleMS(el, qid) {{
    const block = document.getElementById(qid);
    if (block.dataset.answered) return;
    el.classList.toggle('selected');
  }}

  function checkMS(qid, correctAnswers) {{
    const block = document.getElementById(qid);
    if (block.dataset.answered) return;
    block.dataset.answered = '1';
    answered++;
    const opts = block.querySelectorAll('.ms-opt');
    let allRight = true;
    opts.forEach(o => {{
      o.classList.add('locked');
      const isCorrect = o.dataset.correct === 'true';
      const isSelected = o.classList.contains('selected');
      if (isCorrect) o.classList.add('correct');
      else if (isSelected) {{ o.classList.add('wrong'); allRight = false; }}
      if (isCorrect && !isSelected) allRight = false;
    }});
    const fb = document.getElementById(qid + '-fb');
    if (allRight) {{
      fb.textContent = 'Correct!';
      fb.className = 'q-feedback fb-correct';
      correct++;
    }} else {{
      fb.textContent = 'Incorrect — correct options highlighted.';
      fb.className = 'q-feedback fb-wrong';
    }}
    document.getElementById(qid + '-exp').classList.remove('hidden');
    updateScore();
  }}

  function toggleSol(qid) {{
    const sol = document.getElementById(qid + '-sol');
    sol.classList.toggle('hidden');
  }}

  function compareCode(qid) {{
    const ta = document.getElementById(qid + '-answer');
    const yours = document.getElementById(qid + '-yours');
    const val = ta.value.trim();
    if (val === '') {{
      yours.textContent = '(no answer written yet)';
      yours.classList.add('empty');
    }} else {{
      yours.textContent = val;
      yours.classList.remove('empty');
    }}
    document.getElementById(qid + '-cmp').classList.remove('hidden');
    document.getElementById(qid + '-sol').classList.remove('hidden');
  }}

  function clearCode(qid) {{
    document.getElementById(qid + '-answer').value = '';
    document.getElementById(qid + '-cmp').classList.add('hidden');
  }}

  // Tab key in textareas
  document.querySelectorAll('.code-editor').forEach(ta => {{
    ta.addEventListener('keydown', e => {{
      if (e.key === 'Tab') {{
        e.preventDefault();
        const s = ta.selectionStart, end = ta.selectionEnd;
        ta.value = ta.value.substring(0, s) + '  ' + ta.value.substring(end);
        ta.selectionStart = ta.selectionEnd = s + 2;
      }}
    }});
  }});
</script>
</body>
</html>'''


for year in YEARS:
    memo_path = os.path.join(BASE, f"{year}_examination_memo.json")
    out_path  = os.path.join(BASE, f"{year}_examination.html")
    with open(memo_path, "r") as f:
        data = json.load(f)
    html_content = generate_page(year, data)
    with open(out_path, "w") as f:
        f.write(html_content)
    print(f"Generated {year}_examination.html ({len(data['questions'])} questions)")
