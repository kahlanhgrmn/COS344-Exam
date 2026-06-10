<!-- Slide number: 1 -->
# Chapter 12Part 2
Support forObject-Oriented Programming

### Notes:

<!-- Slide number: 2 -->
# Chapter 12 Topics
Support for OOP in C++
Support for OOP in Java
Support for OOP in C#
Support for OOP in Ruby
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Support for OOP in C++
General Characteristics
Evolved from C and SIMULA 67
Among the most widely used OOP languages
Hybrid language
Mixed typing system
Imperative types (structs, unions, etc.)
Object-oriented classes
Allows functions that are not part of a class
Procedural and OO programming supported
Efficient execution
Smalltalk is ~10 times slower
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:

<!-- Slide number: 4 -->
# Inheritance in C++
Inheritance
Class need not be a subclass of any class
Access controls for members are
Public
Member is visible to subclasses and clients
Private
Member is visible only to the class and friends
Protected
Member is visible to the class and in subclasses
Member is not visible to clients
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:

<!-- Slide number: 5 -->
# Inheritance in C++
Inheritance can also have access controls
Defines potential changes in the access controls of inherited members within subclasses
Two types
Public derivation
Inherited public and protected members remain public and protected in subclasses
Private derivation
Inherited public and protected members become private in subclasses
Disallows subclasses from being subtypes
When would this be useful?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:
Don’t confuse the concept of public and private inheritance with the concept of public and private members.

Public derivation is the most commonly used, and works in the most natural way. Public subclasses are always subtypes of their parent classes.

If class B privately inherits from A, everything that is public and protected in A is inherited by B, but is made private in B. Can you explain why this means that B is not a subtype of A? Can you think of a situation in which this would be useful?

There is also protected inheritance (not discussed in the textbook), which does the same kind of thing as private inheritance, but makes the inherited members protected (instead of private). Consider how the effect of protected inheritance is different to private inheritance.

<!-- Slide number: 6 -->
# Inheritance Example in C++
class base_class {
   private:
      int a;
      float x;
   protected:
      int b;
      float y;
   public:
     int c;
     float z;
};

class subclass_1 : public base_class { ... };
// Here, b and y are protected and c and z are public

class subclass_2 : private base_class { ... };
// Here, b, y, c, and z are private, and no derived class
// of subclass_2 has access to any member of base_class
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:

<!-- Slide number: 7 -->
# Re-Exportation in C++
Members private due to private derivation
Can be re-exported
Makes the member visible
As if it had been inherited publicly
Use the scope resolution operator (::)

      class subclass_3 : private base_class {
         using base_class :: c;
         ...
      }
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:
The code example assumes that base_class has a member named c. sub_class_3 then inherits privately from base_class, but chooses to make it available again by explicitly re-exporting it.

Note that the textbook doesn’t use the using reserved word. The approach used by the textbook works, but is deprecated in favour of what’s on this slide.

<!-- Slide number: 8 -->
# Multiple Inheritance in C++
Multiple inheritance is supported

class Thread { ... }
class Drawing { ... }
class DrawThread : public Thread, public Drawing { ... }

If there are 2 inherited members with same name
Reference either with scope resolution operator (::)
For example, Drawing::display() in DrawThread

Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:

<!-- Slide number: 9 -->
# Message Binding in C++
Programmer decides at class design time
Static binding for methods by default
Faster than dynamic binding
Dynamic binding
A method can be defined to be virtual
It can be called through polymorphic variables
Messages will be dynamically bound to method
A pure virtual function has no definition at all
A class with at least one pure virtual function
An abstract class
Cannot be instantiated
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:

<!-- Slide number: 10 -->
# Message Binding in C++
class Shape {
   public:
      virtual void draw() = 0;
   ...
};

class Circle : public Shape {
   public:
      void draw() { ... }
   ...
};

class Rectangle : public Shape {
   public:
      void draw() { ... }
   ...
};
Circle *circ = new Circle;
Rectangle *rect = new Rectangle;
Shape *ptr_shape;

ptr_shape = circ;  // Points to a Circle

ptr_shape->draw(); // Dynamically
                   // bound to draw()                   // in Circle

rect->draw();      // Statically bound
                   // to draw() in
                   // Rectangle
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

<!-- Slide number: 11 -->
# Message Binding in C++
If objects are allocated from the stack
Assignment to parent variable truncates objects
Message binding is not dynamic

  class Square : public Rectangle {
    public:
      void draw() { ... }
  };

  Rectangle rect;  // Allocates a Rectangle object from the stack
  Square sqr;      // Allocates a Square object from the stack
  rect = sqr;      // Copies data member values from sqr object
  rect.draw();     // Calls the draw from Rectangle
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

<!-- Slide number: 12 -->
# Support for OOP in Java
Close relationship to C++
We focus on the differences between the two
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

<!-- Slide number: 13 -->
# Support for OOP in Java
General Characteristics
All data are objects except the primitive types
Wrapper classes for primitive types, storing a value
All objects
Part of a class hierarchy, with Object at the root
Heap-dynamic (most are allocated with new)
Referenced through reference variables
Memory management through garbage collector
Garbage collector frees memory automatically
As garbage collector about to reclaim object storage
A finalize method implicitly called
When this happens is unpredictable
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:
There are a few cases where Java objects aren’t created using new. These include (amongst others):

When using an array initialiser.
When using a String literal.
When autoboxing and unboxing to create a wrapper for a primitive type.

<!-- Slide number: 14 -->
# Support for OOP in Java
Inheritance
Only single inheritance is supported
An interface
Like an abstract class
Provides some benefits of multiple inheritance
Only method declarations and named constants

		    public interface Comparable <T> {
			    public int comparedTo (T b);
		    }

Simpler than C++ multiple inheritance (why?)
Methods that are final cannot be overriden
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:
What effect does Java’s use of only single inheritance have in terms of the language evaluation criteria (particularly in comparison to C++)?

<!-- Slide number: 15 -->
# Support for OOP in Java
Dynamic Binding
All messages are dynamically bound to methods
Static binding only in specific circumstances
When method cannot be overridden
The method is final
The method is private
The method is static (i.e. a class method)
In these cases dynamic binding serves no purpose
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:
This means that Java uses dynamic message binding in all cases, except where static message binding is guaranteed to work. What tradeoffs are apparent here, in terms of the language evaluation criteria, when compared to C++ and Smalltalk?

<!-- Slide number: 16 -->
# Support for OOP in Java
Nested classes in another class
Nesting class can access all nested class members
Nonstatic nested class, or inner class
Can access all members of its nesting class
Static nested class
Can’t access members of nesting class
Nested classes in methods of a nesting class
Called a local nested class
No class access specifier (private or public)
Members visible only in nesting method
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:
Nested classes can be anonymous. Anonymous classes are classes without names, which are only meant to be used once. They are defined to inherit from an existing class, or to implement an existing interface, and then add their own functionality. For example, if we assume that the following interface is defined:

interface HelloWorld {
   public void greet();
   public void greetSomeone(String someone);
}

Then we can create an anonymous class that implements the interface, like this:

HelloWorld frenchGreeting = new HelloWorld() {

   String name = "tout le monde";

   public void greet() {
      greetSomeone("tout le monde");
   }

   public void greetSomeone(String someone) {
      name = someone;
      System.out.println("Salut " + name);
   }
};

We can then directly use the variable frenchGreeting. Note that frenchGreeting isn’t an object of a named class, but rather an object of an unnamed class that implements the HelloWorld interface. We just have to use this class once, so there’s no need to create an entirely separate class that has to be compiled into its own bytecode file.

<!-- Slide number: 17 -->
# Support for OOP in C#
General characteristics
Support for OOP is similar to Java
Includes both class and struct constructs
Classes are similar to Java’s classes
A struct is less powerful than in C++
A stack-dynamic construct
No inheritance
No members referencing the struct itself
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:
In C++, a struct is very similar to a class. The only difference is that the default access modifier is private in a class, and public in a struct. In C# structs and classes are quite different, with structs intended for the very limited purpose of only storing data in a single syntactic unit, while classes are meant for proper OO programming.

<!-- Slide number: 18 -->
# Support for OOP in C#
Inheritance
Uses the syntax of C++ for defining classes
Overriding a method inherited from parent class
Mark the overriding method’s definition with new
Advantages of this approach?
Disadvantage of this approach?
Parent class version called explicitly with base prefix
base.Draw()
Also supports interfaces, like in Java
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:
Try to answer the question on the slide.

C# does not support multiple inheritance. However, interfaces provide some of the benefits of multiple inheritance, in the same way they do in Java.

<!-- Slide number: 19 -->
# Support for OOP in C#
Dynamic binding
For dynamic binding of messages to methods
The base class method is marked virtual
Implemented virtual methods marked override
Advantages of this approach?
Disadvantage of this approach?
Abstract methods are marked abstract
All classes are derived from a root Object class
Copyright © 2023 Addison-Wesley. All rights reserved.
1-19

### Notes:
What is the effect of marking implemented virtual methods with the override keyword, in terms of the language evaluation criteria?

Compare the C# approach of marking abstract methods using an abstract keyword to the C++ approach (marking the abstract method as virtual, and adding “= 0” after it), in terms of the language evaluation criteria.

<!-- Slide number: 20 -->
# Support for OOP in C#
Nested Classes
A class that is directly nested in a nesting class
Behaves like a Java static nested class
Thus cannot access members of the nesting class
No nested classes like the non-static classes of Java
Copyright © 2023 Addison-Wesley. All rights reserved.
1-20

### Notes:

<!-- Slide number: 21 -->
# Support for OOP in Ruby
General Characteristics
Everything is an object
All computation is through message passing
Class definitions are executable
Secondary definitions can add members
Method definitions are also executable
Method definition can be changed at runtime
All variables are typeless object references
Copyright © 2023 Addison-Wesley. All rights reserved.
1-21

### Notes:
Ruby has a similar approach to Smalltalk, in the sense that everything is represented as an object, and all operations are performed by means of message passing.

<!-- Slide number: 22 -->
# Support for OOP in Ruby
General Characteristics
Access control is different for data and methods
All data is private, and this cannot change
Methods can be either public, private, or protected
Method access is checked at runtime (result?)
Getters and setters can be defined by shortcuts

Copyright © 2023 Addison-Wesley. All rights reserved.
1-22

### Notes:
What are the implications of all data being private in Ruby classes, in terms of the language evaluation criteria?

Regarding getter and setter shortcuts, consider the following example:

class Person
   attr_reader :age
   ...
end

Here an accessor is automatically created for the age member variable. Also provided by Ruby are attr_writer, which creates a setter, and attr_accessor, which creates both a getter and a setter. This kind of notation is really just a shortcut for explicitly defining getters and setters.

<!-- Slide number: 23 -->
# Support for OOP in Ruby
Inheritance
Ruby doesn’t support true multiple inheritance
Parent class access control can change in child
So subclasses are not necessarily subtypes
Does not support abstract classes
Copyright © 2023 Addison-Wesley. All rights reserved.
1-23

### Notes:

<!-- Slide number: 24 -->
# Support for OOP in Ruby
Dynamic Binding
All variables are typeless object references
These references are polymorphic
Copyright © 2023 Addison-Wesley. All rights reserved.
1-24

### Notes:
