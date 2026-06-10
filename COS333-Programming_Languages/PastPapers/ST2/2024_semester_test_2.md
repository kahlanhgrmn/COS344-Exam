# COS 333 – Programming Languages
## Semester Test 2 — 14 May 2024

**Examiner:** Mr W. S. van Heerden
**Duration:** 1.5 hours | **Total:** 35 marks | **Questions:** 20

> **Instructions:** Read the questions carefully and answer all questions. This test is closed book. Allowed references: Practical 3 & 4 specifications and the SWI-Prolog Reference Manual.

---

## Question 1 *(1 point)*

Assume that the following Prolog-like program code is provided:

```prolog
tennis(angela).
soccer(gary).
sportsPerson(X) :- soccer(X).
sportsPerson(X) :- tennis(X).
```

Also assume that the following query is provided:

```prolog
?- sportsPerson(angela).
```

Select from the options to complete the following steps, if **bottom-up resolution (forward chaining)** is performed to prove the query. Select "No step performed" for any steps you do not use.

**Step 1:** _______________

**Step 2:** _______________

---

## Question 2 *(2 points)*

Assume that you have a Prolog program with three kinds of facts: `cat(X)` (X is a cat), `dog(X)` (X is a dog), and `pet(X, Y)` (X is a pet owned by Y). You wish to write a query that determines whether `peter` owns a pet that is a cat. Select the query that **most efficiently** determines an instantiation for the pet of peter.

- [ ] `?- cat(X), pet(X, peter).`
- [ ] `?- pet(X, peter), cat(X).`
- [ ] `?- cat(X).` then `?- pet(X, peter).`
- [ ] `?- pet(X, peter).` then `?- cat(X).`

---

## Question 3 *(5 points)*

Assume that you have Prolog facts describing tenants and addresses:

```prolog
tenant(alice, tony).
tenant(tom, jane).
tenant(joe, tony).
tenant(mary, jane).
address(alice, pineStreet12).
address(tom, shillingLane15).
address(joe, duncanRoad6).
address(mary, shillingLane15).
address(jonathan, pineStreet12).
```

`tenant(X, Y)` means X rents from Y. `address(X, Y)` means X lives at Y.

Write a Prolog proposition called `ownsSharedProperty(X)`, which succeeds if atom X owns a property rented by two individuals who share the same address. In the above example, only `jane` satisfies this (tom and mary are both her tenants and both live at `shillingLane15`).

**Requirements:**
- You may **not** define any additional facts other than `tenant` and `address`.
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, and built-in predicates from the textbook/slides. Do **not** use if-then, if-then-else, or complex system predicates.

Submit file `s99999999.pl` to slot **"Semester Test 2: Simple Prolog Proposition"**.

**Did you submit?**
- [ ] Yes
- [ ] No

---

## Question 4 *(5 points)*

Write a Prolog proposition called `countNonMatching(E, L, C)`, which succeeds if C is the number of elements in list L that **do not match** atom E. For example:

```prolog
?- countNonMatching(a, [a, a], X).
% X = 0

?- countNonMatching(a, [a, b, a, c, d], X).
% X = 3
```

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, and built-in predicates from the textbook/slides. Do **not** use if-then, if-then-else, or complex system predicates.

Submit file `s99999999.pl` to slot **"Semester Test 2: List Processing Prolog Proposition"**.

**Did you submit?**
- [ ] Yes
- [ ] No

---

## Question 5 *(1 point)*

Consider the following programming languages, and select the one that is the **most writable** in terms of name length, in a real-world context.

- [ ] Fortran 95
- [ ] C99
- [ ] C++
- [ ] Ada

---

## Question 6 *(2 points)*

Consider the following program code in a hypothetical programming language:

```
1.  class MyClass {
2.     int count;
3.     MyClass(int aCount) {
4.        count = aCount
5.     }
6.     int getCount() {
7.        return count
8.     }
9.  }
10. void main() {
11.    int class = 5
12.    MyClass m(class)
13. }
```

Identify the type of special words used in this programming language:

- If a **compilation error occurs on line 11**: the special words are _______________
- If **no compilation error occurs**: the special words are _______________

---

## Question 7 *(1 point)*

Consider the following program code in a hypothetical programming language:

```
1. myVariable = [1, 2, 3]
2. myVariable = 14
```

Assume the above code results in a **compilation error on line 2**. Select the kind of type binding most likely used for `myVariable`.

- [ ] Explicit type declaration
- [ ] Implicit type declaration without type inferencing
- [ ] Implicit type declaration with type inferencing
- [ ] Dynamic type binding

---

## Question 8 *(1 point)*

Consider the following categories of variables, and select the one that **has no name** associated with it.

- [ ] Static variables
- [ ] Stack-dynamic variables
- [ ] Explicit heap-dynamic variables
- [ ] Implicit heap-dynamic variables

---

## Question 9 *(4 points)*

Consider the following program code in a hypothetical programming language (line numbers for reference):

```
1. void doSomething()
2.    myValue = 2
3.    print myValue
4.    myValue = [5, 7, 9]
5.    print myValue

7. int main()
8.    doSomething()
9.    return 0
```

Assume static scope, variables not explicitly declared, `main` executes first, and indentation indicates subprogram body. Fill in using line numbers only:

**Scope of `myValue`:** From line ___ up to and including line ___

**Lifetime of the single integer value stored by `myValue`:** From line ___ up to and including line ___

---

## Question 10 *(2 points)*

Consider the following program code in a hypothetical programming language:

```
void f1() {
   var X = 8
   call f2()
}

void f2() {
   print(X)
}

void main() {
   var X = 3
   call f1()
}
```

Assume the language implements variable hiding and execution starts with `main`. Provide **only the numeric output** (or `Error` if an error occurs):

**Static scoping:** _______________

**Dynamic scoping:** _______________

---

## Question 11 *(1 point)*

Some programming languages support complex numbers as a primitive data type. Select the statement that **most accurately describes an implication** of such support.

- [ ] Computations using complex number types have a somewhat high cost of execution, because these computations are not directly supported by most hardware.
- [ ] Computations using complex number types have a very low cost of execution, because these computations are directly supported by most hardware.
- [ ] Support for complex number types greatly increases the readability of a programming language.
- [ ] Support for complex number types greatly decreases the writability of a programming language.

---

## Question 12 *(1 point)*

Select the statement that most accurately describes a potential **drawback associated with Boolean data types**.

- [ ] Operations on Boolean data types have a high execution cost.
- [ ] Boolean data types are inefficient in terms of memory space.
- [ ] Boolean data types have low readability in most modern programming languages.
- [ ] Boolean data types are never considered to be ordinal.

---

## Question 13 *(1 point)*

Consider the following enumeration type definition:

```
enumeration month {jan, feb, mar}
```

Assume that other types can be coerced into enumeration types. Select the snippet that correctly represents an **error** that could occur due to this coercion.

- [ ] `month firstMonth = feb` / `month secondMonth = mar` / `print(firstMonth + secondMonth)`
- [ ] `month myMonth = 1`
- [ ] `month myMonth = 4`
- [ ] `print(jan)`

---

## Question 14 *(1 point)*

Consider the following statements about **index range checking** for arrays in Ada and Java, and select the most correct.

- [ ] Ada's index range checking is always less reliable than Java's range checking.
- [ ] Ada's index range checking can be more reliable than Java's range checking.
- [ ] Ada's index range checking is much less writable than Java's range checking.
- [ ] Ada's index range checking is much more writable than Java's range checking.

---

## Question 15 *(1 point)*

Consider the following program code:

```
void f() {
   integer myVar = 3
   integer myArray[myVar]
   myArray[0] = 5
   myArray[1] = 2
   myArray[2] = 4
   print(myArray[1])
}
```

Select the statement that most correctly describes the **category of `myArray`**.

- [ ] Static
- [ ] Fixed stack-dynamic
- [ ] Stack-dynamic
- [ ] Fixed heap-dynamic
- [ ] Heap-dynamic

---

## Question 16 *(2 points)*

Assume you wish to simulate a **heterogeneous array** in a language that does not directly support them. Select **only** the approaches that will correctly simulate this functionality. *(Incorrectly selected options will be penalised.)*

- [ ] Using a normal array in a statically typed language which stores values of different primitive data types.
- [ ] Using a normal array in a statically typed language which stores instances of an `Object` class, where all other classes inherit from `Object`.
- [ ] Using two normal arrays in a statically typed language, where one stores keys and the other stores corresponding values.
- [ ] Using a normal array in a dynamically typed programming language.

---

## Question 17 *(1 point)*

Matrices in C do not support array slices. Select the statement that most correctly describes the **reason** for this.

- [ ] C implements matrices using arrays containing other arrays. Arrays in C have built-in slice operations, meaning the matrix itself does not require support for slice operations.
- [ ] C implements matrices using arrays containing other arrays. It is therefore easy to retrieve part of the matrix using standard array operations.
- [ ] C implements matrices using rectangular arrays. Rectangular arrays cannot support slice operations.
- [ ] C implements matrices using rectangular arrays. Rectangular arrays cannot represent matrices.

---

## Question 18 *(1 point)*

Select the statement about the **MOVE CORRESPONDING** operation in COBOL that is the most correct.

- [ ] The MOVE CORRESPONDING operation in COBOL is equivalent to an assignment between records in most modern imperative programming languages.
- [ ] The MOVE CORRESPONDING operation in COBOL is useful because it concatenates two records, which is a common operation in COBOL's programming domain.
- [ ] The MOVE CORRESPONDING operation in COBOL is useful because it extracts sub-records within another record, which is a common operation in COBOL's programming domain.
- [ ] The MOVE CORRESPONDING operation in COBOL is useful because it copies only relevant data between two records, which is a common operation in COBOL's programming domain.

---

## Question 19 *(1 point)*

Select the statement about **list comprehensions** that is the most correct.

- [ ] Support for list comprehensions greatly increases the writability of lists and list operations.
- [ ] Support for list comprehensions greatly increases the readability of lists and list operations.
- [ ] Support for list comprehensions greatly increases the orthogonality of lists and list operations.
- [ ] Support for list comprehensions greatly decreases the amount of memory space occupied by lists.

---

## Question 20 *(1 point)*

Some programming languages implicitly dereference all pointers. Select the statement that is the most correct.

- [ ] Implicitly dereferenced pointers are more reliable than explicitly dereferenced pointers.
- [ ] Implicitly dereferenced pointers prevent pointers from being used for indirect addressing.
- [ ] Implicitly dereferenced pointers prevent pointers from being used for dynamic storage management.
- [ ] Implicitly dereferenced pointers disallow pointer arithmetic.
