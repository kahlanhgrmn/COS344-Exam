<!-- Slide number: 1 -->

![Front Cover: Concepts of Programming Languages, Global Edition, by Robert W Sebesta](Picture8.jpg)
# Chapter 1Part 2
Preliminaries

### Notes:

<!-- Slide number: 2 -->
# Topics
Language Evaluation Criteria
Language Design Trade-Offs
Programming Domains
Influences on Language Design

1-2

### Notes:

<!-- Slide number: 3 -->
# Language Evaluation Criteria
Readability:
The ease with which programs can be read and understood
Writability:
The ease with which a language can be used to create programs
Reliability:
Whether the language performs to its specifications under all conditions
Cost:
The ultimate total cost of using the language

1-3

### Notes:

<!-- Slide number: 4 -->
# Evaluation Criteria: Readability
Overall simplicity
A manageable set of features and constructs
Minimal feature multiplicity
Minimal operator overloading
Too much simplicity can be bad for readability

Orthogonality
Definition
A relatively small set of primitive constructs can be combined in a relatively small number of ways
AND (most importantly) every possible combination is legal
Small set of constructs is not sufficient on its own for high orthogonality
An orthogonal language feature is context independent
Lack of orthogonality = exceptions
Too much orthogonality can be bad for readability (ALGOL 68)

1-4

### Notes:
A manageable set of features and constructs: Large, complex languages allow for programs that are difficult to follow. A good example of a complex language is C++.

Minimal feature multiplicity: If there are several ways to achieve the same thing, the language becomes more difficult to read. For example, in C++ there are several ways to increment a variable (for example, var=var+1, var+=1, ++var, and var++).

Minimal operator overloading: It’s more difficult to understand program written in a language that uses the same operator symbol for different things. For example, in C++ the * operator is used to represent multiplication, pointer declarations, and pointer dereferencing.

A good example of orthogonality is basic addition. As you should already know, integer addition and floating point addition are very different operations on a machine level. If a language has a single addition operator for integer and floating point addition, the language is highly orthogonal. This is because the same operator is used to add two integer values, two floating point values, an integer and a float, and a float and an integer. All these combinations are legal without any exceptions. On the other hand, if a programming language has different operators for adding two integers and adding two floating point values, the language is not very orthogonal. There is an exception for how addition is done, depending on the operands being added. Additionally, it isn’t possible to add an integer and a floating point value, or a floating point value and an integer (without either providing separate operators for these operations, or using manual type conversions).

<!-- Slide number: 5 -->
# Evaluation Criteria: Readability
Data types
Adequate predefined data types and data structures
If required types are missing, they must be simulated

Syntax considerations
Identifier forms
Lack of naming restrictions increases readability
Special words
Sensible special words are more readable
Compound statement (block) notation can affect readability
Form and meaning
Self-descriptive constructs, meaningful keywords
Avoid language constructs with same name, different meaning

1-5

### Notes:
A naming restriction might be a length limit for a variable name, or rules allowing only certain characters to be used in a variable name.

A special word is something like int, float, class, and static in C++. A special word like integer would be considered more readable than int, for example (can you think of a drawback to using integer instead of int?). Special words can be used to start and end a block. For example a language might use BEGIN and END to start and end a block. This is more readable than the C-based programming languages, which use braces (can you think of a drawback to using BEGIN and END?). A language will be even more readable if the type of block is described by special words (for example BEGIN IF and END IF).

Meaningful keywords should have names that describe what they do. An example of where this is not the case is in C++ where the static special word is used to indicate a class variable. The name “static” doesn’t give a good idea of what it represents. The static special word is also an example of a case in which two language constructs have the same name, but different meanings. In a variable declaration, like this:

static int a = 5;

the static special word indicates that the variable is allocated once at the start of program execution. In a class, static indicates a class-level variable.

<!-- Slide number: 6 -->
# Evaluation Criteria: Writability
Simplicity and orthogonality
Few constructs, a small number of primitives, a small set of rules for combining them

Support for abstraction
The ability to define and use complex structures or operations in ways that allow details to be ignored
Process abstraction: provision for subprograms
Data abstraction: classes, pointers & dynamic memory

Expressivity
A set of relatively convenient ways of specifying operations
Strength and number of operators and predefined functions

1-6

### Notes:

<!-- Slide number: 7 -->
# Evaluation Criteria: Reliability
Type checking
Testing for type errors
Compile-time type checking is preferable to run-time checking
Exception handling
Intercept run-time errors and take corrective measures
Aliasing
Two or more distinct referencing names for one memory location
Generally accepted to be a dangerous feature
Readability and writability
A language that does not support “natural” ways of expressing an algorithm will require the use  of “unnatural” approaches, and hence reduced reliability


1-7

### Notes:

<!-- Slide number: 8 -->
# Evaluation Criteria: Cost
Training programmers to use language
Writing programs
How close the language is to the application area
Compiling programs
Executing programs
Language implementation system
The availability of free compilers
Reliability
Poor reliability = high costs
Maintaining programs

1-8

### Notes:

<!-- Slide number: 9 -->
# Evaluation Criteria: Others
Portability
The ease with which programs can be moved from one implementation to another
Generality
The applicability to a wide range of applications
Well-definedness
The completeness and precision of the language’s official definition

1-9

### Notes:

<!-- Slide number: 10 -->
# Language Design Trade-Offs
Reliability vs. cost of execution
Java example
All references to array elements are checked for proper indexing
Increased execution costs
Better reliability

Readability vs. writability
APL example
Many powerful operators (and many non-standard symbols)
Allows complex computations to be written compactly
But results in very poor readability

Writability (flexibility) vs. reliability
C++ example
Pointers are powerful, expressive, and very flexible
Reduced reliability

1-10

### Notes:

<!-- Slide number: 11 -->
# Programming Domains
Scientific applications
Large numbers of floating point computations and array use
Fortran
Business applications
Produce reports, use decimal numbers and characters
COBOL
Artificial intelligence
Symbols rather than numbers manipulated; use of linked lists
LISP
Systems programming
Need efficiency because of continuous use
C
Web Software
Eclectic collection of languages
Markup (HTML), scripting (PHP), general-purpose (Java)

1-11

### Notes:

<!-- Slide number: 12 -->
# Influences on Language Design
Computer Architecture
Languages are developed around the prevalent computer architecture, which is known as the von Neumann architecture
Programming Methodologies
New software development methodologies (e.g., object-oriented software development) led to new programming paradigms and by extension, new programming languages

1-12

### Notes:

<!-- Slide number: 13 -->
# Computer Architecture Influence
Best-known computer architecture: Von Neumann
Imperative languages are most dominant, because of von Neumann computers
Data and programs stored in memory
Memory is separate from CPU
Instructions and data are piped from memory to CPU
Basis for imperative languages
Variables model memory cells
Assignment statements model piping
Iteration is efficient, recursion is discouraged


1-13

### Notes:

<!-- Slide number: 14 -->
# The von Neumann Architecture

![](Picture4.jpg)

1-14

### Notes:

<!-- Slide number: 15 -->
# Programming Methodologies Influences
1950s and early 1960s: Simple applications
Worry about machine efficiency
Late 1960s: People efficiency became important
Improved readability, better control structures
Structured programming
Top-down design and step-wise refinement
Late 1970s: Process-oriented to data-oriented
Data abstraction
Middle 1980s: Object-oriented programming
Data abstraction + inheritance + polymorphism

1-15

### Notes:
Structured programming uses block-like structures like sequences, selections (like if statements), and iteration (loop structures) to avoid goto statements. It is also often associated with modular programming, which breaks up the program into manageable parts (e.g. using functions, methods, or procedures).
