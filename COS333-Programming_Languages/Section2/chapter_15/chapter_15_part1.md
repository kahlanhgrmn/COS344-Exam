<!-- Slide number: 1 -->

![Front Cover: Concepts of Programming Languages, Global Edition, by Robert W Sebesta](Picture8.jpg)
# Chapter 15Part 1
Functional Programming Languages

### Notes:

<!-- Slide number: 2 -->
# Chapter 15 Topics
Introduction
Mathematical Functions
Fundamentals of Functional Programming Languages
Introduction to Scheme
Origins of Scheme
The Scheme Interpreter
Function Evaluation
Primitive Numeric Functions
Defining Functions
Output Functions
Numeric Predicate Functions
Control Flow
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Introduction
Imperative language design is based directly on the von Neumann architecture
Efficiency is the primary concern
Suitability for software development is less important
The design of the functional languages is based on mathematical functions
A solid theoretical basis
Closer to the user
Unconcerned with machine architecture
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:

<!-- Slide number: 4 -->
# Mathematical Functions
A function is a kind of subprogram
A collection of parameterized computations
Produces results by returning values
Functional side effects
When a function changes a parameter or a global variable
Problem with functional side effects
When a function referenced in an expression alters another operand of the expression
For example
	 	  a = 10;
 		  b = a + fun(&a);
What if fun changes the value of its parameter?
How does the same problem arise with global variables?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:
Functional side effects and referential transparency are discussed in Section 7.2.2 of the textbook.

<!-- Slide number: 5 -->
# Mathematical Functions
Two possible solutions to the problem of side effects, both based on the language definition

Disallow functional side effects
No two-way parameters for functions
No non-local references in functions
Advantage
It works!
Disadvantage
Inflexibility of one-way parameters
Lack of non-local references

Demand fixed operand evaluation order
Java: Operands seem to be evaluated left to right
Disadvantage
Limits some compiler optimizations
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# Mathematical Functions
A program has referential transparency if
Any two expressions that are equivalent
Can be substituted for one another in the program
This does not affect the action of the program
One cause of referential transparency breakdown
Functional side effects
For example

If fun has no side effects, result1 = result2
If not, referential transparency is violated
How can referential transparency break in the example?
Can referential transparency break in other ways?
result1 = (fun(a) + b) / (fun(a) – a);
temp = fun(a);
result2 = (temp + b) / (temp – a);
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:

<!-- Slide number: 7 -->
# Mathematical Functions
Advantage of referential transparency
Program semantics much easier to understand
Programs in pure functional languages
Do not have variables
Consider a function
Global variables can’t exist (so can’t be modified)
Parameter value must be constant (no variables)
This means there is no possibility of side effects
Functions cannot have state
State must be stored in variables
Value of the function depends only on parameters
Thus such languages are referentially transparent
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# Fundamentals of Functional Programming Languages
The objective of a functional language’s design
To mimic mathematical functions as closely as possible
The basic process of computation is fundamentally different in a FPL than in an imperative language
In an imperative language
Expressions are evaluated and the results are stored in variables for later use
Management of variables is a constant concern and a source of complexity for imperative programming
In a purely functional language
Variables are not used, as is the case in mathematics
We don’t need to worry about managing variables and the associated ambiguity
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:

<!-- Slide number: 9 -->
# Origins of Scheme
LISP
The first functional programming language
Scheme
A mid-1970s dialect of LISP
Designed to be a cleaner, more modern, and simpler version than contemporary LISP dialects
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:

<!-- Slide number: 10 -->
# Scheme Data Objects & Structures
Data object categories
Atoms and lists
Two kinds of atoms
Symbols (identifiers like a and x)
Numeric literals (like 4.8 and 26)
List form
Sequences of atoms and/or sublists
Stored internally as single-linked lists
(a b (c d) e)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:
Symbolic atoms are things like A and X. They don’t have an intrinsic meaning, and aren’t characters or strings. They were originally designed for AI applications to represent the idea of abstract concepts that AI programs could work with.

Numeric atoms are things like 4.8 and 26. We can perform arithmetic operations on them, like in an imperative language.

Both symbolic and numeric atoms can be stored in lists.

<!-- Slide number: 11 -->
# The Scheme Interpreter
Data and function applications have the same form
The list (a b c) interpreted as data
A simple list of 3 atoms, namely a, b, and c
The list (a b c) interpreted as a function application
The function named a is applied to two parameters, b and c
The result is that functions are first-class entities
Functions can be passed as parameters to other functions
Functions can be returned by another function
Scheme programs are built up of only functions
There are no operators or control structures
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:

<!-- Slide number: 12 -->
# Function Evaluation
Literals evaluate to themselves
Function applications evaluated as follows
Parameters are evaluated, in no particular order
Values of parameters substituted into the function body
The function body is evaluated
The value of the last expression evaluated in the body is the value that the function defines
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:
Here “no particular order” means that there is an order of parameter evaluation implemented in a Scheme interpreter (this is required for the interpreter to work), but that the order is unimportant. Firstly, if the parameters are just values, the order they are handled in obviously doesn’t matter. But if the parameters are applications of functions (what you know as function calls) the order of evaluation is still unimportant. This is because, as we’ve seen before, functional languages have no functional side effects. This means that no parameter evaluation can affect any other parameter evaluation, and so the order the functions are evaluated in can’t affect the final outcome.

The last point on this slide is also important to remember.

<!-- Slide number: 13 -->
# Primitive Numeric Functions
Arithmetic operations
Remember that these are all functions!
Includes a set of primitive functions
We’ll use ‎+, -, *, /, abs, sqrt, remainder, min, and max
For example
The function application (+ 5 2) yields 7
Most can use multiple parameters
For example, (+ 5 2 8 9)
Except abs, sqrt, and remainder
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:
Remember that everything in Scheme is a function. So +, -, *, and / are actually the names of functions that are provided by Scheme. Notice that their syntax is exactly the same as a normal function (function name first, followed by parameters).

<!-- Slide number: 14 -->
# Defining Functions
Two general forms of define

To bind a name to the value of an expression
Examples
		    (define pi 3.141593)
		    (define two_pi (* 2 pi))

The binding can happen only once (unlike a variable)

To bind names to functions
For example
		    (define (square x) (* x x))

We can now use the name in a function application
	  (square 5)

The evaluation process for define is different!
First parameter is not evaluated as a normal function would
If it were evaluated, Scheme would find it was undefined

Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:
The term “binding” simply means an association (or linking). The first example under point 1 uses define to bind (or associate, or link) the name pi to the numeric literal 3.141593. From this point the symbol pi now “means” 3.141593. The second example under point 1 uses define to bind the name two_pi to the value of the expression (* 2 pi). The value of the expression (* 2 pi) is 6.28318, so from this point the symbol two_pi now “means” 6.28318.

The first example under point 2 uses define to bind the name “square” to the lambda expression (lambda (x) (* x x)). Note that we use an abbreviated form for the lambda expression, because we don’t have to explicitly use the lambda function within the define. It is actually possible to use the full lambda expression syntax within a define, but we won’t be doing this to make our programs more readable.

We will mostly be using define when we write functions. This means that we now have a name for the function, which we can use anywhere in our program. The define function is therefore useful on its own (as in the second example), unlike lambda in the first and third examples on the previous slide. You can think of define as achieving the same thing as a function declaration in a language like C++. However, also take note that define is a function itself, which simply performs a binding of a name to a lambda expression, so it is actually not the same thing as a function declaration.

<!-- Slide number: 15 -->
# Output Functions
To print an expression
	(display expression)
To print a newline character
	(newline)
Generally, however, output functions aren’t used
Programs simply use the interpreter’s normal output
Any top-level (not nested) function result is printed
Explicit input and output are not part of pure FP
Input operations change the state of the program
Output operations are side effects
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:
Related to the last point: Of course, for a functional language to be useful we can’t avoid input and output. So even a “pure” functional language can’t entirely get away from side effects. In practise, however, input and output are fairly safe side effects.

<!-- Slide number: 16 -->
# Numeric Predicate Functions
Predicate function
A function that defines a Boolean value
The value #t is true, the value #f is false
Sometimes () is used for #f
Any non-null list is interpreted as #t

Predefined predicate functions for numbers
For multiple parameters
We’ll use ‎=, >, <, >=, and <=
Single value tests
We’ll use ‎even?, odd?, zero?, negative?, positive?
The not function is applied to a Boolean parameter
Inverts the logic of a Boolean expression
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:
In Scheme, <> refers to the “not equals” comparison. This function is, unfortunately, not supported in DrRacket. You can use a combination of the not and = functions to achieve the equivalent functionality.

Again, note that =, >, <, >=, and <= are actually the names of functions.

Finally, these numeric predicate functions only work for numeric atoms, not symbolic atoms.

<!-- Slide number: 17 -->
# Control Flow: if function
Two-way selector, with the following general form
    (if predicate then_exp else_exp)

For example
    (define (divide numer denom)
       (if (= denom 0)
          0
          (/ numer denom)
       )
    )

    (divide 1.0 2.0)
    (divide 5.0 0.0)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:
The else expression can be left out in many implementations of Scheme (although this is almost never useful). In this case, if the predicate is false, an unspecified evaluation is produced. An unspecified evaluation actually produces a result that denotes an “undefined” value. Typically, this represents a mistake in an implementation, because you can’t do anything useful with an undefined value. However, in DrRacket, the else expression is required.

In this example, define produces a function named “divide”, which takes two parameters, “numer” and “denom”.
The function tests to see if denom is 0. If it is, the result of the entire divide function is 0. Why is the 0 not placed in parentheses?
If denom is not 0, numer is divided by denom, and the result of this division becomes the result of the divide function.

Again, note that if is a function. Its parameters are two expressions. Each expression can either be a simple value, like 0, or a function application, like (/ numer denom).

<!-- Slide number: 18 -->
# Control Flow: cond function
Multiple selector, with the following general form

    (cond
       (predicate_1  expression)
       (predicate_2  expression)
       ...
       (predicate_n  expression)
       (else expression)
    )

Evaluates to the value of the expression for the first predicate that evaluates to true
If no predicate is true
Evaluates to the optional else expression
Evaluation is unspecified if no else is provided
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:
The cond function is discussed in Section 8.2.2.4 of the textbook.

Often you’ll see cond used where an if would also work (i.e. when there are only two predicate-expression pairs in the cond). Either is correct in a test/exam situation.

As is the case with the if function, an unspecified evaluation actually produces a result that denotes an “undefined” value. In DrRacket, this value is denoted #<void>

<!-- Slide number: 19 -->
# Control Flow: Repetition
How do we handle repetition in Scheme?
Scheme is a pure functional programming language
There are no variables
Therefore no loop control variables or loops
All repetition is handled through recursion
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:
