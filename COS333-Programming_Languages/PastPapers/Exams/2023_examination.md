# COS 333 – Programming Languages
## Examination — 14 November 2023

**Examiner:** Mr W. S. van Heerden | **External Examiner:** Prof A. B. van der Merwe (Stellenbosch)
**Duration:** 3 hours | **Total:** 40 marks | **Questions:** 29

> **Instructions:** Read the questions carefully and answer all questions. This test is closed book. Allowed references: MIT/GNU Scheme Reference Manual and SWI-Prolog Reference Manual.

---

## Question 1 *(1 point)*

Various factors can influence programming language design. Consider the following programming language design influences, and select the one that had its **earliest impact on the design of SIMULA 67**.

- [ ] Computer architecture.
- [ ] Programmer efficiency becoming more important than machine efficiency.
- [ ] The move from process oriented programming to data oriented programming.
- [ ] The move to object-oriented programming.

---

## Question 2 *(2 points)*

Consider the following programming language evaluation criteria, and select **only** those that benefit from the use of a **hybrid implementation system**. *(Incorrectly selected options will be penalised.)*

- [ ] Readability.
- [ ] Writability.
- [ ] Cost.
- [ ] Portability.

---

## Question 3 *(1 point)*

Consider only the syntax used by **Plankalkül** for an assignment using arrays and subscripts. Consider the following statements, and select the one that is the most correct.

- [ ] The syntax had poor readability.
- [ ] The syntax had poor writability.
- [ ] The syntax had poor reliability.
- [ ] The syntax had poor execution cost.

---

## Question 4 *(1 point)*

The language specification of **ALGOL 60** lacked support for I/O operations. Consider the following statements, and select the one that most correctly describes a consequence this lack of support had on a main design goal of ALGOL 60.

- [ ] The reliability of ALGOL 60 suffered.
- [ ] The execution cost of ALGOL 60 suffered.
- [ ] The execution cost of ALGOL 60 improved.
- [ ] The machine independence of ALGOL 60 suffered.

---

## Question 5 *(1 point)*

Consider the following statements about **Lua**, and select the one that is the most correct.

- [ ] Lua uses full compilation for the sake of reduced execution cost.
- [ ] Lua requires heap allocated variables to be explicitly deallocated.
- [ ] Lua supports functional programming.
- [ ] Lua is a fully featured object-oriented programming language.

---

## Question 6 *(5 points)*

Write a Scheme function named `doublePositives`, which receives one parameter: a simple list containing only numeric atoms. The function should yield (not print) a list containing the same values as the parameter list, but with **positive values doubled**. Negative and zero values remain unchanged.

*Examples:*
```scheme
(doublePositives '())
; => ()   (no elements in the parameter list)

(doublePositives '(2 -4 7 -3))
; => (4 -4 14 -3)   (2→4, 7→14; -4 and -3 are unchanged)
```

> *Note: Start your program with `#lang racket`.*

**Allowed built-in functions:**
- **Function construction:** `lambda`, `define`
- **Binding:** `let`
- **Arithmetic:** `+`, `-`, `*`, `/`, `abs`, `sqrt`, `remainder`, `modulo`, `min`, `max`
- **Boolean values:** `#t`, `#f`
- **Equality predicates:** `=`, `>`, `<`, `>=`, `<=`, `even?`, `odd?`, `zero?`, `negative?`, `eqv?`, `eq?`
- **Logical predicates:** `and`, `or`, `not`
- **List predicates:** `list?`, `null?`
- **Conditionals:** `if`, `cond`, `else`
- **Quoting:** `quote`, `'`
- **List manipulation:** `list`, `car`, `cdr`, `cons`
- **I/O:** `display`, `printf`, `newline`, `read`

Submit file `s99999999.scm` to slot **"Examination: Scheme Function"**.

**Did you submit?**
- [ ] Yes
- [ ] No

---

## Question 7 *(5 points)*

Write a Prolog proposition called `doubleNonMatching(L1, X, L2)`, which succeeds if the list L2 contains the same values as the list L1, without their order being modified, but with all **values that do not match X doubled**. All values that do match X should remain unchanged.

*Examples:*
```prolog
?- doubleNonMatching([], 2, X).
% X = []

?- doubleNonMatching([3, 2, 4, 4, 2], 2, X).
% X = [6, 2, 8, 8, 2]
```

*Hint: In Prolog arithmetic, `*` represents multiplication.*

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, and built-in predicates from the textbook/slides. Do **not** use if-then, if-then-else, or complex system predicates.

Submit file `s99999999.pl` to slot **"Examination: Prolog Proposition"**.

**Did you submit?**
- [ ] Yes
- [ ] No

---

## Question 8 *(1 point)*

Consider the following program code in a hypothetical programming language:

```
void main() {
   var myVariable = "Test"
   print(myVariable)

   var anotherVariable = 5
   myVariable = anotherVariable * 2
   print(myVariable)
}
```

Select the option that most correctly describes the **category of `myVariable`** in terms of lifetime.

- [ ] Static variable.
- [ ] Stack-dynamic variable.
- [ ] Explicit heap-dynamic variable.
- [ ] Implicit heap-dynamic variable.

---

## Question 9 *(1 point)*

Consider the following two subprograms in a hypothetical programming language:

```
void f1() {
   constant LENGTH = 3
   var firstArray[LENGTH] = {6, 8, 7}
}
void f2() {
   constant INPUT_LENGTH
   readInteger(INPUT_LENGTH)
   var secondArray[INPUT_LENGTH]
}
```

The special word `constant` is the only way to declare a named constant. Subprogram `f1` is legal, while subprogram `f2` is illegal and will not compile. Name the **type of named constants** supported in this programming language.

**Answer:** _______________

---

## Question 10 *(1 point)*

Consider the following statements about **list comprehensions in Python**, and select the one that is the most correct.

- [ ] List comprehensions increase the readability of Python.
- [ ] List comprehensions increase the writability of Python.
- [ ] List comprehensions improve the reliability of Python.
- [ ] List comprehensions reduce the execution cost of Python.

---

## Question 11 *(1 point)*

C++ is not considered a very strongly typed programming language. Consider the following reasons, and select the one that most correctly describes a reason contributing to the **weak typing of C++**.

- [ ] The way in which C++ supports pointers.
- [ ] The fact that C++ supports only discriminated unions.
- [ ] The fact that C++ performs no parameter type checking.
- [ ] The fact that C++ does not perform index range checking in arrays.

---

## Question 12 *(1 point)*

Both Ruby and Java are object-oriented programming languages. Consider the following statements about **arithmetic operators in Ruby and Java**, and select the one that is the most correct.

- [ ] Arithmetic operators in Ruby are less flexible than arithmetic operators in Java.
- [ ] Arithmetic operators in Ruby are always as reliable as arithmetic operators in Java.
- [ ] Arithmetic operators in Ruby are implemented in a more orthogonal way than arithmetic operators in Java.
- [ ] Arithmetic operators in Ruby have a lower execution cost than arithmetic operators in Java.

---

## Question 13 *(1 point)*

Consider the following statements about the **unary `*` operator in C++**, and select the one that is the most correct.

- [ ] The unary `*` operator is poorly designed, because it is overloaded to produce very different results depending on the context in which it is used.
- [ ] The unary `*` operator is poorly designed, because C++ could have been designed to avoid its use while leaving the language's flexibility and conciseness unchanged.
- [ ] The unary `*` operator is well designed, because it is not overloaded.
- [ ] The unary `*` operator is well designed, because it cannot be confused with any non-unary operators.

---

## Question 14 *(1 point)*

Consider the following statements about **conditional targets**, and select the one that is the most correct.

- [ ] Conditional targets improve the readability of assignments.
- [ ] Conditional targets improve the writability of assignments.
- [ ] Conditional targets improve the reliability of assignments.
- [ ] Conditional targets decrease the cost of execution of assignments.

---

## Question 15 *(1 point)*

Consider the following statements about **mixed-mode assignments in Ada and C**, and select the one that is the most correct.

- [ ] Mixed-mode assignments in Ada are less readable than mixed-mode assignments in C.
- [ ] Mixed-mode assignments in Ada are less writable than mixed-mode assignments in C.
- [ ] Mixed-mode assignments in Ada are less reliable than mixed-mode assignments in C.
- [ ] Mixed-mode assignments in Ada have a higher execution cost than mixed-mode assignments in C.

---

## Question 16 *(1 point)*

Consider the following statements about the **approaches used by Ruby and Perl to disambiguate nested selectors**, and select the one that is the most correct.

- [ ] Ruby uses a less reliable approach than Perl.
- [ ] Ruby uses a less readable approach than Perl.
- [ ] Ruby uses a less writable approach than Perl.
- [ ] Ruby uses a more writable approach than Perl.

---

## Question 17 *(1 point)*

Consider the following statements about **selector expressions used in assignments**, and select the one that is the most correct.

- [ ] Readability is improved if the `else` clause is left out of a selector expression used in an assignment.
- [ ] Readability is reduced if the `else` clause is left out of a selector expression used in an assignment.
- [ ] Reliability is improved if the `else` clause is left out of a selector expression used in an assignment.
- [ ] The programming language evaluation criteria are not affected if the `else` clause is left out of a selector expression used in an assignment.

---

## Question 18 *(1 point)*

Consider the following statements about **counter-controlled loops in Ada and C**, and select the one that is the most correct.

- [ ] Counter-controlled loops are more writable in Ada than in C.
- [ ] Counter-controlled loops are less readable in Ada than in C.
- [ ] Counter-controlled loops are more reliable in Ada than in C.
- [ ] Counter-controlled loops have a higher cost of execution in Ada than in C.

---

## Question 19 *(1 point)*

Consider the following program code in Ruby:

```ruby
def doSomething()
   count = 1
   value = 1
   while count <= 3
      value = value * 2
      count = count + 1
      yield value
   end
end
```

Provide the **output** if the `doSomething` subprogram is used with a block that has a single formal parameter and prints it followed by a single space.

**Answer:** _______________

---

## Question 20 *(1 point)*

Consider the following statements about **default values for subprogram parameters**, and select the one that is the most correct.

- [ ] There is no way for a default parameter value to appear anywhere but the beginning of a subprogram's list of parameters.
- [ ] There is no way for a default parameter value to appear anywhere but the end of a subprogram's list of parameters.
- [ ] It is possible for a default parameter to appear anywhere in a subprogram's list of parameters if positional parameters are used.
- [ ] It is possible for a default parameter to appear anywhere in a subprogram's list of parameters if keyword parameters are used.

---

## Question 21 *(1 point)*

Consider the following statements about a **drawback associated with Lua**, and select the one that is the most correct.

- [ ] Anonymous functions in Lua cannot be used after the function's definition.
- [ ] It is easy for a programmer to unintentionally create a stack-dynamic variable in Lua.
- [ ] It is easy for a programmer to unintentionally create a global variable in Lua.
- [ ] Lua does not allow a function to receive a variable number of parameters.

---

## Question 22 *(1 point)*

Consider the following statements about **pass-by-result subprogram parameters**, and select the one that is the most correct.

- [ ] Pass-by-result parameters can only copy a value to the caller.
- [ ] Pass-by-result parameters can only transfer an access path to the caller.
- [ ] Pass-by-result parameters can either copy a value to the caller, or transfer an access path to the caller.
- [ ] Pass-by-result can neither copy a value to the caller, nor transfer an access path to the caller.

---

## Question 23 *(2 points)*

Consider the following program code in a hypothetical programming language:

```
var A = 12
fun sub1() {
   print A
}
fun sub2(param) {
   var A = 35
   call param()
}
fun main() {
   var A = 22
   sub2(sub1)
}
```

Assume the programming language allows subprograms to be passed as parameters, uses **static scoping**, and that execution starts with `main`. Provide the **output** if the following types of binding are used to determine the referencing environment of the passed subprogram.

**Ad-hoc binding:** _______________

**Shallow binding:** _______________

---

## Question 24 *(1 point)*

Consider the following program code in a hypothetical programming language that supports **coroutines**:

```
sub main() {
   resume second
}
coroutine first {
   print "1 "
   resume second
   print "2 "
}
coroutine second {
   print "3 "
   resume first
   print "4 "
}
```

Assume execution starts with `main`. Provide the **output** of the program. If an error occurs, write `Error`. *(Note: there is a single space after each number that is printed.)*

**Answer:** _______________

---

## Question 25 *(1 point)*

Consider the following statements about **properties in C# classes**, and select the one that is the most correct.

- [ ] Properties provide instance variables within a C# class.
- [ ] Properties provide class variables within a C# class.
- [ ] Properties provide a less writable alternative to getters and setters within a C# class, from the perspective of a user of the class.
- [ ] Properties provide a more writable alternative to getters and setters within a C# class, from the perspective of a user of the class.

---

## Question 26 *(1 point)*

Consider the following statements about the **approach used by Java to hide the representation of ADT objects** from the users of these objects, and select the one that is the most correct.

- [ ] The ADT interface is provided in a header file, which the user is allowed to see. The ADT implementation is compiled into a class file, and only the class file is provided to the user.
- [ ] The ADT interface is not provided to the user. The ADT implementation is compiled into a class file, and only the class file is provided to the user.
- [ ] The ADT interface is automatically generated as documentation, which the user is allowed to see. The ADT implementation is compiled into a class file, and only the class file is provided to the user.
- [ ] Java does not hide the representation of ADT objects from the users of these objects.

---

## Question 27 *(1 point)*

Consider the following program code in Java:

```java
public class MyClass<T> {
   private T data;
   public MyClass(T param) {
      data = param;
   }
   public T getData() {
      return data;
   }
}
```

Also assume the following `main` method is provided:

```java
public static void main(String[] args) {
   MyClass<String> a = new MyClass<String>("test");
   Integer myInt = new Integer(12);
   MyClass<Integer> b = new MyClass<Integer>(myInt);
}
```

Identify the **number of versions of `MyClass`** that exist after compile time. Type only the digit.

**Answer:** _______________

---

## Question 28 *(1 point)*

Consider a hypothetical programming language that supports object-oriented programming with **multiple inheritance**. Four classes A, B, C, and D are defined. Classes B and C both inherit only from class A. Class D inherits from both B and C. An **implicit name collision** is possible. Select **only** the implementation details that together result in an implicit name collision (not explicit). *(Incorrectly selected options will be penalised.)*

- [ ] Defining a method named `myMethod` in class A.
- [ ] Defining a method named `myMethod` in class B.
- [ ] Defining a method named `myMethod` in class C.
- [ ] Defining a method named `myMethod` in class D.

---

## Question 29 *(2 points)*

C++ has a lower cost of execution than Smalltalk. Select **only** the factors that contribute to the **lower cost of execution in C++**. *(Incorrectly selected options will be penalised.)*

- [ ] The approach C++ uses in relation to the exclusivity of classes.
- [ ] The approach C++ uses to perform message binding.
- [ ] The fact that C++ supports heap allocated objects.
- [ ] The fact that subclasses are not necessarily subtypes in C++.
