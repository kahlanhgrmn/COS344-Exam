<!-- Slide number: 1 -->
# Chapter 8Part 2
Statement-Level Control Structures

### Notes:

<!-- Slide number: 2 -->
# Chapter 8 Topics
Iterative Statements
Unconditional Branching
Guarded Commands
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Iterative Statements
Either iteration or recursion
Achieve the repeated execution of a statement or compound statement
We’ll focus on iteration here
General design issues for all iteration control statements
1. How is iteration controlled?
2. Where is the control mechanism in the loop?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:
The second design decision relates to whether the control mechanism is at the top of the statement (like a while loop), the bottom of the statement (like a do-while loop), or somewhere else (like a for loop, which places it in the middle of three control statements at the top of the loop).

<!-- Slide number: 4 -->
# Counter-Controlled Loops
Counting iterative statement has
Loop variable
Variable’s initial, terminal, and stepsize values
Design issues
What are the type & scope of the loop variable?
Should it be legal for the loop variable or loop parameters to be changed in the loop body, and if so, does the change affect loop control?
Should the loop parameters be evaluated only once, or once for every iteration?
What is the loop variable’s value after the loop?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:

<!-- Slide number: 5 -->
# Counter-Controlled Loops: Examples
The C-based languages

	  for ([expr_1]; [expr_2]; [expr_3]) statement

The expressions
1st expression is evaluated once
2nd and 3rd expressions evaluated each iteration
If 2nd or 3rd statement is absent: an infinite loop
Expressions may be
Whole statements
Statement sequences, separated by commas
Evaluates to value of last statement in expression
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:
As you should know, typically expr_1 is used to initialise the loop variable, expr_2 is the loop condition (evaluated at the start of each iteration), and expr_3 is the loop variable update (evaluated at the end of each iteration).

<!-- Slide number: 6 -->
# Counter-Controlled Loops: Examples
C-based languages’ design choices
There is no explicit loop variable
Everything can be changed in the loop
Legal to branch into the body of the loop in C
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:
How do these decisions affect the programming language evaluation criteria?

<!-- Slide number: 7 -->
# Counter-Controlled Loops: Examples
C++ differs from C in two ways:
The control expression can also be Boolean
C only supports integer-represented Boolean
Initial expression can include variable definitions

   for (int i = 0; ...; ...) { ... }

Scope is from definition to end of the loop body

Java and C# differ from C++
The control expression must be Boolean
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# Counter-Controlled Loops: Examples
Python

	  for loop_variable in object:
	    loop body
	  [else:
	    else clause]

Object is often a range
A list of values in brackets, like [2, 4, 6]
Range function call: range(3) returns [0, 1, 2]
Loop variable takes on range values each iteration
Optional else clause
Executes if loop terminates normally (not via a break)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:
The else clause is not commonly seen in other programming languages. Can you think of a situation in which it might be useful?

<!-- Slide number: 9 -->
# Logically-Controlled Loops
Repetition control uses Boolean expression
More general than counter-controlled loops
Every counter-controlled loop can be written as a logically-controlled loop
The opposite is not always true
Design issues:
Should control be pretest or posttest?
Should logically controlled loop be special case of counting loop statement, or separate statement?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:

<!-- Slide number: 10 -->
# Logically-Controlled Loops: Examples
C and C++ have pretest and posttest forms

Java is like C and C++, except:
Body can only be entered at the beginning
This is because Java has no goto statement
Effect on language evaluation criteria?
do
  loop body
while (ctrl_expr)
while (ctrl_expr)
  loop body
and
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:
As you should know, a pretest while loop evaluates the control expression before the first iteration (meaning the loop body may never execute), while the posttest while loop evaluates the control expression after the first iteration (meaning the loop body executes at least once).

<!-- Slide number: 11 -->
# User-Located Loop Control Mechanisms
Sometimes convenient
To choose location for loop control
Where location is not top or bottom of the loop
Simple design for single loops
For example, using a break or continue
Design issues for nested loops
Should a conditional be part of the exit?
Something like break(condition)
Why? How often does a break have no condition?
Is control transferrable out of multiple loops?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:
Design issue 1 relates to whether a condition should be part of a break or continue statement, or whether a programmer is responsible for the condition themselves. C++ and Java require the programmer to include whichever condition they want using a selection statement. For example:

while (test)
{
   …
   if (something == somethingElse)
   {
      break;
   }
}

It is possible for a break or continue to incorporate a condition (similar to the if statement’s condition in the example). Something like this:

break (something == somethingElse);

What would the effect of this be in terms of the language evaluation criteria?

The second design issue requires labeled break or continue statements (see the slide 35).

<!-- Slide number: 12 -->
# User-Located Loop Control Mechanisms
C , C++, Python, Ruby, and C#
Have unconditional unlabeled exits ( break)
Skips rest of current iteration and exits the loop
C, C++, and Python
Have an unlabeled continue control statement
Skips rest of current iteration without exiting loop
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:

<!-- Slide number: 13 -->
# User-Located Loop Control Mechanisms
Java and Perl
Have unconditional labeled exits
Called break in Java, last in Perl
Used to exit out of any loop
In Java

	   first:
	   for (int i = 0; i < 10; i++) {
	      second:
	      for (int j = 0; j < 5; j++) {
	         break xxx;
	      }
	   }
xxx can be either
first or second
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:
If xxx is second, the break behaves the same way as in C or C++ (i.e. the inner loop terminates, and control moves on to the next iteration of the outer loop). If xxx is first, the break terminates both loops, and execution continues after the outer loop.

The same is possible with the continue loop control mechanism, with the difference being that the loop in question doesn’t terminate, but rather skips the rest of the loop body and begins with its next iteration.

<!-- Slide number: 14 -->
# User-Located Loop Control Mechanisms
Java and Perl
Also have a labeled continue
Allow specification of which loop to continue
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:

<!-- Slide number: 15 -->
# Iteration Based on Data Structures
Iteration controlled by
Number of elements in a data structure
Control by means of a call to an iterator
Returns next element in chosen order
If no next element exists, loop is terminate
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:

<!-- Slide number: 16 -->
# Iteration Based on Data Structures
PHP
​current($arr) points to one array element
​next($arr) moves current to the next element
​reset $arr moves current to the first element
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:
Here is an example of a loop that iterates through an array named transport:

$transport = array('foot', 'bike', 'car', 'plane');

while (current($transport) != 'car') {
    echo current($transport), " ";
    next($transport);
}

The output of this program code will be:

foot bike

<!-- Slide number: 17 -->
# Iteration Based on Data Structures
Java 5.0 uses for
It is usually called a foreach loop
Arrays/classes implementing Iterable interface
For example, for an ArrayList

	      for (String myElement : myList) { ... }

The myElement variable is the loop variable
Each iteration, takes value of next myList element
C# uses a similar approach to Java
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:

<!-- Slide number: 18 -->
# Iteration Based on Data Structures
Ruby blocks
Sequences of code
Delimited by braces, or do and end
Can be used with methods to create iterators
Predefined iterator methods times, each, upto
​3.times {puts "Hey!"}
the block containing the puts is executed 3 times
​list.each {|value| puts value}
list is an array, value is block’s formal parameter
​1.upto(5) {|x| print x, " "}

Ruby for statement are converted into upto calls
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:
In the last example, x is also a formal parameter for the block.

<!-- Slide number: 19 -->
# Iteration Based on Data Structures
Ruby blocks
Block formal parameters get values from methods
From method yield statement with actual parameters
Here each iteration’s yield is a result for num

	    def fibonacci(last)
	       first, second = 1, 1
	       while first < last
	          yield first
	          first, second = second, first + second
	       end
	    end

	    puts "Fibonacci numbers less than 100 are:"
	    fibonacci(100) {|num| print num, " "}
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:
Think of the yield as a return statement that doesn’t terminate the fibonacci method. Instead, it just makes the result available to a block associated with a call to the fibonacci method. Look at the last line of the code example. The fibonacci method generates each of the fibonacci numbers between 1 and 100. It doesn’t store these numbers, or print them out. Instead it simply executes a yield for each number, then lets the block handle what to do with those numbers. The block in this example simply prints each number as it is generated (num is the formal parameter of the block). You could just as easily have written a block to do something else with each of the generated numbers (e.g. double each one before printing, or adding them all together using a variable).

<!-- Slide number: 20 -->
# Unconditional Branching
Transfers control to specific place in program
Implemented using a goto statement
Very heated debate in the 1960s and 1970s
The major concern was readability
Some languages have no goto
For example, Java
C# offers a goto statement
One well-designed use in a switch (discussed earlier)
Drawback to loop exit statements
These are break and continue statements
Restricted and camouflaged goto statements
Copyright © 2023 Addison-Wesley. All rights reserved.
1-20

### Notes:
A C# goto can also be used like a normal C or C++ goto.

<!-- Slide number: 21 -->
# Guarded Commands
Not very widely supported
Designed by Dijkstra
Supports new programming methodology
Allowing correctness verification in development
Basis of 2 methods for concurrent programming
In CSP and Ada
Basic Idea
If the order of evaluation is not important
The program should not specify an order
Copyright © 2023 Addison-Wesley. All rights reserved.
1-21

### Notes:
Pay attention to guarded commands. They are easy to understand, and there will probably be a question on them in the test or exam.

CSP stands for “communicating sequential processes”, and is a formal language for describing patterns of interaction in concurrent systems.

<!-- Slide number: 22 -->
# Selection with Guarded Commands
Form of a guarded selection

  if Boolean_exp_1 -> statement_1
  [] Boolean_exp_2 -> statement_2
   ...
  [] Boolean_exp_n -> statement_n
  fi

Semantics: when construct is reached,
Evaluate all Boolean expressions
If more than one are true
Choose one non-deterministically
If none are true
Generate a runtime error
Copyright © 2023 Addison-Wesley. All rights reserved.
1-22

### Notes:
Non-deterministically means that the order is not specified. From a practical perspective a compiler or interpreter will usually have a mechanism for deciding which statement is executed (often it will simply be the statement for the first matching Boolean expression). But from a theoretical perspective the decision could just as well be randomly made (it typically wouldn’t be random in a real compiler or interpreter, however).

<!-- Slide number: 23 -->
# Loop with Guarded Commands
Form of a guarded loop

  do Boolean_exp_1 -> statement_1
  [] Boolean_exp_2 -> statement_2
   ...
  [] Boolean_exp_n -> statement_n
  od

Semantics: for each iteration
Evaluate all Boolean expressions
If more than one are true
Choose one non-deterministically, start loop again
If none are true
Exit the loop
Copyright © 2023 Addison-Wesley. All rights reserved.
1-23

### Notes:
See the previous slide for an explanation of “non-deterministic”.

<!-- Slide number: 24 -->
# Guarded Commands: Rationale
Control statements
Have a strong impact on program verification
Verification is almost impossible
If goto statements used
Verification is possible
If only selection and logical pretest loops used
Verification is relatively simple
If only guarded commands used
Copyright © 2023 Addison-Wesley. All rights reserved.
1-24

### Notes:
