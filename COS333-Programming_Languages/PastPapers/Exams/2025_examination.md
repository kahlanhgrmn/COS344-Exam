# COS 333 – Programming Languages
## Examination — 17 June 2025

**Examiner:** Mr W. S. van Heerden | **External Examiner:** Mr W. H. K. Bester (Stellenbosch University)
**Duration:** 3 hours | **Total:** 40 marks | **Questions:** 31

> **Instructions:** Read the questions carefully and answer all questions. This test is closed book. Allowed references: Practical 2, 3, & 4 specifications, MIT/GNU Scheme Reference Manual, and SWI-Prolog Reference Manual.

---

## Question 1 *(1 point)*

Consider the following types of cost that can be associated with a programming language, and select the one that is **most relevant to consider in a modern computing context**.

- [ ] Cost of compiling programs
- [ ] Cost of executing programs
- [ ] Cost of reliability
- [ ] Cost of the language implementation system

---

## Question 2 *(1 point)*

Consider the following programming languages, and select the one that has the **highest level of portability**.

- [ ] Fortran I
- [ ] PL/I
- [ ] Swift
- [ ] Java

---

## Question 3 *(1 point)*

Consider the following programming languages, and select the one that had the **highest overall readability**.

- [ ] C++
- [ ] BASIC
- [ ] Ada
- [ ] C#

---

## Question 4 *(1 point)*

Consider the following programming languages, and select the one that **focused the most on the well-definedness** of the original language design.

- [ ] Fortran I
- [ ] ALGOL 68
- [ ] C
- [ ] C++

---

## Question 5 *(5 points)*

Write a Scheme function named `getZerosDoublePositives`, which is applied to one parameter: a simple numeric list `lst`. The function should yield (not print) a list containing the values in `lst`, in their original order, where **zero values remain unchanged**, **positive values are doubled**, and **negative values are omitted**.

*Examples:*
```scheme
(getZerosDoublePositives '())
; => ()

(getZerosDoublePositives '(-5))
; => ()   (negative values are omitted)

(getZerosDoublePositives '(-1 4 0 -3 12))
; => (8 0 24)   (-1 and -3 omitted; 4→8, 12→24; 0 unchanged)
```

**Allowed built-in functions:**
- **Function construction:** `lambda`, `define`
- **Binding:** `let` (complex forms like `let*` and named `let` are **not** allowed)
- **Arithmetic:** `+`, `-`, `*`, `/`, `abs`, `sqrt`, `remainder`, `modulo`, `min`, `max`
- **Boolean values:** `#t`, `#f`
- **Equality predicates:** `=`, `>`, `<`, `>=`, `<=`, `even?`, `odd?`, `zero?`, `negative?`, `eqv?`, `eq?`
- **Logical predicates:** `and`, `or`, `not`
- **List predicates:** `list?`, `null?`
- **Conditionals:** `if`, `cond`, `else`
- **Quoting:** `quote`, `'`
- **List manipulation:** `list`, `car`, `cdr`, `cons`
- **I/O:** `display`, `printf`, `newline`, `read`

Submit file `u99999999.scm` to slot **"Examination: Scheme Function"**.

**Did you submit?**
- [ ] True
- [ ] False

---

## Question 6 *(5 points)*

Write a Prolog proposition called `getNegativesNegatePositives(L1, L2)`, where L1 and L2 are both simple numeric lists. The proposition succeeds if L2 contains the values in L1 in their original order, where **negative values remain unchanged**, **positive values are negated**, and **zero values are omitted**.

*Examples:*
```prolog
?- getNegativesNegatePositives([0], X).
% X = []   (zero values are omitted)

?- getNegativesNegatePositives([1, 0, -2, 0], X).
% X = [-1, -2]   (1 negated to -1; -2 unchanged; zeros omitted)
```

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, the `is` operator, cuts, and the built-in `not` proposition. Do **not** use if-then, if-then-else, the semicolon (`;`) or pipe (`|`) operator outside of a list, or complex system predicates (including built-in `member`, `append`, `reverse`).

Submit file `u99999999.pl` to slot **"Examination: Prolog Proposition"**.

**Did you submit?**
- [ ] True
- [ ] False

---

## Question 7 *(1 point)*

Consider the following program code in a hypothetical programming language:

```
main() {
   var switch
   write("Do you wish to continue?")
   read(switch)

   while(switch) {
      var input
      write("Which action would you like to perform?")
      read(input)
      switch (input) {
         case 1: call action1()
                 break
         case 2: call action2()
                 break
      }
      write("Do you wish to continue?")
      read(switch)
   }
}
```

Identify and fill in the **kind of special word** that `switch` is in this program.

**Answer:** _______________

---

## Question 8 *(1 point)*

Consider the following statements about **accessing and modifying global variables in PHP, Python, and C**, and select the most correct.

- [ ] PHP's approach to accessing and modifying global variables is less writable than both Python and C.
- [ ] PHP's approach to accessing and modifying global variables is less reliable than both Python and C.
- [ ] PHP's approach to accessing and modifying global variables is less readable than both Python and C.
- [ ] PHP's approach to accessing and modifying global variables has a lower cost of execution than both Python and C.

---

## Question 9 *(1 point)*

Fortran supports **elemental array operations**, which are not supported in most other high-level languages. Select the reason that describes a **strong justification** for their inclusion in Fortran.

- [ ] Elemental array operations improve the orthogonality of Fortran.
- [ ] Elemental array operations make sense because their purpose is unambiguous.
- [ ] Elemental array operations make sense for the implementation method that Fortran uses.
- [ ] Elemental array operations make sense in the programming domain for which Fortran was designed.

---

## Question 10 *(1 point)*

Consider the following statements about **list comprehensions in Python**, and select the most correct.

- [ ] List comprehensions improve the readability of list operations in Python.
- [ ] List comprehensions improve the writability of list operations in Python.
- [ ] List comprehensions improve the reliability of list operations in Python.
- [ ] List comprehensions improve the cost of training programmers in Python.

---

## Question 11 *(1 point)*

Consider the following statements about **operator precedence and associativity in APL**, and select the most correct.

- [ ] Operator precedence and associativity in APL is highly orthogonal.
- [ ] Operator precedence and associativity in APL is very complex due to the large number of operators.
- [ ] Operator precedence and associativity in APL introduces a high cost of execution.
- [ ] Operator precedence and associativity in APL is unreliable.

---

## Question 12 *(1 point)*

Consider the following statements about **operators in Ruby**, and select the most correct.

- [ ] Operators in Ruby are implemented in a way that is not very orthogonal.
- [ ] Operators in Ruby are not very writable.
- [ ] Operators in Ruby have a high cost of execution.
- [ ] Operators in Ruby are very reliable.

---

## Question 13 *(1 point)*

Consider the following statements about **mixed mode arithmetic expressions in F# and C++**, and select the most correct.

- [ ] Mixed mode arithmetic expressions in F# are less readable than in C++.
- [ ] Mixed mode arithmetic expressions in F# are more writable than in C++.
- [ ] Mixed mode arithmetic expressions in F# have a higher execution cost than in C++.
- [ ] Mixed mode arithmetic expressions in F# are more reliable than in C++.

---

## Question 14 *(1 point)*

Consider the following program code in a hypothetical programming language:

```
main() {
   int input
   int total = 0

   while ((total <= 100) or ((input = read()) != EOF)) {
      total = total + input
   }
   write(total)
}
```

The program reads a file of numbers, adding values to a total until either the total exceeds 100 or the end of file is reached. Assume C-like syntax, assignment is an expression, `or` is a logical or, and `EOF` indicates end of file. Select the statement that most correctly describes a **problem** with this program.

- [ ] If the `or` operator is short-circuit evaluated a side effect will occur, which causes a problem.
- [ ] If the `or` operator is short-circuit evaluated a side effect will **not** occur, which causes a problem.
- [ ] If the `or` operator is **not** short-circuit evaluated a side effect will occur, which causes a problem.
- [ ] If the `or` operator is **not** short-circuit evaluated a side effect will not occur, which causes a problem.

---

## Question 15 *(1 point)*

Consider the following statements about **conditional targets**, and select the most correct.

- [ ] Conditional targets reduce the writability of assignments.
- [ ] Conditional targets increase the readability of assignments.
- [ ] Conditional targets increase the cost of execution of assignments.
- [ ] Conditional targets reduce the reliability of assignments.

---

## Question 16 *(1 point)*

Consider the following statements about **multiple-target multiple-source assignments in Ruby**, and select the most correct.

- [ ] Multiple-target multiple-source assignments make Ruby more writable.
- [ ] Multiple-target multiple-source assignments make Ruby more readable.
- [ ] Multiple-target multiple-source assignments make Ruby more reliable.
- [ ] Multiple-target multiple-source assignments decrease the cost of execution of Ruby.

---

## Question 17 *(1 point)*

Consider the following statements about the method that **Python and Perl** use to **disambiguate nested selectors**, and select the most correct.

- [ ] Python's approach is less writable than Perl's approach.
- [ ] Python's approach is less readable than Perl's approach.
- [ ] Python's approach can be less reliable than Perl's approach.
- [ ] Python's approach has a higher cost of execution than Perl's approach.

---

## Question 18 *(1 point)*

Consider a situation where you have two variables `first` and `second`. You wish to assign different values to `second` depending on the value of `first`, using a **multiple-way selection** where the control expression is `first`. Select the programming language that allows you to achieve this in the **most writable** way.

- [ ] C++
- [ ] JavaScript
- [ ] C#
- [ ] Ruby

---

## Question 19 *(1 point)*

Consider the following statements about **counter-controlled loops in C++**, and select the most correct.

- [ ] Counter-controlled loops in C++ are reliable because the loop body always executes a fixed number of times, which is clear from the three control expressions at the start of the loop.
- [ ] Counter-controlled loops in C++ are reliable because it is possible to include the definition of the loop variable in the first control expression at the start of the loop.
- [ ] Counter-controlled loops in C++ are unreliable because it is possible to branch into the loop body.
- [ ] Counter-controlled loops in C++ are unreliable because it is not possible to modify how many times the loop body executes once execution has entered the loop.

---

## Question 20 *(1 point)*

Consider the following statements about **user-located loop control mechanisms in Java and C++**, and select the most correct.

- [ ] Java has more writable user-located loop control mechanisms than C++ does.
- [ ] Java has less writable user-located loop control mechanisms than C++ does.
- [ ] User-located loop control mechanisms are equally writable in Java and C++.
- [ ] Java has less reliable user-located loop control mechanisms than C++ does.

---

## Question 21 *(1 point)*

Consider the following program code in Ruby:

```ruby
def doSomething()
  num = 3
  while num > 0
      yield num
      num = num - 1
  end
end
```

Provide the **output** if the `doSomething` subprogram is used with a block that has a single formal parameter and prints it followed by a single space. Provide just the numeric output, without any punctuation.

**Answer:** _______________

---

## Question 22 *(1 point)*

Some programming languages allow **default values** to be given to a formal parameter when an actual parameter is left out. Select the option that most correctly describes a mechanism that allows **any** actual parameter to be left out of a subprogram call, regardless of the order in which the formal parameters are listed.

- [ ] By using positional parameters.
- [ ] By using keyword parameters.
- [ ] It is impossible to allow any actual parameter to be left out of a subprogram call, regardless of the order in which the formal parameters are listed.
- [ ] Subprograms always allow any actual parameter to be left out of a subprogram call, regardless of the order in which the formal parameters are listed.

---

## Question 23 *(1 point)*

Consider the following statements about **subprograms in Ruby**, and select the most correct.

- [ ] Ruby does not allow a subprogram to have a variable number of parameters.
- [ ] Ruby allows subprograms to have a variable number of parameters, but all the parameters must have the same type because the parameters are stored in an array of a fixed type.
- [ ] Ruby allows subprograms to have a variable number of parameters of any type because the parameters are stored in an array of objects.
- [ ] Ruby allows subprograms to have a variable number of parameters of any type because the parameters are stored in an array, and are all dynamically typed.

---

## Question 24 *(1 point)*

The following C++ program code is not legal:

```cpp
int doSomething(int val) {
   return val + 2;
}

float doSomething(int val) {
   return val + 1.0;
}
```

Select the option that most correctly describes the **underlying reason** for this being illegal.

- [ ] The fact that C++ does not support overloaded subprograms.
- [ ] The fact that variables of different types cannot be added.
- [ ] The fact that C++ performs a large number of coercions.
- [ ] The fact that C++ performs no coercions.

---

## Question 25 *(1 point)*

Consider the following JavaScript program code:

```javascript
function doSomething(a, b) {
   return function(y) {return (a + b) - y;}
}

var thing = doSomething(10, 20);
```

Select the option that most correctly describes what `thing` is.

- [ ] The function `function(y) {return (a + b) - y;}`
- [ ] The function `function(y) {return (10 + 20) - y;}`
- [ ] A reference to the `doSomething` function.
- [ ] An invalid function, because a value for `y` cannot be specified.

---

## Question 26 *(1 point)*

Consider the following statements about **pass-by-result parameters**, and select the most correct.

- [ ] Pass-by-result parameters can be passed using a physical copy or an access path.
- [ ] Pass-by-result parameters can be passed using only a physical copy because using an access path would create a functional side effect.
- [ ] Pass-by-result parameters can be passed using only a physical copy because the formal parameter is deallocated once the function terminates.
- [ ] Pass-by-result parameters can be passed using only an access path because a physical copy would take up additional memory and processing time.
- [ ] Pass-by-result parameters can be passed using only an access path because a physical copy would cause the calling function to work with an out-of-date copy of the formal parameter.

---

## Question 27 *(1 point)*

Consider the following statements about **multidimensional arrays as subprogram parameters in C and C#**, and select the most correct.

- [ ] The approach to passing multidimensional arrays in C is more writable than the approach used in C#.
- [ ] The approach to passing multidimensional arrays in C is more readable than the approach used in C#.
- [ ] The approach to passing multidimensional arrays in C is more reliable than the approach used in C#.
- [ ] The approach to passing multidimensional arrays in C is less orthogonal than the approach used in C#.

---

## Question 28 *(2 points)*

Consider a hypothetical programming language that supports **multiple inheritance**. Four classes A, B, C, and D are defined. Classes B and C both inherit only from A. Class D inherits from both B and C. An **implicit name collision** is possible. Select **only** the implementation details that together result in an implicit name collision (not explicit). *(Incorrectly selected options will be penalised.)*

- [ ] Defining a method named `myMethod` in class A.
- [ ] Defining a method named `myMethod` in class B.
- [ ] Defining a method named `myMethod` in class C.
- [ ] Defining a method named `myMethod` in class D.

---

## Question 29 *(2 points)*

You wish to implement a linked list and its nodes. Select **only** the programming language constructs that can be used to implement the **linked list nodes**. *(Incorrectly selected options will be penalised.)*

- [ ] A `struct` in C#
- [ ] A `struct` in C++
- [ ] A `class` in C++
- [ ] A `union` in C++

---

## Question 30 *(1 point)*

Consider the following statements about **Ruby**, and select the most correct.

- [ ] Ruby has highly efficient primitive types.
- [ ] Ruby has support for a programmer to explicitly allocate and deallocate heap memory for objects.
- [ ] Ruby allows the programmer to choose between dynamic and static message binding.
- [ ] Ruby classes have very unreliable message interfaces.

---

## Question 31 *(1 point)*

Consider the following statements about **Java and C++**, and select the most correct.

- [ ] Java uses objects less exclusively than C++.
- [ ] Java supports some of the benefits of multiple inheritance, while preventing name collisions.
- [ ] Java supports some of the benefits of multiple inheritance, but does not prevent name collisions.
- [ ] Java exclusively supports dynamic message binding, while C++ allows the programmer to choose between dynamic and static message binding.
