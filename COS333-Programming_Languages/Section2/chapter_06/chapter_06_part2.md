<!-- Slide number: 1 -->
# Chapter 6Part 2
Data Types

### Notes:

<!-- Slide number: 2 -->
# Chapter 6 Topics
Record Types
Tuple Types
List Types
Union Types
Pointer and Reference Types
Type Checking
Strong Typing
Type Equivalence
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Record Types
A record
A possibly heterogeneous aggregate of data elements
Data elements are called fields, and identified by names
Design issues
What is the syntactic form of a field reference?
Are elliptical references allowed?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:

<!-- Slide number: 4 -->
# Records in COBOL
COBOL allows nested records
Level numbers show hierarchical structure

	  01 EMPLOYEE-RECORD.
      02 EMPLOYEE-NAME.
         05 FIRST    PICTURE IS X(20).
         05 MIDDLE   PICTURE IS X(10).
         05 LAST     PICTURE IS X(20).
      02 HOURLY-RATE PICTURE IS 99V99.
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:
COBOL records are not implemented as records within records. How does this affect the language evaluation criteria of COBOL?

How does the use of level numbers affect the language evaluation criteria for COBOL?

<!-- Slide number: 5 -->
# Orthogonal Records
Languages other than COBOL use records in records
For example, in Ada:

		type Employee_Name_Type is record
		    First: String (1..20);
		    Middle: String (1..10);
		    Last: String (1..20);
		end record;

		type Employee_Record_Type is record
		    Employee_Name: Employee_Name_Type;
		    Hourly_Rate: Float;
		end record;

		Employee_Record: Employee_Record_Type;
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:
How does Ada’s use of records within records affect the orthogonality of the programming language?

<!-- Slide number: 6 -->
# References to Records
Record field references
COBOL
 MIDDLE OF EMPLOYEE-NAME OF EMPLOYEE-RECORD

Other languages use dot notation
 Employee_Record.Employee_Name.Middle

Fully qualified references
Must include all record names

Elliptical references
Allow leaving out record names if the reference is unambiguous
For example in COBOL, the following are all equivalent
 FIRST
 FIRST OF EMPLOYEE-NAME
 FIRST OF EMPLOYEE-RECORD
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:
How does support for elliptical references affect (positively and negatively) the language evaluation criteria of a programming language?

<!-- Slide number: 7 -->
# Tuple Types
Similar to a record
However, the elements are not named
Used in Python, ML, and F#
Allow functions to return multiple values
In Python
Closely related to lists, but are immutable
Create with a tuple literal
   	    myTuple = (3, 5.8, 'apple')

Referenced with subscripts (myTuple[0] references 3)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:
The textbook states that the base index for Python tuples is 1. This is incorrect, and the base index is 0, as stated in this slide.

<!-- Slide number: 8 -->
# List Types
A list
Ordered sequence of often heterogeneous values
Typically represented as a linked list
Lists in LISP and Scheme
We’ve discussed these in Chapter 15
These lists are immutable
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

<!-- Slide number: 9 -->
# List Types
Python lists
Also serve as heterogeneous arrays
Python’s lists are mutable
Elements can be of any type
Create a list with an assignment
       myList = [3, 5.8, "grape"]

List elements are referenced with subscripting
Indices begin at zero
For example, to set x to 5.8
           x = myList[1]

List elements can be deleted with del
           del myList[1]
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

<!-- Slide number: 10 -->
# List Types
Python lists (continued)
List Comprehensions

       list = [x ** 2 for x in range(12) if x % 3 == 0]

First, the variable x takes on integer values from 0 to 12
For each value divisible by 3 (that is 0, 3, 6, 9, and 12) it then computes the square (that is 0, 9, 36, 81, and 144)
Places these squared values into a new list
Therefore list contains [0, 9, 36, 81, 144]
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

<!-- Slide number: 11 -->
# Unions Types
A union
A type whose variables can store values of different types at different times during execution
However, a union only has one value at a time
What could a union be used for?
Design issues
Should type checking be required?
Should unions be embedded in records?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:

<!-- Slide number: 12 -->
# Discriminated vs. Free Unions
In Fortran, C, and C++
Unions have no support for type checking
These unions are called free unions
Up to the programmer to keep track of which type is stored
Example in C

	   	 union flexType {
		     int intEl;
		     float floatEl;
	   	 };

	   	 union flexType u1;
	   	 u1.intEl = 12;
	   	 u1.floatEl = 22.8;
	   	 float x = u1.floatEl;
		 int y = u1.intEl;
Retrieving integer when a float is stored
Legal, but produces garbage

Float bits are simply stored in int variable
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:

<!-- Slide number: 13 -->
# Discriminated vs. Free Unions
Type checking of unions
Supported by ML, Haskell, and F#
Require that each union include a type indicator called a discriminant or a tag
The discriminant is used to check the type of a union, and detect errors if invalid fields are accessed
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

<!-- Slide number: 14 -->
# Discriminated Unions
Discriminated union example in memory

If the discriminant, Form, is set to Circle
We can assign a value to Diameter
But we can’t assign values to
Side_1, Side_2, Left_Side, Right_Side, or Angle

![fig_06_08.jpg](Picture6.jpg)

Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:

<!-- Slide number: 15 -->
# Pointer and Reference Types
A pointer type variable
Values are memory addresses that reference a memory cell
Special value, nil, means it doesn’t refer to a memory cell
Two possible uses of pointers
Provide the power of indirect addressing
A means of referring to a variable via a different name
Provide a way to manage dynamic memory
A pointer can be used to access a location in the area where storage is dynamically created (the heap)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:

<!-- Slide number: 16 -->
# Design Issues of Pointers
What are the scope & lifetime of a pointer variable?
Note: Not the scope and lifetime of the referenced value

What is the lifetime of a heap-dynamic variable?
Relevant if pointers used for dynamic memory management

Restrictions on the type of value to which pointers can point?

What pointers are used for
Dynamic storage management?
Indirect addressing?
Both?

Should the language support
Pointer types?
Reference types?
Both?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:

<!-- Slide number: 17 -->
# Pointer Operations
Two fundamental operations for pointers
Assignment
Sets a pointer variable’s value to an address
If variable isn’t on heap, needs a way to get a variable address
For example, in C++ this sets p to the address of val

		int *p = &val;

Dereferencing
Yields the value stored at the location represented by the pointer’s value
Can be explicit or implicit
C++ has explicit dereferencing via the * operator

		j = *ptr;

	Sets j to the value located at memory address stored in ptr
Implicit pointers are automatically dereferenced when used
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:
An implicit dereferencing means that a dereferencing operator is not used when you want to get the value the pointer points to. Instead, you simply use the pointer, and you’ll get the value being pointed to (not its address). What are the implications of implicit dereferencing?

<!-- Slide number: 18 -->
# Problems with Pointers
Dangling pointers
A pointer to a deallocated heap-dynamic variable
Dangerous (why?)
Lost heap-dynamic variable
An allocated heap-dynamic variable that is no longer accessible to the user program (often called garbage)
For example
Pointer p1 is set to point to a newly created heap-dynamic variable
Pointer p1 is later set to point to another newly created heap-dynamic variable (without first deallocating p1)

The process is called memory leakage

p1

p1

Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:

<!-- Slide number: 19 -->
# Pointers in C and C++
Extremely flexible but must be used with care
Pointers can point to any variable regardless of when or where it was allocated
For dynamic storage management and addressing
Explicit dereferencing and address-of operators
Domain type need not be fixed
A void* can point to value of any type
Cannot be de-referenced unless converted to another type
How does this affect type checking?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:
Here’s an example of a void pointer in C++:

int value = 5;
void *voidPtr = &value;

//cout << *voidPtr << endl;                    // this is illegal

int *intPtr = static_cast<int*>(voidPtr);   // here we cast the void pointer to an int pointer
cout << *intPtr << endl;                         // dereferencing the cast pointer is legal

It is possible to cast a void pointer to a pointer for an incorrect type. For example, the previous example could have performed a static cast to a float*, and assigned the result to the variable float *floatPtr. In this case, the compiler will accept the cast, but the value pointed to will be garbage. Therefore, dereferencing floatPtr will produce a value unrelated to 5.

<!-- Slide number: 20 -->
# Pointers in C and C++
Example of dynamic storage management in C++
Dynamic storage allocation uses new

	int *p = new int[10];

		Here p points to newly allocated heap memory
To deallocate heap memory pointed to by p

			delete[] p;

C uses functions
malloc to allocate heap memory
free to deallocate heap memory
Copyright © 2023 Addison-Wesley. All rights reserved.
1-20

### Notes:

<!-- Slide number: 21 -->
# Reference Types
C++ includes a reference type
References are similar to pointers
In this example ref is a reference to v

	 int v = 10;
	 int &ref = v;

Used primarily for formal parameters, giving benefits of pass-by reference and pass-by-value

	 void f(int &p) { ... }

	 int val = 12;
	 f(val);

	Here p is a reference to a parameter, works like an int 	variable, but doesn’t need to be dereferenced like a pointer
Don’t work with memory addresses, so safer than pointers
Copyright © 2023 Addison-Wesley. All rights reserved.
1-21

### Notes:

<!-- Slide number: 22 -->
# Reference Types
Java extends C++ reference variables
Allows them to replace pointers entirely
References can refer only to objects, not primitives
How does this affect the language evaluation criteria?

C# includes both pointers and references
References are similar to those in Java
C++ pointers (but only in subprograms marked as unsafe)
How does this affect the language evaluation criteria?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-22

### Notes:

<!-- Slide number: 23 -->
# Type Checking
For this section, we generalize operands and operators to include subprograms and assignments
For subprogram call f(1.2), operator is f, operand is 1.2
For assignment a = 43, operator is =, operands are a & 43
Type checking
Ensures operands for operator are compatible types
A compatible type is one that is either
Legal for the operator
Or is allowed under language rules to be implicitly converted, by the compiler, to a legal type (coercion)
A type error
Application of operator to an operand of inappropriate type
Copyright © 2023 Addison-Wesley. All rights reserved.
1-23

<!-- Slide number: 24 -->
# Type Checking
If all type bindings are static
Nearly all type checking can be static
Why is this the case?
If type bindings are dynamic
Type checking must be dynamic
Why is this the case?
Strongly typed programming language
Type errors are always detected
Advantage
Detects all variable misuses causing type errors
Usually the strength of typing is relative
“Language A is more strongly typed than language B”
Copyright © 2023 Addison-Wesley. All rights reserved.
1-24

### Notes:
When type bindings are static, dynamic type checking may still be necessary in certain cases. One example of this is when a programming language supports subtypes. In such a language, we can define two types, A and B, where B is a subtype of A. If we define a variable of type A, called myVar, it can store a value of type B. We can then convert myVar to type B, which is called downcasting. However, it is not guaranteed that myVar actually stores a value of type B. If myVar is actually storing a value of type B, then the downcast will be successful. If not, a type error will occur. The error can only be detected at runtime, meaning that the type checking in this instance is dynamic. We see this kind of downcasting in object-oriented programming languages.

<!-- Slide number: 25 -->
# Strong Typing
Language examples
C and C++ are not strongly typed
In pre-C99 parameter type checking can be avoided
Both include unions, which are not type checked
Can you think of other reasons C or C++ aren’t strongly typed?
Java and C#
Implicit type errors cannot go undetected
But explicit casting can result in type errors
Person p = new Lecturer();
Student s = (Student) p;
Therefore more strongly typed than C and C++
Copyright © 2023 Addison-Wesley. All rights reserved.
1-25

### Notes:
Explicit casting in Java can lead to type errors. For example, assume the class Child inherits from the class Parent. The following will compile in Java:

Child obj = (Child) new Parent();

However, a runtime error will occur. Here the programmer is performing an explicit cast, which the compiler will accept because an object reference to a Parent could be an instance of class Child. Only at runtime does the JVM determine that the Parent object reference is not actually a Child object.

<!-- Slide number: 26 -->
# Strong Typing
Coercion rules can weaken typing
Coercion automatically converts operands to same type
Can cause accidental type mismatches to go undetected
For example, if a and b are int variables and d is a float
You mean to add a and b, but mistype b as d
Compiler/interpreter converts a to a float
Mistyping error isn’t detected
Language examples
C++ has many coercions
Therefore less reliable
Java has half of C++ assignment coercions
Therefore more reliable
Copyright © 2023 Addison-Wesley. All rights reserved.
1-26

<!-- Slide number: 27 -->
# Type Equivalence
Defines when operands of two types can be substitutable, with no coercion
Defines types of operands acceptable for all operators
For predefined scalar types
Simple and rigid (usually a type is only equivalent to itself)
For structured types and some user-defined types
Type equivalence rules are more complex
Copyright © 2023 Addison-Wesley. All rights reserved.
1-27

<!-- Slide number: 28 -->
# Type Equivalence
Name type equivalence
Variables have equivalent types only if they have exactly the same type
Easy to implement but restrictive
For example, subprogram parameters in call must exactly match the parameters in the subprogram definition
Structure type equivalence
Variables have equivalent types if their types have identical structures
More flexible, but harder to implement
Copyright © 2023 Addison-Wesley. All rights reserved.
1-28
