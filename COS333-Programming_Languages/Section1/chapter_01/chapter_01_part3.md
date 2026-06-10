<!-- Slide number: 1 -->

![Front Cover: Concepts of Programming Languages, Global Edition, by Robert W Sebesta](Picture8.jpg)
# Chapter 1Part 3
Preliminaries

### Notes:

<!-- Slide number: 2 -->
# Topics
Language Categories
Implementation Methods

1-2

### Notes:

<!-- Slide number: 3 -->
# Language Categories
Imperative
Central features: variables, assignment statements, iteration
Includes languages that support object-oriented programming
Includes scripting languages
Includes the visual languages
Examples: C, Java, Perl, JavaScript, Visual BASIC .NET, C++

Functional
Main means of computation: applying functions to parameters
Examples: LISP, Scheme, ML, F#

Logic
Rule-based (rules are specified in no particular order)
Example: Prolog

Markup/programming hybrid
Markup languages extended to support some programming
Examples: JSTL, XSLT


1-3

### Notes:

<!-- Slide number: 4 -->
# Implementation Methods
Compilation
Programs are translated into machine language
Large commercial applications

Pure Interpretation
Programs interpreted by a separate interpreter program
Small programs or when efficiency is not an issue

Hybrid Implementation Systems
A compromise between compilers and pure interpreters
Small/medium systems, efficiency not the first concern

1-4

### Notes:

<!-- Slide number: 5 -->
# Compilation
Translate high-level program (source language) into machine code (machine language)
Slow translation, fast execution
Compilation process has several phases

1-5

### Notes:
Additional compilation terminology

Load module (executable image)
The user and system code together
For example, I/O code provided by the OS
Linking and loading
The process of collecting system program units and linking them to a user program

<!-- Slide number: 6 -->
# The Compilation Process

![](Picture4.jpg)

1-6

### Notes:

<!-- Slide number: 7 -->
# Pure Interpretation
No translation
Easier implementation of programs
Run-time errors can easily and immediately be displayed
Slower execution
10 to 100 times slower than compiled programs
Decoding high-level statements vs machine language
Repeated statement executions are repeatedly decoded
Often requires more space
Source program and symbol table are present at runtime
Now rare for traditional high-level languages
Significant use of pure interpretation today
Used by Web scripting languages (e.g., JavaScript and PHP)

1-7

### Notes:

<!-- Slide number: 8 -->
# Pure Interpretation Process

![](Picture4.jpg)

1-8

### Notes:

<!-- Slide number: 9 -->
# Hybrid Implementation Systems
Compromise between compilers & pure interpreters
High-level language program translated to an intermediate language allowing easy interpretation
Faster than pure interpretation

Perl programs use a hybrid implementation system
Partially compiled to detect errors before interpretation

Typical Java implementations are hybrid
Programs compiled into intermediate form called byte code
Byte code is portability to any machine that has
Byte code interpreter
A run-time system
Together, these are called the Java Virtual Machine

1-9

### Notes:

<!-- Slide number: 10 -->
# Hybrid Implementation Systems

![](Picture4.jpg)

1-10

### Notes:

<!-- Slide number: 11 -->
# Just-in-Time Implementation Systems
JIT systems are a kind of hybrid system
Initially translate programs to an intermediate language
Then compile the intermediate language of the subprograms into machine code when they are called
Machine code version is kept for subsequent calls
In essence, JIT systems are delayed compilers
Examples
JIT systems are widely used for Java programs
The .NET languages implemented using JIT system

1-11

### Notes:
