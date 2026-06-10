<!-- Slide number: 1 -->

![Front Cover: Concepts of Programming Languages, Global Edition, by Robert W Sebesta](Picture8.jpg)
# Chapter 5Part 2
Names, Bindings, and Scopes

### Notes:

<!-- Slide number: 2 -->
# Chapter 5 Topics
Scope
Scope and Lifetime
Referencing Environments
Named Constants

1-2

### Notes:

<!-- Slide number: 3 -->
# Variable Attributes: Scope
The scope of a variable
The range of statements over which it is visible
The local variables of a program unit
Variables declared in the unit
The nonlocal variables of a program unit
Variables that are visible but not declared in the unit
Global variables
Special category of nonlocal variables
Language scope rules
Define how name references are associated with variables

1-3

### Notes:
Program units are things like subprograms, blocks, segments in a selection statement, and the bodies of loops.

<!-- Slide number: 4 -->
# Variable Attributes: Scope
Two approaches to scoping rules
Static scope
Dynamic scope

1-4

### Notes:

<!-- Slide number: 5 -->
# Static Scope
Based on program text
To connect a name reference to a variable
The compiler (and a reader) must find the declaration
Search process
Search declarations, starting in local program unit
Continue search in increasingly larger enclosing scopes
Stop when a declaration is found for the given name

     void f() {
        int i = 10;

        for (...) {
           if (...) {
              i++;
           }
        }
     }

1-5

### Notes:

<!-- Slide number: 6 -->
# Static Scope
Enclosing static scopes are called static ancestors
Nearest static ancestor is called a static parent

   void f() {
      int i = 10;

      for (...) {
         if (...) {
            i++;
         }
      }
   }

Some languages allow nested subprogram definitions, which create nested static scopes
For example: Ada, JavaScript, Common LISP, Scheme, Fortran 2003, F#, and Python

1-6

### Notes:

<!-- Slide number: 7 -->
# Static Scope
If a variable in a “closer” scope has the same name as a variable in a static ancestor
The variable in the static ancestor is “hidden”

   void f() {
      int i = 10;

      for (...) {
         int i = 20;
      }
   }

1-7

### Notes:

<!-- Slide number: 8 -->
# Blocks
Method to create static scopes inside program units
From ALGOL 60
Example in C

 		void sub() {
  		    int count;
		    while (...) {
		        int count;
		        count++;
		    }
		}

Variable hiding in blocks is legal in C and C++
Java & C#: No variable hiding in blocks (error-prone)

1-8

### Notes:

<!-- Slide number: 9 -->
# The let Construct
Most functional languages
Include a let construct to create scope for name bindings
A let construct has two parts
The first part binds names to values
The second part uses the names defined in the first part
A let in Scheme

		(let
		  (
		    (top (+ a b))
		    (bottom (- c d))
		  )
		  (/ top bottom)
		)

1-9

### Notes:
In Scheme, the scope of names in the first part of the let is only in the second part of the let. It is not possible to use names defined higher up in the first part in values bound to other names. For instance, in the example on this slide it is not possible to use the name top in the value for bottom.

<!-- Slide number: 10 -->
# Declaration Order
In C99, C++, Java, and C#
Variable declarations can appear anywhere a statement can
In C99, C++, and Java
Scope of local variable is from declaration to end of block
In C++, Java, and C#
Loop control variables can be declared in for loop header
Loop control variable scope restricted to the for statement

     for (int i = 0; i < 10; i++) {
        // i is in scope within the body, but not outside it
     }

1-10

### Notes:

<!-- Slide number: 11 -->
# Declaration Order
In C#
Variable scope is the whole block it appears in
However a variable can only be used after a declaration

     {
        {
           int x;
        }
        int x;
     }
Legal in C99, C++, and Java

Not legal in C# (can you explain why?)

1-11

### Notes:
Recall that C# disallows variable hiding in blocks. Therefore, the following is illegal:

{
   int x;
   { int x; }
}

The example in this slide is similar to the above code, even though the declaration of x in the outer block appears after the nested block. This is because the declaration of x in the outer block has scope over the entire outer block (including the nested block). The declaration of x in the nested block is therefore illegal, because it hides the declaration in the outer block. You can still only use the x declared in the outer block after the declaration.

<!-- Slide number: 12 -->
# Global Scope
In C, C++, PHP, and Python allow
A sequence of function definitions
Global variable declarations are outside function definitions
Global variables have global scope (covers all functions)

1-12

### Notes:
Global variables in C and C++ have a scope that extends from their declaration to the end of the file they are declared in. Global variables in PHP and Python have a scope that covers additional files in your program, not just the file where the global variable has been declared. Accessing global variables in PHP and Python is a different matter we’ll get to in the next two slides.

The extern keyword indicates that a variable is defined somewhere else (e.g. in a different header or implementation file). It’s also possible to declare extern functions. Here’s an example of how extern could be used in C:

=======
File test1.c:
=======

int var = 10;				// global variable that should be usable throughout the program

int foo(void) {
   return ++var;
}

=======
File test2.c:
=======

extern int var;
extern int foo();

void main() {
   printf("value of var from foo: %d\n", foo());		// here we call foo
   printf("accessing var directly:%d\n ", var);		// here we access the value of var
}

What we’ve done here is write two implementation files, which are linked at compile time (using a compilation command like “gcc -o test test2.c test1.c”). We’ve declared a global variable (var) in the file test1.c, as well as a function (foo), both of which should be usable throughout the program. In test2.c we call foo and access the value of var.

Note that test1.c is not included (using #include) in test2.c because we don’t typically include implementation files (usually we only include header files). We can’t just access var or foo in test2.c because neither has been defined in test2.c. We also can’t re-define var or foo in test2.c because we would then be defining var and foo twice in the program, which would cause a compilation error.

So how do we solve this problem? We need to declare var and foo in test2.c using the extern keyword. This is basically telling the compiler “Don’t worry about finding a definition for var and foo in test2.c because var and foo are defined in another file that will be linked during compilation”. The extern keyword indicates that var and foo are available for use, but doesn’t tell the compiler anything about how memory is allocated for var, or what the body of foo looks like. The memory allocation and implementation of foo are only provided when test1.c and test2.c are linked by the compiler.

<!-- Slide number: 13 -->
# Global Scope
In PHP
Programs in XHTML markup documents
Statements and function definitions can be mixed
Variable implicitly declared in a function
Scope is local to the function
Variable implicitly declared outside a function
Scope is from the declaration to end of the program
Skips over any intervening functions
Global variables can only be accessed in a function
Through the $GLOBALS array
By declaring it global in the function
Called functions defined above the global variable declaration can also access the variable in this way

1-13

### Notes:
What is the advantage of PHP’s method for handling global variables?

Based on the scope rules of PHP, this is legal:

<?php

function calculate_count() {
    global $count;
    echo $count++ . "<br/>";
}

$count = 5;
calculate_count();
echo $count;
?>

and outputs 5 for the echo in the function body, and 6 for the echo outside the function body.

<!-- Slide number: 14 -->
# Global Scope
In Python
Global scope works the same way it does in PHP
Global variables can be referenced in functions
BUT, a global variable can only be assigned to in a function if declared as global in the function

1-14

### Notes:
What is the advantage of Python’s method for handling global variables?

Based on the scope rules of Python, this is legal:

def calculate_count():
    global count
    count += 1
    print(count)

count = 5
calculate_count()
print(count)

and outputs 6 for the print in the function body, and 6 for the print outside the function body.

<!-- Slide number: 15 -->
# Evaluation of Static Scoping
Advantage
Works well in many situations
Disadvantage
In most cases, too much access is possible
As program evolves
Local variables tend to gravitate towards becoming global
Subprograms gravitate toward become global, rather than nested

1-15

### Notes:

<!-- Slide number: 16 -->
# Dynamic Scope
Based on calling sequences of program units
Not based on textual layout, like global scope
In other words, dynamic scope is temporal, not spatial
To connect a variable reference to a declaration
Searching back through chain of subprogram calls that brought execution to the variable reference

1-16

### Notes:

<!-- Slide number: 17 -->
# Scope Example
Big
{
     declare X

     Sub1
     {
          declare X
          call Sub2
     }

     Sub2
     {
          refer to X
     }

     call Sub1
}
Call order
 Big calls Sub1
 Sub1 calls Sub2
 Sub2 uses X

Static scoping
 Reference to X is to the X in Big

Dynamic scoping
 Reference to X is the X in Sub1


1-17

### Notes:

<!-- Slide number: 18 -->
# Evaluation of Dynamic Scoping
Advantage
Convenience (eliminates need for parameters – why?)
Disadvantages
While a subprogram is executing, its variables are visible to all subprograms it calls
Impossible to statically type check (why?)
Programs more difficult to read (why?)
Access to non-local variables is slower (why?)

1-18

### Notes:

<!-- Slide number: 19 -->
# Scope and Lifetime
Scope and lifetime
Sometimes closely related
Local variable in Java method
int f() {
   int a = 10;
   return a;
}

What is the scope? What is the lifetime?

But are different concepts
A local static variable in a C or C++ function
int f() {
   static int sVar = 10;
   return ++sVar;
}

What is the scope? What is the lifetime?

1-19

### Notes:

<!-- Slide number: 20 -->
# Referencing Environments
The referencing environment of a statement
Collection of all names that are visible in the statement
In a language using static scope
The local variables plus all of the visible variables in all of the enclosing scopes
In a language using dynamic scope
The local variables plus all the visible variables in all of the active subprograms
Active subprograms have started execution and have not yet terminated

1-20

### Notes:

<!-- Slide number: 21 -->
# Referencing Environments Example
Main() {
	def A, B;

	Sub1 {
	    def B, C;
	    <--- (2)
	    call Sub2;
	}

	Sub2 {
	    def C, D;
	    <--- (3)
	}

	<--- (1)
	call Sub1;
}
Referencing environment for static scoping:
 (1): A and B in Main
 (2): B and C in Sub1, and A in Main
 (3): C and D in Sub2, and A & B in Main

Referencing environment for dynamic scoping:
 (1): A and B in Main
 (2): B and C in Sub1, and A in Main
 (3): C and D in Sub2, B in Sub1, and A in Main

1-21

<!-- Slide number: 22 -->
# Named Constants
Named constants
A name bound to a value only once
Used to parameterize programs

     const int SIZE = 10;
     int arr[SIZE];
     for (int i = 0; i < SIZE; i++) { ... }

Advantages
Readability and reliability

Binding of values to named constants
Static (manifest constants)
     const int SIZE = 10 + 5;

Dynamic
     const int SIZE;
     SIZE = a + 1;

1-22

### Notes:
You should be familiar with using named constants to parameterise programs from your introductory programming course. Here is an example in C++:

const int SIZE = 10;
int array[SIZE];

for (int i = 0; i < SIZE; i++) {
   // do something with array
}

This code allows you to easily change the value of SIZE, which then propagates the change throughout your code without having to change the declaration of array or the stopping condition for the loop.

Static constants have values bound to them at compile time. Because of this, a value must be assigned to the static constant where it is defined. Additionally, only expressions involving other constants and literals may be assigned to the static constant. It is illegal to use variables in the assignment. This is because the value binding to the static constant takes place at compile time, so the value being bound must be known at compile time (the values of variables are only known at runtime).

Dynamic constants are simply variables that can only be assigned to once. Because of this, the value assigned to a dynamic constant is allowed to be an expression that only gets a value at runtime. This implies that variables can be used in the expression that is assigned to a dynamic constant. Additionally, one can usually assign a value to a dynamic constant after it is declared, but you are restricted in terms of assigning to the dynamic constant after the first assignment.

<!-- Slide number: 23 -->
# Named Constants
Examples of named constants in languages

FORTRAN 95
Constant-valued expressions (static or dynamic?)

Ada, C++, and Java
Expressions of any kind (static or dynamic?)

C# has two kinds
Values of const named constants bound at compile time
Values of readonly named constants dynamically bound

1-23

### Notes:
In C# the following is legal:

const int C1 = 5;
const int C2 = C1 + 100;

The following, however, is illegal (because the expression on the right of the assignment to C contains a variable):

int variable;
variable = 5;
const int C = variable + 100;

In C#, a readonly constant is a dynamic constant. However, you may only declare a readonly constant as a field of a class (i.e. a member variable of a class), and may only assign a value to a readonly constant in the constant’s definition or a constructor. The following example illustrates the use of dynamic constants in C#:

public class Program {

   static readonly int c;

   static Program() {
      int variable = 5;
      c = variable + 100;
   }
}
