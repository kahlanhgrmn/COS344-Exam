<!-- Slide number: 1 -->
# Chapter 9Part 3
Subprograms

### Notes:

<!-- Slide number: 2 -->
# Chapter 9 Topics
Overloaded Subprograms
Generic Subprograms
Design Issues for Functions
User-Defined Overloaded Operators
Closures
Coroutines
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Overloaded Subprograms
An overloaded subprogram
Has the same name as another subprogram in the same referencing environment
Every overloaded subprogram has unique protocol
Subprogram protocol is parameter and return types
Some languages restrict this to just parameter profile
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:

<!-- Slide number: 4 -->
# Overloaded Subprograms
Examples
In C++, Java, and C#
Disambiguation based on parameter profile
Type coercion complicates the mapping process (why?)
In some languages (e.g. Ada)
Return type can disambiguate function calls
So, overloaded functions can have same parameters
Why can this not work in languages like C++?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:
Can you explain why type coercion complicates the mapping process for overloaded subprograms in languages like C++, Java, and C#?

Try to answer the question under the last point.

<!-- Slide number: 5 -->
# Generic Subprograms
Generic or polymorphic subprogram
Take different parameter types in different calls
Ad hoc polymorphism
Provided by overloaded subprograms
Parametric polymorphism
Not provided in all languages
A subprogram takes a generic parameter
A generic parameter
Describes subprogram parameter and/or return types
Different instantiations of the same subprogram get different generic parameters
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# Generic Subprograms
C++ supports generic subprograms
Are preceded by a template clause
Lists the generic variables
Variables can take on type names or class names

	      template <class T>
	      T max(T first, T second) {
	         return first > second ? first : second;
	      }

Here T is the generic parameter
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:
It is also possible to specify multiple generic parameters for a C++ generic subprogram.

<!-- Slide number: 7 -->
# Generic Subprograms
C++ supports generic subprograms
Assuming the previous template function

	      template <class T>
	      T max(T first, T second) {
	         return first > second ? first : second;
	      }

Subprogram versions are created at compile time
Happens whenever new types are used when
Subprogram is called
Subprogram address is taken with the & operator
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# Generic Subprograms
C++ supports generic subprograms
Continuing with our previous example

	      template <class T>
	      T max(T first, T second) {
	         return first > second ? first : second;
	      }

Subprogram versions are created at compile time
For example, if max function is used as follows
	          int a, b, c;
	          c = max(a, b);
Compiler generates new version of max function
The new version has every T replaced with int
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:

<!-- Slide number: 9 -->
# Generic Subprograms
Java 5.0 generics differ from C++
Generic parameters must be classes
Consider this doIt method and call to doIt

	      public static <T> T doIt(T[] list) { ... }

	      String[] myList = new String[10];
	      doIt<String>(myList);

The above is legal because String is a class
Illegal to use primitive types like int or float
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:
The discussion on this slide and the next two is the most important part of understanding how generics in Java differ from generics in C++, and is important for the exam.

Generics in Java are not strictly required (and weren’t included in earlier versions of Java). They increase the reliability of programs by detecting type errors at compile time, rather than runtime.

<!-- Slide number: 10 -->
# Generic Subprograms
Java 5.0 generics differ from C++
Continuing with out previous example

	      public static <T> T doIt(T[] list) { ... }

	      String[] myList = new String[10];
	      doIt<String>(myList);

Generic methods are instantiated once at run time
Instances of Object used wherever T appears
Therefore doIt is represented internally as

	      public static Object doIt(Object[] list) { ... }

This means that doIt can work with any object
Because all objects inherit from the Object class
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:

<!-- Slide number: 11 -->
# Generic Subprograms
Java 5.0 generics differ from C++
Continuing with our previous example

	      public static <T> T doIt(T[] list) { ... }

	      String[] myList = new String[10];
	      doIt<String>(myList);

Which is represented internally as

	      public static Object doIt(Object[] list) { ... }

Compiler inserts casts to the appropriate type
A cast for the parameter to String[]
A cast for the returned value to String
Ensures that any type misuses by a user of doIt are picked up at compile time, rather than runtime
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:
If the casts were not automatically inserted, any type errors would only be detected at runtime. This would work, but would make it more difficult to debug generic methods. As an example, imagine if we implemented doIt to simply received an Object array, and returned an Object. Then we send a String array as the parameter, but cast the returned value to a Student object. Of course, the return will be a String, but this can’t be detected at compile time. Only at runtime will it become clear that the return type doesn’t match with the variable you’re assigning to.

<!-- Slide number: 12 -->
# Generic Subprograms
Java 5.0 generics differ from C++
Can restrict class ranges for generic parameters

	    public static <T extends Comparable> T doIt(T[] list)
	    { ... }

Ensures that T is a subtype of Comparable
This means T must be a class that either
Inherits from a class called Comparable
Implements an interface called Comparable
Here, Comparable is an interface provided by Java
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:

<!-- Slide number: 13 -->
# Generic Subprograms
Java 5.0 generics differ from C++
Wildcard types for generic parameters

	    void printCollection(Collection<?> c) { ... }

The wildcard is indicated by the question mark
Means “any object”
Therefore, the printCollection method can receive an instance of the Collection class containing objects of any class
Also possible to restrict the wildcard using extends
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:

<!-- Slide number: 14 -->
# Generic Subprograms
In C# 2005
Creates subprogram versions at runtime
For primitive types, this works Almost like C++ does
For any object, a version for Object class is created
Differences:
No support for wildcards
If the compiler can infer the unspecified type
Actual type parameters in a call can be omitted
For example:

	     public static T DoIt<T>(T p1) {...}

	     int myInt = MyClass.DoIt(17);
	     string myStr = MyClass.DoIt('apples');
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:
More specifically, if a generic method is used with a primitive type, a new version of the method for the specified type is created at runtime. If the same generic method is used for any kind of object type, a new version of the method for an object is created. Any future use of the generic method with a different object type will reuse the already created version of the method that works with objects.

So, essentially, C# uses Java’s approach when the generic type is an object. If the generic type is a primitive type, C# works more like C++ by creating different versions of the generic method. However, these different versions are created at runtime, not compile time.

<!-- Slide number: 15 -->
# Design Issues for Functions
Are side effects allowed?
We’ve spoken about side effects in Chapter 15
To reduce side effects
Parameters should ideally be in-mode
Purely functional languages enforce this, but most other languages don’t
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:

<!-- Slide number: 16 -->
# Design Issues for Functions
How many values can be returned?
Most languages only allow one return value
Ruby methods
Multiple returns allowed through an array of values

     def multiple_values
        return 1, 2, 3, 4
     end
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:
In Ruby, multiple returned values are actually packaged in an Array. You can assign such a returned array to multiple variables. Therefore, for the Ruby example on this slide, you can do the following:

a, b, c, d = multiple_values

This will assign 1 to a, 2 to b, 3 to c, and 4 to d. Behind the scenes, the values are actually extracted from a returned array.

<!-- Slide number: 17 -->
# Design Issues for Functions
What types of return values are allowed?
Functions in C and C++
Any type can be returned
Except arrays and functions
How can these returns be simulated?
C++ also allows user-defined types to be returned
Java and C# methods
Can return any type (but methods are not types)
Python and Ruby
Any class can be returned
Methods are first-class objects, so can be returned
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:
In C++, however, it is possible to return a pointer (which refers to the start of an array), or a function pointer (however, you must use a typedef to do this).

<!-- Slide number: 18 -->
# User-Defined Overloaded Operators
Supported in C++, Python, and Ruby
For example, in the Complex class of Python:

        def __add__ (self, second) :
           return Complex(self.real + second.real,
                          self.imag + second.imag)

An addition operator for two Complex objects
Used in two ways, if x and y are Complex objects

  x + y
  x.__add__(y)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

<!-- Slide number: 19 -->
# Closures
A JavaScript closure

      function makeAdder(x) {
         return function(y) { return y + x; }
      }

The makeAdder function
Creates and returns a new anonymous function
Anonymous function is called a closure
It receives a numeric parameter y
It returns sum of y and a value
Second value specified by x parameter of makeAdder
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:

<!-- Slide number: 20 -->
# Closures
A JavaScript closure

      function makeAdder(x) {
         return function(y) { return y + x; }
      }

      var add10 = makeAdder(10);
      var add5 = makeAdder(5);
      document.write(″add 10 to 20: ″ + add10(20) + ″<br />″);
      document.write(″add 5 to 20: ″ + add5(20) + ″<br />″);

Consider the calls to makeAdder
The variable add10 refers to anonymous function

	     function(y) { return y + 10; }

The variable add5 refers to anonymous function

	     function(y) { return y + 5; }
Copyright © 2023 Addison-Wesley. All rights reserved.
1-20

### Notes:
Of course, the call to add10(20) passes 20 as the parameter to the anonymous function

function(y) { return 10 + y; }

which will return 30, and this result will be printed. Similarly, the call add5(20) will pass 20 as the parameter to the anonymous function

function(y) { return 5 + y; }

which will return 25, and this result will be printed.

The important thing to understand, however, is not what is printed, but what add10 and add5 are, and how they are created.

<!-- Slide number: 21 -->
# Closures
A JavaScript closure

      function makeAdder(x) {
         return function(y) { return y + x; }
      }

      var add10 = makeAdder(10);
      var add5 = makeAdder(5);
      document.write(″add 10 to 20: ″ + add10(20) + ″<br />″);
      document.write(″add 5 to 20: ″ + add5(20) + ″<br />″);

Assume a variable is passed to makeAdder

    var add = makeAdder(val);

Can call add anywhere, and val may be out of scope
So, val lifetime must be over full program execution
The variable val is said to have unlimited extent
Copyright © 2023 Addison-Wesley. All rights reserved.
1-21

### Notes:

<!-- Slide number: 22 -->
# Coroutines
A coroutine
A subprogram with multiple entry points
Controls entry points itself
Introduced in Simula 67, supported in Lua
Also called symmetric control
The caller and called coroutines exist on a more equal basis
Copyright © 2023 Addison-Wesley. All rights reserved.
1-22

### Notes:
This work is easy and will probably come up during the exam.

<!-- Slide number: 23 -->
# Coroutines
A coroutine call is named a resume
The first resume of a coroutine is to its beginning
Later resumes enter after last executed statement
Coroutines can resume each other forever
Coroutines allow quasi-concurrent execution
Their execution is interleaved, but not overlapped
Copyright © 2023 Addison-Wesley. All rights reserved.
1-23

### Notes:

<!-- Slide number: 24 -->
# Coroutines Illustrated: Possible Execution Controls

![](Picture4.jpg)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-24

### Notes:

<!-- Slide number: 25 -->
# Coroutines Illustrated: Possible Execution Controls with Loops

![](Picture4.jpg)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-25

### Notes:
