<!-- Slide number: 1 -->
# Chapter 16Part 1
Logic Programming Languages

### Notes:

<!-- Slide number: 2 -->
# Chapter 16 Topics
Introduction
A Brief Introduction to Predicate Calculus
Copyright © 2023 Addison-Wesley. All rights reserved.
1-2

### Notes:

<!-- Slide number: 3 -->
# Introduction
Logic programming languages
Also called declarative programming languages
Express programs in a form of symbolic logic
Logical inferencing process produces results
Declarative rather that procedural
Only specify the form of results
Not the detailed procedures for producing them
Copyright © 2023 Addison-Wesley. All rights reserved.
1-3

### Notes:

<!-- Slide number: 4 -->
# Predicate Calculus:Propositions
Definition of a proposition
A logical statement that may or may not be true
Consists of
One or more objects
Relationships among objects
Copyright © 2023 Addison-Wesley. All rights reserved.
1-4

### Notes:
A proposition is basically a statement of fact about objects. Objects are simply things we want to reason about. So a proposition might be that Mary is married to John. Mary and John are objects, and the relationship between them is that they are married. Note that we, as humans, associate a meaning to Mary, John, and married. However, as far as symbolic logic (discussed in the next slide) is concerned, these are just abstract things that will be reasoned with.

<!-- Slide number: 5 -->
# Predicate Calculus:Symbolic Logic
Symbolic logic
Logic which can be used for the three basic needs of formal logic
Express propositions
Express relationships between propositions
Describe how new propositions can be inferred from other propositions
First-order predicate calculus
The particular form of symbolic logic that is used for logic programming
Copyright © 2023 Addison-Wesley. All rights reserved.
1-5

### Notes:
Examples of the three basic needs of symbolic logic:

We might have the proposition that Peter is a parent of Joe, or that Peter is old.
We can place an “and” relationship between the two propositions, meaning that Peter is both Joe’s parent, and also old.
We can specify that “if X is the parent of something, then X is also old”, which allows us to infer one proposition from another. Descriptions like this are represented as rules.

Prolog has an inferencing engine that reasons about logic programs using first-order predicate calculus.

<!-- Slide number: 6 -->
# Predicate Calculus:Object Representation
Simple terms
Represent objects in propositions
Constant
A symbol that represents a particular object
Variable
A symbol that can represent different objects at different times
Different from variables in imperative languages
Copyright © 2023 Addison-Wesley. All rights reserved.
1-6

### Notes:
Continuing from the examples in the notes on the previous slide:

Something like Peter is a constant. It represents a particular object. Again, we (as humans) associate a meaning with this constant, but Prolog treats them only as abstract “things” it can reason about. Usually we will use the convention of a lowercase letter starting a constant name (i.e. peter instead of Peter), because this is what Prolog does.
X is a variable. It means “any particular object”. It doesn’t store a value like a variable in an imperative language. Variables are used within rules, as the example in the notes of the previous slide showed. We use the convention of an uppercase letter starting a variable name, because this is what Prolog does.

<!-- Slide number: 7 -->
# Predicate Calculus:Atomic Propositions
Two types of propositions
Atomic propositions
Compound propositions
Atomic propositions
The simplest kind of proposition
Written like a mathematical function
Copyright © 2023 Addison-Wesley. All rights reserved.
1-7

### Notes:

<!-- Slide number: 8 -->
# Predicate Calculus:Parts of Atomic Propositions
Atomic proposition is composed of two parts
Functor
Function symbol that names the relationships
Ordered list of parameters
Tuple (e.g. 1-tuple, 2-tuple, etc.)
Atomic propositions expressing relationships
		student(jon)
		like(seth, osx)
		like(nick, windows)
		like(jim, linux)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-8

### Notes:
In the examples:

“jon”, “seth”, “osx”, “nick”, “windows”, “jim”, and “linux” are constants that represent objects.
“student” and “like” are functors that represent relationships between objects.
student(jon) is a proposition that specifies some property of “jon”. We attach the meaning “jon attends a university” to the proposition, but it has no intrinsic meaning to symbolic logic. We could just as easily have attached another meaning to the proposition.
like(seth, osx) is a proposition that specifies a relationship between “seth” and “osx”. We attach the meaning “seth likes osx” to the proposition, but again it has no intrinsic meaning to symbolic logic. We could again attach another meaning to the proposition.

Also note that we use the convention of starting functors and objects with lowercase letters, because this is what is done by Prolog.

<!-- Slide number: 9 -->
# Predicate Calculus:Forms of a Proposition
Propositions can be stated in two forms
Fact: Proposition is assumed to be true
Query: Truth of proposition is to be determined
For example, given student(jon)
As fact: “Jon is a student”
As query: “Can you prove that Jon is a student?”
Copyright © 2023 Addison-Wesley. All rights reserved.
1-9

### Notes:

<!-- Slide number: 10 -->
# Predicate Calculus:Compound Propositions
We’ve looked at atomic propositions
Compound propositions
More complex than atomic propositions
Have two or more atomic propositions
Atomic propositions are connected by operators
Copyright © 2023 Addison-Wesley. All rights reserved.
1-10

### Notes:

<!-- Slide number: 11 -->
# Predicate Calculus: Logical Operators
| Name | Symbol | Example | Meaning |
| --- | --- | --- | --- |
| negation |  |  a | not a |
| conjunction |  | a  b | a and b |
| disjunction |  | a  b | a or b |
| equivalence |  | a  b | a is equivalent to b |
| implication |   | a  b a  b | a implies b b implies a |
Copyright © 2023 Addison-Wesley. All rights reserved.
1-11

### Notes:

<!-- Slide number: 12 -->
# Horn Clauses
We use a restricted form of propositions
Horn clauses can represent most propositions
Horn clause can have only two forms
Headed
Conjunction of propositions on right (antecedent)
One atomic proposition on left side (consequent)
State relationships (rules)
likes(bob, trout)  likes(bob, fish)  fish(trout)
Headless
Empty left side
State facts and queries
father(bob, jake)
Copyright © 2023 Addison-Wesley. All rights reserved.
1-12

### Notes:
The headed Horn clause example is interpreted as:
“If bob likes fish and trout is a fish, then bob likes trout”

The headless Horn clause is interpreted as either:
The fact, “bob is the father of jake”
The query, “Is bob the father of jake?”

<!-- Slide number: 13 -->
# Predicate Calculus & Proving Theorems
Want to infer facts from known propositions
Resolution is an inference principle
Allows inferred propositions to be computed from given propositions
For example, given
older(joanna, jake)  mother(joanna, jake)
wiser(joanna, jake)  older(joanna, jake)
Resolution can infer that
wiser(joanna, jake)  mother(joanna, jake)
This is a matching process
Copyright © 2023 Addison-Wesley. All rights reserved.
1-13

### Notes:

<!-- Slide number: 14 -->
# Predicate Calculus & Proving Theorems
Variables can appear in propositions
father(X, jake)
Unification process
Finds values for variables in propositions
These values allow a matching process to succeed
Matching process leads to assumed propositions
A variable is instantiated to a temporary value to try to allow unification to succeed
After instantiating a variable with a value
Matching may fail
Backtrack: instantiate variable with different value
Copyright © 2023 Addison-Wesley. All rights reserved.
1-14

### Notes:
father(X, jake) is read as “Can you find a value for X so that X is the father of jake?”

<!-- Slide number: 15 -->
# Predicate Calculus & Proving Theorems
Resolution can be used to prove theorems
Hypotheses
A set of assumed propositions
Theorem
A new proposition we want to infer
Copyright © 2023 Addison-Wesley. All rights reserved.
1-15

### Notes:
