<!-- Slide number: 1 -->

![Front Cover: Concepts of Programming Languages, Global Edition, by Robert W Sebesta](Picture8.jpg)
# Chapter 15Part 2
Functional Programming Languages

### Notes:

<!-- Slide number: 2 -->
# Chapter 15 Topics
Introduction to Scheme
List Functions
Predicate Functions for Lists
Predicate Functions for Equivalence
The let Function
Example Scheme Functions
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# List Functions: quote
The Scheme interpreter
Always evaluates parameters of function applications

Lists have the same form as functions
(a b c) versus (member a list)
Lists should not be evaluated when they are parameters

The quote primitive function
Used to avoid parameter evaluation when not appropriate
Takes one parameter, returns parameter without evaluation
For example
		 (foo (quote (a b c))) rather than (foo (a b c))

Can be abbreviated with the apostrophe prefix operator
		 '(a b) is equivalent to (quote (a b))
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:
List functions are discussed in Section 6.9 of the textbook.

In the example, (foo (quote (a b c))), the function named foo is applied to one parameter (a list containing the atoms a, b, and c). We prefer using (foo ‘(a b c)) instead, because it is easier to read and less typing.

In the example, (foo (a b c)), we are first applying the function named a to the parameters b and c, getting the result, and then applying the function named foo to the result. If there is no function named a, the interpreter will give you an error.

What this implies is that a quote must be included whenever a list is used as a parameter.

<!-- Slide number: 4 -->
# List Functions: list function
The list function
Takes any number of parameters
Yields a list with the parameters as elements
	  (list 'a 'b 'c) yields (a b c)
    (list 'a 'b '(c d)) yields (a b (c d))
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:
Note how single symbolic atoms must also be quoted when they’re used as parameters. Without the quote, Scheme will interpret them as names. Therefore, a is interpreted as the name a, while ‘a is interpreted as a symbolic atom a. The atoms in quoted lists (in this example, c and d) aren’t quoted, because the lists aren’t being interpreted as functions.

The parameters of list are inserted without modification into the returned list. Therefore:

(list ‘(a) ‘(b) ‘(c)) yields ((a) (b) (c))
(list ‘(a) ‘b ‘c) yields ((a) b c)
(list ‘(a)) yields ((a))

<!-- Slide number: 5 -->
# List Functions: car and cdr
List functions in Scheme
The car function yields first element of its list parameter
    (car '(a b c)) yields a
    (car '((a b) c d)) yields (a b)
    (car 'a) produces an error
    (car '()) produces an error

The cdr function yields remainder of its list parameter after first element has been removed
       (cdr '(a b c)) yields (b c)
       (cdr '((a b) c d)) yields (c d)
       (cdr '(a)) yields ()
       (cdr 'a) produces an error
       (cdr '()) produces an error
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:
Lists in Scheme are immutable. This means that functions producing lists as a result generate a new list (in other words, a cdr produces a new list, not a pointer or reference into the parameter list).

Note, in particular, that the result of a cdr on a list containing a single element is an empty list. It helps if you think about lists as containers for elements, where the last element is implicitly an empty list. This idea is often used as a base case in a recursive function, to determine when the end of the list has been reached.

<!-- Slide number: 6 -->
# List Functions: cons function
List functions in Scheme
The cons function puts its first parameter into its second parameter, a list, to make a new list
       (cons 'a '(b c)) yields (a b c)
       (cons '(a b) '(c d)) yields ((a b) c d)
       (cons '() '(a b)) yields (() a b)

       (cons 'a '()) yields (a)

       (cons 'a 'b) yields the dotted pair (a . b)
       (cons '(a b) 'c) yields the dotted pair ((a b) . c)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:
Lists in Scheme are immutable. This means that cons does not modify any parameters, but produces a new list.

If the second parameter of a cons is an empty list, the result is simply the first parameter placed inside a list. So the result of (cons ‘a ‘()) is (a), while the result of (cons ‘(a b) ‘()) is ((a b)).

If the last parameter of cons is a single element, you get what is called a dotted pair, which does not work like a list. Generating a dotted pair is usually not what you want when working with lists. If you get output with dots in when you expect a list, you are probably trying to apply cons with a second parameter that is an atom. Try using list instead of cons if this happens.

Dotted pairs do have a use in Scheme. They are essentially key-value pairs. We won’t be using them for this purpose, however.

<!-- Slide number: 7 -->
# List Predicates: list? & null?
The list? predicate function
Takes one parameter
Yields #t if parameter is a list, #f otherwise
The null? predicate function
Takes one parameter
Yields #t if parameter is empty list, otherwise yields #f
Note that the parameter must be completely empty
null? will yield #t if the parameter is ()
null? will yield #f if the parameter is (())
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# Equivalence Predicates: eqv?
The eqv? predicate function
Yields #t if two values are the same
Works for both symbolic and numeric atoms
For example
		 (eqv? 3 3) yields #t
		 (eqv? 'a 'a) yields #t
		 (eqv? 'a 'b) yields #f
		 (eqv? 3.4 (+ 3 0.4)) yields #t
Does not work for lists
		 (eqv? '(a b) '(a b)) yields #f
Floats and integers are different values
		 (eqv? 3.0 3) yields #f
		 (= 3.0 3) yields #t

Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:
The last point highlights that we should generally use the = function for comparing numeric atoms. The eqv? function is usually used only to compare symbolic atoms like ‘a and ‘b.

<!-- Slide number: 9 -->
# Equivalence Predicates: eq?
The eq? predicate function
Yields #t if two parameters are the same object in memory (i.e. performs a pointer comparison)
Examples
 (eq? 'a 'a) yields #t
 (eq? 'a 'b) yields #f
 (eq? 'a '(b c)) yields #f
Note: For two list parameters, the result is not reliable
 (eq? '(a b) '(a b)) yields #t or #f
Note: eq? is not reliable for numeric atoms
 (eq? 3.4 (+ 3 0.4))) yields #t or #f
In most cases eqv? is more appropriate than eq?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:
In this case, “not reliable” means that the result is dependent on context in a program and the Scheme interpreter’s implementation. Depending on how lists and numeric atoms are created on a lower level, the results vary (sometimes they are the same object in memory, sometimes not).

<!-- Slide number: 10 -->
# The let Function
General form:
   (let
     (
       (name_1 expression_1)
       (name_2 expression_2)
       ...
       (name_n expression_n)
     )
     body
   )
Semantics
Bindings: Evaluate expressions, bind their values to names
Body: Evaluate using names in bindings
The let function yields the value of the body
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:
The let function is discussed in Section 5.5.2 of the textbook.

Remember that name bindings can also be performed by the define function. The difference between a name binding using a let is that the name is defined only in the body of the let function. A name binding performed using the define function holds for the entire program.

<!-- Slide number: 11 -->
# The let Function
(define (computation a b c d)
  (let
    (
      (top (+ a b))
      (bottom (- c d))
    )
    (/ top bottom)
  )
)
(define (computation a b c d)
  (let
    (
      (top (+ a b))
      (bottom (- c d))
    )
    (display (/ top bottom))
    (newline)
    (* top bottom)
  )
)
Multiple function applications allowed in the body
Function applications are evaluated in sequence
The let construct yields the value of the last application
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:
In both of these examples, we are defining a function named computation, which is applied to four parameters (a, b, c, and d).

In the first example, (+ a b) is evaluated, yielding a numeric result, which is then bound to the name top. Similarly, (- c d) is evaluated, yielding a numeric result, which is then bound to the name bottom. Note that top and bottom are names, not variables. This means that they behave like constants. You cannot do something like increment the value of top or bottom. Finally, (/ top bottom) is evaluated, producing a numeric result. Because this is the last function application in the body of the let, the entire let evaluates to the result of the division. The let, in turn, is the last function in the body of the computation function, and so the entire computation function also yields the result of the division.

In the second example, the same two bindings to top and bottom are performed. In the body of the let, there are three function applications. The first function application first results in (/ top bottom) being applied, the result of is printed to the screen by the display function. Next, the newline function is evaluated, printing a newline character. Finally, the function (* top bottom) is applied, which yields a numeric result. This is the final function application in the body of the let, so the entire let evaluates to the result of the multiplication. The let, in turn, is the last function in the body of the computation function, and so the entire computation function also yields the result of the multiplication.

<!-- Slide number: 12 -->
# Example Scheme Function: member
The member function
Applied to an atom (atm) and a simple list (lis)
Yields #t if atom is in the list, #f otherwise
Strategy: Recursively compare atm to each list atom; Return #t if atm found, #f if all list atoms are exhausted

		(define (member atm lis)
		   (cond
		      ((null? lis) #f)
		      ((eqv? atm (car lis)) #t)
		      (else (member atm (cdr lis)))
		   )
		)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:
In the second semester test and exam, I will ask you to write code. The programs will never be more complex that the ones in these slides. I very strongly recommend that you ensure that you can write the programs in the Scheme practical as well.

This example defines a function named member, which is applied to two parameters, atm (the atom being searched for) and lis (the list in which we’re searching for atm).

The function is recursive, because it uses the member function. It has two base cases, and one recursive case.

Our strategy is as follows: We check to see if the first item in the list is the atom we’re looking for. If it is, the result is true (we’ve found the item). If it isn’t, we ignore the first item in the list, and do a membership test on the remaining items. We keep doing this until either we’ve found the atom we’re looking for, or we run out of elements. If we run out of elements, we know the item isn’t in the list, and the result is false.

The first base case is if the list is empty (tested by null?). This happens if either an empty list is provided as input when the user calls member, or if we’ve run out of elements to check (i.e. the entire list has been searched). In both cases we haven’t found atm, so the result of the member function is #f.

The second base case is if the head of the list (retrieved using car) is equivalent to atm (the atom we’re looking for). If this is the case, we know we’ve found the atom, so the result is #t.

Finally, the recursive case removes the first element of the list (we only want the tail) using the cdr function. We then recursively apply the member function to the tail of the list. This call will continue executing while there are elements in the list, and will eventually lead to the first base case (because we’ve ignored the only element left in the list, and the cdr of the list is now an empty list).

It’s important to note that we have to solve this problem recursively, because there are no loops in Scheme (there are no loops because there are no variables). What does this imply about the efficiency and resource usage of the Scheme program in comparison to an implementation in a language like C++?

Also note the order of the cases. The two base cases must be before the recursive case, otherwise we will get an infinite recursion. Can you explain why this will happen? It is also necessary for the null? test to appear before the eqv? comparison. What will happen if the list is empty and the eqv? test happens before the null? test (hint: look at the car function)?

Also note that the textbook uses the eq? function rather than the eqv? function. Both work, but I recommended that eqv? be used instead of eq? due to reliability concerns.

<!-- Slide number: 13 -->
# Example Scheme Function: equalsimp
The equalsimp function
Applied to two simple lists (lis1 and lis2)
Yields #t if lis1 and lis2 are equal, #f otherwise
Strategy: Recursively compare list element pairs; Yield #t if both lists are exhausted simultaneously, #f if an element pair is unequal or one list is exhausted before the other

		(define (equalsimp lis1 lis2)
		   (cond
		      ((null? lis1) (null? lis2))
		      ((null? lis2) #f)
		      ((eqv? (car lis1) (car lis2))
		         (equalsimp(cdr lis1)(cdr lis2)))
		      (else #f)
		   )
		)
Copyright © 2012 Addison-Wesley. All rights reserved.
1-13

### Notes:
This example defines a function named equalsimp, which is applied to two parameters, lis1 and lis2 (both lists). The lists are both “simple”, meaning that we assume they hold only atoms, and no sublists. The function results in a true if the lists contain exactly the same elements, and false otherwise.

The function is again recursive, because it uses the equalsimp function. It has three base cases, and one recursive case.

Our strategy is as follows: We compare the first element in each list. If we see that they’re the same, we can continue checking the rest of the lists by ignoring the first elements of each and testing the tails. We can conclude they the lists aren’t the same if we find one pair of elements that doesn’t match. Also, if one of the lists runs out of elements before the other, the lists are different lengths, so we can conclude that they aren’t equal.

The first two base cases deal with either the first or second list being empty. Look at the first base case. It tests whether the first list is empty. If the first list is empty, then we need to look at the second list. If the second list is also empty, then the two lists are equal (they are both empty lists). If the second list is not empty (it contains one or more elements), then the lists obviously aren’t equal (lis2 is longer than lis1). In other words, if the second list is empty, the null? function produces a #t result, and the equalsimp function’s result is also #t. If the second list is not empty, the null? function produces a #f result, which also becomes the result of equalsimp.

Let’s look at the second base case. Remember that the first base case has eliminated the possibility that lis1 is empty. So if lis2 is empty, we know lis1 must be longer than lis2, and therefore the lists are not equal. The result is therefore #f, and we don’t need to check whether lis1 is empty.

The final base case is for when both lists still have elements, but we’ve found that the first elements in each don’t match. Obviously we know that the lists can’t be equal in this case. Now we could have checked for that explicitly (can you write the predicate that would test this?), but because the recursive case needs to handle the situation where the first elements in each list match, we can simply specify it as the else part, which will be used if none of the previous tests are successful. If we have eliminated all the conditions before the else, we can see that the only other outcome possible is if the first elements in the lists don’t match, and the result must be #f.

Now for the recursive case. What we want to do here is confirm that the first elements of the two lists are the same. This is done using the eqv? function on the car of each list. If the elements match, we know we can continue testing the remaining elements in the lists. So we ignore the first elements (we’ve already found that they’re the same) and call the equalsimp function itself on the cdr of each list. This will continue until either the first list or the second runs out of elements before the other list (the first two base cases), an element is found that doesn’t match (the final base case), or both lists run out of elements at the same time (the first base case again). Only in the last case do we get a #t.

Again, we have to solve this problem recursively, not iteratively.

Now consider the order of the base and recursive cases. What happens if we move the recursive case to the top of the cond? What happens if we place the null? check on lis2 above the null? check on lis1? If we have an explicit test to check for when the first elements in the lists don’t match, where can we place it?

Again, note that this example used the eqv? function, while the textbook uses the eq? function. The eqv? function is preferred.

<!-- Slide number: 14 -->
# Example Scheme Function: equal
The equal function
Applied to two general lists (lis1 and lis2)
Yields #t if the two lists are equal, #f otherwise
Strategy: Same as equalsimp, but adapted to compare atoms and lists; Use equal to compare list element pairs

		(define (equal lis1 lis2)
	  	   (cond
		      ((not (list? lis1))(eqv? lis1 lis2))
		      ((not (list? lis2)) #f)
		      ((null? lis1) (null? lis2))
		      ((null? lis2) #f)
		      ((equal (car lis1) (car lis2))
			   (equal (cdr lis1) (cdr lis2)))
		      (else #f)
		   )
		)
Copyright © 2012 Addison-Wesley. All rights reserved.
1-14

### Notes:
The issue with the previous program is that it doesn’t work if we have sublists in either lis1 or lis2. Why is this? Because eqv? always yields #f when it compares lists. This function overcomes this problem.

Compare this function to equalsimp. You’ll see that the three base cases and the recursive case are almost the same. Firstly, we’ve replaced the eqv? function with another recursive call to the equal function. What is the result of this? Because the equal function tests whether two lists are equal, it will now be able to compare items in lis1 and lis2 that are also lists. Are we done? Not yet. We’ve now also removed the mechanism for testing individual atoms (we don’t use eqv? in the predicate of the recursive case, and equalsimp doesn’t have base cases to deal specifically with atoms). So how do we solve this? We need to add base cases to handle atoms.

The additional base cases are at the top of the program. The first one tests whether lis1 is not a list. This will only be the case if lis1 is an atom. In that case we use eqv? on lis1 and lis2. Remember that eqv? yields #t if its parameters are atoms that are the same, and #f otherwise. So if lis1 is an atom, and lis2 is the same atom, the result is #t. Obviously if lis1 and lis2 are different atoms, the result is #f. What if lis1 is an atom, but lis2 is a list? The eqv? fails, and the result is #f, as we expect. So all of these cases are handled by the first base case.

Now let’s consider what we haven’t handled yet. We need to look at the case where lis1 is a list, and lis2 is an atom. This is handled by the second base case, which is triggered if lis2 is not a list (i.e. an atom). Because of the first base case, we know lis1 can’t be an atom, so it must be a list. So the second base case only handles the case where lis1 is a list, and lis2 is an atom. In this case the result must obviously be #f.

Again, note that this example used the eqv? function, while the textbook uses the eq? function. The eqv? function is preferred.

<!-- Slide number: 15 -->
# Example Scheme Function: append
The append function
Applied to two lists (lis1 and lis2)
Yields new list containing the elements of lis1 followed by the elements of lis2
Why can’t we use the list function to do the appending?
Why can’t we cons elements of lis2 to lis1 in order?
Strategy: cons elements of lis1 to lis2 in reverse order

		(define (append lis1 lis2)
	  	   (cond
		      ((null? lis1) lis2)
		      (else (cons (car lis1) (append (cdr lis1) lis2)))
		   )
		)
(append (a b) (c d)) → (cons a (b c d))
(append (b) (c d)) → (cons b (c d))

(append (a b) (c d)) → (cons a (b c d)) → (a b c d)
(append (b) (c d)) → (cons b (c d)) → (b c d)

(append (a b) (c d)) → (cons a (append (b) (cd)))
(append (b) (c d)) → (cons b (append () (c d)))
(append () (c d)) → (c d)
(append (a b) (c d))
(append (b) (c d))
(append () (c d))

Copyright © 2012 Addison-Wesley. All rights reserved.
1-15

### Notes:
This example is a bit simpler than the previous one. Here we want to append lis2 to lis1.

The function has a base case and a recursive case. The base case handles the case where lis1 is empty. In this case the result is simply lis2, because it has been appended to nothing.

The recursive case adds the head of lis1 to the result of appending lis2 to the tail of lis1. So the result is that lis2 is passed along lis1, until the end of lis1 (remember, there is effectively an empty list at the end of every list). This produces lis2, and then we use cons to add the last element in lis1 to lis2. Then we add the second last element. Then the third last. And so on until we reach the first element in lis1, which is also added to the resulting list.

So we get something like this, given the code (append (A B) (C D)):
(cons A (append (B) (C D)))
Then (append (B) (C D)) => (cons B (append () (C D)))
Then (append () (C D)) => (C D)

And substituting results back as the recursive calls terminate:
(cons B (C D)) producing the list (B C D)
(cons A (B C D)) producing the list (A B C D)

Now try to answer the question on this slide (Hint: consider what will happen if you use cons to append C to (A B), and also what will happen if you use the list function instead of cons).
