<!-- Slide number: 1 -->
# Chapter 16Part 2
Logic Programming Languages

### Notes:

<!-- Slide number: 2 -->
# Chapter 16 Topics
An Overview of Logic Programming
The Origins of Prolog
The Basic Elements of Prolog
Terms
Fact Statements
Rule Statements
Goal Statements
Prolog Inferencing Process
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Overview of Logic Programming
Declarative semantics
There is a simple way to determine the meaning of each statement
Statement meaning is context-independent
Thus, logic programming language semantics is simpler than imperative language semantics
Programming is nonprocedural
Programs do not state how a result is to be computed, but rather the form of the result
Use predicate calculus (descriptive mechanism) and resolution (inferencing process)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:
Saying that statement meaning is context-independent means that the meaning of the statement can be determined from the statement itself, without referring to previous statements. In an imperative programming language this is not the case, because we need to understand the entire program’s execution up to the statement in order to understand the statement (e.g. if the statement uses a variable, we need to know what the variable’s value is). Context-independence also implies that the order of statements is unimportant. This isn’t strictly speaking true in Prolog, as we’ll see.

<!-- Slide number: 4 -->
# Example: Sorting a List
In an imperative language (procedural)
Describe an algorithm for sorting the list
Computer executes the steps of the algorithm
In a logic language (non-procedural)
Describe the characteristics of a sorted list, not the process of rearranging a list:

		sort(old_list, new_list)  permute(old_list, new_list)                  	                                                  sorted (new_list)

		sorted (list)  j such that 1 j<n, list(j)  list(j+1)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:
Consider the example program: new_list is a sorted version of old_list if new_list is a permutation of old_list, and the elements in new_list are also sorted. A list is sorted if the elements are ordered in ascending order. Note that this describes the characteristics of a sorted list, not how the list should be sorted. How would this program be executed? Prolog will repeatedly generate permutations of old_list, and test each one to see whether it is sorted. This process continues until one of the permutations is sorted. Clearly this is an inefficient process, which is one of the drawbacks to Logic programming, which we’ll look at towards the end of the chapter.

<!-- Slide number: 5 -->
# The Origins of Prolog
Development started in early 1970s
University of Aix-Marseille
Alain Colmerauer and Phillippe Roussel
Natural language processing
University of Edinburgh
Robert Kowalski
Automated theorem proving
Two main dialects exist
We will use Edinburgh syntax
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:

<!-- Slide number: 6 -->
# Prolog: Terms
Term
A constant, variable, or structure
Constant
An atom or an integer (e.g. 42)
Atom
A symbolic value in Prolog
Consists of either
A string of letters, digits and underscores starting with a lowercase letter (e.g. joe)
A string of any printable ASCII characters delimited by apostrophes (e.g. 'Some Atom')
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:
A symbolic value is an object we are reasoning about.

<!-- Slide number: 7 -->
# Prolog: Terms
Variable
String of letters, digits, and underscores starting with uppercase letter (e.g. X or MyVar)
Instantiation: Binding a variable to a value
Only happens during the resolution process
We’ll return to this later
Structure
Represents an atomic proposition
Syntax
		 functor(parameter1, parameter2, ...)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# Prolog: Statements
Three kinds of statements
Fact statements
Rule statements
Goal statements

Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:

<!-- Slide number: 9 -->
# Prolog: Fact Statements
Fact statements
Atomic propositions used for the hypotheses
Structures representing headless Horn clauses
Examples
		 female(shelley).
		 female(anna).
		 male(bill).
		 father(bill, jake).
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:
We’ve looked at atomic propositions before. Fact statements are represented and interpreted in the same way.

<!-- Slide number: 10 -->
# Prolog: Rule Statements
Rule statements
Used for the hypotheses
Headed Horn clauses
Right side: Antecedent (if part)
May be single term or conjunction of terms
Form of conjunction
Several terms separated by commas
Logical AND operators are implied by each comma
Left side: Consequent (then part)
Must be a single term
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:

<!-- Slide number: 11 -->
# Prolog: Rule Statement Examples
A specific rule (using atoms):
		ancestor(mary, shelley) :- mother(mary, shelley).

General rules use variables (universal objects):
		parent(X, Y) :- mother(X, Y).
		parent(X, Y) :- father(X, Y).
		grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
		sibling(X, Y) :- mother(M, X), mother(M, Y),
		                 father(F, X), father(F, Y).
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:
Logical “and” operators are represented using commas. A logical implication is specified using the :- notation. Implications work from right to left, so the right hand side of :- represents the antecedent, and the left hand side represents the consequent.

The first rule should be read as follows:
If mary is the mother of shelley, mary is the ancestor of shelley.
Note that specific rules are less useful than general rules, because general rules can reason about facts, while specific rules are just statements about facts.

The second set of rules:
If X is the mother of Y, then X is also the parent of Y.
If X is the father of Y, then X is also the parent of Y.
If X is the parent of Y, and Y is the parent of Z, then X is also the grandparent of Z.
If M is the mother of X, and M is the mother of Y, and F is the father of X, and F is the father of Y, then X is also the sibling of Y.

A logical or is not explicitly represented, but is implied by separate rules with the same antecedent, but different consequents.

<!-- Slide number: 12 -->
# Prolog: Goal Statements
Goals or queries are used in theorem proving
A theorem
A proposition Prolog must try to prove
A simple goal uses the syntax of a fact statement
Example (the ?- is a prompt Prolog often uses)
		 ?- man(fred).

Conjunctive propositions and propositions with variables are also legal goals
		 ?- parent(X, mike).
		 ?- parent(X, mike), male(X).

Conjunctive propositions made up of subgoals
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:
In the case of “man(fred)”, you are asking Prolog “Can you prove that fred is a man?” Prolog will respond with either “true” (meaning that it can prove this query holds), or “false” (meaning that Prolog can’t prove the query holds). Note that a “false” doesn’t necessarily mean that the query does not hold, just that Prolog can’t prove it given the facts and rules it has. Prolog may not be able to prove a query holds if you haven’t given it the facts or rules necessary to prove the query.

In the case of “parent(X,mike)”, you are asking Prolog “Can you find an X so that X is the parent of mike?” If Prolog can’t find an X to make the query hold, it will immediately respond with “false”. If Prolog can find an X to make the query hold, it will respond with “true” and a value of X that makes the query hold. You can re-query Prolog, which means “Can you find another X so that X is the parent of mike?” You can continue querying for a new X until Prolog can’t find any more values for X that make the query hold. Once this happens, Prolog responds with a “false”.

You can have multiple sub-queries, where each sub-query is separated by a comma (because all sub-queries must be proved to hold, a comma again represents a logical “and”).

Subgoals are illustrated in the case of “parent(X, mike), male(X)”, where the “parent(X, mike)” term is the first subgoal, and “male(X)” is the second subgoal. You are asking Prolog “Can you find an X so that X is the parent of mike, and X is also male?” If Prolog can’t find an X to make the “parent(X, mike)” proposition hold, it will immediately respond with “false”. If Prolog can find an X to make the query hold, it has satisfied the first subgoal, and moves on to the second, to try to prove that the same X is also a male. If Prolog can prove the second subgoal, it will respond with “true” and a value of X that makes the query hold. You can re-query Prolog, which means “Can you find another X so that X is the parent of mike, and X is also male?” You can continue querying for a new X until Prolog can’t find any more values for X that make the query hold. Once this happens, Prolog responds with a “false”. We’ll look at this process in more detail when discuss the inferencing process in the coming slides .

<!-- Slide number: 13 -->
# Prolog: Inferencing Process
To prove a goal or subgoal is true
Must find a chain of facts and rules
For goal Q, find fact A, such that
		 B :- A
		 C :- B
		   …
		 Q :- P

This process is called matching
Proving a subgoal is called satisfying the subgoal
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:

<!-- Slide number: 14 -->
# Prolog Inferencing Process: Approaches
Bottom-up resolution, or forward chaining
Begin with facts and rules
Attempt to find a sequence of matches that leads to goal
Works well with a large set of possibly appropriate facts
Top-down resolution, or backward chaining
Begin with goal
Attempt to find a sequence of matches that leads to facts
Works well with a small set of possibly appropriate facts
Prolog uses this approach
Compare bottom-up and top-down resolution
	father(bob).
	man(X) :- father(X).
?- man(bob).
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:
If forward chaining is used, we start with the facts. There is only one fact, so we start with:

father(bob).

Now we try to find a rule that will make man(bob) true. We find the rule:

man(X) :- father(X).

And can substitute bob for X, because this produces:

man(bob) :- father(bob).

and we already know that father(bob) holds. We see that we’ve established that man(bob) also holds, because of the rule, and we conclude that the query does hold.

========

If backward chaining is used, we start with the goal:

man(bob).

Now we want to find a path to a fact. We look at the rules first, and find:

man(X) :- father(X).

and can substitute bob for X because we have assumed that man(bob) holds. So we get:

man(bob) :- father(bob).

From this rule, we see that father(bob) must hold if man(bob) holds. Now we’ve found a path from the query to a fact, so the query must hold.

<!-- Slide number: 15 -->
# Prolog Inferencing Process: Subgoals
When goal has multiple subgoals, can use
Breadth-first search
Work on all the subgoals in parallel
Depth-first search
Find a complete proof for the first subgoal, then work on the second, and so on
Can be done with fewer computational resources
Prolog uses this approach
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:

<!-- Slide number: 16 -->
# Prolog Inferencing Process: Backtracking
Backtracking
Multiple subgoals, and we fail to prove one
Reconsider previous subgoal for different solution
Begin search where previous search left off
Can take lots of time and space
May find all possible proofs to every subgoal
Consider the goal
	?- male(X), parent(X, shelley).
Instantiates first X that is male, then tests if X is shelley’s parent.
If not, backtrack and try another X.

What makes this query suboptimal? How would you solve it?
Copyright © 2023 Addison-Wesley. All rights reserved.
1-16

### Notes:
Prolog always works from left to right when trying to prove sub-goals, and top to bottom when matching facts.

Given the last example, Prolog will end up searching for a long time if there are a lot of male(...) facts. The worst case scenario is if there is no fact (or rule) supporting that shelley has a male parent. In that case, all males will have to be checked before Prolog can respond with a “false”.

Can we solve this problem? If we restate the goal as follows:

parent(X,shelley), male(X).

Prolog will first try to find an X that is a parent of shelley, and then test whether that parent is male. If we assume that any person will have a maximum of two parents, this means Prolog will have to go through a maximum of only two instantiations for X before either finding an object that satisfies the subgoals, or concluding that it can’t prove the goal.

Note that this breaks Prolog’s context independence, because it should not matter which order the subgoals appear in.

<!-- Slide number: 17 -->
# Prolog Inferencing Process:Tracing Model
Prolog has a built-in trace structure
Displays variable instantiations at each step
Tracing model of execution has 4 events
Call (beginning of attempt to satisfy goal)
Exit (when a goal has been satisfied)
Redo (when backtracking occurs)
Fail (when goal fails)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-17

### Notes:

<!-- Slide number: 18 -->
# Prolog Inferencing Process:Tracing Model Example

![](Picture4.jpg)
likes(jake, chocolate).
likes(jake, apricots).
likes(darcie, licorice).
likes(darcie, apricots).

?- trace.
?- likes(jake, X), likes(darcie, X).

 1 Call: likes(jake, _0)?
(1) 1 Exit: likes(jake, chocolate)
(2) 1 Call: likes(darcie, chocolate)?
(2) 1 Fail: likes(darcie, chocolate)
 1 Redo: likes(jake, _0)?
(1) 1 Exit: likes(jake, apricots)
(3) 1 Call: likes(darcie, apricots)?
(3) 1 Exit: likes(darcie, apricots)
X = apricots

Copyright © 2023 Addison-Wesley. All rights reserved.
1-18

### Notes:
This example illustrates the steps Prolog goes through to prove a query. Prolog always works from left to right, and top to bottom when trying to prove a query holds.

The query is attempting to find an X that both jake and darcie like. The basic approach is as follows:

Prolog starts with the leftmost sub-goal. It needs to find an instantiation for X that makes likes(jake, X) true.
Prolog starts searching for a fact from the top. The first fact it finds is likes(jake, chocolate), so X is instantiated to chocolate.
The first sub-goal has been satisfied, so Prolog moves on to the second sub-goal, likes(darcie, X). Because X has been instantiated to chocolate, the second sub-goal to prove is likes(darcie, chocolate).
Prolog searches for a matching fact, but can’t find anything.
Prolog must now backtrack to the previous sub-goal, and try to find another X that makes likes(jake, X) true. The search continues from where the first sub-goal was satisfied.
The next matching fact is likes(jake, apricots), so X is instantiated to apricots.
Prolog now moves to the second sub-goal, likes(darcie, X), which becomes likes(darcie, apricots) because X has been instantiated to apricots.
Prolog finds likes(darcie, apricots), which satisfies the second sub-goal.
We have no further sub-goals to satisfy, so Prolog responds with “X = apricots”.

If we were to re-query Prolog after this process, no further instantiations for X can be found to satisfy the first sub-goal, so Prolog responds with “false”.
