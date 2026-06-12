# COS333 Exam Study Checklist

## General

- [ ] Study from **both** the textbook and slides (each covers material the other does not)
- [ ] Read the slide notes in PowerPoint/LibreOffice for additional context
- [ ] Learn all terminology precisely — use the correct terms in answers
- [ ] Be as specific as possible when naming programming language features

---

## Implementation Questions

- [ ] **Scheme** — one list processing question (DrRacket interpreter under Windows)
  - [ ] Familiarise yourself with DrRacket before the exam if you used a different interpreter
  - [ ] Can write: `member`, `equalsimp`, `equal`, `append` style functions
  - [ ] Complete Practical 2 for practice
- [ ] **Prolog** — one list processing question (SWI-Prolog interpreter under Windows)
  - [ ] Familiarise yourself with SWI-Prolog before the exam if you used a different interpreter
  - [ ] Can write: `member`, `append`, `reverse` style propositions
  - [ ] Complete Practicals 3 and 4 for practice
  - [ ] Only use language features from the textbook + practical specification hints
  - [ ] During exam: SWI-Prolog docs and Practical 3 & 4 specs available (for quick reference only — don't rely heavily on them)

---

## Chapter 1 — Introduction

- [ ] Know the whole chapter **except**: Figure 1.2 discussion, Section 1.7.4, Section 1.8
- [ ] Section 1.7: no need to know detailed steps of compilation and hybrid implementation processes
- [ ] Can apply reasons for studying PLs to a specific scenario/person (junior programmer, manager, lecturer, etc.) — answer must relate to the scenario, not just list generic reasons
- [ ] Can apply **language evaluation criteria** to features/decisions in real-world AND hypothetical languages
- [ ] Understand **orthogonality** thoroughly — will definitely be tested

---

## Chapter 2 — Evolution of the Major Programming Languages

- [ ] Leave out: Sections 2.1, 2.2, 2.6.2, 2.9.2
- [ ] Section 2.20: only focus on what is in the slides
- [ ] For the remaining sections, don't focus on finer details
- [ ] For each language, know:
  - [ ] The **environment** for its development and application (intended users, application area, popular software engineering approaches at the time, general computer system characteristics)
  - [ ] How that environment **affected** the language design
  - [ ] The **main contribution(s)** of the language
- [ ] Do NOT memorise: specific version features, dates, computer model names/numbers, developer names, design committee details

---

## Chapter 5 — Names, Bindings, and Scopes

- [ ] The **whole chapter** is examinable

---

## Chapter 6 — Data Types

- [ ] Leave out: Sections 6.3.5, 6.5.9, 6.6.2, 6.7.4, 6.10.5, 6.11.7 (compiler construction topics)
- [ ] Leave out: Sections 6.4, 6.5.4, 6.12, 6.16
- [ ] Section 6.15: only the details in the slides are examinable (reading the section gives useful insight into name vs. structure type equivalence)
- [ ] Understand **discriminated unions** (see graphical example in slides; textbook uses F# for the same concept)

---

## Chapter 7 — Expressions and Assignment Statements

- [ ] The **whole chapter** is examinable
- [ ] Pay special attention to **side effects** and **referential transparency** (covered in Chapter 15 slides)

---

## Chapter 8 — Statement-Level Control Structures

- [ ] Leave out: Section 8.2.2.3, Section 8.3.1.4, the last paragraph and example of 8.3.2.2 (pretest logical loops in functional languages)
- [ ] Understand **Ruby blocks** (Section 8.3.4)
- [ ] Pay special attention to **guarded commands** (Section 8.5)

---

## Chapter 9 — Subprograms

- [ ] Terminology is important — know the meaning of all terms
- [ ] Understand **referencing environments**
- [ ] Section 9.5.3 is **not** examinable
- [ ] Understand all **parameter passing methods** thoroughly
- [ ] Sections 9.6 and 9.7 are **very important**
- [ ] Know the differences between **generic subprograms** in C++, Java, and C# (Sections 9.10.1, 9.10.2, 9.10.3 — also use slides for C# which go into more detail)
- [ ] Section 9.10.4 is **not** examinable
- [ ] **Closures** are very important (Section 9.12):
  - [ ] Can trace JavaScript code involving closures
  - [ ] Can provide output of implementations similar to the `MakeAdder` example
- [ ] Understand **coroutines** (Section 9.13):
  - [ ] Can provide output of pseudocode coroutine examples

---

## Chapter 11 — Abstract Data Types and Encapsulation Constructs

- [ ] Not directly examinable — but read it to better understand Chapter 12
- [ ] Refer to it for unclear terms or concepts used in Chapter 12
- [ ] Know the most important terms from slide 4 of Chapter 12, Part 1

---

## Chapter 12 — Support for Object-Oriented Programming

- [ ] This chapter is **very important**
- [ ] Sections 12.5 and 12.6 are **not** examinable
- [ ] Know all the important OOP terms (refer to Chapter 11 if needed)

---

## Chapter 15 — Functional Programming Languages

- [ ] Study all material up to and including **Section 15.5.11** (Scheme list processing examples)
- [ ] Leave out: Common Lisp, ML, Haskell, F#, and functional support in imperative languages
- [ ] Leave out: Sections 15.2 and 15.4 (not directly examinable, but reading consolidates concepts)
- [ ] Leave out: lambda expressions in Section 15.5.4
- [ ] Also examinable from slides: Sections 7.2.2, 8.2.2.4, 6.9, and 5.5.2
- [ ] Can analyse and write Scheme programs up to the complexity of `member`, `equalsimp`, `equal`, `append`
- [ ] Practice with example test/exam papers for additional Scheme exercises

---

## Chapter 16 — Logic Programming Languages

- [ ] The **whole chapter** is examinable
- [ ] Can analyse and write Prolog programs up to the complexity of `member`, `append`, `reverse`
- [ ] Practice with example test/exam papers for additional Prolog exercises
