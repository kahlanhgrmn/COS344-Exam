<!-- Slide number: 1 -->

![Front Cover: Concepts of Programming Languages, Global Edition, by Robert W Sebesta](Picture8.jpg)
# Chapter 2Part 2
Evolution of the Major Programming Languages

### Notes:

<!-- Slide number: 2 -->
# Chapter 2 Topics
The First Step Toward Sophistication: ALGOL 60
Computerizing Business Records: COBOL
The Beginnings of Timesharing: BASIC
Everything for Everybody: PL/I
An Early Dynamic Language: APL
The Beginnings of Data Abstraction: SIMULA 67


1-2

### Notes:

<!-- Slide number: 3 -->
# Genealogy of Common Languages

![](Picture1.jpg)

1-3

<!-- Slide number: 4 -->
# The First Step Toward Sophistication: ALGOL 60
Environment of development
FORTRAN had (barely) arrived for IBM 70x
Many other languages were being developed
All for specific machines
No portable language
No universal way to communicate algorithms
An effort to design a universal language
Universal in terms of machine independence
ALGOL 60 was still a scientific language

1-4

### Notes:

<!-- Slide number: 5 -->
# Early Design Process
ACM and GAMM met for four days for design (May 27 to June 1, 1958)
International Algorithmic Language (IAL), then renamed ALGOrithmic Language
Goals of the language
Close to mathematical notation
Good for describing algorithms
Must be translatable to machine code

1-5

### Notes:
ACM: Association of Computing Machinery
GAMM: German acronym for Society of Applied Mathematics and Mechanics

<!-- Slide number: 6 -->
# ALGOL 58
Design of ALGOL 58
Concept of type was formalized
Names could be any length
Arrays
Could have any number of subscripts
Subscripts were placed in brackets
Lower bound could be specified by the programmer
Parameters were separated by mode (in & out)
Compound statements (begin ... end)
Semicolon as a statement separator
Assignment operator was := (evolved from <=)
The if had else-if clause, and could be nested
No I/O - “would make it machine dependent”

1-6

### Notes:

<!-- Slide number: 7 -->
# ALGOL 58 Implementation
Not meant to be implemented
IBM
Initially enthusiastic
But all support was dropped by mid 1959

1-7

### Notes:

<!-- Slide number: 8 -->
# ALGOL 60 Overview
Modified ALGOL 58 at 6-day Paris meeting
New features
Block structure with local scope
Complex parameter passing methods
Pass by value and pass by name
Subprogram recursion
First to introduce this for imperative languages
Stack-dynamic arrays
Allowed run-time size declaration of arrays
BUT still no I/O and no string handling

1-8

### Notes:
Subprograms are like functions in C++, or methods in Java. We’ll get into more detail on them in Chapter 9.

Recall that recursion and dynamic arrays were only added to Fortran 90, around 30 years later.

<!-- Slide number: 9 -->
# ALGOL 60 Evaluation
Successes
Algorithm publishing standard for over 20 years
Basis for all subsequent imperative languages
First machine-independent language
First language with formally defined syntax (BNF)


1-9

### Notes:
BNF is Backus-Naur Form, which is a notation for describing a programming language’s syntax. You will learn more about this in the compiler construction module.

<!-- Slide number: 10 -->
# ALGOL 60 Evaluation (continued)
Failure
Never widely used, especially in U.S.
Reasons
Lack of I/O
Ironically made programs non-portable
Too flexible
Hard to understand and implement
Formal syntax description
Confusing at the time
Now BNF is a standard, and widely understood
Entrenchment of Fortran and lack of IBM support

1-10

### Notes:

<!-- Slide number: 11 -->
# Computerizing Business Records: COBOL
First Common Business Language (CBL), then COmmon Business-Oriented Language
Environment of development
Only a few proprietary business languages
UNIVAC was beginning to use FLOW-MATIC
USAF was beginning to use AIMACO
IBM was developing COMTRAN
COBOL was based on FLOW-MATIC

1-11

### Notes:

<!-- Slide number: 12 -->
# COBOL Design Process
First Design Meeting (Pentagon) in May 1959
Design goals
Must look like simple English
Must be easy to use, even if that means less power
Must broaden the base of computer users
Must not be biased by current compiler problems
Design committee members were all from computer manufacturers and DoD branches
Design problems
Arithmetic expressions?
Subscripts?
Fights among manufacturers

1-12

### Notes:

<!-- Slide number: 13 -->
# COBOL Evaluation
Contributions
Hierarchical data structures (records)
Nested selection statements
Long names (up to 30 characters), with hyphens
Separate and very detailed data division
Still most used business applications language
Drawbacks
Relatively weak procedure division
First word in every statement was a verb
English names for arithmetic operations
Initially no subprograms with parameters

1-13

### Notes:
Macros in COBOL are similar to inline functions in C and C++.

Arithmetic in COBOL looks like this:

ADD REGULAR-PAY TO OVERTIME-PAY GIVING GROSS-PAY

What influence does this type of arithmetic syntax have on the programming language evaluation criteria?

<!-- Slide number: 14 -->
# The Beginning of Timesharing: BASIC
Beginner’s All-Purpose Symbolic Instruction Code
Designed by Kemeny & Kurtz at Dartmouth College
Design Goals:
Easy to learn and use for non-science students
Must be “pleasant and friendly”
Fast turnaround for homework
Free and private access
User time is more important than computer time
First widely-used language with time sharing
Current popular dialects
Visual BASIC
VB.NET

1-14

### Notes:
Time sharing is a method of computing where a central processor switches rapidly between multiple terminals, giving the illusion of each of the users of the terminals working in real-time.

<!-- Slide number: 15 -->
# Everything for Everybody: PL/I
Programming Language One
Designed by IBM and SHARE
Computing situation in 1964 (IBM’s view)
Scientific computing
IBM 1620 and 7090 computers
FORTRAN
SHARE user group
Business computing
IBM 1401, 7080 computers
COBOL
GUIDE user group

1-15

### Notes:

<!-- Slide number: 16 -->
# PL/I: Background
By 1963
Scientific users needing better I/O, like COBOL provided
Business users needing floating point and arrays (for MIS)
A problem was developing for organizations
Two kinds of computers, languages, and support staff
Far too costly
The obvious solution
Build a new computer for both applications
IBM System/360 line
Design a new language for both applications
Added systems programming and list processing too

1-16

### Notes:

<!-- Slide number: 17 -->
# PL/I: Design Process
Designed in 5 months by 3x3 Committee
Three members from IBM
Three members from SHARE
Initial concept
An extension of Fortran IV called Fortran VI
Quickly refocused into a new language
Initially NPL (New Programming Language)
Name changed to PL/I in 1965

1-17

### Notes:

<!-- Slide number: 18 -->
# PL/I: Evaluation
PL/I contributions
First unit-level concurrency
First exception handling
Switch-selectable recursion
First pointer data type
First array cross sections
Concerns
Many new features were poorly designed
Too large and too complex
Tried to incorporate all available constructs
Many different data structures


1-18

### Notes:

<!-- Slide number: 19 -->
# An Early Dynamic Language: APL
A Programming Language
Characterized by
Dynamic typing
Variable acquires a type when it is assigned a value
Variable type can change at runtime
Dynamic storage allocation
Variable storage allocated when value is assigned
Variable storage can change at runtime

1-19

### Notes:

<!-- Slide number: 20 -->
# An Early Dynamic Language: APL
Designed at IBM by Ken Iverson circa 1960
Initially a hardware description language
Highly expressive
Very large number of operators
Operators work for scalars and arrays
Programs are very difficult to read
Still in use with minimal changes

1-20

### Notes:

<!-- Slide number: 21 -->
# APL
Examples of APL programs
Sort a list of words according to word length

Generate 6 non-repeating pseudo-random integers between 1 and 40, and print them in ascending order

Find all the prime numbers from 1 to R

![example1.bmp](Picture5.jpg)

![example2.bmp](Picture6.jpg)

![example3.bmp](Picture7.jpg)

1-21

<!-- Slide number: 22 -->
# The Beginning of Data Abstraction: SIMULA 67
Designed in Norway by Nygaard & Dahl
Primarily for system simulation
Based on ALGOL 60 and SIMULA I
Primary Contributions
Coroutines
Subprograms
Can restart where they were previously stopped
The beginnings of data abstraction
Classes and objects
Not full object-oriented programming


1-22

### Notes:
