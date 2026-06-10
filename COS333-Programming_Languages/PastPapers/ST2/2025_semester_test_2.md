# COS 333 – Programming Languages
## Semester Test 2 — 9 May 2025

**Examiner:** Mr W. S. van Heerden
**Duration:** 1.5 hours | **Total:** 35 marks | **Questions:** 23

> **Instructions:** Read the questions carefully and answer all questions. This test is closed book. Allowed references: Practical 3 & 4 specifications and the SWI-Prolog Reference Manual.

---

## Question 1 *(1 point)*

Consider the following Prolog proposition implementation:

```prolog
tail([], []).
tail([H|T], T).
```

The `tail` proposition succeeds if the second parameter is the tail of the first parameter (the tail of an empty list is an empty list). This implementation causes a Prolog interpreter to raise a warning. Select the statement that is most correct.

- [ ] The warning can be avoided by replacing `H` with `_`, although the `tail` proposition will not work correctly for certain queries.
- [ ] The warning can be avoided by replacing `H` with `_`, although the `tail` proposition will be less efficient than the original implementation.
- [ ] The warning can be avoided by replacing `H` with `_`, although the `tail` proposition will be less reliable than the original implementation.
- [ ] The warning can be avoided without changing how the `tail` proposition works by replacing `H` with `_`.

---

## Question 2 *(1 point)*

Consider the following Prolog proposition implementation:

```prolog
primeGreaterThanOneMillion(X) :- prime(X), X > 1000000.
```

Assume `prime(X)` succeeds if X is a prime number. Select the statement that is most correct.

- [ ] The `primeGreaterThanOneMillion` proposition will execute **more** efficiently if rewritten as: `primeGreaterThanOneMillion(X) :- X > 1000000, prime(X).`
- [ ] The `primeGreaterThanOneMillion` proposition will execute **less** efficiently if rewritten as: `primeGreaterThanOneMillion(X) :- X > 1000000, prime(X).`
- [ ] The `primeGreaterThanOneMillion` proposition will **not work correctly** unless rewritten as: `primeGreaterThanOneMillion(X) :- X > 1000000, prime(X).`
- [ ] The `primeGreaterThanOneMillion` proposition cannot be successfully implemented, due to a deficiency of Prolog.

---

## Question 3 *(1 point)*

Assume you wish to write a Prolog proposition that ensures two variables X and Y do not represent the same thing. Select the statement that describes the **most rigorous and correct** way to achieve this.

- [ ] X and Y are always different because X and Y represent two distinct atoms.
- [ ] X and Y are always different because X and Y represent two distinct variables.
- [ ] By defining a proposition called `unequal(X, Y)` for every pair of atoms that are not the same.
- [ ] By using the proposition `not(X = Y)`.

---

## Question 4 *(5 points)*

Assume you have Prolog facts describing family relationships:

```prolog
father(bill, jake).
father(bill, shelley).
father(jake, ted).
father(ron, liz).

mother(mary, jake).
mother(mary, shelley).
mother(janet, ted).
mother(shelley, liz).
```

`father(X, Y)` means X is the father of Y. `mother(X, Y)` means X is the mother of Y.

Write a Prolog proposition called `nephewNiece(X, Y)`, which succeeds if person X is the **nephew or niece** of person Y. A person's nephew/niece is the son/daughter of that person's brother or sister. Two people are siblings if they share at least one parent.

*Example: `shelley` is the sister of `jake` (they share `bill` or `mary`). Therefore `ted` is the nephew of `shelley`, and `liz` is the niece of `jake`.*

**Requirements:**
- You may **not** define any additional facts other than `father` and `mother`.
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, the `is` operator, cuts, and the built-in `not` proposition. Do **not** use if-then, if-then-else, the semicolon (`;`) operator, or complex system predicates (including built-in `member`, `append`, `reverse`).

Submit file `u99999999.pl` to slot **"Semester Test 2: Simple Prolog Proposition"**.

**Did you submit?**
- [ ] True
- [ ] False

---

## Question 5 *(5 points)*

Write a Prolog proposition called `getAbsNonZeros(L1, L2)`, where L1 and L2 are both simple numeric lists. The proposition succeeds if L2 contains the **absolute values of only the non-zero elements** of L1, in their original order. For example:

```prolog
?- getAbsNonZeros([0], X).
% X = []

?- getAbsNonZeros([1, 0, -2, 0], X).
% X = [1, 2]
```

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, the `is` operator, cuts, and the built-in `not` proposition. Do **not** use if-then, if-then-else, the semicolon (`;`) operator, or complex system predicates (including built-in `member`, `append`, `reverse`).

Submit file `u99999999.pl` to slot **"Semester Test 2: List Processing Prolog Proposition"**.

**Did you submit?**
- [ ] True
- [ ] False

---

## Question 6 *(1 point)*

Consider the following programming languages, and select the one that is the **least reliable** in terms of name length.

- [ ] Fortran
- [ ] C99
- [ ] C++
- [ ] C#

---

## Question 7 *(1 point)*

Consider the following statements about variable names in **Perl and Java**, and select the most correct.

- [ ] Variable names in Perl have a higher cost of maintenance than variable names in Java.
- [ ] Variable names in Perl are more writable than variable names in Java.
- [ ] Variable names in Perl are more readable than variable names in Java.
- [ ] Variable names in Perl are less reliable than variable names in Java.

---

## Question 8 *(1 point)*

Select the time at which a name is bound to a **stack-dynamic variable**.

- [ ] Language design time
- [ ] Language implementation time
- [ ] Compile time
- [ ] Load time
- [ ] Runtime

---

## Question 9 *(1 point)*

In Fortran I, a variable whose name starts with I, J, K, L, M, or N is automatically an integer variable. Select the option that most correctly describes the kind of **type binding** that takes place.

- [ ] Explicit type declaration
- [ ] Implicit type declaration without type inferencing
- [ ] Implicit type declaration with type inferencing
- [ ] Dynamic type binding

---

## Question 10 *(1 point)*

Consider the following program code:

```
f() {
   myValue = 10
   print(myValue)
   myValue = myValue + 5
}

main() {
   f()
   f()
   f()
}
```

Assume execution starts with `main` and the output of the program is:

```
10 15 20
```

Select the option that correctly describes the **category of `myValue`** according to lifetime.

- [ ] Static variable
- [ ] Stack-dynamic variable
- [ ] Explicit heap-dynamic variable
- [ ] Implicit heap-dynamic variable

---

## Question 11 *(1 point)*

Assume a hypothetical programming language uses **dynamic type binding**. Select the option that most correctly describes the category of the variables in this language, according to lifetime.

- [ ] Static variables
- [ ] Stack-dynamic variables
- [ ] Explicit heap-dynamic variables
- [ ] Implicit heap-dynamic variables

---

## Question 12 *(2 points)*

Consider the following program code:

```
void main() {

  void doSomething() {
      print(X)
  }

  var X = 10

  call doSomething()
}
```

Assume variable hiding is implemented, scope ranges from declaration to end of block, nested subprograms are supported, and execution starts with `main`. Provide **only the numeric output** (or `Error` if an error occurs):

**Static scoping:** _______________

**Dynamic scoping:** _______________

---

## Question 13 *(2 points)*

Consider the following program code (line numbers for reference):

```
1. void f()
2.    allocateInteger(myValue, 15)
3.    print(myValue)

4. int main()
5.    f()
6.    return 0
```

Assume static scope, variables not explicitly declared, `main` executes first, and indentation indicates subprogram body. Fill in using line numbers only:

**Lifetime of `myValue`:** From line ___ up to and including line ___

---

## Question 14 *(1 point)*

Identify the kind of named constants that are used in C++.

**Answer:** _______________

---

## Question 15 *(1 point)*

Some programming languages support a primitive data type that represents a **complex number**. Select the statement that is most correct.

- [ ] Support for a primitive complex number type improves the **writability** of a programming language.
- [ ] Support for a primitive complex number type improves the **readability** of a programming language.
- [ ] Support for a primitive complex number type improves the **execution cost** of a programming language.
- [ ] Support for a primitive complex number type improves the **reliability** of a programming language.

---

## Question 16 *(1 point)*

Consider the following statements about the **`String` and `StringBuffer` classes** in Java, and select the most correct.

- [ ] A `String` object is less readable than a `StringBuffer` object.
- [ ] A `String` object is less writable than a `StringBuffer` object.
- [ ] A `String` object is less reliable than a `StringBuffer` object.
- [ ] A `String` object has a lower cost of execution than a `StringBuffer` object.

---

## Question 17 *(2 points)*

Consider the following program code:

```
main() {
   constant integer LENGTH = 3
   integer myArray[LENGTH]
   myArray[0] = 6
   myArray[1] = 2
   myArray[2] = 5
   print(myArray[2])
}
```

Assume the length of `myArray` cannot be changed after it has been set. Select **only** the options that could possibly correctly describe the **category of `myArray`**. *(Incorrectly selected options will be penalised.)*

- [ ] Static
- [ ] Fixed stack-dynamic
- [ ] Stack-dynamic
- [ ] Fixed heap-dynamic
- [ ] Heap-dynamic

---

## Question 18 *(1 point)*

Assume you wish to simulate the functionality of an **associative array** in a language that does not directly support them. Select the one option that will correctly simulate this functionality.

- [ ] Using a normal array in a statically typed language which stores values of different primitive data types.
- [ ] Using a normal array in a statically typed language which stores instances of an `Object` class, where all other classes inherit from `Object`.
- [ ] Using a normal array in a statically typed language, where the array stores a key and a value at each subscript.
- [ ] Using two normal arrays in a statically typed language, where one stores keys and the other stores corresponding values.

---

## Question 19 *(1 point)*

Consider the following statements about **records in COBOL and Ada**, and select the most correct.

- [ ] References to record fields in COBOL are less writable than references to record fields in Ada.
- [ ] Records in COBOL have a lower cost of maintenance than records in Ada.
- [ ] Records in COBOL are less orthogonal than records in Ada.
- [ ] Records in COBOL are more orthogonal than records in Ada.

---

## Question 20 *(1 point)*

Consider the following statements about **unions**, and select the most correct.

- [ ] Free unions have a lower cost of maintenance than discriminated unions.
- [ ] Free unions are more orthogonal than discriminated unions.
- [ ] Free unions are less writable than discriminated unions.
- [ ] Free unions are more effective at saving memory than discriminated unions.

---

## Question 21 *(1 point)*

Consider the following statements about **pointers and references in C++, Java, and C#**, and select the most correct.

- [ ] Pointers and references have the most reliable support in Java.
- [ ] Pointers and references have the most reliable support in C#.
- [ ] Pointers and references have the least writable support in C#.
- [ ] Pointers and references have the least writable support in C++.

---

## Question 22 *(2 points)*

C++ is not considered to be a strongly typed programming language. Select **only** the language features that contribute to C++ not being strongly typed. *(Incorrectly selected options will be penalised.)*

- [ ] Explicit type declarations
- [ ] Void pointers
- [ ] Casting a base class pointer to a derived class pointer
- [ ] Casting a derived class pointer to a base class pointer

---

## Question 23 *(1 point)*

Consider the following statements about **name type equivalence and structure type equivalence**, and select the most correct.

- [ ] Name type equivalence has a lower cost of execution than structure type equivalence.
- [ ] Name type equivalence is more writable than structure type equivalence.
- [ ] Name type equivalence is less readable than structure type equivalence.
- [ ] Name type equivalence is less reliable than structure type equivalence.
