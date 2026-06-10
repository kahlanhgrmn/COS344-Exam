<!-- Slide number: 1 -->
# Chapter 12Part 1
Support forObject-Oriented Programming

### Notes:

<!-- Slide number: 2 -->
# Chapter 12 Topics
Introduction
Object-Oriented Programming
Design Issues for OO Languages
Support for OOP in Smalltalk
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Introduction
There are many OOP languages
Some are procedural and data-oriented
For example, C++
Some support functional programming
For example, CLOS
Newer languages
Do not support other paradigms
But use some basic imperative structures
For example, Java and C#
Some are considered pure OOP language
For example, Smalltalk and Ruby
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:

<!-- Slide number: 4 -->
# Abstract Data Types (ADTs)
Abstract data types
Chapter 11, but not explicitly examinable
User defined data type, to create objects
Defines representation and operations
Use variables and subprograms
Single syntactic unit (e.g. a struct or a class)
Creates an abstraction
Representation of objects hidden from user
On their own, have no OOP concepts
Inheritance
Polymorphism
Dynamic message binding
Copyright © 2012 Addison-Wesley. All rights reserved.
1-4

<!-- Slide number: 5 -->
# Object-Oriented Programming
Any OOP language must support
Abstract data types
In an OOP context, these are classes
Inheritance
Inheritance is the central theme in OOP
Polymorphism
Dynamic binding of method calls to methods
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# Inheritance
Productivity increases can come from reuse
Problems with basic ADTs (classes)
Difficult to reuse without some changes
All are independent and at the same level
Inheritance
Allows new classes defined i.t.o. existing ones
In other words, they can inherit common parts
Inheritance addresses both concerns
Reuse ADTs after minor changes
Define classes in a hierarchy
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:
Basic ADTs are classes and structs that don’t support any form of inheritance or concepts related to inheritance (such as polymorphism). Object-Oriented Programming refers to ADTs with support for proper inheritance (and all the concepts related to inheritance).

<!-- Slide number: 7 -->
# Object-Oriented Concepts
ADTs
Usually called classes
Class instances
Are called objects
A class that inherits
A derived class or a subclass
The class from which another class inherits
A parent class or superclass
Subprograms defining operations on objects
Are called methods
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:
The term “child class” is sometimes used to mean “subclass”.

C++ calls its methods “member functions”.

<!-- Slide number: 8 -->
# Object-Oriented Concepts
Calls to methods
Are called messages
Entire collection of an object’s methods
Message protocol or message interface
Messages have two parts: obj.meth()
Method name: meth
Destination object: obj
The simplest case
Class inherits all the entities of its parent
Adds more entities
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:
In a call such as:

myStudent.writeExam();

the method name is writeExam, while the destination object is myStudent

It is obviously possible for a class to inherit from a parent and not add any more entities (member variables or methods), but this is generally never done because the derived class is then redundant.

<!-- Slide number: 9 -->
# Object-Oriented Concepts
Inheritance can be more complicated
Access controls to encapsulated entities
A class can hide entities from its subclasses
A class can hide entities from its clients
A class can hide entities from its clients while allowing its subclasses to see them
Besides inheriting methods as is
A class can modify an inherited method
The new one overrides the inherited one
The method in the parent is overriden
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:
Private members are hidden from subclasses and clients. In the case of private member variables in the parent class, the derived class essentially has these members, but can only access them through public or protected methods in the parent class.

Protected members are accessible to derived classes, but not to clients. One would use protected methods to provide functionality that is commonly needed by derived classes, but should be hidden from client code. Protected access isn’t strictly speaking necessary (some OOP languages only support public and private access), but is very convenient. If protected access isn’t provided, the only way to access private members is via the public interface (which would be able to access the private members).

<!-- Slide number: 10 -->
# Object-Oriented Concepts
There are two kinds of variables in a class
Class variables: One per class
Instance variables: One per object
There are two kinds of methods in a class
Class methods: Accept messages to the class
Instance methods: Accept messages to objects
Single inheritance vs. multiple inheritance
One disadvantage of inheritance for reuse
Creates interdependencies among classes
May complicate maintenance
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:
In the C++ derived languages class members are called “static members”. This is an unfortunate naming decision, because static local variables are a completely different concept. Static local variables (i.e. static variables in a function body) are variables that have scope only in their function, but have a lifetime that lasts through program execution (from the start to the end of the program run), and are also history sensitive. Static members are class-level members (static member variables have one copy shared by all objects of the class, while static methods are usually called on the class and work only with static member variables). For example, in C++:

class BankAccount {
   private:
      double balance;
      static int numberOfAccounts;

   public:
      double getBalance();
      static int getNumberOfAccounts();
}

Here balance is an instance variable, so every individual BankAccount object has its own balance, while numberOfAccounts is a class variable, meaning that there is a count of the number of accounts that is shared by all objects (i.e. there is only one numberOfAccounts). Similarly, every bank account has its own getBalance method (which would be called as follows: myBankAccount.getBalance() if we assume that myBankAccount is an object of class BankAccount). The static method exists for the whole class (it would usually be called as BankAccount.getNumberOfAccounts(), although some languages allow you to call it on an object as well). The main difference is that static methods can’t work with non-static member variables (because these variables are defined for objects, not the class as a whole).

Interdependencies between classes mean that modifications to a parent class often requires modification of the derived class. Obviously this can expand with a large number of derived classes, which causes a lot of headaches if you need to refactor code.

<!-- Slide number: 11 -->
# Dynamic Binding
A polymorphic reference or pointer
Can refer to objects of either a class or any descendant of that class
​Person* p;p = new Student();
When overridden methods are called through a polymorphic variable
Binding to the correct method will be dynamic
For example, p->print() must bind to Student
Allows easy extensions to software systems
Both during development and maintenance
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:
The code example assumes that Person is the parent class from which Student is derived. Because a student is a specific example of a more general person, we can assign a Student to a Person pointer or reference (note that things work a bit differently if we’re talking about Student and Person objects – more on this a bit later). We can’t assign a Person to a Student, because Student is more specific.

Dynamic method binding requires that the variable to which the method is sent must be a pointer or a reference.

<!-- Slide number: 12 -->
# Dynamic Binding Concepts
An abstract method
Does not include a definition
Only defines a protocol
An abstract class
Includes at least one abstract method
Cannot be instantiated
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:
C++ uses the term “pure virtual member function” to mean “abstract method”. An abstract method is used when you want to ensure that all derived classes must provide the method, but it doesn’t make sense to implement the method in the parent class. For example, in C++:

class Shape {
   virtual draw() = 0;
}

class Circle : public Shape {
   virtual draw() { … };
}

It doesn’t make sense to implement the draw method in Shape, because we have no idea how a shape should be drawn. By providing the draw() method as an abstract method, this ensures that Circle must implement a draw() method (which makes sense, because a circle has enough information to be able to draw itself). Because Shape has an abstract method, it means that Shape is also an abstract class. We can therefore only create an object of Circle (because it has no abstract methods after we’ve implemented the draw() method), but not of the Shape class.

<!-- Slide number: 13 -->
# Design Issues for OOP Languages
The Exclusivity of Objects
Are Subclasses Subtypes?
Single and Multiple Inheritance
Object Allocation and Deallocation
Dynamic and Static Binding
Nested Classes
Initialization of Objects
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:

<!-- Slide number: 14 -->
# The Exclusivity of Objects
Everything is an object
Advantage: Elegance and pure uniformity
Disadvantage: Simple operations are slow
Add objects to a complete typing system
Advantage: Simple operations can be fast
Disadvantage: Results in confusing type system
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:
In Smalltalk everything is an object. What does the uniformity of this approach suggest in terms of the language evaluation criteria?

C++ adds objects to a complete type system (it has classes with inheritance, as well as things like structs, unions, arrays, and C-style strings, which don’t use objects).

<!-- Slide number: 15 -->
# The Exclusivity of Objects
Use an imperative typing system for primitives, make everything else objects
Advantage: Simple operations can be fast, but the typing system remains relatively small
Disadvantage: Two type systems still have to mix
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:
Java uses an imperative type system for primitive types, while everything else is an object. The basic types (like int, float, and boolean) are not handled through objects (and are therefore fast), while all the more complex structures are all handled through objects.

<!-- Slide number: 16 -->
# Are Subclasses Subtypes?
Does an “is-a” relationship hold between a subclass object and a parent class object?
If so, derived class is a subtype of the parent
Derived class objects behave like parent objects
Practically, this means
Subclass can only add variables and methods
Methods can only be overidden in “compatible” ways
Same number of parameters
Parameters & return type must be type compatible
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:
If a subclass can decide to not inherit methods or variables from a parent class, the derived class is not a subtype of the parent class. For example, using C++ syntax:

class Parent {
   public:
      int getData();
}

class Child : public Parent {
   private:
      using Parent::getData;      // this changes the access of getData() to private
}

In this case, Child is not a subtype of Parent because it no longer behaves the same way as Parent (i.e. it is not possible for a client program to call getData() on a Child object, but it is possible to call it on a Parent object). This also holds for member variables. Similarly, if Child could somehow change getData() to (for example) return nothing, Child will again not be a subtype of Parent.

<!-- Slide number: 17 -->
# Single and Multiple Inheritance
Multiple inheritance
A new class inherits from two or more classes
Advantage
Sometimes it is quite convenient and valuable
Disadvantages
Potential inefficiency
Multiple inheritance dynamic binding costs more
But not a great deal more
Language and implementation complexity
Primarily due to name collisions
When 2 parent classes have entities with same name
Implicit when diamond inheritance takes place
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:

<!-- Slide number: 18 -->
# Single and Multiple Inheritance
A
B
C
D
Diamond inheritance
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:
Consider this example, in C++:

class P1 {
   public:
      void d();
}

class P2 {
   public:
      void d();
}

class C : public P1, public P2 {
   // must use either P1::d() or P2::d() to disambiguate the call
}

In this case C inherits from both P1 and P2, both of which have a method called d. It is necessary to differentiate any reference to d (either from inside class C, or in client code that uses class C). We do this by using the scope resolution operator (the :: operator) to specify the class from which d() should be called.

Diamond inheritance always introduces this type of problem. For example:

class T {
   public:
      void d();
}

class P1 : public T {
   ;
}

class P2 : public T {
   ;
}

class C : public P1, public P2 {
   // must use either P1::d() or P2::d() to disambiguate the call
}

In this example there is only one d() method, in the class T. However, both P1 and P2 inherit d() from T, meaning that each also has a d() method. This means that C is now unsure of which inherited method should be used. We can again solve this problem by explicitly using the scope resolution operator. Another way of dealing with this problem is to use virtual inheritance, but we won’t be going into that for this module.

<!-- Slide number: 19 -->
# Allocation and Deallocation of Objects
From where are objects allocated?
If objects behave like ADTs
Can be allocated from the run-time stack, AND
Can be explicitly created on the heap (e.g. via new)
If objects are all heap-dynamic
Uniform use through pointer or reference variable
Simplifies assignment (just a reference copy)
Dereferencing can be implicit
If objects are stack dynamic
A problem with subtypes: Assume B is subtype of A
Truncation if: A aVar; B bVar; aVar = bVar;
Is heap deallocation explicit or implicit?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:
Truncation is often referred to as object slicing. Consider the following example in C++:

class A {
   public:
      int a1;
}

class B : public A {
   public:
      int b1;
}

int main() {
   A myA;
   B myB;
   myA = myB;
}

Note that we are using object variables, not pointers or references. Object variables are allocated on the stack, not the heap. In this case the assignment is valid, because B is a subtype of A. However, myA only has memory allocated to store its member variables. Therefore, when myB is assigned to myA, the b1 member variable is not copied, thus truncating the object. The a1 member variable is successfully copied, however.

Explicit heap deallocation happens when a keyword/reserved word (like “delete” in C++) is used to deallocate objects. Implicit heap deallocation happens if the language provides a garbage collector that automatically releases objects that are no longer needed.

<!-- Slide number: 20 -->
# Dynamic and Static Binding
Should every binding of a message to a method be dynamic?
If none are, lose advantages of dynamic binding
If all are, it is inefficient
Allow the programmer to specify?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-20

### Notes:
Smalltalk uses only dynamic binding. What does this tell us in terms of the language evaluation criteria?

C++ allows the user to specify by using either virtual or non-virtual member functions.

<!-- Slide number: 21 -->
# Nested Classes
If a new class is needed by only one class
No reason for it to be visible to other classes
Can new class be nested in the class that uses it?
Can the new class be nested inside a subprogram?
Other issue
Visibility of members
Of the nesting class to the nested class
Of the nested class to the nesting class
Copyright © 2023 Addison-Wesley. All rights reserved.
1-21

### Notes:

<!-- Slide number: 22 -->
# Initialization of Objects
Are objects initialized to values when they are created?
Explicit initialization
Implicit initialization

How are parent class members initialized when a subclass object is created?
Explicit initialization
Implicit initialization
Copyright © 2023 Addison-Wesley. All rights reserved.
1-22

### Notes:
Object initialisation is typically dealt with by means of constructors (Ruby is a notable exception). If some sort of default constructor mechanism is built in to the language, the object initialisation can be implicit. For implicit initialisation it is typically necessary to use modifiers (setter methods) to change the implicitly initialised member variable values.

Of more interest is the parent class initialisation. Explicit initialisation in this context requires that a derived class constructor call a parent class constructor. If some default mechanism is used, there is usually an assumption that the default constructor of the parent class is called by a derived class constructor.

<!-- Slide number: 23 -->
# Support for OOP in Smalltalk
Smalltalk is a pure OOP language
Basis of most OOP as we know it
Everything is an object
No characteristics of imperative languages
All objects are allocated from the heap
Slow (why?)
All computation is uniform
Objects sending messages to objects
Slow (why?)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-23

### Notes:
Try to answer the questions on this slide.

Consider the fact that everything (including all the “primitive” types) is an object in Smalltalk, and that all operations are messages between objects. How does this affect the language evaluation criteria?

<!-- Slide number: 24 -->
# Support for OOP in Smalltalk
Smalltalk is a pure OOP language
Object access
By means of typeless reference variables
References are implicitly dereferenced
All deallocation is implicit
Uses a garbage collector
Can be slow, depending on implementation
Copyright © 2023 Addison-Wesley. All rights reserved.
1-24

### Notes:
Smalltalk doesn’t use anything other than object references, which means that no object variables exist, and therefore object slicing is impossible.

Garbage collection is typically slow because the programmer can’t control when it clears memory (even in Java, one can use a method call to suggest that the garbage collector clean up memory, but it isn’t guaranteed that it will at that moment).

<!-- Slide number: 25 -->
# Support for OOP in Smalltalk
Inheritance
A Smalltalk subclass inherits from its superclass
All instance variables & methods, and class methods
All subclasses are subtypes
Nothing defined in parent class can be removed
Simple inheritance model
Methods with same name and protocol as a parent method override and hide the parent method
Access to overridden methods using super
No multiple inheritance
Copyright © 2023 Addison-Wesley. All rights reserved.
1-25

### Notes:
Inheritance in Smalltalk also follows only one approach (compare this to how C++ handles different types of inheritance). What does this mean for the language evaluation criteria?

How does the lack of multiple inheritance affect the language evaluation criteria?

<!-- Slide number: 26 -->
# Support for OOP in Smalltalk
Dynamic binding
All binding of messages to methods is dynamic
Search for the correct method
Start in the object to which the message is sent
Continue up the class hierarchy, to Object
Another factor making Smalltalk slow
Copyright © 2012 Addison-Wesley. All rights reserved.
1-26

### Notes:
Consider the fact that all message binding is dynamic in Smalltalk. How does this affect the language evaluation criteria?
