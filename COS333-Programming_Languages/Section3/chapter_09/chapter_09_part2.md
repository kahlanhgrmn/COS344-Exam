<!-- Slide number: 1 -->
# Chapter 9Part 2
Subprograms

### Notes:

<!-- Slide number: 2 -->
# Chapter 9 Topics
Parameter-Passing Methods
Parameters That Are Subprograms
Calling Subprograms Indirectly
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Semantic Models of Parameter Passing

![](Picture3.jpg)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:

<!-- Slide number: 4 -->
# Conceptual Models of Transfer
Two ways data transfer can take place
Physically copy a value
Transmit an access path to a value
This gives us five implementation models for parameter passing
Pass-by-value
Pass-by-result
Pass-by-value-result
Pass-by-reference
Pass-by-name
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:

<!-- Slide number: 5 -->
# Pass-by-Value (In Mode)
The value of the actual parameter is used to initialize corresponding formal parameter
For example, in C++

 void foo(int a) {
    a += 2;  // has no effect on b in main
 }

 int main() {
    int b = 12;
    foo(b);  // copies value 12 to a in foo
 }
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:
A physical move is used for by-value parameter passing in C++. If we were passing objects, rather than integers, the copy operation could take some time.

<!-- Slide number: 6 -->
# Pass-by-Value (In Mode)
Implementation of pass-by-value
Normally implemented by copying
Disadvantages
Additional storage is required (stored twice)
Actual move can be costly (for large parameters)
Can be done by transmitting an access path
Not recommended
Disadvantages
Must write-protect in the called subprogram
Accesses cost more (indirect addressing)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:

<!-- Slide number: 7 -->
# Pass-by-Result (Out Mode)
Value of formal parameter is used to change corresponding actual parameter
For example, in Ada

	procedure A_Test (A, B: in Integer; C: out Integer) is
	begin
	   C := A + B;
	end A_Test;

Consider this call

	A_Test (5 + P, 48, Q);

Here, no value can be transmitted to C
After call, Q is overwritten by the value assigned to C

Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:
Pass-by-result is not supported by C, C++ or Java.

In the example, note that if C is not modified in the procedure, Q will have garbage written to it. It is therefore good practice to initialise all out parameters.

<!-- Slide number: 8 -->
# Pass-by-Result (Out Mode)
Implementation of pass-by-result
The value of the formal parameter is used to change the corresponding actual parameter
Pass happens when control is returned to the caller
Copy from formal parameter to actual parameter
Can an access path be transferred instead?
Potential problems
Requires extra storage location and copy operation
For the subprogram definition sub(a, b) {...}
Consider the call sub(p1, p1);
​​p1’s value depends on order parameters copied
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:

<!-- Slide number: 9 -->
# Pass-by-Value-Result (inout Mode)
Combines pass-by-value and pass-by-result
Formal parameters have local storage
Drawbacks of pass-by-result and pass-by-value
For example, in Ada

	   procedure A_Test (A, in Integer; C: in out Integer) is
	   begin
	      C := A + C;
	   end A_Test;

Here the formal parameter C is used for two things
It passes a value into A_Test
Can be assigned to, copying to the actual parameter
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:
Pass-by-value-result is not supported by C, C++ or Java.

In the Ada example, it is legal to use the value of C sent by the procedure call. It is also legal to modify the value of C. The procedure could be called with the statement

A_Test (5 + P, 48, Q);

The value of Q will be sent to the procedure, and will also be overwritten by the procedure. If C is not modified, Q remains unchanged.

<!-- Slide number: 10 -->
# Pass-by-Reference (Inout Mode)
Pass an access path
Implemented using a reference or a pointer
Also called pass-by-sharing
For example, in C++

  void foo(int *p, int &r) {
     *p = 23 + r;
     r = 19 - *p;
  }

Both p and r are passed by reference
The p parameter is a pointer, while r is a reference
Both can be used to pass data into the foo function
Both can be used to send data back to the caller
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:
The example function can be called as follows:

int val = 88;
int *varPointer = &val;
int secondVal = 97;
foo(varPointer, secondVal);

In this case, the value pointed to by varPointer is modified in the function. The value of secondValue is also modified in the function.

<!-- Slide number: 11 -->
# Pass-by-Reference (Inout Mode)
Pass an access path
Advantage
Efficient execution (no copying)
Efficient storage (no duplicated storage)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:

<!-- Slide number: 12 -->
# Pass-by-Reference (Inout Mode)
Pass an access path
Disadvantages
Compared to pass-by-value
Slower accesses to formal parameters
Potential for unwanted side effects (see Chapter 15)
Unwanted aliases (broader access allows collisions)
Consider this function definition

	 void fun(int &first, int &second) {...}

Now look at this function call

	 fun(total, total)

Here first and second are aliases for total
What potential problems could this result in?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:

<!-- Slide number: 13 -->
# Pass-by-Name (Inout Mode)
Pass-by-name uses textual substitution
Older approach, not used in modern languages
All formal parameter occurrences are replaced by the appropriate actual parameter
Formal parameters are bound to access method
At call time
Access method could be a copy or a reference
Actual binding to a value or address
Only when formal parameter is used in subprogram
Allows flexibility in late binding
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:

<!-- Slide number: 14 -->
# Pass-by-Name (Inout Mode)
Pass-by-name works by textual substitution
For example, consider this implementation

  void foo(int a, int b) {
     a = 1;
     print(a, b);
  }

  void main() {
     int val = 0;
     int arr[3] = {2, 8, 9};
     foo(val, arr[val]);
  }

First, let’s assume normal pass-by-value is used
The output will be “1 2”, as we’d expect
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:

<!-- Slide number: 15 -->
# Pass-by-Name (Inout Mode)
Pass-by-name works by textual substitution
Now assume pass-by-name

  void foo(int a, int b) {
     a = 1;
     print(a, b);
  }

  void main() {
     int val = 0;
     int arr[3] = {2, 8, 9};
     foo(val, arr[val]);
  }

Substitute val for a and arr[val] for b
Body becomes: val = 1; print(val, arr[val]);
The output will be “1 8”
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:
By using pass-by-name in this example, we’ve achieved a kind of late binding. This means we got to specify at runtime which subscript in the array to access through the value of the a variable (remember, this is a variable, so its value can change during runtime).

Now assume that the foo subprogram is used as follows:

int val1 = 0;
int val2 = 2;
foo(val1, val2);

Will there be any difference between the output if normal pass-by-value is used versus if pass-by-name is used?

<!-- Slide number: 16 -->
# Parameter Passing Method Examples
In C and C++
Pass-by-value
Pass-by-reference
Pointer parameters in C
Pointer or reference parameters in C++
In Java
All parameters are passed by value
Objects seem to be passed by reference
Actually, object references are passed by value
In Fortran 95 and newer
Parameters can be In, Out, or Inout mode
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:

<!-- Slide number: 17 -->
# Parameter Passing Method Examples
In C#
Pass-by-value
Pass-by-reference
Precede formal parameter and actual parameter with ref
In Perl
Implicitly places actual parameters in @_ array
Elements of @_ are aliases for actual parameters
Which passing method does this imply?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:
PHP differs slightly from C# in that either the formal or actual parameter can be marked with ref.

Try to answer the question under the last point.

<!-- Slide number: 18 -->
# Parameter Passing Method Examples
Python and Ruby use pass-by-assignment
Actual parameter assigned to formal parameter
Remember that all data values are objects
Assigning one object to another is a reference change
This means it works like pass-by-reference
Except when assigning to immutable objects(what happens here?)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:
Immutable objects in Python include:

Numbers (Integer, Rational, Float, Decimal, Complex, and Booleans)
Strings
Tuples
Frozen Sets

In Ruby, most objects are mutable. Immutable objects in Ruby include numbers and Boolean values. It is also possible to make an existing object immutable by freezing the object.

Now try to answer the question. Remember that immutable objects can’t be modified.

<!-- Slide number: 19 -->
# Type Checking Parameters
Parameter type checking
Testing if actual & formal parameter types match
Very important for reliability

FORTRAN 77, early C, Perl, JavaScript, PHP
Do no checking (what is the result of this?)

C versus C++
No type
checking:
Original C,
C89
double sin(x)
   double x;
   { ... }
double sin(double x)
   { ... }
Type checking with coercion:
C89, C++
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:
If no type checking is performed for a parameter, it means that there is no way to confirm that a specific expected type is actually what will be passed through as an actual parameter in a subprogram call. Even if a type is specified (for example, look at the leftmost C example), these are really just hints. In the example, we are basically only saying “you can probably expect that the parameter x will be a double value, but there aren’t any guarantees”. Anyone calling the sin function can pass through whatever they like as a parameter. Whatever is passed as the parameter is then interpreted on a bit level as a double value.

So a lack of type checking is almost always dangerous. Can you give concrete reasons what might happen if a type mismatch occurs?

<!-- Slide number: 20 -->
# Type Checking Parameters
Pascal, FORTRAN 90, Java, and Ada
Always required (what is the result of this?)

Python and Ruby
Variables do not have types (objects do)
For example, consider this assignment in Ruby

    p = Person.new

The object assigned to p has the type of Person
The variable p has no type
So formal parameters are typeless
Meaning formal parameters can’t be type checked
Copyright © 2023 Addison-Wesley. All rights reserved.
1-20

### Notes:
Consider the statement “variables do not have types, but objects do”, in relation to Python and Ruby. What does this mean? Let’s look at Python. Consider the following assignment:

p = Person.new

Here the variable is p. When the assignment completes, what we’ve really done is create a Person object, and assigned this to the variable p. The assignment means that the variable p is now a reference to the Person object. The object has a type (a Person), but the variable p does not. You can think of this as a variable of type Object in Java. So now let’s assume we have a function as follows:

def my_function(value):
  print(value)

We have a formal parameter named value. This is a variable, and therefore has no type associated with it. This means that any particular object could be passed to my_function. Because value has no type associated with it, no type checking can take place.

We would see a similar type of thing in Java if we wrote a method that accepted an Object parameter – we would have to cast the parameter before we could use it. Here’s a Java method illustrating this:

public static void doSomething (Object o) {
      Person myP = (Person) o;
      myP.printName();
      myP.printAge();
}

This method works, but it assumes that the object we pass to the doSomething method is an instance of the Person class. It’s completely possible to pass some other object to doSomething, and the program code will compile, but cause a runtime error. This illustrates the potential dangers associated with a lack of parameter type checking.

<!-- Slide number: 21 -->
# Multidimensional Arrays as Parameters
Formal array parameters in C and C++
Include sizes of all subscripts except the first
For example

	     void fun(int matrix[][10]) { ... }

Disadvantage
Disallows writing flexible subprograms
The matrix above must have 10 columns
Copyright © 2023 Addison-Wesley. All rights reserved.
1-21

### Notes:
The mapping function needs to know the size of all dimensions except the first because of the way arrays are organised in memory. Consider the following array (where part of the array initialisation is left out for simplicity):

int myArr[ ][3] = {{1, 2, 3}, {4, 5, 6}, … };

This array is arranged as follows in memory:

[1][2][3][4][5][6] …

In order for the compiler to know where the start of each row is in memory, it must know how much memory is taken up by each row. This is why it must know that the second dimension is 3. It doesn’t need to know the size of the first dimension because the same pattern is followed by all rows, so there can be an arbitrary number of rows (indicated by the ellipsis in the above representation). The same logic holds for more than two dimensions (each row now consists of further fixed length arrays).

In C and C++ this is particularly a problem, because a function can be compiled in a separate file. This means the compiler can’t rely on the call to the subprogram to determine the array’s dimensionality (and therefore the mapping function). The mapping function can only be determined from the function itself, hence requiring that all but the first array dimension be provided.

<!-- Slide number: 22 -->
# Multidimensional Arrays as Parameters
Solution
Pass array as a pointer
Pass dimension sizes as separate parameters
For example

	 void fun (int *p, int numRows, int numCols) { ... }

Use pointer arithmetic to access array values
Disadvantages?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-22

### Notes:
You should be familiar with this approach to passing dynamic and multidimensional arrays to C++ functions. Try to answer the question.

<!-- Slide number: 23 -->
# Multidimensional Arrays as Parameters
In Java and C#
Arrays are objects
They are all single-dimensional
But, the elements can be arrays
Each array has a named constant
Set to the length of the array when array is created
Called length in Java
Called Length in C#
This means we can query an array to find its length
No sizes are specified in the formal parameters
Copyright © 2023 Addison-Wesley. All rights reserved.
1-23

### Notes:

<!-- Slide number: 24 -->
# Calling Subprograms Indirectly
Subprograms are called indirectly when
There are several possible subprograms to call
The correct one is not known until execution
For example, during event handling
In C and C++
Such calls are made through function pointers
Pointer includes parameter and return types
For example

   float myFunc(float a, int b) { ... }

   float (*ptr)(float, int) = myFunc;
   ptr(1.8, 3);
Copyright © 2023 Addison-Wesley. All rights reserved.
1-24

### Notes:
In the code example, ptr is a pointer to a function that returns a float, and receives two parameters, where the first is a float and the second is an int. If we assign ptr to myFunc (note that myFunc has the same return and parameter types), we can call ptr the same way as myFunc.

Function pointers allow a kind of parameterization for programs, because they can point to any function with the required return type and parameters. It’s therefore possible to:
Write several functions that perform different tasks
Dynamically figure out which one needs to be used at run time
Pass the appropriate function to another function that uses it

So you might write an event dispatcher function that executes runtime events. You can then write the code for individual event handlers in functions. As long as all the event handler functions have the same parameters and return types, whichever one is appropriate at the time can be passed to the dispatcher, where it will be executed.

<!-- Slide number: 25 -->
# Calling Subprograms Indirectly
In C# method pointers are possible
Implemented as objects called delegates
Declaring a delegate type named Change
     public delegate int Change(int x);

A delegate object is instantiated with method that has the appropriate protocol
     static int m1(int x) { ... }
     Change myChangeFunction = new Change(m1);
     myChangeFunction(12);
Multicast delegates
Store several method pointers, run in sequence
     myChangeFunction += fun2;
Copyright © 2023 Addison-Wesley. All rights reserved.
1-25

### Notes:
What advantage does a C# delegate have in comparison to a C or C++ function pointer? Consider the fact that a delegate in C# uses a delegate type.

Can you think of a practical situation in which a multicast delegate might be useful?

<!-- Slide number: 26 -->
# Parameters that are Subprogram Names
It is sometimes convenient to
Pass subprogram names as parameters
Requires a way to call a subprogram indirectly
Two issues
Are parameter types checked?
Referencing environment for passed subprogram?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-26

### Notes:

<!-- Slide number: 27 -->
# Parameters that are Subprogram Names: Parameter Type Checking
C and C++
Function pointers passed as parameters
Allows parameters to be type checked (why?)
FORTRAN 95
Allows subprograms to be passed as parameters
Type checks parameters
Java
Doesn’t allow parameters that are subprograms
Copyright © 2023 Addison-Wesley. All rights reserved.
1-27

### Notes:
Try to answer the question (consider the discussion on function pointers in the previous slides).

<!-- Slide number: 28 -->
# Parameters that are Subprogram Names: Referencing Environment
Recall that a referencing environment is
All variables visible to a statement
That is, variables the statement can reference
A passed subprogram
Has a referencing environment
This becomes important when
Passed subprogram refers to a variable
Variable is defined outside passed subprogram
Need to disambiguate which variable is referred to
Copyright © 2023 Addison-Wesley. All rights reserved.
1-28

### Notes:

<!-- Slide number: 29 -->
# Parameters that are Subprogram Names: Referencing Environment
We’ll illustrate concepts using this example
We assume nested subprograms are allowed
We assume static scoping rules
sub1 calls sub3
sub3 passes sub2 as a parameter to sub4
sub4 executes the subprogram passed to it

The question is
When sub2 prints x, it refers to a variable outside its local scope
Output depends on which x it is referring to
Dictated by referencing environment of sub2

Three possible approaches
Shallow binding
Deep binding
Ad hoc binding

fun sub1() {
   var x = 1

   fun sub2() {
      print x
   }

   fun sub3() {
      var x = 3
      call sub4(sub2)
   }

   fun sub4(subx) {
      var x = 4
      call subx()
   }

   call sub3()
}
Copyright © 2023 Addison-Wesley. All rights reserved.
1-29

### Notes:
This is important work for examination purposes.

<!-- Slide number: 30 -->
# Parameters that are Subprogram Names: Referencing Environment
Shallow binding:
Passed subprogram referencing environment
The call enacting the passed subprogram
Natural for dynamic-scoped languages
In the example
The referencing environment of the subx call
Therefore, the x in sub4 is referenced
The output is 4
fun sub1() {
   var x = 1

   fun sub2() {
      print x
   }

   fun sub3() {
      var x = 3
      call sub4(sub2)
   }

   fun sub4(subx) {
      var x = 4
      call subx()
   }

   call sub3()
}
Copyright © 2023 Addison-Wesley. All rights reserved.
1-30

### Notes:
This is important work for examination purposes.

<!-- Slide number: 31 -->
# Parameters that are Subprogram Names: Referencing Environment
Deep binding:
Passed subprogram referencing environment
The passed subprogram definition
Natural for static-scoped languages
In the example
Referencing environment of sub2 definition
We’re assuming that static scoping is used
Therefore, the x in sub1 is referenced
The output is 1 (assuming static scoping)
fun sub1() {
   var x = 1

   fun sub2() {
      print x
   }

   fun sub3() {
      var x = 3
      call sub4(sub2)
   }

   fun sub4(subx) {
      var x = 4
      call subx()
   }

   call sub3()
}
Copyright © 2023 Addison-Wesley. All rights reserved.
1-31

### Notes:
This is important work for examination purposes.

<!-- Slide number: 32 -->
# Parameters that are Subprogram Names: Referencing Environment
Ad-hoc binding:
Passed subprogram referencing environment
Call statement that passed the subprogram
In the example
Referencing environment of the sub4 call
Therefore, the x in sub3 is referenced
The output is 3
fun sub1() {
   var x = 1

   fun sub2() {
      print x
   }

   fun sub3() {
      var x = 3
      call sub4(sub2)
   }

   fun sub4(subx) {
      var x = 4
      call subx()
   }

   call sub3()
}
Copyright © 2023 Addison-Wesley. All rights reserved.
1-32

### Notes:
This is important work for examination purposes.
