<!-- Slide number: 1 -->

![Front Cover: Concepts of Programming Languages, Global Edition, by Robert W Sebesta](Picture8.jpg)
# Chapter 5Part 1
Names, Bindings, and Scopes

### Notes:

<!-- Slide number: 2 -->
# Chapter 5 Topics
Introduction
Names
Variables
The Concept of Binding

1-2

### Notes:

<!-- Slide number: 3 -->
# Introduction
Imperative languages are abstractions of thevon Neumann architecture
Memory
Processor
Variables
Abstractions of memory cells
Are characterized by attributes
We will focus on variable types in Chapter 6
A type’s design requires consideration of several issues
These issues are names, bindings, and scopes


1-3

### Notes:

<!-- Slide number: 4 -->
# Names
Design issues for names (also called identifiers)
What form can names take?
Are special words reserved words or keywords?

1-4

### Notes:

<!-- Slide number: 5 -->
# Names: Form
The form of a name has several aspects
Name length
Use of special characters
Case sensitivity


1-5

### Notes:

<!-- Slide number: 6 -->
# Names: Form
Length
If too short, they cannot be connotative
Examples of how languages deal with name length
Fortran
Up to 63 in Fortran 2003, 31 in Fortran 95, 6 in Fortran I
C99 (the 1999 revised C standard)
No limit but only the first 63 are significant
External names are limited to a maximum of 31
C++
No limit, but implementers often impose one
C#, Ada, and Java
No limit, and all are significant

1-6

### Notes:
In C99, a definition is different to a declaration. A declaration for a variable provides the name and type of the variable, but no storage allocation. A definition of a variable also provides the name and type of the variable, but additionally allocates storage for the variable (possibly also providing a value for the variable).

External names are declared with the extern special word. Declaring a variable as extern indicates to the compiler that the definition of this name (with storage allocation) is provided in a different file. So, for example, if we provide the following in a C99 implementation file called main.cpp:

extern int a;

this means that the variable a is declared, but not defined (i.e. storage has not been allocated). We are telling the compiler “don’t worry about where this variable is defined, because the definition is in another file, and you will find it during the linking phase of compilation”. In another file called vars.cpp, we could have something like this:

int a = 10;

which is the definition of the variable (note that memory is allocated for the a variable at this point). If we link vars.cpp with main.cpp, everything will work correctly, and any use of a in main.cpp will use the definition of a provided in vars.cpp. Note that we can’t use the variable a in main.cpp unless we provide the extern declaration (otherwise the compiler won’t know anything about the variable). We also can’t provide a definition for the variable a in main.cpp, because then linking would find that there are two conflicting definitions for variables named a.

<!-- Slide number: 7 -->
# Names: Form
Special characters
PHP
All variable names must begin with dollar signs
Perl
All variable names begin with special characters
The special character specifies the variable’s type
Scalars use a $, arrays use a @, hashes use a %
Ruby
Instance variable names begin with @
Class variable names begin with @@

1-7

### Notes:
A scalar in Perl can store either a string or a numeric value. Hashes in Perl are data structures that store key-value pairs, as in a hashtable. Hashes in Perl are also used for associative arrays, which we will discuss in Chapter 6.

<!-- Slide number: 8 -->
# Names: Form
Case sensitivity
Does the compiler ignore case in variable names or not?
Disadvantages
Readability
Names in the C-based languages are case sensitive
Names that look alike are actually different
For example, myname versus myName
Names in many other languages are not
Writability
In C++, Java, and C# predefined names are mixed case
For example, IndexOutOfBoundsException
Programmer has to remember the case for these names

1-8

<!-- Slide number: 9 -->
# Names: Special Words
Special words
Aid to readability by naming actions
Also separate parts of statements and programs
Reserved word cannot be a user-defined name
For example, int means an integer type in all contexts
Potential problem
If there are too many, name collisions are more likely
COBOL has 300 reserved words!
Keyword is special only in certain contexts
In Fortran
Real VarName
	Real is a keyword, denoting a data type
Real = 3.4
	Real is a variable

1-9

### Notes:

<!-- Slide number: 10 -->
# Variables
A variable
An abstraction of a memory cell
Can be characterized by six attributes
Name
Address
Value
Type
Lifetime
Scope

1-10

### Notes:

<!-- Slide number: 11 -->
# Variables: Name and Address
Name
Not all variables have them (more on this later)

Address
The memory address with which a variable is associated
May have different addresses at different execution times
If two variable names can be used to access the same memory location, they are called aliases
Created via pointers, references, and unions
Bad for readability (readers must remember all of them)

1-11

### Notes:

<!-- Slide number: 12 -->
# Variables: Value
Value
Contents of memory location variable is associated with
Represents an abstract memory cell
The physical cell or collection of cells associated with a variable
Example: A float occupies 4 bytes, but 1 abstract memory cell
The variable’s address represents the start of the memory cell

1-12

### Notes:

<!-- Slide number: 13 -->
# Variables: Type
Type
Determines
Set of values of variables (for floating point, also the precision)
Set of operations that are defined for values of that type
How a value is stored in memory

1-13

### Notes:

<!-- Slide number: 14 -->
# The Concept of Binding
A binding is simply an association
Between an attribute and an entity
Example: Between a variable and its type or value
Or between an operation and a symbol
Example: Between a multiplication operation and *
Binding time
Time that binding takes place
Several are possible

1-14

### Notes:

<!-- Slide number: 15 -->
# Possible Binding Times
Language design time
Binding operator symbols to operations
Language implementation time
Binding floating point type to a representation
Compile time
Binding a variable to a type in C or Java
Load time
Binding a C or C++ local static variable to memory cell
Runtime
Binding nonstatic local variable to a memory cell

1-15

### Notes:

<!-- Slide number: 16 -->
# Static and Dynamic Binding
Static binding
Occurs before run time
Remains unchanged throughout program execution
Dynamic binding
Occurs during execution or can change during execution

1-16

### Notes:

<!-- Slide number: 17 -->
# Type Binding
Type binding
The binding of a variable to a type
Design issues for type binding
How is a type specified?
When does the binding take place?
Is it static?
Is it dynamic?

1-17

### Notes:

<!-- Slide number: 18 -->
# Static Type Binding
Explicit declaration
A program statement used to declare types of variables
For example, in C++: int myVar;
Implicit declaration
A default mechanism for specifying variable types
Involves the first appearance of a variable in the program
Naming conventions may determine type
Used in BASIC, Perl, Ruby, JavaScript, and PHP
Advantage: Writability
A minor convenience
Disadvantage: Reliability
Typographic errors can’t be picked up by the compiler
Less trouble with Perl (why?)
Fortran has both explicit and implicit declarations

1-18

### Notes:

<!-- Slide number: 19 -->
# Static Type Binding
Implicit declarations can also use type inferencing
Determine types of variables from context
For example:
C# optionally uses type inferencing
Variable can be declared with var and initial value
The initial value sets the variable type
	var value = 12;
Also used in
Visual BASIC 9.0+
Haskell
ML
F#

1-19

<!-- Slide number: 20 -->
# Dynamic Type Binding
Type is specified by assignment statement
For example, in JavaScript
		list = [2, 4.33, 6, 8];
		list = 17.3;
How does this differ from type inferencing?
Advantage
Flexibility (variable usability, generic program units)
Disadvantages
Cost (dynamic type checking and interpretation)
Type error detection by compiler/interpreter is difficult
Used in JavaScript, Python, Ruby, PHP, C# (limited)

1-20

### Notes:
C# support for dynamic type binding is limited because it only works for objects, not primitive types. Primitive types will automatically be converted to objects, but behave in unexpected ways. You can read more about this at https://blogs.msdn.microsoft.com/samng/2008/12/15/dynamic-in-c-vi-what-dynamic-does-not-do/

<!-- Slide number: 21 -->
# Storage Bindings and Lifetime
Storage bindings and Lifetime
Allocation
Getting a cell from a pool of available memory cells
This is a storage binding
Deallocation
Putting a memory cell back into the pool
Lifetime of a variable
The time during which a variable is bound to a particular memory cell

1-21

### Notes:

<!-- Slide number: 22 -->
# Categories of Variables by Lifetimes
Static variables
Bound to memory cells before execution begins and stays bound to the same memory cell throughout execution
For example, C and C++ static variables
	  int f() {
	     static int sVar = 10;
	     return ++sVar;
	  }

Advantages
Often efficiency because of direct addressing
History-sensitive subprogram support
Disadvantages
Lack of flexibility (do not allow for recursion)
Storage cannot be shared amongst variables

1-22

### Notes:
Static variables are allocated from static memory.

<!-- Slide number: 23 -->
# Categories of Variables by Lifetimes
Stack-dynamic variables
Storage bindings are created for variables when their declaration statements are elaborated
When the executable code associated with it is executed
Scalars (variables that hold one value at a time)
All attributes except storage and address are statically bound
For example, normal local variables in C functions

     void f() { int myVar; }

Advantage
Allows recursion
Conserves storage
Disadvantages
Overhead of allocation and deallocation
Subprograms cannot be history sensitive
Inefficient references (indirect addressing)

1-23

### Notes:
Stack-dynamic variables are allocated from stack memory.

<!-- Slide number: 24 -->
# Categories of Variables by Lifetimes
Explicit heap-dynamic variables
Allocated and deallocated by explicit directives, specified by the programmer, which take effect during execution
These variables are nameless
Referenced only through separate pointers or references
For example
Dynamic variables in C++ (via new and delete), all objects in Java
In C++:  int* p = new int(12);
Advantage
Provides for custom dynamic storage management
Disadvantage
Often unreliable (difficult to use correctly)
Inefficient (why?)
Difficult to implement

1-24

### Notes:
Explicit heap-dynamic variables are allocated from heap memory.

<!-- Slide number: 25 -->
# Categories of Variables by Lifetimes
Implicit heap-dynamic variables
Allocation and deallocation caused by assignments
What kind of type binding does this imply?
For example
All variables in APL
All strings and arrays in Perl, JavaScript, and PHP
Advantage
Flexibility (generic code)
Disadvantages
Inefficient (because most attribute binding is dynamic)
Loss of error detection

1-25

### Notes:
Explicit heap-dynamic variables are allocated from heap memory.
