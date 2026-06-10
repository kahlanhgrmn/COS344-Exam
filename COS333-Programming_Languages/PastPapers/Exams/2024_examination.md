# COS 333 – Programming Languages
## Examination — 25 June 2024

**Examiner:** Mr W. S. van Heerden | **External Examiner:** Mr Willem H. K. Bester (Stellenbosch)
**Duration:** 3 hours | **Total:** 40 marks | **Questions:** 28

> **Instructions:** Read the questions carefully and answer all questions. This test is closed book. Allowed references: Practical 2 & 3 specifications, MIT/GNU Scheme Reference Manual, SWI-Prolog Reference Manual, and Practical 4 specification.

---

## Question 1 *(1 point)*

There are often trade-offs between the programming language evaluation criteria. Select the statement that most correctly describes a likely **trade-off when readability improves**.

- [ ] The cost of execution becomes worse.
- [ ] The cost of maintenance becomes worse.
- [ ] The cost of implementation becomes worse.
- [ ] Reliability becomes worse.

---

## Question 2 *(1 point)*

An additional evaluation criterion not heavily focused on in this course is **generality**. Select the programming language that has the **best generality**.

- [ ] Fortran I
- [ ] ALGOL 60
- [ ] SIMULA 67
- [ ] PL/I

---

## Question 3 *(1 point)*

Consider the following statements about **Pascal and C**, and select the most correct.

- [ ] Pascal is more readable than C.
- [ ] Pascal is more writable than C.
- [ ] Pascal is less reliable than C.
- [ ] Pascal has a higher cost of maintenance than C.

---

## Question 4 *(1 point)*

An additional evaluation criterion not heavily focused on in this course is **portability**. Select the programming language that is the **most portable**.

- [ ] Fortran 90
- [ ] C++
- [ ] PL/I
- [ ] JavaScript

---

## Question 5 *(5 points)*

Write a Scheme function named `removePositiveOddValues`, which receives one parameter: a simple list containing only numeric atoms. The function should yield (not print) a list containing the values in the parameter list, in their original order, with all **positive odd values removed**.

*Examples:*
```scheme
(removePositiveOddValues '(3 9))
; => ()   (all values are positive odd)

(removePositiveOddValues '(-5 3 0 5 9))
; => (-5 0)   (3, 5, 9 are positive odd and are removed)
```

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

## Question 6 *(5 points)*

Write a Prolog proposition called `doublePositives(L1, L2)`, which succeeds if L2 is a list containing all the elements in L1 in their original order, with every **positive value doubled** and every **non-positive value unchanged**.

*Examples:*
```prolog
?- doublePositives([-4, -9], X).
% X = [-4, -9]

?- doublePositives([-3, 6, 7, -1, -5], X).
% X = [-3, 12, 14, -1, -5]
```

*Hint: Comparison operators (`<`, `=<`, `>`, `>=`) can be used as terms in Prolog. Multiplication is represented by `*`.*

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, and built-in predicates from the textbook/slides and hints. Do **not** use if-then, if-then-else, or complex system predicates.

Submit file `s99999999.pl` to slot **"Examination: Prolog Proposition"**.

**Did you submit?**
- [ ] Yes
- [ ] No

---

## Question 7 *(1 point)*

Binding can occur at different times. Select the option that most correctly describes the **binding time** of a standard 32-bit signed integer type in a statically typed language to either a sign-and-magnitude or two's complement representation.

- [ ] Language design time
- [ ] Language implementation time
- [ ] Compile time
- [ ] Load time
- [ ] Runtime

---

## Question 8 *(1 point)*

Consider the following program code in C# (line numbers for reference):

```csharp
1. {
2.    int y;
3.    {
4.       int x = 5;
5.    }
6.    int x = 2;
7. }
```

Select the most correct statement.

- [ ] The provided program code does not compile because the variable `y` is not initialised.
- [ ] The provided program code does not compile because the variable `x` on line 4 hides the variable `x` on line 6.
- [ ] The provided program code does not compile because the variable `x` on line 6 hides the variable `x` on line 4.
- [ ] The provided program code compiles and runs successfully.

---

## Question 9 *(1 point)*

Consider the following statements about **character string types** in programming languages, and select the most correct.

- [ ] In programming languages that represent character strings using only classes, character strings are always mutable.
- [ ] In programming languages that represent character strings using only classes, character strings are always immutable.
- [ ] Limited dynamic length strings have a higher overall hardware resource cost than static length strings, and a lower overall hardware resource cost than dynamic length strings.
- [ ] C supports character strings as a primitive type.

---

## Question 10 *(1 point)*

Consider the following statements about **unions**, and select the most correct.

- [ ] Unions are closely related to classes in object-oriented programming, but are more limited in terms of functionality.
- [ ] Discriminated unions are more memory efficient than free unions.
- [ ] Unions can be used as a mechanism for returning multiple values from a subprogram.
- [ ] Unions are used when memory cost is of great concern.

---

## Question 11 *(1 point)*

Consider the following statements about **arithmetic operations in Scheme**, and select the most correct.

- [ ] The order in which arithmetic operations are evaluated in Scheme is unambiguously determined based on clear precedence levels and associativity rules.
- [ ] The order in which arithmetic operations are evaluated in Scheme is unambiguously determined based on function and parameter evaluation.
- [ ] The order in which arithmetic operations are evaluated in Scheme is unambiguously determined because all operators have the same precedence level and associate from left to right.
- [ ] The order in which arithmetic operations are evaluated in Scheme is ambiguous because function parameters are evaluated in no particular order.

---

## Question 12 *(1 point)*

Consider the following statements about **expressions in Ada**, and select the most correct.

- [ ] The lack of coercions in Ada makes the language more readable.
- [ ] The lack of coercions in Ada makes the language less reliable.
- [ ] The common use of coercions in Ada makes the language more writable.
- [ ] The common use of coercions in Ada makes the language less reliable.

---

## Question 13 *(1 point)*

Consider the following program code in a hypothetical programming language:

```
int count = 5
double result = 0.0

while ((count > 0) and (result = (10.0 / count))) {
   print result
   count = count - 1
}
```

Assume C-like syntax, assignment as an expression, `and` for logical AND, and integers are interpreted as Boolean values like in C. Select the most correct statement.

- [ ] The provided program code produces an error regardless of whether the logical `and` is short-circuit evaluated or not.
- [ ] The provided program code produces an error if the logical `and` is short-circuit evaluated.
- [ ] The provided program code produces an error if the logical `and` is **not** short-circuit evaluated.
- [ ] The provided program code produces no error regardless of whether the logical `and` is short-circuit evaluated or not.

---

## Question 14 *(1 point)*

Consider the following statements about **unary assignment operators**, and select the most correct.

- [ ] Unary assignment operators reduce readability, if they are overloaded to provide prefix and postfix versions.
- [ ] Unary assignment operators reduce writability, if they are overloaded to provide prefix and postfix versions.
- [ ] Unary assignment operators reduce the execution cost of a programming language.
- [ ] Unary assignment operators are essential within a programming language.

---

## Question 15 *(2 points)*

Select **only** the statements that are true about **counter-controlled loops**. *(Incorrectly selected options will be penalised.)*

- [ ] Counter-controlled loops are required in order to implement any flowchart-represented algorithm.
- [ ] Counter-controlled loops in Python are more reliable than counter-controlled loops in C.
- [ ] Counter-controlled loops in C are more readable than counter-controlled loops in Java.
- [ ] Counter-controlled loops are not directly supported in purely functional programming languages.

---

## Question 16 *(2 points)*

Select **only** the correct statements about **disambiguating nested selection statements**. *(Incorrectly selected options will be penalised.)*

- [ ] Python's approach to disambiguating nested selection statements is less readable than Java's approach.
- [ ] Python's approach to disambiguating nested selection statements is less reliable than Java's approach.
- [ ] Ruby and Perl use very similar approaches to disambiguating nested selection statements, but Perl's approach is more writable than Ruby's approach.
- [ ] Python and Ruby use very similar approaches to disambiguating nested selection statements, but Python's approach is more writable than Ruby's approach.

---

## Question 17 *(1 point)*

Consider the following program code in a hypothetical programming language that supports **guarded commands**:

```
var myVal = 2

do (myVal < 0) -> print("A ")
                  myVal = 1
[] (myVal > 0) -> print("B ")
                  myVal = myVal - 1
od
```

Provide the **output** of the program. If the program produces no output, write `Nothing`. If there is a compile-time error, write `Compilation error`. If there is a runtime error, write `Runtime error` at the point where it occurs. *(Note: there is a single space at the end of each print output.)*

**Answer:** _______________

---

## Question 18 *(1 point)*

Consider the following statements about **subprograms defined outside a class definition**, and select the most correct.

- [ ] Ruby subprograms defined outside a class definition are more writable than C++ subprograms defined outside a class definition.
- [ ] Ruby subprograms defined outside a class definition are less writable than C++ subprograms defined outside a class definition.
- [ ] Ruby subprograms defined outside a class definition are more orthogonal than C++ subprograms defined outside a class definition.
- [ ] Ruby subprograms defined outside a class definition behave in exactly the same way as C++ subprograms defined outside a class definition.

---

## Question 19 *(1 point)*

Consider the following statements about **procedures and functions**, and select the most correct.

- [ ] A procedure can produce a result if all its parameters use pass-by-value semantics.
- [ ] A procedure is guaranteed to produce no side effect if it produces a result.
- [ ] A function is guaranteed to produce a side effect if it produces a result.
- [ ] A procedure can more easily produce multiple results than a function can.

---

## Question 20 *(1 point)*

Consider the following program code in a hypothetical programming language:

```
doSomething(int first, int second) {
   first = 2
   print(first)
   print(" ")
   print(second)
}
void main() {
   int val1 = 5
   int val2 = val1 + 1
   foo(val1, val2)
}
```

Provide the **output** of the program if the language uses **pass-by-name** for all parameter passing. If an error occurs, write `Error`. *(Note: the second `print` call outputs a single space.)*

**Answer:** _______________

---

## Question 21 *(1 point)*

Consider the following program code in a hypothetical programming language:

```
var A = 2

main() {
   var A = 5
   call sub1(sub2)
}

sub1(param) {
   var A = 3
   call param()
}

sub2() {
   print(A)
}
```

Assume subprograms can be passed as parameters, execution starts with `main`. Provide the **output** if **deep binding** is used to determine the referencing environment of the passed subprogram, but the language uses **dynamic scoping**. If an error occurs, write `Error`.

**Answer:** _______________

---

## Question 22 *(1 point)*

Consider the following program code in C#:

```csharp
public static void doSomething<T>(T p1, T p2) {
   Console.WriteLine(p1 + " " + p2);
}
```

Assume the following calls are made:

```csharp
Program.doSomething(5, 2);
Program.doSomething(false, true);
```

Select the most correct statement about the use of the `doSomething` method.

- [ ] One version of the `doSomething` method is created at compile time, and is used with `int` and `bool` parameters.
- [ ] Two versions of the `doSomething` method are created at compile time. One is used with `int` parameters, while the other is used with `bool` parameters.
- [ ] One version of the `doSomething` method is created at runtime, and is used with `Object` parameters.
- [ ] Two versions of the `doSomething` method are created at runtime. One is used with `int` parameters, while the other is used with `bool` parameters.

---

## Question 23 *(1 point)*

Consider the following program code in a hypothetical programming language that supports **coroutines**:

```
main() {
   resume first
}

coroutine first {
   print("X ")
   resume second
   print("Y ")
}

coroutine second() {
   print("A ")
   resume first
   print("B ")
}
```

Assume execution starts with `main`. Provide the **output** of the program. If an error occurs, write `Error`. *(Note: there is a single space at the end of each print output.)*

**Answer:** _______________

---

## Question 24 *(2 points)*

Abstract data types (ADTs) aim to hide the representations of ADT objects from clients. Select **only** the correct C++ features that **detract from the effectiveness of ADT representation hiding**. *(Incorrectly selected options will be penalised.)*

- [ ] The existence of friend functions and friend classes.
- [ ] The fact that C++ supports stand-alone functions that are not part of a class.
- [ ] The fact that C++ requires that classes and member function definitions must appear in the same file.
- [ ] The fact that all class data members must appear in header files.

---

## Question 25 *(1 point)*

Consider the following statements about **ADTs in Ruby**, and select the most correct.

- [ ] Instance and class variable names are more readable in Ruby than they are in Java.
- [ ] Ruby supports multiple constructors, each of which can be implicitly called when `new` is used with the appropriate class name and parameters.
- [ ] It is impossible to implement the functionality of multiple constructors in Ruby.
- [ ] The interface of a Ruby ADT is very reliable.

---

## Question 26 *(1 point)*

Imagine a hypothetical programming language in which a subclass can inherit a public method from a parent class and **change its access control to private or protected**. Select the most correct statement.

- [ ] In the hypothetical programming language, dynamic binding is less efficient.
- [ ] In the hypothetical programming language, dynamic binding is impossible.
- [ ] In the hypothetical programming language, subclasses are subtypes.
- [ ] In the hypothetical programming language, subclasses are not subtypes.

---

## Question 27 *(2 points)*

Select **only** the approaches that make **Smalltalk more orthogonal than Java**. *(Incorrectly selected options will be penalised.)*

- [ ] The difference in approach to the exclusivity of objects in Smalltalk and Java.
- [ ] The difference in approach to dynamic and static binding in Smalltalk and Java.
- [ ] The difference in approach to subclasses and subtypes in Smalltalk and Java.
- [ ] The difference in approach to object deallocation in Smalltalk and Java.

---

## Question 28 *(1 point)*

Consider the following statements about **object-oriented programming in C++ and C#**, and select the most correct.

- [ ] C++ provides worse support for multiple inheritance than C# does.
- [ ] C++ provides less writability in terms of nested classes than C# does.
- [ ] C++ uses a more orthogonal approach to object-oriented programming than C# does.
- [ ] C++ provides a more readable approach to dynamic message binding than C# does.
