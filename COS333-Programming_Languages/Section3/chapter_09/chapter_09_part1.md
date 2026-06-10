<!-- Slide number: 1 -->
# Chapter 9Part 1
Subprograms

### Notes:

<!-- Slide number: 2 -->
# Chapter 9 Topics
Introduction
Fundamentals of Subprograms
Design Issues for Subprograms
Local Referencing Environments
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Introduction
Two fundamental abstraction facilities
Process abstraction
Emphasized from the early days of programming
Discussed in this chapter
Data abstraction
Emphasized in the1980s
Through ADTs and OOP
Discussed at length in Chapter 12
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:

<!-- Slide number: 4 -->
# Fundamentals of Subprograms
Each subprogram has a single entry point
During execution of the called subprogram
The calling program is suspended
When called subprogram execution ends
Control always returns to the caller
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:

<!-- Slide number: 5 -->
# Basic Definitions
Subprogram definition
Defines interface and actions of a subprogram
Interface specifies
How the subprogram is used
Details like subprogram name, parameter types, etc
Actions
Specify what the subprogram does
In other words, the body of the subprogram
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# Basic Definitions
Subprogram definition
In Python
Subprogram definitions are executable

	    if ...
	       def fun():
	       ...
	    else
	       def fun():
	       ...

So we can have different definitions for fun
It all depends on the outcome of the if
Effect on the language evaluation criteria?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:
Python’s executable subprograms allow Boolean conditions to create different implementations for the same subprogram name. This is a kind of parameterization.

It is even possible to define two functions with the same name directly after one another (i.e. not in an if statement). In this case, the last one defined will be the one used by a call. This is not very useful, however, so you’ll typically see different definitions of the same subprogram in if statements.

<!-- Slide number: 7 -->
# Basic Definitions
Subprogram definition
In Ruby
Function definitions in a class definition
Members of the class
Function definitions outside a class definition
Actually methods of class Object
But can be called without an object
Therefore, they look like a C function, but are not
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# Basic Definitions
Subprogram header
First part of the subprogram definition
Name, kind of subprogram, formal parameters
Subprogram call
Explicit subprogram execution request
For example

	void doSomething(int first, float second)
	{ ... }

	doSomething(1, 23.7);

Header
Subprogram call
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:

<!-- Slide number: 9 -->
# Basic Definitions
Formal parameter
Dummy variable listed in subprogram header
They are used in the subprogram
Actual parameter
Value or address used in the subprogram call
For example

	void doSomething(int first, float second)
	{ ... }

	doSomething(1, 23.7);

Formal parameters
Actual parameters
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:
Given the following code:

int foo(double a, int b) { … }

int main()
{
   foo(1.2, 4);
}

The subprogram header is foo(double a, int b), and the type of subprogram, which is a function in this case (because there is a return value – see slide 14).

foo(1.2, 4); is the subprogram call.

The variables a and b are formal parameters, while 1.2 and 4 are actual parameters.

<!-- Slide number: 10 -->
# Basic Definitions
Parameter profile (also called the signature)
Number, order, and types of parameters
In the previous example
Two parameters, an int followed by a float
Protocol
Parameter profile with function return types
In the previous example
Two parameters, an int followed by a float
With a void return
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:

<!-- Slide number: 11 -->
# Basic Definitions
Subprogram declaration
Provides subprogram protocol, but not its body
Often called prototypes in C and C++

The prototype usually appears in a header file

   void doSomething(int, float);

The function definition goes in an implementation file

   void doSomething(int first, float second)    {
      ...
   }
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:
Given the following code:

int foo(double a, int b) { … }

int main()
{
   foo(1.2, 4);
}

The parameter profile consists of two parameters, a double followed by an int.

The protocol consists of an int return type, and two parameters, a double followed by an int.

In a language like C++, the subprogram declaration would appear somewhere above the example code (often in a header file), and would look as follows (note that there is no subprogram body):

int foo(double a, int b);

<!-- Slide number: 12 -->
# Actual/Formal Parameter Correspondence
For a subprogram call, we must match
Actual parameters (in subprogram call) to the formal parameters (in subprogram definition)
Positional parameters
Bind actual to formal parameters by position
1st actual parameter bound to the 1st formal parameter
2nd to the 2nd, and so on
Most high-level languages use this approach
Advantage
Safe and effective
Disadvantage?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:
Try to think of one drawback (look at the next slide if you’re not sure).

<!-- Slide number: 13 -->
# Actual/Formal Parameter Correspondence
Keyword parameters
Binding uses the names of formal parameters
Names specified with the actual parameters in call
For example:
	    add(first = 10, second = 12, third = 3)
Advantage
Parameters can appear in any order
Avoid parameter correspondence errors
Disadvantage?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:
Ruby, for example, supports both positional parameters and keyword parameters.

<!-- Slide number: 14 -->
# Formal Parameter Default Values
Default values for formal parameters
Some actual parameters can be left out in a call
Default values assumed for these actual parameters
Defaults used only if no actual parameter passed
Supported in C++, Python, Ruby, Ada, and PHP
In C++, default parameters must appear last
Two related questions
Why must default parameters appear last in C++?
How could default parameters be allowed anywhere?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:
Try to answer the question (consider the previous slides).

<!-- Slide number: 15 -->
# Variable Number of Parameters
Variable number of parameters
A subprogram has one or more actual parameters
Not the same as default parameters
Default parameters can be left out
Variable number of parameters processed like a list
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

<!-- Slide number: 16 -->
# Variable Number of Parameters
In C#
Method can accept variable number of parameters
The parameters have to be of the same type
The formal parameter is an array preceded by params
Why do you think parameters must be the same type?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:

<!-- Slide number: 17 -->
# Variable Number of Parameters
In C#
For example, in class MyClass

     public void DisplayList(params int[] list) {
        foreach (int next in list) {
           Console.WriteLine("Value {0}", next);
        }
     }

Can be used in the following two ways:

     Myclass myObject = new Myclass;

     int[] myList = new int[6] {2, 4, 6, 8, 10, 12};
     myObject.DisplayList(myList);               // first way

     myObject.DisplayList(2, 4, 3 * x - 1, 17);  // second way
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:
In C#, a params array can be mixed with normal parameters, but must appear last in the parameter list.

<!-- Slide number: 18 -->
# Variable Number of Parameters
In Ruby
Actual parameters sent as elements of an Array
The array can contain mixed types (why?)
Formal parameter is preceded by an asterisk

	   def tester(p1, p2, *p3)
	      ...
	   end

Python uses a similar approach to Ruby
Actual parameters are sent in a list
Why does Python allow mixed types?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:
Why does the approach used by Ruby and Python allow for mixed types? (Hint: the reasons are different for the two languages)

In Ruby, a variable argument needs to be after all your required and optional parameters, and before any keyword parameters.

In Python, the variable number of parameters must appear last in the parameter list.

<!-- Slide number: 19 -->
# Procedures and Functions
There are two categories of subprograms
Procedures are collections of statements that define parameterized computations
Produce results by modifying
Variables visible from an enclosing scope
Formal parameters that transfer data to caller
They therefore have no return values

Functions resemble procedures but semantically modeled on mathematical functions
Produce results by returning a value
They are expected to produce no side effects
In practice, many languages allow side effects
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:

<!-- Slide number: 20 -->
# Design Issues for Subprograms
Are local variable allocations static or dynamic?
Can subprogram definitions be nested?
What parameter passing methods are provided?
Are parameter types checked?
If subprograms can be passed as parameters and subprograms can be nested, what is the referencing environment of a passed subprogram?
Are functional side effects allowed?
What return types are allowed from functions?
How many values can a function return?
Can subprograms be overloaded?
Can subprogram be generic?
If nested subprograms are legal, are closures supported?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-20

### Notes:

<!-- Slide number: 21 -->
# Local Referencing Environments
In most contemporary languages
Local variables are stack dynamic
In C and C++ functions
Local variables are by default stack dynamic
But can be declared static
The methods of Java, Python, and C#
Only have stack dynamic local variables
Copyright © 2023 Addison-Wesley. All rights reserved.
1-21

### Notes:
