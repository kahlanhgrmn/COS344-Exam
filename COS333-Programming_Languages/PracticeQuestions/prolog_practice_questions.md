# Prolog Practice Questions
## COS 333 — Exam Style (5 marks each)

---

## Question 1 *(5 points)*

Write a Prolog proposition called `triplePositivesRemoveNegatives(L1, L2)`, which succeeds if L2 is a list containing all the elements in L1 in their original order, where **positive values are tripled**, **zero values remain unchanged**, and **negative values are omitted**.

*Examples:*
```prolog
?- triplePositivesRemoveNegatives([], X).
% X = []

?- triplePositivesRemoveNegatives([-3, -7], X).
% X = []   (all values are negative, so all omitted)

?- triplePositivesRemoveNegatives([-2, 0, 4, -1, 3], X).
% X = [0, 12, 9]   (-2 and -1 omitted; 0 unchanged; 4→12, 3→9)
```

*Hint: Comparison operators (`<`, `=<`, `>`, `>=`) and the `=:=` operator can be used as terms in Prolog. Multiplication is represented by `*`.*

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, the `is` operator, cuts, and the built-in `not` proposition. Do **not** use if-then, if-then-else, the semicolon (`;`) or pipe (`|`) operator outside of a list, or complex system predicates (including built-in `member`, `append`, `reverse`).

---

### Solution — Question 1

**Pattern:** Filter+Map C — 3-way split: omit negatives, keep zeros, triple positives.

```prolog
triplePositivesRemoveNegatives([], []).

triplePositivesRemoveNegatives([H|T], R) :-
    H < 0,
    triplePositivesRemoveNegatives(T, R).

triplePositivesRemoveNegatives([H|T], [H|R]) :-
    H =:= 0,
    triplePositivesRemoveNegatives(T, R).

triplePositivesRemoveNegatives([H|T], [Triple|R]) :-
    H > 0,
    Triple is H * 3,
    triplePositivesRemoveNegatives(T, R).
```

**How it works:**
- Clause 1: Base case — empty input, empty result.
- Clause 2: H < 0 — omit H, result is just the tail's result.
- Clause 3: H = 0 — keep H unchanged, prepend to tail result.
- Clause 4: H > 0 — compute `Triple = H * 3`, prepend to tail result.

**Trace for `triplePositivesRemoveNegatives([-2, 0, 4], X)`:**
- H=-2, H<0 → skip, recurse on [0, 4]
- H=0, H=:=0 → keep 0, recurse on [4] → [0 | ...]
- H=4, H>0 → Triple=12, recurse on [] → [12 | []]
- Unwind: X = [0, 12]

---

## Question 2 *(5 points)*

Write a Prolog proposition called `squareAll(L1, L2)`, which succeeds if L2 is a list containing the **square of every element** in L1, in their original order.

*Examples:*
```prolog
?- squareAll([], X).
% X = []

?- squareAll([-3, 0, 4], X).
% X = [9, 0, 16]

?- squareAll([2, -5, 1], X).
% X = [4, 25, 1]
```

*Hint: Multiplication is represented by `*`.*

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, the `is` operator, cuts, and the built-in `not` proposition. Do **not** use if-then, if-then-else, the semicolon (`;`) or pipe (`|`) operator outside of a list, or complex system predicates.

---

### Solution — Question 2

**Pattern:** Map B — transform every element (square it). Two clauses: base + recursive.

```prolog
squareAll([], []).

squareAll([H|T], [Sq|R]) :-
    Sq is H * H,
    squareAll(T, R).
```

**How it works:**
- Clause 1: empty input → empty result.
- Clause 2: compute `Sq = H * H`, prepend to result of squaring the tail.

**Trace for `squareAll([-3, 0, 4], X)`:**
- H=-3, Sq=9, recurse on [0, 4]
- H=0, Sq=0, recurse on [4]
- H=4, Sq=16, recurse on []
- Base: []
- Unwind: X = [9, 0, 16]

---

## Question 3 *(5 points)*

Write a Prolog proposition called `absNonNegativesRemovePositives(L1, L2)`, which succeeds if L2 is a list containing the elements of L1 in their original order, where **positive values are omitted**, **zero values remain unchanged**, and **negative values are replaced by their absolute value**.

*Examples:*
```prolog
?- absNonNegativesRemovePositives([], X).
% X = []

?- absNonNegativesRemovePositives([1, 5, 3], X).
% X = []   (all positive values omitted)

?- absNonNegativesRemovePositives([-4, 2, 0, -1, 7], X).
% X = [4, 0, 1]   (2 and 7 omitted; -4→4, 0→0, -1→1)
```

*Hint: `abs(X)` computes the absolute value of X. Use `Abs is abs(H)` to bind Abs to the absolute value of H.*

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, the `is` operator, cuts, and the built-in `not` proposition. Do **not** use if-then, if-then-else, the semicolon (`;`) or pipe (`|`) operator outside of a list, or complex system predicates.

---

### Solution — Question 3

**Pattern:** Filter+Map C — 3-way split: omit positives, keep zeros, abs of negatives.

```prolog
absNonNegativesRemovePositives([], []).

absNonNegativesRemovePositives([H|T], R) :-
    H > 0,
    absNonNegativesRemovePositives(T, R).

absNonNegativesRemovePositives([H|T], [H|R]) :-
    H =:= 0,
    absNonNegativesRemovePositives(T, R).

absNonNegativesRemovePositives([H|T], [Abs|R]) :-
    H < 0,
    Abs is abs(H),
    absNonNegativesRemovePositives(T, R).
```

**How it works:**
- Clause 2: H > 0 → skip.
- Clause 3: H = 0 → keep unchanged.
- Clause 4: H < 0 → compute absolute value, include in result.

---

## Question 4 *(5 points)*

Write a Prolog proposition called `sumList(L, S)`, which succeeds if S is the **sum of all elements** in the numeric list L.

*Examples:*
```prolog
?- sumList([], S).
% S = 0

?- sumList([5], S).
% S = 5

?- sumList([3, -1, 4, -2], S).
% S = 4
```

*Hint: Addition is represented by `+`. Use `S is A + B` to compute arithmetic sums.*

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, the `is` operator, cuts, and the built-in `not` proposition. Do **not** use if-then, if-then-else, the semicolon (`;`) or pipe (`|`) operator outside of a list, or complex system predicates.

---

### Solution — Question 4

**Pattern:** Accumulate D — base case is 0, recursive case adds head to sum of tail.

```prolog
sumList([], 0).

sumList([H|T], S) :-
    sumList(T, Rest),
    S is H + Rest.
```

**How it works:**
- Clause 1: empty list → sum is 0.
- Clause 2: recurse on tail to get sum of tail (`Rest`), then add head H.

**Trace for `sumList([3, -1, 4], S)`:**
- H=3, recurse on [-1, 4] → Rest=3
- H=-1, recurse on [4] → Rest=3
- H=4, recurse on [] → Rest=0
- Base: 0
- Unwind: S=4+0=4 → S=-1+4=3 → S=3+3=6

**Answer:** S = 6

---

## Question 5 *(5 points)*

Write a Prolog proposition called `halfEvensNegateOdds(L1, L2)`, which succeeds if L2 is a list containing all the elements in L1 in their original order, where **even values are halved** (divided by 2) and **odd values are negated** (multiplied by -1). Zero is considered even.

*Examples:*
```prolog
?- halfEvensNegateOdds([], X).
% X = []

?- halfEvensNegateOdds([4, 3, 6, -5, 0], X).
% X = [2, -3, 3, 5, 0]
% (4→2 halved; 3→-3 negated; 6→3 halved; -5→5 negated; 0→0 halved)
```

*Hint: `mod(X, 2)` gives the remainder when X is divided by 2. Division is represented by `//` for integer division. Use `R is mod(H, 2)` to compute the remainder.*

**Requirements:**
- You may define additional helper propositions.
- Only use constants, variables, list manipulation, arithmetic, relational expressions, the `is` operator, cuts, and the built-in `not` proposition. Do **not** use if-then, if-then-else, the semicolon (`;`) or pipe (`|`) operator outside of a list, or complex system predicates.

---

### Solution — Question 5

**Pattern:** Map B with conditional transform — every element appears, transformed based on parity.

```prolog
halfEvensNegateOdds([], []).

halfEvensNegateOdds([H|T], [Half|R]) :-
    0 is mod(H, 2),
    Half is H // 2,
    halfEvensNegateOdds(T, R).

halfEvensNegateOdds([H|T], [Neg|R]) :-
    not(0 is mod(H, 2)),
    Neg is H * -1,
    halfEvensNegateOdds(T, R).
```

**Alternative using a helper proposition for even/odd test:**

```prolog
isEven(X) :- 0 is mod(X, 2).

halfEvensNegateOdds([], []).

halfEvensNegateOdds([H|T], [Half|R]) :-
    isEven(H),
    Half is H // 2,
    halfEvensNegateOdds(T, R).

halfEvensNegateOdds([H|T], [Neg|R]) :-
    not(isEven(H)),
    Neg is H * -1,
    halfEvensNegateOdds(T, R).
```

**How it works:**
- Clause 2: H is even (`mod(H, 2) = 0`) → compute `Half = H // 2` (integer division).
- Clause 3: H is odd → compute `Neg = H * -1`.
- Every element appears in result — this is a pure map.

**Trace for `halfEvensNegateOdds([4, 3, 6], X)`:**
- H=4, mod=0, Half=2, recurse on [3, 6]
- H=3, mod=1 (not 0), Neg=-3, recurse on [6]
- H=6, mod=0, Half=3, recurse on []
- Base: []
- Unwind: X = [2, -3, 3]
