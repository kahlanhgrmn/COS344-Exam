<!-- Slide number: 1 -->
# Chapter 7Part 2
Expressions and Assignment Statements

### Notes:

<!-- Slide number: 2 -->
# Chapter 7 Topics
Relational and Boolean Expressions
Short-Circuit Evaluation
Assignment Statements
Mixed-Mode Assignment
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Relational and Boolean Expressions:Relational Expressions
Relational expressions evaluate to Booleans
JavaScript and PHP
The relational operators == and !=
Equality and inequality check with operand coercion
Therefore "7" == 7 is true
The relational operators === and !==
Similar to == and != with no operand coercion
Therefore "7" === 7 is false
Ruby
Uses == for numeric equality with coercions
Uses eql? for numeric equality without coercions
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:
In the case of "7"==7, the string is coerced into an integer in both JavaScript and PHP.

In Ruby, equality with coercions does not allow comparison of strings and numbers (in terms of the example, "7" == 7 will be false), but it does allow the comparison of numeric values of different types (so 7 == 7.0 would be true). Therefore, in Ruby:

1 == 1.0     # returns true
1.eql? 1.0   # returns false

<!-- Slide number: 4 -->
# Relational and Boolean Expressions:No Boolean Type in C
Boolean Expressions
Operands and result of expression are Boolean
C89 has no Boolean type
Uses int type for operands
Nonzero interpreted as true, 0 interpreted as false
Boolean expressions evaluate to int values
True expression evaluates to 1
False expression evaluates to 0
One odd result of this design
​a < b < c  is legal but works unexpectedly
Left operator (a < b) is evaluated, producing 1 or 0
Tests if 1 or 0 result is less than third operand (c)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:
What is the result of the last point, in terms of the programming language evaluation criteria?

<!-- Slide number: 5 -->
# Short Circuit Evaluation
Short circuit evaluation computes result
Doesn’t evaluate all operands and/or operators
For example, (13 * a) * (b / 13 – 1)
If a is zero, no need to evaluate (b / 13 - 1)
Problem with non-short-circuit evaluation
Assume that list has length elements

	  index = 0;
	  while ((index < length) && (list[index] != value)) {
		    index++;
		 }

What if && is not short-circuit evaluated?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# Short Circuit Evaluation
Examples
C, C++, and Java
Standard Boolean operators are short-circuit (&& and ||)
Bitwise Boolean operators are not short circuit (& and |)
Ruby, Perl, ML, F#, and Python
All logic operators are short-circuit evaluated
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:

<!-- Slide number: 7 -->
# Short Circuit Evaluation
Short-circuit evaluation can be a problem
If side effects are expected in expressions
For example
Assume that || is a short-circuit logical OR
   (a > b) || (b++ / 3)
Recall that a functional side effect occurs when a function modifies a parameter or a global variable
Operators cause side effects by changing operands
Which operator causes a side effect?
If we rely on the fact that this side effect occurs every time the expression is evaluated
When will the side effect not occur?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# Assignment Statements
The general syntax
  <target_var> <assign_operator> <expression>
The assignment operator
FORTRAN, BASIC, and the C-based languages
Use the = operator
The ALGOLs, Pascal, and Ada
Use the := operator
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:

<!-- Slide number: 9 -->
# Assignment Statements
Possible problem
If = is overloaded for relational equality operator
Ambiguity between assignment and equality test
Solutions to this problem
C-based languages use == as relational operator
ALGOL 58’s := operator is unambiguous
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:

<!-- Slide number: 10 -->
# Assignment Statements:Conditional Targets
Conditional targets
Provided by Perl
Similar to conditional expressions
But are used as the target of an assignment
Conditional targets have the form
	     ($flag ? $total : $subtotal) = 0

Which is equivalent to
	     if ($flag){
		      $total = 0
	     } else {
		      $subtotal = 0
	     }
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:

<!-- Slide number: 11 -->
# Assignment Statements:Compound Assignment Operators
Compound assignment operators
A shorthand method of specifying a commonly needed form of assignment
Introduced in ALGOL 68, later adopted by C
For example
The compound assignment
	    a += b
Is equivalent to the normal assignment
	    a = a + b
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:

<!-- Slide number: 12 -->
# Assignment Statements:Unary Assignment Operators
Unary assignments in C-based languages
Combine increment/decrement with assignment
Prefix increment count, then assign to sum
	    sum = ++count

Assign count to sum, then postfix increment count
	    sum = count++

Postfix ++ and --
Are left to right associative
    count++-- is equivalent to (count++)—

Prefix ++ and --, and unary + and -
 Are right to left associative
	    -++count is equivalent to -(++count)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:
Also note that the postfix increment/decrement operators have a higher precedence than prefix increment/decrement and unary plus/minus. Prefix increment/decrement and unary plus/minus are on the same precedence level.

<!-- Slide number: 13 -->
# Assignment Statements:Assignment as an Expression
In C-based languages, Perl, and JavaScript
An assignment statement produces a result
The result is the value that has been assigned
For example, the value of this assignment is 4
 number = 4

This means that
An assignment can be used as an expression
An assignment can be used as an operand
For example
	if (a == (b = c)) { ... }
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:

<!-- Slide number: 14 -->
# Assignment Statements:Assignment as an Expression
In C-based languages, Perl, and JavaScript
Common example of assignment as an operand

   while ((ch = getchar())!= EOF){ ... }

ch = getchar() reads input character, assigns it to ch
The value assigned to ch is the assignment’s result
Assignment’s result is compared to the EOF character
Problems
Reduces error detection if  ==  is mistyped as  =
For example, if (x = y) { ... } is valid
Assignment can cause a side effect
Recall operators cause side effects by changing operands
How is a side effect caused in the first example?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:
EOF is the end-of-file condition. If the program is reading from a file, this is simply the end of the file. If the program is reading from the keyboard, end-of-file is triggered by pressing Ctrl-z followed by the Enter key in Windows. In Unix/Linux, the end-of-file is usually triggered by pressing Ctrl-d.

<!-- Slide number: 15 -->
# Assignment Statements:Multiple Assignments
Perl, Ruby, and Lua
Multiple-target multiple-source assignments
For example, in Perl
	  ($first, $second, $third) = (20, 30, 40);
Even allows an easy swap of variable values!
	  ($first, $second) = ($second, $first);
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:
In Perl, Ruby, and Lua, additional variables on the left hand side of the assignment are simply not assigned to. Similarly, additional values on the right hand side of the assignment are not assigned.

In Ruby and Lua, the syntax for a multiple-target multiple-source assignment is as follows:

first, second, third = 20, 30, 40

<!-- Slide number: 16 -->
# Assignment Statements:Assignment in Functional Languages
As we’ve seen, in functional languages
Identifiers are only names for values
In ML
Names are bound to values with val
	  val fruit = apples + oranges;
If another val for fruit follows
It is a new name, and the previous fruit is hidden
In F#
The F# let is like val in ML
However, let also creates a new scope

Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

<!-- Slide number: 17 -->
# Assignment Statements:Mixed-Mode Assignment
Assignments can also be mixed-mode
Right and left operands have different types
Can assign value of different type than variable
In Fortran, C, C++, and Perl
Coercion rules allow assignments
From any numeric type value
To any numeric type variable
What problem can this cause?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:

<!-- Slide number: 18 -->
# Assignment Statements:Mixed-Mode Assignment
In Java and C#
Only widening assignment coercions are done
Why is this safer than Fortran, C, C++, and Perl?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:
