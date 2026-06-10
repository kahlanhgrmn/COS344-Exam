# COS 333 – Programming Languages
## Semester Test 1 — 25 March 2025

**Examiner:** Mr W. S. van Heerden
**Duration:** 1.5 hours | **Total:** 35 marks | **Questions:** 21

> **Instructions:** Read the questions carefully and answer all questions. This test is closed book. Allowed references: Practical 2 specification and the MIT/GNU Scheme Reference Manual.

---

## Question 1 *(2 points)*

Imagine that a recent graduate joins a company as a **software tester** (providing high- and low-level feedback on software errors, but not developing new systems). The graduate learned Java during their studies. The company uses Python and considers execution performance very important.

Identify **two reasons for studying concepts of programming languages** applicable to this graduate.

**Reason 1:** _______________

**Reason 2:** _______________

---

## Question 2 *(1 point)*

Assume two hypothetical programming languages, A and B, both supporting primitive numeric types and functions. Language A allows functions to return only numeric types. Language B allows functions to return numeric types and functions. Select the most correct statement.

- [ ] Programming language A is more orthogonal than B because A supports a smaller set of constructs than B.
- [ ] Programming language A is more orthogonal than B because returning functions makes no sense.
- [ ] Programming language B is more orthogonal than A because B supports a larger set of constructs than A.
- [ ] Programming language B is more orthogonal than A because B allows more legal return values than A.

---

## Question 3 *(1 point)*

Some programming languages use special words to mark the start and end of a compound statement (block). Select the option that most correctly describes a **consequence** of using special words to mark compound statements.

- [ ] Readability is decreased.
- [ ] Writability is improved.
- [ ] Writability is decreased.
- [ ] Reliability is improved.

---

## Question 4 *(1 point)*

Many programming languages support some kind of **aliasing**. Select the option that most correctly describes a **consequence** of including support for aliasing.

- [ ] Readability is improved.
- [ ] Writability is improved.
- [ ] Reliability is increased.
- [ ] The overall cost of the programming language decreases.

---

## Question 5 *(1 point)*

Type checking is generally considered beneficial to reliability. Select the most correct statement about **type checking**.

- [ ] Type checking increases the cost of execution for a programming language.
- [ ] Type checking increases the cost of reliability for a programming language.
- [ ] Type checking increases the writability of a programming language, because it gives the programmer more flexibility.
- [ ] Type checking has no impact on any of the programming language evaluation criteria.

---

## Question 6 *(1 point)*

Consider the following programming domains, and select the one that a **hybrid implementation system** is most suitable for.

- [ ] Scientific applications
- [ ] Business applications
- [ ] Systems programming
- [ ] Web software

---

## Question 7 *(2 points)*

Scheme has **poor execution performance**. Select **only** the factors that contribute to this poor performance. *(Incorrectly selected options will be penalised.)*

- [ ] The implementation method that is most often used for Scheme.
- [ ] The programming domain that Scheme was designed for.
- [ ] The programming methodology that is most often used with Scheme.
- [ ] Modern computer architecture.

---

## Question 8 *(1 point)*

Various factors can influence programming language design. Select the programming language design influence that had its **earliest impact** on the design of **Smalltalk**.

- [ ] Computer architecture
- [ ] Programmer efficiency becoming more important than machine efficiency
- [ ] The move from process-oriented programming to data-oriented programming
- [ ] The move to object-oriented programming

---

## Question 9 *(1 point)*

Consider the following statements about **Fortran 90**, and select the most correct.

- [ ] Fortran 90 was only focused on the execution speed of compiled program code.
- [ ] Fortran 90 introduced language features that improved writability at the expense of the execution speed of compiled program code.
- [ ] Fortran 90 introduced language features that reduced writability in order to improve the execution speed of compiled program code.
- [ ] Fortran 90 required code to be structured in a way that facilitated code execution from punch cards.

---

## Question 10 *(1 point)*

Consider the following statements about the **successes of ALGOL 60**, and select the most correct.

- [ ] ALGOL 60 was successful as a programming language that was applicable to many different programming domains.
- [ ] ALGOL 60 was completely successful as a machine-independent programming language.
- [ ] ALGOL 60 served as a very readable standard for documenting algorithms.
- [ ] ALGOL 60 had a formal syntax description that was widely accepted at the time ALGOL 60 was created.

---

## Question 11 *(1 point)*

Consider the following statements about **PL/I**, and select the most correct.

- [ ] PL/I was intended for scientific applications.
- [ ] PL/I aimed to be more well-defined than programming languages developed in previous years.
- [ ] PL/I aimed to have better generality than programming languages developed in previous years.
- [ ] PL/I aimed to have better portability than programming languages developed in previous years.

---

## Question 12 *(1 point)*

Consider the following statements about **APL**, and select the most correct.

- [ ] APL demonstrates that there is not necessarily a tradeoff between readability and writability, because it has both good readability and good writability.
- [ ] APL demonstrates that there is often a tradeoff between readability and writability, because APL has good readability and poor writability.
- [ ] APL demonstrates that there is often a tradeoff between readability and writability, because APL has poor readability and good writability.
- [ ] APL demonstrates that there is not necessarily a tradeoff between readability and writability, because it has both poor readability and poor writability.

---

## Question 13 *(2 points)*

Select **only** the language features that were **pioneered by Simula 67**. *(Incorrectly selected options will be penalised.)*

- [ ] Systems programming support
- [ ] Coroutines
- [ ] Classes and objects
- [ ] Inheritance and polymorphism

---

## Question 14 *(1 point)*

Consider the following statements about **Delphi**, and select the most correct.

- [ ] Delphi is an imperative programming language that was extended with support for object-oriented programming.
- [ ] Delphi is a purely object-oriented programming language.
- [ ] Delphi has no support for object-oriented programming.
- [ ] Delphi is less reliable than C++.

---

## Question 15 *(1 point)*

Consider the following statements about **Ruby**, and select the most correct.

- [ ] Ruby is a compiled programming language.
- [ ] Ruby is primarily an imperative programming language with optional support for object-oriented programming.
- [ ] Ruby supports classes and objects, but does not support inheritance and polymorphism.
- [ ] Ruby is unreliable because its classes and objects can have different structures at different times.

---

## Question 16 *(2 points)*

Select **only** the programming language features that improve the **orthogonality of Scheme**. *(Incorrectly selected options will be penalised.)*

- [ ] The fact that only symbolic and numeric atoms are supported.
- [ ] The fact that functions and lists are represented the same way.
- [ ] The fact that functions can be used as parameters.
- [ ] The fact that functional side effects are not allowed.

---

## Question 17 *(2 points)*

Consider the following Scheme code:

```scheme
(doSomething thing)
```

Select **only** the options that describe what `thing` can be. *(Incorrectly selected options will be penalised.)*

- [ ] A symbolic atom.
- [ ] A name to which a value has been bound, and for which the binding can change at a later time.
- [ ] A name to which a value has been bound, and for which the binding cannot change.
- [ ] The name of a function.

---

## Question 18 *(2 points)*

One way referential transparency can break down is through **functional side effects**. Select **only** the options that describe a **different way** in which referential transparency could break down (i.e. not a functional side effect). *(Incorrectly selected options will be penalised.)*

- [ ] When a variable is used in a function.
- [ ] When a function returns no value.
- [ ] When a function returns a random value.
- [ ] When a function reads a user input, and returns this value.

---

## Question 19 *(1 point)*

Consider the following Scheme code:

```scheme
(eval '(+ 2 3))
```

Select the option that most correctly explains what happens when this code is executed.

- [ ] The code fails to execute because the `eval` function is undefined.
- [ ] The Scheme interpreter evaluates the list `(+ 2 3)` as if it is a function application, producing the result `5`.
- [ ] The function application `(+ 2 3)` is evaluated, producing the result `5`. The function `eval` prints out this result.
- [ ] The function application `(+ 2 3)` is evaluated, producing the result `5`. The result is converted into the list `(5)`. The function `eval` prints out the content of this list, which is the value `5`.

---

## Question 20 *(5 points)*

Write a Scheme function named `coneArea`, which receives two numeric parameters: the **radius** of the circular base and the **slant height** of the cone. The function should yield (not print) the area of the cone:

```
area = pi * r^2 + pi * r * l
```

The function should yield `0` if either the radius or slant height is negative. Use a `let` (not `define`) to bind `22/7` to the name `pi` and the result of `r^2` to the name `rSquared`.

*Example:* `(display (coneArea 1.2 2.1))` should yield approximately `12.445714285714285`.

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

Submit file `u99999999.scm` to slot **"Semester Test 1: Arithmetic Scheme Function"**.

**Did you submit?**
- [ ] True
- [ ] False

---

## Question 21 *(5 points)*

Write a Scheme function named `countDivisors`, which is applied to two parameters: a numeric atom `atm` and a simple numeric list `lst`. The function should yield (not print) the **number of divisors of `atm`** contained in `lst`. A divisor of `a` is a value that divides perfectly into `a`.

*Examples:*
```scheme
(countDivisors 6 '())
; => 0   (empty list contains no divisors)

(countDivisors 6 '(4 12))
; => 0   (4 and 12 are not divisors of 6)

(countDivisors 6 '(1 4 3 12))
; => 2   (only 1 and 3 are divisors of 6)
```

**Allowed built-in functions:** *(same as Question 20)*

Submit file `u99999999.scm` to slot **"Semester Test 1: List Processing Scheme Function"**.

**Did you submit?**
- [ ] True
- [ ] False
