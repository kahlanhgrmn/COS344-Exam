<!-- Slide number: 1 -->
# Chapter 8Part 1
Statement-Level Control Structures

### Notes:

<!-- Slide number: 2 -->
# Chapter 8 Topics
Introduction
Selection Statements
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Control Statements: Evolution
Fortran I control statements
Based directly on IBM 704 hardware
Recall three-way selection statement (Chapter 2)
Much research and argument in the 1960s
One important result
All flowchart-represented algorithms can be coded with only two-way selection & pretest logical loops
Thus, an unconditional branch statement (i.e. the goto statement) is unnecessary
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:
To use a goto statement, you have to provide a statement label where you want control to jump to. The goto statement then includes this statement label. When execution reaches the goto statement, control immediately jumps to statement label.

<!-- Slide number: 4 -->
# Control Structure
A control structure is
A control statement, and
The statements whose execution are controlled
One design question for all control structures
Should a control structure have multiple entries?
Only possible with goto and statement labels
Generally considered to add little flexibility relative to the decreased readability they introduce
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:

<!-- Slide number: 5 -->
# Selection Statements
A selection statement provides
Choice between two or more execution paths
Two general categories
Two-way selectors
Multiple-way selectors
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# Two-Way Selection Statements
General form

	if control_expression
	then clause
	else clause

Design issues
What is the control expression’s form & type?
How are the then and else clauses specified?
How should nested selectors be disambiguated?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:

<!-- Slide number: 7 -->
# The Control Expression
The then clause
Can be introduced by a then special word
	  if condition then then_clause

The control expression can be in parentheses
	  if (condition) then_clause

In C89, C99, Python, and C++
Control expression can be arithmetic
Integer condition is interpreted as Boolean value
In most other languages
Control expression must be Boolean
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:
Note that parentheses are not required if a then special word is used to introduce the then clause. Why is this?

<!-- Slide number: 8 -->
# Clause Form & Disambiguating Nested Selectors
Java example

	  if (sum == 0)
	    if (count == 0)
	      result = 0;
	  else result = 1;

Which if gets the else?
Java uses a semantic rule
Each else matches with the nearest if
So the else actually matches with the inner if
Even though the indentation suggests otherwise
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:
Which effects does this approach have on the programming language evaluation criteria?

<!-- Slide number: 9 -->
# Clause Form & Disambiguating Nested Selectors
To force alternative semantics
Must use compound statements (block)
For example

	     if (sum == 0) {
	       if (count == 0)
	         result = 0;
	     }
	     else result = 1;

Now the else matches with the outer if
This solution is used in C, C++, and C#
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:

<!-- Slide number: 10 -->
# Clause Form & Disambiguating Nested Selectors
Perl
Forces all then and else clauses to be compound
Even if a clause contains only a single statement
This eliminates any ambiguity
The previous example written in Perl

	  if ($sum == 0) {
	     if ($count == 0) {
	        $result = 0;
	     }
	  } else {
	     $result = 1;
	  }
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:
Which effects does this approach have on the programming language evaluation criteria?

<!-- Slide number: 11 -->
# Clause Form & Disambiguating Nested Selectors
Ruby
Clauses are statement sequences
Special word end marks selection statement end
This also eliminates any ambiguity
Is this really different to Perl’s approach?
The previous example written in Ruby

		  if sum == 0 then
		     if count == 0 then
		        result = 0
		     end
		  else
		     result = 1
		  end
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:
Which effects does this approach have on the programming language evaluation criteria?

<!-- Slide number: 12 -->
# Clause Form & Disambiguating Nested Selectors
Python
Clauses are statement sequences
Indentation eliminates ambiguity
Can use either spaces or tabs (but not both)
What problem could this result in?
The previous example written in Python

		if sum == 0 :
		   if count == 0 :
		      result = 0
		else :
		   result = 1
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:
Which effects does this approach have on the programming language evaluation criteria?

<!-- Slide number: 13 -->
# Selector Expressions
In ML, F#, and LISP
The selection statement is an expression
This means the statement evaluates to a value
For example, in F#
          let y =
            if x > 0 then x
            else 2 * x

If x is greater than 0, x is assigned to y
If x is 0 or less, 2 * x is assigned to y
If the if expression returns a value
There must be an else clause
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:
More specifically, if there is no else clause, the if yields a unit value (this is similar to a null value). The then and else clauses must have matching types, which means the then clause must also yield a unit value. This is typically not useful in a practical setting.

Lisp has similar behaviour. A missing else causes the if to yield a nil value.

<!-- Slide number: 14 -->
# Multiple-Way Selection Statements
Allow the selection of one of any number of statements or statement groups
You’ll know these as switch or case statements
Design issues
What is the control expression’s form & type?
How are the selectable segments specified?
Is execution through the structure restricted to include just a single selectable segment?
How are the case values specified?
Are unrepresented expression values handled?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

<!-- Slide number: 15 -->
# Multiple-Way Selection: Examples
In C, C++, Java, and JavaScript

	    switch (control_expression) {
	      case const_expr_1: segment_1;
	      ...
	      case const_expr_n: segment_n;
	      [default: segment_n+1]
	    }

Control expression is compared to constants
Finds first matching constant expression
Corresponding selectable segment is executed
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:

<!-- Slide number: 16 -->
# Multiple-Way Selection: Examples
Design choices for C’s switch statement
Control expression and constant expressions can be integers, characters or enumerations
Selectable segments can be statement sequences, or compound statements (blocks)
Control can flow through multiple segments
Explicit unconditional branch (break) at end of selectable segment, or control flows to next segment
Default clause is for unrepresented values
If control expression matches no constant expressions and no default is present, the whole statement does nothing
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

<!-- Slide number: 17 -->
# Multiple-Way Selection: Examples
C# differs from C
Has a semantic rule that disallows the implicit execution of more than one segment
Each selectable segment must end with an unconditional branch (i.e. goto or break)
Only situation where an unconditional branch can be left out is when the selectable segment is empty
What effect does this have on the reliability of C#?
Both the control expression and the case constants can be strings (not possible in C)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:
A break has the same syntax and semantics as a break in a C++ or Java switch statement.

A goto needs a case label to which control is passed. For example:

switch (n)
{
   case 0:
   case 1:
      cost += 25;
      break;
   case 2:
      cost += 25;
      goto case 1;
   case 3:
      cost += 50;
      goto case 1;
   default:
      Console.WriteLine("Invalid selection.");
      break;
}

Note that a continue can be left out only if there is no selectable code segment (look at case 0). If there is selectable code, there must be either a break or continue at the end of the selectable segment.

<!-- Slide number: 18 -->
Multiple-Way Selection: Examples
Ruby has two forms of case expressions
This means that the case produces a result
First form of case expression
Uses only when conditions (no case value)
Works like a sequence of if-then-else statements
For example
		   leap = case
		             when year % 400 == 0 then true
		             when year % 100 == 0 then false
		             else year % 4 == 0
		          end
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:
Both forms of the case expression produce a result, which can be used directly (e.g. in this example, where the appropriate Boolean value will be assigned to leap).

<!-- Slide number: 19 -->
Multiple-Way Selection: Examples
Ruby has two forms of case expressions
Second form of case expression
Uses a case value and when values
Works more like a traditional switch
For example
		   val = case in_val
		            when -1 then threshold - 1
		            when 0 then threshold
		            when 1 then threshold + 1
		            else error_code
		         end
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:
Both forms of the case expression produce a result, which can be used directly (e.g. in this example, where the appropriate integer value will be assigned to val).

<!-- Slide number: 20 -->
# Multiple-Way Selection Using if
Multiple Selectors
Boolean multiple selection alternative to poorly readable nested two-way selection statements
For example, in Python:

	  if count < 10 :
	     bag1 = True
	  elif count < 100 :
	     bag2 = True
	  elif count < 1000 :
	     bag3 = True
Copyright © 2023 Addison-Wesley. All rights reserved.
1-20

### Notes:
This is similar to the first form of Ruby’s case expression, except that Python’s multiple selectors don’t produce values.
