<!-- Slide number: 1 -->
# Chapter 16Part 3
Logic Programming Languages

### Notes:

<!-- Slide number: 2 -->
# Chapter 16 Topics
The Basic Elements of Prolog
Simple arithmetic
List Structures
Deficiencies of Prolog
Applications of Logic Programming
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Simple Arithmetic
Prolog has integer variables and arithmetic
The is operator
Right operand is an arithmetic expression
Left operand is a variable
For example
		  A is B / 17 + C.
All variables on RHS must be instantiated
Variable on LHS must not be instantiated, and becomes instantiated with the value of the RHS
Not an assignment statement, so this is illegal
		  Sum is Sum + Number.
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:
The last example is always illegal. If Sum is instantiated, the LHS is instantiated, which is illegal. If Sum is not instantiated, the RHS has an uninstantiated variable, which is also illegal.

<!-- Slide number: 4 -->
# Simple Arithmetic: Example
Consider this query:
  ?- distance(chevy, X)

Instantiations caused by this query:
  speed(chevy, Speed)
  Speed to 105
  time(chevy, Time)
  Time to 21
  Y to 105 * 21 (i.e. 2205)

Therefore Prolog answers:
  X = 2205
speed(ford, 100).
speed(chevy, 105).
speed(dodge, 95).
speed(volvo, 80).

time(ford, 20).
time(chevy, 21).
time(dodge, 24).
time(volvo, 24).

distance(X, Y) :- speed(X, Speed),
                  time(X, Time),
                  Y is Speed * Time.
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:

<!-- Slide number: 5 -->
# Numeric Equalities and Inequalities
Prolog supports inequality comparisons
Equal to: = (note that this is not an assignment)
Less than: <
Greater than: >
Less than or equal to: =<
Greater than or equal to: >=
Can be used as terms
		  lessThan(X, Y) :- X < Y.
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# List Structures
The list
Lists are the second basic data structure
In addition to atomic propositions
A sequence of any number of elements
Atoms
Atomic propositions, and/or
Other lists
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:

<!-- Slide number: 7 -->
# List Structures
Examples of lists
Simple list of atoms
 	    [apple, prune, grape]
Complex list
	    [[a, b], son(X, bob)]
Empty list
	    []
List with one element, X
	    [X]
List with head X and tail Y
	    [X | Y]
List with X1 and X2, followed by tail Y
	   [X1, X2 | Y]
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# List Structures
When writing list processing propositions
Use same recursive strategy as Scheme
But remember that there are no “returns” in Prolog
The result is defined as a parameter
Base and recursive cases are separate statements
Base cases: often atomic propositions using variables
Recursive cases: rules using variables
We also don’t specify negative (false) cases
Order of statements is important
Prolog matches from top to bottom
Base case statements should appear first
This means Prolog isn’t entirely context-independent
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:
We’ll illustration of how we don’t specify negative cases in the upcoming member proposition.

<!-- Slide number: 9 -->
# List Structures
During list processing (also elsewhere)
A value might not be relevant
For example, we might need to ignore the head
We can use an underscore character
An anonymous variable
We don’t care what unification instantiates it to
Typically replaces a variable that is unused to define a result in an atomic proposition or a rule
Just simplifies code (not strictly speaking required)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:

<!-- Slide number: 10 -->
# List Structures: Examples
A member proposition
If member(X, Y) is true, the term X is a member of list Y
​member(a, [b, a, c]) should be true
Recursive strategy: A term is a member if it is either the head of a list, or a member of the tail of the list
The base case should be placed before the recursive step, since it should be matched first

		member(Element, [Element | _]).
		member(Element, [_ | Lis]) :- member(Element, Lis).

Valid queries:
	?- member(a, [d, b, c]).
	?- member(X, [a, b, c]).
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:
Read the proposition as follows: An element is a member of a list if it is the first element in the list. An element is also a member of a list if the element is a member of the tail of the list.

Note that you need separate proposition definitions, one for the base case (the first proposition definition), and one for the recursive case (the second proposition definition, because it uses the member proposition itself).

Compare this to the member function in Scheme. The biggest difference is that we don’t have to define a proposition that handles an empty list (in Scheme, this was done using the null? function). This is because an element cannot be a member of an empty list. We therefore don’t even have to consider this possibility in Prolog, because we are only writing the proposition to define a situation in which an element is a member of a list. The proposition will automatically be false if we try to find membership of an empty list (either because we are directly testing whether an element is a member of an empty list, or we’ve reached the end of our recursive search for the element). This is an illustration of the fact that we don’t specify negative cases in Prolog, as mentioned earlier.

One of the nice features in Prolog is that you can construct any queries that make sense for the propositions your rules define:
member(a,[d, b, c]) will result in “false”
member(X,[a, b, c]) will result in “X = a”, followed by “X = b”, and “X = c” if you re-query Prolog.

Note that no additional code is required to get these queries to work. Prolog’s inferencing engine handles the query for you.

<!-- Slide number: 11 -->
# List Structures: Examples
An append proposition
If append(X, Y, Z) is true, list Y appended to list X makes list Z
​append([a, b], [c, d], [a, b, c, d]) should be true
Recursive strategy: Append the second list to the first list’s tail to give a result, then prepend the head of the first list to the result

		append([], Lis, Lis).
		append([Head | Lis_1], Lis_2, [Head | Lis_3]) :-
			append(Lis_1, Lis_2, Lis_3).

Valid queries:
		?- append([a, b], [c, d], [a, b, c, d]).
		?- append([a, b], [c, d], X).
		?- append([a, b], X, [a, b, c, d]).
		?- append(X, [c, d], [a, b, c, d]).
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:
Read the proposition as follows: If you append a list to an empty list, the result is the appended list. If you append a list to a second non-empty list, the result is the head of the second list, followed by the result of appending the first list to the tail of the second list.

Compare this to the Scheme implementation of the append function, and you will see that the append proposition uses the same strategy. In this case, we do have to define a proposition for the case where the first list is empty, because the append proposition is still valid if we’re appending to an empty list.

Note the various ways in which the append proposition can be used:
The first asks “if [c, d] is appended to [a, b], is the result [a, b, c, d]?” Prolog will repond with “true”
The second asks ”if [c, d] is appended to [a, b], what is the result?” Prolog will respond with “X = [a, b, c, d]”
The third asks “what needs to be appended to [a, b] to produce [a, b, c, d]?” Prolog will respond with “X = [c, d]”.
The fourth asks “what does [c, d] need to be appended to produce [a, b, c, d]?” Prolog will respond with “X = [a, b]”.

<!-- Slide number: 12 -->
# List Structures: Examples
A reverse proposition
If reverse(X, Y) is true, list Y is the reversed version of list X
​reverse([a, b, c], [c, b, a]) should be true
Recursive strategy: Append the head of the first list to the reversed version of its own tail

		reverse([], []).
		reverse([Head | Tail], List) :-
			reverse(Tail, Result),
			append(Result, [Head], List).

Valid queries:
		?- reverse([a, b, c], [c, b, a]).
		?- reverse([a, b, c], X).
		?- reverse(X, [a, b, c]).
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:
Read the proposition as follows: The reversed version of an empty list is an empty list. The reversed version of a non-empty list is the head of the list appended to the reverse of the tail of the list.

Note that, in the recursive call, we have to place Head in brackets. This is because Head is an element in the first parameter’s list. The append proposition assumes it is appending one list to another list, not an element to a list. We therefore make Head into a single element list by simply placing brackets around it. Note that no additional syntax is necessary to achieve this, as was the case in Scheme.

Given the three queries:
The first asks “is [c, b, a] the reverse of [a, b, c]?” Prolog responds with “true”
The second asks “what is the reverse of [a, b, c]?” Prolog responds with “X = [c, b, a]”.
The third asks “what is [a, b, c] the reverse of?” Prolog responds with “X = [c, b, a]”.

<!-- Slide number: 13 -->
# Deficiencies of Prolog
Prolog has several deficiencies
Resolution order control
The closed-world assumption
The negation problem
Intrinsic limitations
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:

<!-- Slide number: 14 -->
# Deficiencies of Prolog
Resolution order control
Prolog always matches from top to bottom through facts and rules, and left to right through subgoals

The programmer can affect efficiency
For example, one can place rules that are more likely to succeed higher up in the program
How else could a programmer affect efficiency?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:

<!-- Slide number: 15 -->
# Deficiencies of Prolog
The closed-world assumption
Prolog can only prove things using facts and rules
Assume that a query is made
If Prolog answers “true”
It means the query can be proven true
If Prolog answers “false”
It means the query cannot be proven
	(not that it is necessarily false)
How could we get a “false”, even if the query is true?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:

<!-- Slide number: 16 -->
# Deficiencies of Prolog
The negation problem
It is difficult to handle logical negations in Prolog
Assume the following propositions

		 parent(bill, jake).
		 parent(bill, shelley).
		 sibling(X, Y) :- parent(M, X), parent(M, Y).

Give the following query:

		 ?- sibling(X, Y).
		 X = jake, Y = jake

We can rewrite the sibling rule as:

		 sibling(X, Y) :- parent(M, X), parent(M, Y), not(X=Y).
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:
The query instantiates both X and Y to jake, because these instantiations lead from the goal to a fact, and nothing tells Prolog that X and Y may not be the same. If we re-query Prolog, we will also get the valid instantiations “X = jake, Y = shelley”, “X = shelley, Y = jake”, and “X = shelley, Y = shelley”.

<!-- Slide number: 17 -->
# Deficiencies of Prolog
The negation problem
However, not doesn’t work like a true logical NOT
The not operator succeeds if its parameter fails
Parameter fails if Prolog can’t prove its truth
Doesn’t mean that the parameter is necessarily false

Therefore, not(X=Y)
Means resolution cannot prove that X is the same as Y
In other words, there are no facts stating they are equal
Doesn’t mean that X is not equal to Y
To properly establish that two atoms are unequal would require a separate fact for each pair of atoms (impractical)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:
While not technically ideal, not(X=Y) works well enough for the example on the previous slide.

One of the consequences of the negation problem is that a query like not(not(member(X, [a, b, c]))) does not result in the expected Prolog response “X = a”. You can read more about what happens with such a query in the textbook.

<!-- Slide number: 18 -->
# Deficiencies of Prolog
Intrinsic limitations
Some tasks are impossible to specify efficiently
For example:

        sort(Old_list, New_list) :- permute(Old_list, New_list),
					      sorted(New_list).

        sorted([]).
        sorted([X]).
        sorted([X, Y | List]) :- X <= Y, sorted([Y | List]).

How does this proposition actually “sort” Old_list?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:
See the discussion on slide 18 for more detail.
