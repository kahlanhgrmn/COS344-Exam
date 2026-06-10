<!-- Slide number: 1 -->

![Front Cover: Concepts of Programming Languages, Global Edition, by Robert W Sebesta](Picture8.jpg)
# Chapter 2Part 3
Evolution of the Major Programming Languages

### Notes:

<!-- Slide number: 2 -->
# Chapter 2 Topics
Orthogonal Design: ALGOL 68
Some Early Descendants of the ALGOLs
Programming Based on Logic: Prolog
History's Largest Design Effort: Ada
Object-Oriented Programming: Smalltalk
Combining Imperative and OO Features: C++
An Imperative-Based OO Language: Java
Scripting Languages
The Flagship .NET Language: C#
Markup/Programming Hybrid Languages

1-2

### Notes:

<!-- Slide number: 3 -->
# Genealogy of Common Languages

![](Picture1.jpg)

1-3

<!-- Slide number: 4 -->
# Orthogonal Design: ALGOL 68
From continued development of ALGOL 60
Recall, aim of ALGOL 60: machine independence
But ALGOL 68 was very different from ALGOL 60
Never achieved widespread use
But the source of several new ideas
Design is based on orthogonality
Few basic concepts and combining mechanisms
Allowed for user-defined data structures
How does this contrast to the PL/I approach to support general purpose data structures?

1-4

### Notes:

<!-- Slide number: 5 -->
# ALGOL 68 Evaluation
Contributions
User-defined data structures
Reference types
Implicit heap-dynamic arrays (flex arrays)
Comments
Less usage than ALGOL 60 and PL/I
Too orthogonal in some ways
Language description in unknown meta-language
Van Wijngaarden grammar
Had strong influence on subsequent languages
Especially Pascal, C, and Ada

1-5

### Notes:

<!-- Slide number: 6 -->
# Pascal
Developed in 1971 by Wirth
A former member of the ALGOL 68 committee
Characteristics
Small and simple
Nothing really new
For teaching structured programming
From mid-1970s until the late 1990s, the most widely used language for teaching programming
Still used in South African schools in the early 2000s

1-6

### Notes:

<!-- Slide number: 7 -->
# C
Developed in 1972 by Dennis Richie
For systems programming at Bell Labs
Evolved from several languages
Primarily CPL, BCPL and B
But also from ALGOL 68
Powerful set of operators and functions
Poor type checking and other unsafe features
Initially spread through UNIX
Many areas of application
ANSI standard only in 1989, updated in 1999

1-7

### Notes:

<!-- Slide number: 8 -->
# Programming Based on Logic: Prolog
Programmation en logique
Collaborative developed
Comerauer and Roussel (University of Aix-Marseille)
Help from Kowalski (University of Edinburgh)
Overview
Based on formal logic
Non-procedural
Database of facts, combined with rules
Uses built-in inferencing process to infer the truth of queries
Highly inefficient
Few application areas

1-8

### Notes:

<!-- Slide number: 9 -->
# History’s Largest Design Effort: Ada
Developed for the US DoD
More than 450 languages were in use for DoD projects
They needed a standardized programming language
Initially intended for embedded system development
Huge design effort
Involving hundreds of people
A lot of money
About eight years
Named after Ada Lovelace, the first programmer

1-9

### Notes:

<!-- Slide number: 10 -->
# Ada Evaluation
Contributions
Packages: Support for data abstraction
Exception handling: A very elaborate system
Generic program units
Concurrency: Through the tasking and rendezvous model
Comments
Competitive design
Included everything known about software engineering and language design at the time
Usable compilers were not immediately available
Development of first compilers was very difficult
First usable compiler nearly five years after language design

1-10

### Notes:
Packages in Ada are essentially like classes in modern object-oriented programming languages.

Generic program units are like templates in C++ and generic types in Java. They are closer to C++ templates in terms of how they work. We’ll look at generic subprograms in detail in Chapter 9.

<!-- Slide number: 11 -->
# Object-Oriented Programming: Smalltalk
Developed at Xerox PARC
Initially by Alan Kay
Later by Adele Goldberg
First full implementation of true OOP
Data abstraction
Inheritance
Dynamic binding
Pioneered and promoted
Graphical user interface design
The OOP paradigm

1-11

### Notes:
Alan Kay’s PhD dissertation (published in 1969) was on a system he called Dynabook, which he envisioned as a desktop-like GUI system, similar to Microsoft Windows. He believed non-programmers would use it, and Smalltalk was developed as a programming language to support this system. Object-oriented programming naturally supports GUI systems, because the various elements (windows, buttons, etc) can be represented using objects.

<!-- Slide number: 12 -->
# Combining Imperative andObject-Oriented Programming: C++
Developed at Bell Labs by Stroustrup in 1980
Evolved from C and SIMULA 67
A large and complex language
Procedural (from C) and OOP (partially from SIMULA 67)
Exception handling, operator overloading, pointers, references, template functions, and classes
Rapidly grew in popularity
Good, cheap compilers
Backward-compatible with C
Only OO language at the time suitable for large projects
ANSI standard approved in November 1997
Microsoft’s Managed C++
Included with .NET in 2002
Properties, delegates, interfaces, no multiple inheritance

1-12

### Notes:

<!-- Slide number: 13 -->
# Related OOP Languages
Swift
Replacement for Objective-C released in 2014
Used by Apple for systems programs
Delphi
Developed by Anders Hejlsberg
He also designed Turbo Pascal
Later, the lead architect of C#
Pascal with features to support OOP
More elegant and safer than C++
Go
Designed at Google in 2009
Loosely based on C, but also quite different
Allows an object-oriented style of programming
But does not support traditional OOP

1-13

### Notes:
In what way is Delphi similar to C++ in its approach to support for OOP?

<!-- Slide number: 14 -->
# An Imperative-Based Object-Oriented Language: Java
Developed at Sun in the early 1990s
Initially for embedded electronic devices
C and C++ not suited to this task (unreliable)

Based on C++
Significantly simplified and more reliable
Discards C++ features
Removes struct, union, and enum
No pointers & pointer arithmetic (references only)
Half the assignment coercions
Supports only OOP
Supports applets, concurrency,  GUI design

1-14

### Notes:
Java does support enumerations, but they are implemented as classes, not primitive ordinal types, as in C++.

<!-- Slide number: 15 -->
# Java Evaluation
Eliminated many unsafe features of C++
Less powerful and flexible than C++
Many built-in libraries
Concurrency, applets, GUIs, database access
Portable
Java Virtual Machine, JIT compilers
Widely used for Web programming
Use increased incredibly quickly

1-15

### Notes:

<!-- Slide number: 16 -->
# Scripting Languages for the Web
In general, scripting languages are imperative
Differences from normal imperative languages
Intended purpose
Scripting languages: Smaller tasks
Full imperative languages: Larger tasks
Implementation system
Scripting languages: Usually interpreted
Full imperative languages: Usually compiled
Constructs
Scripting languages: Usually mostly dynamic
Full imperative languages: More static features

1-16

<!-- Slide number: 17 -->
# Scripting Languages for the Web
Perl
Designed by Larry Wall in 1987
Variables statically typed but implicitly declared
Denoted by first character of a variable’s name
Scalars: $, arrays: @, hashes: %
Powerful, but somewhat dangerous
Dynamic length, sparse arrays
Coercions between strings and numbers
No error detection for array access
Language uses
Initially for UNIX system text file processing
Widespread use for CGI programming on the Web
Still used for UNIX general system administration

1-17

### Notes:
We’ll talk about static and dynamic typing and related concepts in Chapter 5.

CGI programming involves a Web user’s HTTP or HTTPS request executing a server-side script, which produces output (usually in the form of HTML) which is set to the users Web browser. Server-side means that the script runs on a Web server.

<!-- Slide number: 18 -->
# Scripting Languages for the Web
PHP
Designed by Rasmus Lerdorf
Language name
Originally Personal Home Page
Later the recursive name PHP: Hypertext Preprocessor
Server-side, HTML-embedded scripting language
Often used for form processing
Also database access via the Web
Purely interpreted

1-18

<!-- Slide number: 19 -->
# Scripting Languages for the Web
JavaScript
Began at Netscape
Then joint venture of Netscape & Sun Microsystems
Language characteristics
A client-side, HTML-embedded
Often for dynamic HTML documents
Purely interpreted
Related to Java only through similar syntax

1-19

### Notes:
It’s important to note the difference between how Perl and PHP handle Web scripting, versus how JavaScript handles it. Perl and PHP are server-side scripting languages, meaning they execute on a server and send results to a user’s Web browser. JavaScript is client-side, meaning it runs on the user’s Web browser, not a server.

<!-- Slide number: 20 -->
# Scripting Languages for the Web
Python
An OO interpreted scripting language
Similar applications as Perl
CGI programming and form processing
System administration
More recent use in data science
Type checked, but dynamically typed
Language features
Pattern matching facilities
Exception handling
Garbage collection
Supports lists, tuples, and hashes
A large number of external libraries

1-20

### Notes:
As for Perl, CGI programming with Python is server-side Web scripting.

<!-- Slide number: 21 -->
# Scripting Languages for the Web
Ruby
Designed by Yukihiro Matsumoto (a.k.a. “Matz”)
First Japanese language to be widely used in US
Began as a replacement for Perl and Python
Purely interpreted

A very pure object-orientation design
All data are objects
Most operators are implemented as methods
User code can redefine operators
Classes and objects are dynamic
They can have different methods at different times

1-21

### Notes:
The last point is important to understand about Ruby, and makes the language quite unique. It’s possible to change classes and objects at runtime, meaning you can add or remove methods, or change how they behave. This is useful for creating classes in different forms at runtime, depending on changing requirements.

<!-- Slide number: 22 -->
# The Flagship .NET Language: C#
Part of the .NET development platform
Announced in 2000, released in 2002
Based on C++, Java, and Delphi
Improved many C++ features
Added some novel features for the time
Pointers, delegates, properties, enumeration types, limited dynamic typing, and anonymous types
Supports component-based development
Common Type System for .NET languages
Provides common class library and interoperability
Intermediate Language (IL) and JIT compiler
All .NET languages compile to IL
Evolving very rapidly

1-22

### Notes:
Component-based development is a very complex topic, beyond the scope of this module. In essence, it involves providing functionality in packaged code (known as components), which can be easily imported into other programs as required. Component-based development often uses components from different languages. The .NET languages support this by allowing classes and types to interoperate between all the languages in the .NET framework. This lets a programmer implement a component in one language, which can then be easily used in a program or component written by a different programmer in another language. This is further supported by the fact that all .NET languages compile to the same intermediate language.

<!-- Slide number: 23 -->
# Markup and Programming Hybrid Languages
XSLT and JSP
Both are based on markup languages
Markup languages define document structure
Extended with programming features
For example, loops, if blocks, and sorting

1-23

### Notes:
