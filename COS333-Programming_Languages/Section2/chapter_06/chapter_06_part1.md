<!-- Slide number: 1 -->
# Chapter 6Part 1
Data Types

### Notes:

<!-- Slide number: 2 -->
# Chapter 6 Topics
Introduction
Primitive Data Types
Character String Types
User-Defined Ordinal Types
Array Types
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Introduction
A data type defines
A collection of data values with a range of values
How the data values are stored in memory
A set of predefined operations on the values
Design issues for all data types
Which operations are defined?
How are data types specified?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:

<!-- Slide number: 4 -->
# Primitive Data Types
Almost all languages provide primitive data types
Those not defined in terms of other data types
Some are merely reflections of the hardware
Others require only a little non-hardware support
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:

<!-- Slide number: 5 -->
# Primitive Data Types: Integer
May be as many as eight different integer types
For example, Java has signed integer sizes
byte
short
int
long
Some languages also have unsigned integers
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# Primitive Data Types: Floating Point
Model real numbers, but only as approximations
Languages for scientific use
At least two floating-point types (e.g. float and double)
Sometimes more floating-point types are supported
IEEE Floating-Point Standard 754 is common
Precision
Accuracy of the number’sfractional part
Range
Defines minimum andmaximum values

![](Picture4.jpg)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:

<!-- Slide number: 7 -->
# Primitive Data Types: Complex
Some languages support a complex type
For example, C99, Fortran and Python
Each value consists of two floats
The real part
The imaginary part
Literal form of a complex value, in Python
For example: (7 + 3j)
Where 7 is the real part, 3 is the imaginary part
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

<!-- Slide number: 8 -->
# Primitive Data Types: Decimal
For business applications (often monetary values)
Essential to COBOL
C# offers a decimal data type
Store a fixed number of decimal digits
Use coded representation (binary coded decimal, or BCD)
Advantage
Accuracy
Disadvantages
Wastes memory
Limited range
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:

<!-- Slide number: 9 -->
# Primitive Data Types: Boolean
Simplest data type of all
Range of values is only two elements
One for “true”
One for “false”
Could be implemented as bits
But addressing limitations usually don’t allow bit retrieval
Therefore bytes are often used (disadvantage?)
Advantage
Readability (why?)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:

<!-- Slide number: 10 -->
# Primitive Data Types: Character
Stored as numeric codings
Most commonly used coding: ASCII
Alternative, 16-bit coding: Unicode (UCS-2)
Characters from most natural languages
32-bit Unicode (UCS-4)
Supported by Fortran (starting with 2003)
The newer UTF-32 standard is used in Java and C#
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:
UCS stands for Universal Coded Character Set. UCS-2 uses 2 bytes to represent each character, and UCS-4 uses 4 bytes per character. UCS has largely been replaced by an updated specification called UTF (Unicode Transformation Format), with UTF-16 using 2 bytes per character, and UTF-32 using 4 bytes.

<!-- Slide number: 11 -->
# Character String Types
Values are sequences of characters
Design issues
A primitive type or just a special kind of array?
Should the string length be static or dynamic?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:

<!-- Slide number: 12 -->
# Character String Type By Language
C and C++
No primitive strings are directly supported
Use char arrays and operations in a library of functions
Fortran and Python
Primitive type with assignment and several operations
Java
Primitive type via the String class
The StringBuffer class is similar to a character array
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:
Java String objects are immutable. This means that string manipulation creates a new String object, and discards the old string for garbage collection. This is very expensive in terms of performance.

StringBuffer objects are mutable. This means that string manipulations modify the existing StringBuffer object, improving runtime performance.

There is also a StringBuilder class, which is similar to the StringBuffer class. StringBuilder objects are not thread safe, while StringBuffer objects are. This makes StringBuilder objects more efficient than StringBuffer objects.

<!-- Slide number: 13 -->
# Character String Length Options
Static length strings
COBOL, and Java’s String class
Limited dynamic length strings
C and C++
Special character used to indicate the end of a string
Length is not maintained explicitly
Dynamic length strings
Variable length
No maximum length
Perl, JavaScript
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:

<!-- Slide number: 14 -->
# Array Types
An array
An aggregate of homogeneous data elements
An individual element is identified by its position, relative to the first element
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:

<!-- Slide number: 15 -->
# Array Design Issues
What types are legal for subscripts?
Are subscripting expressions in elementreferences range checked?
When are subscript ranges bound?
When does allocation take place?
What is the maximum number of subscripts?
Are ragged and/or rectangular arrays allowed?
Can array objects be initialized?
Are any kind of slices supported?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:

<!-- Slide number: 16 -->
# Array Indexing
Indexing (also called subscripting)
A mapping from indices to elements
Index Syntax
FORTRAN, PL/I, and Ada use parentheses
Ada uses parentheses for uniformity between array references and function calls (both are mappings)
Most other languages use brackets
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:

<!-- Slide number: 17 -->
# Array Index Range Checking
C, C++, Perl, and Fortran
No index range checking
Advantage and drawback?
Java, ML, and C#
Have index range checking
Advantage and drawback?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:

<!-- Slide number: 18 -->
# Subscript Binding and Storage Binding
Static
A static local variable that is an array
Subscript range statically bound (length must be constant)
Storage allocation also static
Advantage
Efficient execution (no dynamic allocation)
Fixed stack-dynamic
Subscript range statically bound (length must be constant)
Allocation at declaration elaboration time, with deallocation usually at the end of the array’s scope
Advantage
Space efficiency (why?)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:

<!-- Slide number: 19 -->
# Subscript Binding and Storage Binding
Stack-dynamic
Subscript range dynamically bound (length can be variable)
Storage also dynamically bound
Both subscript range and storage fixed after initial binding
Advantage
Flexibility (array size need not be known until used)
Fixed heap-dynamic
Subscript range and storage binding are dynamic
Both are fixed after allocation
Binding is done when requested (e.g. with new and delete)
For example, dynamic arrays in C++
	 int *p = new int[size];
Storage is allocated from the heap, not the stack
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:

<!-- Slide number: 20 -->
# Subscript Binding and Storage Binding
Heap-dynamic
Binding of subscript ranges and storage are dynamic and can change any number of times
Storage is allocated from the heap, not the stack
Arrays that grow and shrink as items added and removed
Advantage
Flexibility (arrays are exactly the size they need to be)
Disadvantage?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-20

### Notes:

<!-- Slide number: 21 -->
# Subscript Binding and Storage Binding
In C and C++
Arrays that include static modifier are static
Arrays without static are fixed stack-dynamic
Provide fixed heap-dynamic arrays
In C#
Similar support to C++
Heap-dynamic ArrayList class
In Java
All arrays are fixed heap-dynamic
Perl, JavaScript, Python, and Ruby
Support heap-dynamic arrays
Copyright © 2023 Addison-Wesley. All rights reserved.
1-21

### Notes:

<!-- Slide number: 22 -->
# Heterogeneous Arrays
A heterogeneous array
Array in which the elements need not be of the same type
Supported by
Perl, Python, JavaScript, and Ruby
Actually implemented as
Homogenous arrays containing a generic data value
For example, an array containing Object values
Copyright © 2023 Addison-Wesley. All rights reserved.
1-22

### Notes:

<!-- Slide number: 23 -->
# Array Operations
APL
Powerful array operations for vectors, matrices & scalars
For example, to reverse column elements
Python
Array assignments are only reference changes
Array catenation and element membership operations
Java
Array assignments are also reference changes
A clone() method creates a copy
Copyright © 2023 Addison-Wesley. All rights reserved.
1-23

### Notes:
Consider the following code in Python:

cars = ["Ford", "Volvo", "BMW"]
countries = ["USA", "Germany", "France"]
countries = cars

Here, a copy is not performed. Instead, a reference change results in the countries array referring to the cars array. Any change to the cars array will affect countries, and any change to the countries array will affect cars.

<!-- Slide number: 24 -->
# Array Operations
Fortran provides elemental operations
Operations between pairs of array elements
For example, + operator between two arrays results in an array of the sums of the element pairs of the two arrays

	  integer, dimension(3) :: A, B, C
	  A    = (/ 3, 8, 5 /)
	  B    = (/ 2, 1, 3 /)
	  C    = A + B		! C contains 5, 9, 8
Copyright © 2023 Addison-Wesley. All rights reserved.
1-24

### Notes:

<!-- Slide number: 25 -->
# Rectangular and Jagged Arrays
A rectangular array
All rows have the same number of elements
All columns have the same number of elements
Fortran and Ada
A jagged matrix
Rows with varying number of elements
Actually represented as arrays of arrays
C, C++, and Java
C# and F#
Support both jagged and rectangular
Copyright © 2023 Addison-Wesley. All rights reserved.
1-25

### Notes:

<!-- Slide number: 26 -->
# Slices
A slice is some substructure of an array
Nothing more than a referencing mechanism that retrieves part of an array as a unit
Copyright © 2023 Addison-Wesley. All rights reserved.
1-26

### Notes:

<!-- Slide number: 27 -->
# Examples of Slices in Fortran 95

![](Picture4.jpg)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-27

### Notes:

<!-- Slide number: 28 -->
# Associative Arrays
An associative array
An unordered collection of data elements that are indexed by an equal number of keys
Requires that user defined keys must be stored
Design issues
What is the form of references to elements?
Do associative arrays have dynamic or static size?
Built-in type in Perl, Python, Ruby, Lua, and Swift
In Lua, they are supported by tables
In Perl, they are called hashes
Copyright © 2023 Addison-Wesley. All rights reserved.
1-28

### Notes:
