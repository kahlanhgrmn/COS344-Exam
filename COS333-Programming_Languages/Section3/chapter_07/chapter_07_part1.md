<!-- Slide number: 1 -->
# Chapter 7Part 1
Expressions and Assignment Statements

### Notes:

<!-- Slide number: 2 -->
# Chapter 7 Topics
Introduction
Arithmetic Expressions
Overloaded Operators
Type Conversions
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Introduction
Expressions
The fundamental means of specifying computations in a programming language
To understand expression evaluation
Must be familiar with the orders of operator and operand evaluation
Essence of imperative languages
The dominant role of assignment statements
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:

<!-- Slide number: 4 -->
# Arithmetic Expressions
Arithmetic evaluation
One of the motivations for the development of the first programming languages
For example: Fortran
Arithmetic expressions consist of
Operators (like + or *)
Operands (the objects or quantities operated on)
Parentheses
Function calls
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:

<!-- Slide number: 5 -->
# Arithmetic Expressions:Design Issues
Design issues for arithmetic expressions
Two related questions
What are the operator precedence rules?
What are the operator associativity rules?
What is the order of operand evaluation?
Are operand evaluation side effects restricted?
Is user-defined operator overloading allowed?
What type mixing is allowed in expressions?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# Arithmetic Expressions:Operators
A unary operator has one operand
A binary operator has two operands
A ternary operator has three operands
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:

<!-- Slide number: 7 -->
# Arithmetic Expressions:Operator Precedence Rules
Language defines a set of precedence levels
Typical precedence levels that group operators
Parentheses
Unary operators
The ** or ^ operator
Raise left operand to the power of right operand
In Fortran, Ruby, Ada, and Visual Basic
The ​* and / operators
The ​+ and - operators
Operator precedence rules
Define order in which “adjacent” operators of different precedence levels are evaluated
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# Arithmetic Expressions:Operator Associativity Rules
Operator associativity rules
Define the order in which adjacent operators with the same precedence level are evaluated
Typical associativity rules
Left to right (except **, which is right to left)
Some unary operators associate right to left
APL has only one precedence level
All operators associate right to left
Parentheses supported in many languages
Can override precedence and associativity rules
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:
As an example, in the C-based programming languages, the + and – operators are in the same precedence level, and are left to right associative. This means that if a number of + and – operators occur side by side, they are evaluated left to right. Therefore, the expression:

1 + 3 – 2

would be evaluated as though parentheses had been added as follows:

(1 + 3) – 2

The addition happens first because it is leftmost, then the subtraction happens.

In most C-based languages, unary postfix increment and decrement are left to right associative, while unary prefix increment and decrement are right to left associative. Therefore, the expression:

a ++ --

is equivalent to:

((a++)--)

where the postfix increment happens before the postfix decrement.

The expression:

++ -- a

is equivalent to:

(++(--a))

where the prefix decrement happens before the prefix increment

<!-- Slide number: 9 -->
# Arithmetic Expressions:Ruby Expressions
In Ruby
Most operators are implemented as methods
This includes
Arithmetic, relational, and assignment operators
Array indexing operator
Shift operators
Bit-wise logic operators
Because these operators are methods
All of them can be overriden by the programmer
Impact on language evaluation criteria?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:
In Ruby, all arithmetic operators are implemented as methods. There are, however, other operators that are not implemented as methods, notably Boolean operators.

<!-- Slide number: 10 -->
# Arithmetic Expressions:Scheme and Common LISP Expressions
In Scheme and Common LISP
All arithmetic and logic operations
Are implemented as explicitly called subprograms
We looked at this in Chapter 15
For example, the expression a + b * c
Is written as (+ a (* b c))
Here + and * are functions
How does this affect precedence and associativity?
Scheme is dynamically typed
So operator overloading doesn’t make sense
Why does dynamic typing have this effect?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:

<!-- Slide number: 11 -->
# Arithmetic Expressions:Conditional Expressions
Conditional Expressions
Supported in the C-based languages
An example conditional expression
		  average = (count == 0)? 0 : sum / count

The expression evaluates as if written as follows
		  if (count == 0)
        average = 0
		  else
        average = sum / count

Effect on language evaluation criteria?

Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:
The semantics of the conditional expression are as follows:
There are two operator symbols (? and :) and three operands (one before the ? symbol, one between the ? and : symbols, and one after the : symbol).
The first operand is a Boolean expression, and is evaluated.
If the Boolean expression is true, the entire conditional expression evaluates to the second operand (the operand between the ? and : symbols).
If the Boolean expression is false, the entire conditional expression evaluates to the third operand (the operand after the : symbol).

<!-- Slide number: 12 -->
# Arithmetic Expressions:Operand Evaluation Order
Operand evaluation order
Variables
Fetch the value from memory
Constants
Sometimes a fetch from memory
Sometimes in the machine language instruction
Parenthesized expressions
Evaluate all contained operands & operators first
The most interesting case
When an operand is a function with side effects
We covered this in Chapter 15
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:

<!-- Slide number: 13 -->
# Overloaded Operators
Operator overloading
Use of an operator for more than one purpose
Some are common and safe
For example, + used for int and float addition
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:

<!-- Slide number: 14 -->
# Overloaded Operators
Some overloaded operators are problematic
For example, the & operators in C and C++
Used as a binary operator for bitwise logical AND
Used as a unary operator for declaring references and for the address-of operator
Problems
Some loss of readability
Loss of compiler error detection
If you accidentally forget the first operand
Error undetected and & is treated as unary operator
Now consider the * operators in C and C++
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:

<!-- Slide number: 15 -->
# Overloaded Operators
User-defined overloaded operators
C++, C#, and F# support this
Can aid readability when sensibly used
More natural than methods (+ vs add method)
Potential problems
Users can define nonsensical operations
Readability may suffer, even when used sensibly
To understand what an operator does
User must find types of the operands
Different sensible operator implementations
Adding lists: Concatenate or pairwise add elements?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:
Nonsensical operations are simply operations that bear no relation to the operator. For example, defining a + operator to print out the operator’s two operands.

The necessity of finding the types of the operands can be illustrated by the following expression:

a + b

We can’t determine what the expression does by just looking at it. We first need to find what the types of the variables a and b are. This will require us to find the declarations for the variables. All this makes the expression more difficult to read.

Consider the example of adding lists. Let’s assume we have two lists: lis1, which contains the elements [1, 2, 3] and lis2, which contains the elements [4, 5, 6]. Now let’s assume we add them as follows:

lis1 + lis2

There are different sensible interpretations of the operation. One possible interpretation is concatenation, in which a new list is constructed containing the elements in the two operands. This would produce a list containing the elements [1, 2, 3, 4, 5, 6]). Another possible interpretation is a pairwise addition, where corresponding values in the two lists are added to create a new list. In this case, the resulting list would contain the elements [5, 7, 9]. There may be other equally valid interpretations of the addition operation for lists.

<!-- Slide number: 16 -->
# Type Conversions
Narrowing conversion
Converts an object to a type that cannot include all of the values of the original type
Not always safe (value’s magnitude may be lost)
For example, float to int
Widening conversion
Converts an object to a type including at least approximations of all the original type’s values
Generally safe (value’s magnitude preserved)
May lose accuracy
For example, int to float
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:
A float value has a much wider range than an int does. This means that a float value that is either greater than the maximum possible int value, or less than the minimum possible int value, cannot possibly be represented as an int.

An int value has a range that is contained within the range of a float. This means every possible int value can be converted into a float value. Due to the limitations of floating point representations, the float value may not be able to represent the int value perfectly accurately (there may be a very small additional fractional part in the float value). However, the int value is at least approximately represented by the float.

<!-- Slide number: 17 -->
# Type Conversions: Mixed Mode
Mixed-mode expression
Expression that has operands of different types
For example, if a is an int and b is a float
The expression a + b is mixed mode
Addition can’t take place as-is
Coercion
Implicit (automatic) type conversion of operands
Allows mixed mode expression to evaluate
In example, a changes to float or b changes to int
Decreases compiler’s type error detection ability
What kinds of errors can’t be detected?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:

<!-- Slide number: 18 -->
# Type Conversions: Mixed Mode
Many languages
Coerce all numeric types in expressions
Use widening conversions (why?)
In ML and F#
No coercions in expressions
What does this imply?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:

<!-- Slide number: 19 -->
# Type Conversions: Explicit Conversions
Explicit type conversion
Programmer-specified type conversions
Either narrowing or widening
Compiler may give warnings if a narrowing conversion significantly changes an object value
Examples
Called casting in the C-based languages
(int) angle
F# uses a similar syntax to a function call
float(sum)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:
C++ also provides functional casting notation, which has the same syntax as a cast in F#. This does the same thing as the traditional C-style cast. The semantics of what happens when either a C-style cast or a functional cast takes place in C++ are relatively complex (they can be equivalent to static_cast, const_cast, or reinterpret_cast, depending on the situation), which is one of the reasons that the explicit C++ casts (static_cast, const_cast, or reinterpret_cast) are preferred.

<!-- Slide number: 20 -->
# Type Conversions: Errors in Expressions
Causes of expression errors
Type checking and coercion (already discussed)
Inherent limitations of arithmetic
For example, division by zero
Can you think of others?
Limitations of computer arithmetic
Overflow, when a computation produces a value larger or smaller than a type can represent
Can you think of others?
Some run-time errors can be ignored
May require exception handling mechanisms
Copyright © 2023 Addison-Wesley. All rights reserved.
1-20

### Notes:
