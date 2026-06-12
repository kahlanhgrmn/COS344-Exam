# COS 333 – Programming Languages
## Examination — 15 November 2022

**Examiner:** Mr W. S. van Heerden | **External Examiner:** Prof M. C. du Plessis (NMU)
**Duration:** 3 hours | **Total:** 40 marks | **Questions:** 29

> **Instructions:** Read the questions carefully and answer all questions. This test is closed book. Allowed references: MIT/GNU Scheme Reference Manual and SWI-Prolog Reference Manual.

---

## Question 1 *(1 point)*

For programming languages that are designed for **systems programming** applications, the primary concern is efficiency. Consider the following statements, and select the one that most correctly identifies the **second most important concern** in programming languages designed for systems programming.

- [ ] Portability.
- [ ] Generality.
- [ ] Orthogonality.
- [ ] Reliability.

---

## Question 2 *(1 point)*

Pseudocode languages were interpreted rather than compiled. Consider the following statements, and select the option that most correctly identifies **why these languages were interpreted**.

- [ ] Interpretation offers the advantage of cross-platform compatibility.
- [ ] Interpretation is more reliable in terms of error detection than compilation.
- [ ] Certain operations were not supported in hardware at the time, meaning execution was slow regardless of whether interpretation was used.
- [ ] Interpretation requires less computing resources than compilation does, meaning it worked better on the limited hardware of the time.

---

## Question 3 *(1 point)*

Consider the following statements, and select the option that most correctly describes **Objective-C**.

- [ ] Object-oriented programming in Objective-C is based on C.
- [ ] Object-oriented programming in Objective-C is based on C++.
- [ ] Object-oriented programming in Objective-C is based on Smalltalk.
- [ ] Objective-C does not support object-oriented programming.

---

## Question 4 *(5 points)*

Write a Scheme function named `getPositiveOddValues`, which receives one parameter: a simple list containing only numeric atoms. The function should yield (not print) a list containing only the **positive (non-zero) odd values** contained in the parameter list.

*Examples:*
```scheme
(getPositiveOddValues '())
; => ()   (no elements in the parameter list)

(getPositiveOddValues '(1 2 7 -3 4))
; => (1 7)   (1 and 7 are the only positive odd values; 2 and 4 are positive even; -3 is negative)
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

Submit file `s99999999.scm` to slot **"Exam: Scheme Function"**.

**Did you submit?**
- [ ] Yes
- [ ] No

---

## Question 5 *(5 points)*

Write a Prolog proposition called `stripOccurrences(X, L1, L2)`, which succeeds if the list L2 contains all the elements in the list L1, in order, with **all occurrences of X removed**.

*Examples:*
```prolog
?- stripOccurrences(a, [b, c, d], X).
% X = [b, c, d]

?- stripOccurrences(a, [a, b, a, c, a], X).
% X = [b, c]
```

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, and built-in predicates from the textbook/slides. Do **not** use if-then, if-then-else, or complex system predicates.

Submit file `s99999999.pl` to slot **"Exam: Prolog Proposition"**.

**Did you submit?**
- [ ] Yes
- [ ] No

---

## Question 6 *(1 point)*

Consider the following statements about the **scope and lifetime of static variables**, and select the one that is most correct.

- [ ] The scope of the variable is from the point of the variable declaration until the end of its scope, while the lifetime is from the start of program execution until the end of program execution.
- [ ] The scope of the variable is from the start of program execution until the end of program execution, while the lifetime is from the point of the variable declaration until the end of its scope.
- [ ] The scope and lifetime are both from the point of the variable declaration until the end of its scope.
- [ ] The scope and lifetime are both from the start of program execution until the end of program execution.

---

## Question 7 *(1 point)*

It is possible for pointers to be implicitly dereferenced by a programming language. Consider the following possible **disadvantages associated with implicitly dereferenced pointers**, and select the one that is most correct.

- [ ] Void pointers cannot be used.
- [ ] Pointer arithmetic is disallowed.
- [ ] Pointers cannot be used for indirect addressing.
- [ ] Pointers cannot be used for dynamic memory management.

---

## Question 8 *(1 point)*

Consider the following statements about **operator precedence and associativity in APL**, and select the one that is most correct.

- [ ] Precedence rules in APL are more orthogonal than precedence rules in other programming languages, but associativity rules in APL are less orthogonal than associativity rules in other programming languages.
- [ ] Associativity rules in APL are more orthogonal than associativity rules in other programming languages, but precedence rules in APL are less orthogonal than precedence rules in other programming languages.
- [ ] Precedence and associativity rules in APL are both more orthogonal than precedence and associativity rules in other programming languages.
- [ ] Precedence and associativity rules in APL are both less orthogonal than precedence and associativity rules in other programming languages.

---

## Question 9 *(1 point)*

In Scheme, operator overloading isn't supported due to Scheme's reliance on dynamic typing. Select the reason that most correctly explains why **dynamic typing results in a lack of operator overloading in Scheme**.

- [ ] Dynamic typing means Scheme operators can receive operands of any type.
- [ ] Dynamic typing means overloaded operators would be very unreliable.
- [ ] Dynamic typing means overloaded versions of operators are automatically generated.
- [ ] Dynamic typing means operator support doesn't make sense in Scheme.

---

## Question 10 *(1 point)*

Ada supports no assignment coercions. Consider the following statements, and select one that most correctly describes a **result of this lack of assignment coercions**.

- [ ] Ada is more writable.
- [ ] Ada is more orthogonal.
- [ ] Ada is more reliable.
- [ ] Ada has lower cost.

---

## Question 11 *(1 point)*

Perl supports multiple assignments. Consider the following statements, and select one that most correctly describes an **advantage of this support**.

- [ ] Perl is more writable.
- [ ] Perl is more orthogonal.
- [ ] Perl has reduced cost.
- [ ] Perl is more reliable.

---

## Question 12 *(1 point)*

Consider the following program code fragment in a hypothetical programming language:

```
int [] myArr = {3, 4, 1, 6, 2}
int index = 0
int length = 5
int threshold = 10
while ((myArr[index] == threshold) or (++index < length))
{ ... }
```

Select the option that most correctly describes a **problem** with the above program code.

- [ ] If the `or` operator is short-circuit evaluated, a side effect will not occur, which causes a problem.
- [ ] If the `or` operator is short-circuit evaluated, a side effect occurs, which causes a problem.
- [ ] If the `or` operator is not short-circuit evaluated, a side effect will not occur, which causes a problem.
- [ ] If the `or` operator is not short-circuit evaluated, a side effect occurs, which causes a problem.

---

## Question 13 *(2 points)*

Fortran I had a three-way selection statement. In this statement, one branch would be executed if the control variable value was above zero, a second branch would be executed if the control variable value was equal to zero, and a third branch would be executed if the control variable value was below zero. Select **only** the statements that are **properties of the three-way selection statement**. *(Incorrectly selected options will be penalised.)*

- [ ] The three-way selection statement allows flow control to be written, which cannot be written using two-way selection and pretest logical loops.
- [ ] The three-way selection statement is very efficient.
- [ ] The three-way selection statement is an example of programmer time being considered more important than execution time.
- [ ] The three-way selection statement is too closely based on the IBM 704 hardware.

---

## Question 14 *(1 point)*

Counter-controlled loops are supported in **C and Ada**. Consider the following statements, and select the one that is most correct.

- [ ] Counter-controlled loops in C are less writable than counter-controlled loops in Ada.
- [ ] Counter-controlled loops in C are more costly than counter-controlled loops in Ada.
- [ ] Counter-controlled loops in C are less reliable than counter-controlled loops in Ada.
- [ ] Counter-controlled loops in C are more orthogonal than counter-controlled loops in Ada.

---

## Question 15 *(1 point)*

It is possible for a conditional to be part of a break used in a loop. Consider the following drawbacks, and select the one that applies to situations in which **a conditional is part of a break**.

- [ ] Writability is reduced.
- [ ] Readability is reduced.
- [ ] Orthogonality is reduced.
- [ ] Cost is reduced.

---

## Question 16 *(1 point)*

Consider the following program code in a hypothetical programming language that supports **guarded commands**:

```
var a = 11

if (a < 0) -> print("Negative")
[] (a mod 2 == 0) -> print("Even")
fi
```

Provide the **output** of the program. If the program produces no output, write `Nothing`. If there is a compile-time error, write `Compilation error`. If there is a runtime error, write `Runtime error`.

**Answer:** _______________

---

## Question 17 *(1 point)*

In Python, subprogram definitions are executable. Consider the following statements about the **implications of executable subprogram definitions**, and select the one that is most correct.

- [ ] Writability is reduced.
- [ ] Readability is reduced.
- [ ] Cost is reduced.
- [ ] There is no effect on the programming language, because all languages that support subprograms have executable subprogram definitions.

---

## Question 18 *(1 point)*

In programming languages like C++, default parameters must appear last in the list of parameters. Consider the following solutions for **allowing default parameters to appear anywhere in the list of parameters**, and select the one that is most correct.

- [ ] Use a variable number of parameters, if the programming language supports them.
- [ ] Use positional parameters, if the programming language supports them.
- [ ] Use keyword parameters, if the programming language supports them.
- [ ] It is not possible to allow default parameters to appear anywhere in the list of parameters.

---

## Question 19 *(1 point)*

Procedures are a specific kind of subprogram. Consider the following statements, and select the one that is most correct.

- [ ] Procedures are guaranteed to never have side effects.
- [ ] Procedures are guaranteed to always have side effects.
- [ ] Procedures have a high probability of having side effects, unless they are written carefully.
- [ ] Procedures generate side effects unpredictably.

---

## Question 20 *(1 point)*

Consider the following program code in a hypothetical programming language that allows subprogram names to be passed as parameters:

```
A = 4
subprogram f(sub) {
    A = 9
    call sub()
}
subprogram g() {
    print A
}
subprogram main() {
    A = 2
    call f(g)
}
```

Assume execution starts with `main` and the programming language uses **static scoping**. Provide the **output** if **ad-hoc binding** is used.

**Answer:** _______________

---

## Question 21 *(1 point)*

Consider the following program code in a hypothetical programming language that supports **coroutines**:

```
subprogram main() {
    resume g()
}
coroutine f() {
    print "A "
    resume g()
    print "B "
}
coroutine g() {
    print "C "
    resume f()
    print "D "
}
```

Assume execution starts with `main`. Provide the **output** of the program. *(Note: there is a single space at the end of each print output.)*

**Answer:** _______________

---

## Question 22 *(1 point)*

Java supports a mechanism for ensuring that clients can't depend on the implementation of ADTs. Consider the following language features, and select the one that **ensures a lack of client dependence on implementation**.

- [ ] Header files and implementation files.
- [ ] Base classes and derived classes.
- [ ] Classes implementing interfaces.
- [ ] Javadoc and bytecode.

---

## Question 23 *(1 point)*

Classes are dynamic in Ruby. Consider the following statements about the **implications of dynamic classes in Ruby**, and select the one that is most correct.

- [ ] Dynamic classes increase writability.
- [ ] Dynamic classes increase readability.
- [ ] Dynamic classes decrease cost.
- [ ] Dynamic classes increase reliability.

---

## Question 24 *(3 points)*

Briefly outline how the **compiler handles parameterised classes in Java 5.0**.

**Answer:** _______________

---

## Question 25 *(1 point)*

Smalltalk supports object-oriented programming. Consider the following statements, and select the one that is most correct.

- [ ] Smalltalk's support for object-oriented programming is very writable.
- [ ] Smalltalk's support for object-oriented programming is quite efficient.
- [ ] Smalltalk's support for object-oriented programming is highly orthogonal.
- [ ] Smalltalk is essentially equivalent in terms of programming language evaluation criteria to other object-oriented programming languages such as C++ and Java.

---

## Question 26 *(1 point)*

Assume a programming language that supports **multiple inheritance**. There is a parent class called A. Two classes, called B and C, both inherit directly from A. Finally, a class called D inherits from both B and C. Consider the following statements, and select the one that causes an **implicit problem** with the described inheritance hierarchy.

- [ ] If any class member is defined in class A.
- [ ] If any class member is defined in class B.
- [ ] If any class member is defined in class C.
- [ ] If any class member with the same name is defined in classes B and C.

---

## Question 27 *(1 point)*

C++ provides support for **private derivation**. Consider the following statements, and select the one that describes a **valid use for private derivation**.

- [ ] When a derived class wishes to only add to the public interface of its base class.
- [ ] When a derived class wishes to only modify how one part of the public interface provided by its base class works.
- [ ] When a derived class wishes to only make part of its base class interface publicly visible.
- [ ] When a derived class wishes to ensure that it is a subtype of its base class.

---

## Question 28 *(1 point)*

C++ and Java both support **object-oriented message binding**. Consider the following statements, and select the one that is most correct.

- [ ] C++ support for message binding is more writable than Java's support.
- [ ] C++ support for message binding is more readable than Java's support.
- [ ] C++ support for message binding is less efficient than Java's support.
- [ ] C++ support for message binding is more reliable than Java's support.

---

## Question 29 *(1 point)*

Consider the following statements about **classes and structs in C#**, and select the one that is most correct.

- [ ] C# only supports classes, and not structs.
- [ ] Classes are more writable than structs in C#.
- [ ] Structs are more writable than classes in C#.
- [ ] Classes and structs are equally writable in C#.
