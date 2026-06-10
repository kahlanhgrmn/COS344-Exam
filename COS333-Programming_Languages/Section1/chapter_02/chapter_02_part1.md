<!-- Slide number: 1 -->

![Front Cover: Concepts of Programming Languages, Global Edition, by Robert W Sebesta](Picture8.jpg)
# Chapter 2Part 1
Evolution of the Major Programming Languages

### Notes:

<!-- Slide number: 2 -->
# Chapter 2 Topics
Minimal Hardware Programming: Pseudocodes
The IBM 704 and Fortran
Functional Programming: LISP

1-2

### Notes:

<!-- Slide number: 3 -->
# Genealogy of Common Languages

![](Picture1.jpg)

1-3

<!-- Slide number: 4 -->
# Minimal Hardware Programming: Pseudocodes
Late 1940s and early 1950s
Programming done using machine code
Numeric codes to specify instructions
What was wrong with using machine code?
Expression coding was tedious
Poor readability
Poor modifiability
Absolute addressing
Machine deficiencies
No indexing for arrays or floating point operations

1-4

### Notes:

<!-- Slide number: 5 -->
# Minimal Hardware Programming: Pseudocodes
Pseudocodes
Not pseudocode program planning you’ve used
An attempt to make programming simpler
Not fully high-level languages
Computers at the time
Very slow and unreliable
No support for floating point and array indexing
Approach used by pseudocodes
Floating point and array indexing in software
These languages were interpreted

1-5

### Notes:

<!-- Slide number: 6 -->
# IBM 704 and Fortran
IBM Mathematical FORmula TRANslating System

Fortran 0 (1954)
Not implemented

Fortran I (1957)
Designed for the new IBM 704
It had index registers and floating point hardware
Floating point and array indexing were not in software
Therefore no place to hide the cost of interpretation
Led to the idea of compiled programming languages

1-6

### Notes:

<!-- Slide number: 7 -->
# Design Process of Fortran
Environment of Fortran I development
IBM 704 had little memory, and was slow and unreliable
Applications were scientific and fairly simple
No programming methodology or tools
Machine efficiency was the most important concern
Impact of environment on Fortran I design
Compiled programs had to be fast!
No need for dynamic storage
Needed good array handling and counting loops
No string handling, decimal arithmetic, or powerful I/O
These were only found to be necessary for business software
No use for early scientific applications

1-7

### Notes:
Dynamic storage is memory storage that is allocated at runtime. In C++ and Java, this would be anything that is allocated using the new keyword.

Decimal data types, like floating point data types, store values with a decimal point. The difference is that floating point values are approximations, while decimal values are exact representations. We will go into more detail on these types in Chapter 6.

<!-- Slide number: 8 -->
# Fortran I Overview
First implemented version of Fortran
Names could have up to six characters
Post-test counting loop (DO loop)
Very basic formatted I/O
User-defined subprograms
Three-way selection statement (arithmetic IF)
No data typing statements
Data type based on the name of the variable
Variables starting with I, J, K, L, M or N were integers
All other variables were floating point

1-8

### Notes:
DO loops were similar to for loops in languages like C++ and Java. Why does this make sense for a scientific language like Fortran?

The arithmetic IF statement worked in a way that you will not be familiar with. The form of the statement was:

IF (expression) label1, label2, label3

If expression is less than 0, control jumps to label1, if expression is equal to 0, control jumps to label2, and if expression is greater than 0, control jumps to label3. Can you think of a reason that this makes sense for a scientific programming language like Fortran?

Variable names could only be a maximum of six characters long in Fortran I. The Fortran 0 specification only allowed variable names that were a maximum of two characters long.

<!-- Slide number: 9 -->
# Fortran I Overview (continued)
First implemented version of Fortran
Compiler released
April 1957
After 18 worker-years of effort
Programs larger than 400 lines rarely compiled
Mainly due to poor reliability of 704
No solution as no support for separate compilation
Successes
Code was very fast
Quickly became very widely used


1-9

### Notes:
Separate compilation refers to compiling different parts of the program separately, and then linking all of the compiled parts into a single executable. You will have encountered this in C++, where separate classes and the main function are all in their own implementation files. These implementation files are compiled into object files separately. The object files are then linked into a single executable file.

<!-- Slide number: 10 -->
# Fortran II
Distributed in 1958
Independent compilation
More reliable compilation for longer programs
Shortened compilation process (why?)
Fixed bugs in Fortran I

1-10

### Notes:

<!-- Slide number: 11 -->
# Fortran IV
Evolved during 1960-62
Explicit type declarations
Logical selection statement
Subprogram names could be parameters
ANSI standard in 1966

1-11

### Notes:
Note that logical selection statements (i.e. the normal if statements we’re used to) were only introduced in the fourth version of Fortran. This points to the fact that the control structures we use today had to evolve over time.

<!-- Slide number: 12 -->
# Fortran 77
Became the new standard in 1978
Character string handling
Logical loop control statement
An IF-THEN-ELSE statement


1-12

### Notes:
Note that logical loop control (i.e. the normal while loops we’re used to) were only introduced in the fifth version of Fortran. Similarly, selection statements with an else part were only introduced at this stage. This points to the fact that the control structures we use today had to evolve over time.

<!-- Slide number: 13 -->
# Fortran 90
Significantly different from Fortran 77
Modules
Dynamic arrays
Pointers
Recursion
A CASE statement
Parameter type checking
Relaxed fixed code format requirements
Some previous language features deprecated


1-13

### Notes:
Modules in Fortran are like packages in Java. They allow you to organise related functions and subroutines together.

Dynamic arrays are like C++ arrays allocated using new. In other words, we don’t know what size they should be until runtime, when we allocate space for the desired array size.

Consider the inclusion of support for dynamic arrays and recursion, and what you know about these features in languages like C++. What impact does this have on the cost programming language evaluation criterion?

<!-- Slide number: 14 -->
# Latest versions of Fortran
Fortran 95
Relatively minor additions
Some deletions
Fortran 2003
Support for OOP
Procedure pointers
Interoperability with C
Fortran 2008
Blocks with local scopes
Co-arrays
The DO CONCURRENT construct
Fortran 2018 and Fortran 2023
Some relatively minor additions

1-14

### Notes:
Co-arrays allow for parallel execution in programs. The DO CONCURRENT construct indicates that loop iterations can be executed in parallel because they don’t depend on one another.

<!-- Slide number: 15 -->
# Fortran Evaluation
Highly optimized compilers
All versions before Fortran 90
Types & storage of all variables fixed before runtime
No support for recursion
Changed forever how computers are used
The lingua franca of the computing world

1-15

### Notes:
The last statement means that Fortran became so widely used that everyone could understand it and write programs in it.

<!-- Slide number: 16 -->
# Functional Programming: LISP
LISt Processing language
Designed at MIT by John McCarthy
AI research needed a language to support
Processing data in lists (rather than arrays)
Symbolic computation (rather than numeric)
Recursive operation
Automatic dynamic storage handling
Only two data types
Atoms and lists
Syntax is based on lambda calculus

1-16

### Notes:

<!-- Slide number: 17 -->
# Representation of Two LISP Lists

![](Picture4.jpg)
Representing the lists (A B C D)
and (A (B C) D (E (F G)))

1-17

### Notes:

<!-- Slide number: 18 -->
# LISP Evaluation
Pioneered functional programming
No need for variables or assignment
Control via recursion & conditional expressions
Still used in AI domain (but less common)
Contemporary dialects of LISP
COMMON LISP and Scheme
Other functional languages
ML, Haskell, and F#
Syntax very different from LISP

1-18

### Notes:

<!-- Slide number: 19 -->
# Scheme
Developed at MIT in mid 1970s
Small language, simple syntax
Ideal for educational applications
Exclusive use of static scoping
Functions as first-class entities
Functions can be applied to other functions
Functions can receive other functions as parameters
Functions can be results of function applications
Functions can be returned from other functions

1-19

### Notes:

<!-- Slide number: 20 -->
# COMMON LISP
Feature-rich dialect of LISP
Combines features of several LISP dialects
In many ways, the opposite of Scheme
Large and complex
Both static and dynamic scoping
Many data types and structures
Used in industry for some large applications

1-20

### Notes:
