<!-- Slide number: 1 -->

![Front Cover: Concepts of Programming Languages, Global Edition, by Robert W Sebesta](Picture8.jpg)
# Chapter 15Part 3
Functional Programming Languages

### Notes:

<!-- Slide number: 2 -->
# Chapter 15 Topics
Introduction to Scheme
Tail Recursion in Scheme
An Apply-to-All Function
Functions That Build Code
Comparison of Functional and Imperative Languages
Copyright © 2012 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Tail Recursion in Scheme
Recursive functions
Slower than equivalent iterative constructs
Use more memory than equivalent iterative constructs
A tail recursive function
The recursive call is the last operation in the function
Implication
Interpreter can automatically converted to iteration
Makes the function much faster and resource efficient
Scheme language definition requires all tail recursive functions to be converted to iteration
Copyright © 2012 Addison-Wesley. All rights reserved.
1-3

<!-- Slide number: 4 -->
# Tail Recursion in Scheme
Rewriting to make a function tail recursive
(define (factorial n)
   (if (= n 0)
      1
      (* n (factorial (- n 1)))
   )
)
(factorial 3) → (* 3 2) → 6
(factorial 2) → (* 2 1) → 2
(factorial 1) → (* 1 1) → 1

(factorial 3) → (* 3 2)
(factorial 2) → (* 2 1)
(factorial 1) → (* 1 1)

(factorial 3)
(factorial 2)
(factorial 1)
(factorial 0)
(factorial 3) → (* 3 (factorial 2))
(factorial 2) → (* 2 (factorial 1))
(factorial 1) → (* 1 (factorial 0))
(factorial 0) → 1
(define (facthelper n partial)
   (if (<= n 1)
      partial
      (facthelper (- n 1) (* n partial))
   )
)

(define (factorial n)
   (facthelper n 1)
)

(facthelper 3 1) → 6
(facthelper 2 3) → 6

(factorial 3) → 6
(facthelper 3 1) → (facthelper 2 (* 3 1))
(facthelper 2 3) → (facthelper 1 (* 2 3))
(facthelper 1 6) → 6
(factorial 3)
(facthelper 3 1)
(facthelper 2 3)
(facthelper 1 6)
Copyright © 2012 Addison-Wesley. All rights reserved.
1-4

### Notes:
The first example is a standard recursive implementation for computing a factorial. Make sure you understand how it works. The result in this case is built up as follows (I’m using C style notation so that it’s easier to follow):

fact(3) = 3 * fact(2)
call fact(2) = 2 * fact(1)
call fact(1) = 1 * fact(0)
call fact(0) = 1

And then unwinding the recursive calls:

fact(1) = 1 * 1 = 1
fact(2) = 2 * 1 = 2
fact(3) = 3 * 2 = 6

This example is not tail recursive. Why? Because when the recursive case is evaluated, we first have to apply factorial to the result of (- n 1), and then we have to multiply n by the result of the factorial function. So * is the last function evaluated, not factorial. Also, as you can see, the result is computed during the unwinding of the recursive functions.

In the second example, we instead compute a partial result, and pass it along to the next recursive call. We also need to keep track of how many recursive calls we have left. The result is then simply returned as the recursive functions terminate. In other words:

factorial(3)
call facthelper(3, 1)
call facthelper(2, 3 * 1) = facthelper(2, 3)
call facthelper(1, 2 * 3) = facthelper(1, 6)

The last factpartial is 6, so the recursive call unwind as follows:

facthelper(1, 6) = 6
facthelper(2, 3) = 6
facthelper(3, 1) = 6
factorial(3) = 6

So you can see that the first parameter, n, is used to keep track of how many recursive calls we need to perform (it counts down from 3 to 1, almost like a loop control variable in a for loop, even though it isn’t a variable). The second parameter stores the partial result, which we modify with each recursive call.

It is clear that the second example is tail recursive, because the multiplication and subtraction are performed first, and the results are used as parameters for facthelper. Also, we compute the result through the initial recursive calls, and simply send the result back while the calls are unwinding.

<!-- Slide number: 5 -->
# An Apply-to-All Function
A functional form is a function that
Takes one or more functions as parameters, and/or
Yields a function as a result
Copyright © 2012 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# An Apply-to-All Function
Apply-to-all functional form
Apply a function to all elements of a list, building a new list
One approach in Scheme is the following mapcar function

	(define (mapcar fun lis)
	  (cond
	    ((null? lis) ())
	    (else (cons (fun (car lis)) (mapcar fun (cdr lis))))
		 )
	)

Assume square is a function that squares its parameter
		  (define (square x)
		    (* x x)
		  )

Function application (mapcar square '(3 4 2)) yields (9 16 4)
Copyright © 2012 Addison-Wesley. All rights reserved.
1-6

### Notes:
The mapcar function has two parameters, fun and lis. The fun parameter is a function, which must be applied to every element in lis.

So how does this work? Again, we solve it recursively. The recursive case (in the else code) handles the situation where there are still elements in list to process. It applies fun to the first element in the list (which we get using car). It then applies mapcar to the tail of lis (which we get using cdr). Finally, it creates a new list using cons, which contains the result of applying fun to the first element, appended to the list produced for the tail. The base case is used when we get to the end of lis. In this case, the result is just an empty list.

You can see in the example function application that we can use the square function as the first parameter, and have it applied to every element in the list. The recursive calls would look like this:

(mapcar square (3 4 2))
calls (cons (square 3) (mapcar square (4 2))) = (cons 9 (mapcar square (4 2)))
calls (mapcar square (4 2))
calls (cons (square 4) (mapcar square (2))) = (cons 16 (mapcar square (2)))
calls (mapcar square (2))
calls (cons (square 2) (mapcar square ())) = (cons 4 (mapcar square ()))
calls (mapcar square ())
calls (mapcar square ()) = ()

Then we unwind the recursive calls again:

(cons 4 ()) = (4)
(cons 16 (4)) = (16 4)
(cons 9 (16 4)) = (9 16 4)

The final result is a new list containing the values produced by applying the square function to the elements of the original list.

<!-- Slide number: 7 -->
# Functions That Build Code
A Scheme function can actually
Build Scheme code
Request the interpretation of the built Scheme code
This is possible (and easy) because
Functions can be represented as lists, and can be returned
The interpreter is a user-available function, called eval
This is much more difficult in imperative languages
Copyright © 2012 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# Functions That Build Code
A simple example

	  (define (adder lis)
	    (cond
	      ((null? lis) 0)
	      (else (eval (cons '+ lis)))
	    )
	  )

The parameter is a list of numbers to be added
Builds a new list from the + symbol and lis
Use cons to insert the atom + into the list of numbers
Be sure that + is quoted to prevent evaluation
Evaluates the new list
Submit the new list to eval for evaluation
Copyright © 2012 Addison-Wesley. All rights reserved.
1-8

### Notes:
This is just a simple example to illustrate how a function can build code that can be executed. We can obviously build code that is as complex as we like.

The adder function has one parameter, lis, which is a list of numeric atoms.

Let’s first look at the else part of the cond function. First we build a new list containing the + symbol, followed by the elements in lis. This is done this using a cons. Note that the + symbol must be quoted, because we don’t want it to be interpreted as the + function (which is provided by Scheme).

So, if we imagine that lis is the list (13 2 5), then the cons produces a new list (+ 13 2 5). You can see that this has the form of a normal Scheme function application, even though it’s just a list at this stage.

Now we can apply eval to the list built by the cons, which basically means “execute this list as if it had been typed into the Scheme interpreter”. What this does, of course, is apply the + function to the parameters 13, 2, and 5. The result is 20. Note that the numbers don’t need to be quoted, because they are simply numeric atoms, and can’t be confused with names.

Now let’s look at the first condition, which is trivial. It just makes sure that when someone calls (adder ()) we don’t attempt to create a function like (+), which will obviously produce an error when Scheme tries to evaluate it. So if the list is empty, we just produce 0 as a result.

Note that in DrRacket you must provide the following function application before you use the eval function:

(current-namespace (make-base-namespace))

<!-- Slide number: 9 -->
# Comparing Functional andImperative Languages
Imperative Languages
Efficient execution
Complex syntax and semantics
Concurrency is programmer designed
Functional Languages
Simple syntax and semantics
Inefficient execution
Programs can automatically be made concurrent
Copyright © 2012 Addison-Wesley. All rights reserved.
1-9

### Notes:

<!-- Slide number: 10 -->
# Some Final Notes
Slides contain extensive notes
If you need more explanation of the examples, including step-by-step execution traces, look at these notes
In tests and exams
I can ask theory questions
I can ask what the result is of Scheme code
I can ask you to explain how Scheme code executes
I can ask you to analyze or correct Scheme code
I can ask you to implement a Scheme function
Implementations will be no more complex than the examples we covered in these lectures
Be sure you understand the code examples
Be sure to do the functional programming practical
Copyright © 2012 Addison-Wesley. All rights reserved.
1-10

### Notes:
