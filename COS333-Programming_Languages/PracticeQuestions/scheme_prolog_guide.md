# Scheme & Prolog Long-Question Guide
## COS 333 — Exam Preparation

---

## PART 1 — SCHEME

### 1.1 What the exam asks

Every exam has **one 5-mark Scheme question**. You receive a function name and a plain-English description of what it should do to a simple numeric list. You must write a complete, correct recursive Scheme function that **yields** (returns) the result — never prints it.

**Allowed built-in functions (standard across all exams):**
- Function construction: `lambda`, `define`
- Binding: `let`
- Arithmetic: `+`, `-`, `*`, `/`, `abs`, `sqrt`, `remainder`, `modulo`, `min`, `max`
- Boolean: `#t`, `#f`
- Equality predicates: `=`, `>`, `<`, `>=`, `<=`, `even?`, `odd?`, `zero?`, `negative?`, `eqv?`, `eq?`
- Logical: `and`, `or`, `not`
- List predicates: `list?`, `null?`
- Conditionals: `if`, `cond`, `else`
- Quoting: `quote`, `'`
- List manipulation: `list`, `car`, `cdr`, `cons`
- I/O: `display`, `printf`, `newline`, `read`

> `positive?` is **not** in the standard allowed list — use `(> x 0)` instead.

---

### 1.2 The four question patterns

#### Pattern A — Filter (remove or keep elements)
Keep/remove elements based on a condition. Output list has ≤ input length.

**Template:**
```scheme
(define (functionName lst)
  (cond
    ((null? lst) '())
    ((KEEP-CONDITION (car lst))
     (cons (car lst) (functionName (cdr lst))))
    (else
     (functionName (cdr lst)))
  )
)
```
- `null?` base case returns empty list `'()`
- If condition is true → `cons` element onto recursive result
- Otherwise → skip element (recurse without it)

**Example — keep only non-negative values:**
```scheme
(define (keepNonNegatives lst)
  (cond
    ((null? lst) '())
    ((>= (car lst) 0)
     (cons (car lst) (keepNonNegatives (cdr lst))))
    (else
     (keepNonNegatives (cdr lst)))
  )
)
```

---

#### Pattern B — Map (transform every element, same length output)
Every element stays but is transformed. Output length equals input length.

**Template:**
```scheme
(define (functionName lst)
  (cond
    ((null? lst) '())
    (else
     (cons (TRANSFORM (car lst)) (functionName (cdr lst))))
  )
)
```
- `null?` base case returns `'()`
- `cons` the transformed element onto recursive result
- No element is ever skipped

**Example — negate all values:**
```scheme
(define (negateAll lst)
  (cond
    ((null? lst) '())
    (else
     (cons (- (car lst)) (negateAll (cdr lst))))
  )
)
```

---

#### Pattern C — Filter+Map (exam favourite — 3-way split)
Some elements are omitted, some are kept unchanged, some are transformed. This is what the 2025 exam used.

**Template:**
```scheme
(define (functionName lst)
  (cond
    ((null? lst) '())
    ((OMIT-CONDITION (car lst))
     (functionName (cdr lst)))           ; skip this element
    ((TRANSFORM-CONDITION (car lst))
     (cons (TRANSFORM (car lst)) (functionName (cdr lst))))
    (else
     (cons (car lst) (functionName (cdr lst))))  ; keep unchanged
  )
)
```

**Example — omit negatives, keep zeros, double positives:**
```scheme
(define (getZerosDoublePositives lst)
  (cond
    ((null? lst) '())
    ((negative? (car lst))
     (getZerosDoublePositives (cdr lst)))
    ((> (car lst) 0)
     (cons (* 2 (car lst)) (getZerosDoublePositives (cdr lst))))
    (else
     (cons (car lst) (getZerosDoublePositives (cdr lst))))
  )
)
```
> Note: `negative?` IS in the allowed list. `positive?` is NOT — use `(> x 0)`.

---

#### Pattern D — Accumulate (return a number: sum or count)
Recurse through the list building up a number result.

**Template:**
```scheme
(define (functionName lst)
  (cond
    ((null? lst) 0)              ; base: 0 for sum/count
    ((CONDITION (car lst))
     (+ CONTRIBUTION (functionName (cdr lst))))
    (else
     (functionName (cdr lst)))  ; or (+ 0 ...) for count
  )
)
```

**Example — sum all positive values:**
```scheme
(define (sumPositives lst)
  (cond
    ((null? lst) 0)
    ((> (car lst) 0)
     (+ (car lst) (sumPositives (cdr lst))))
    (else
     (sumPositives (cdr lst)))
  )
)
```

---

### 1.3 Step-by-step approach for exam questions

1. **Identify the pattern** from the description:
   - "remove/keep" → Pattern A (filter)
   - "transform every element" → Pattern B (map)
   - "omit ... unchanged ... transformed" (3 categories) → Pattern C (filter+map)
   - "return the count/sum of" → Pattern D (accumulate)

2. **Write the base case first:** `(null? lst)` → `'()` (for A/B/C) or `0` (for D)

3. **Write the condition cases** using `cond` (prefer `cond` over nested `if` for 3+ cases)

4. **Use `cons` to build the output list** — never use `list` to wrap results

5. **Double-check:**
   - Is `positive?` needed? Use `(> x 0)` instead
   - Is the function named exactly as stated in the question?
   - Does it yield (not print)?
   - Is the empty list returned correctly as `'()` (with quote)?

---

### 1.4 Common predicates cheat-sheet

| Test | Scheme code |
|------|-------------|
| x is positive | `(> x 0)` |
| x is negative | `(negative? x)` or `(< x 0)` |
| x is zero | `(zero? x)` |
| x is non-negative | `(>= x 0)` |
| x is even | `(even? x)` |
| x is odd | `(odd? x)` |
| x is positive AND odd | `(and (> x 0) (odd? x))` |
| absolute value of x | `(abs x)` |
| double x | `(* 2 x)` |
| negate x | `(- x)` or `(* -1 x)` |
| halve x (integer) | `(quotient x 2)` |

---

## PART 2 — PROLOG

### 2.1 What the exam asks

Every exam has **one 5-mark Prolog question** and ST2 has **two 5-mark Prolog questions**.

**Exam-style:** Always a list-processing proposition `name(L1, L2)` where L2 is L1 with some filter/map applied.

**ST2-style:** Either a list-processing proposition OR a relational proposition using given facts.

**Requirements (standard across exams):**
- May define additional helper propositions
- Only use: constants, variables, list manipulation, arithmetic, relational expressions, `is` operator, cuts, built-in `not`
- Do **NOT** use: if-then, if-then-else, `;` outside lists, complex predicates like built-in `member`, `append`, `reverse`

---

### 2.2 List processing pattern structure

Every list proposition follows this structure:

```prolog
% Base case: empty list
myProp([], []).

% Recursive case(s): one or more rules for non-empty lists
myProp([Head|Tail], Result) :-
    % conditions on Head,
    % compute transformed head,
    % recurse on tail
```

**Key points:**
- The second parameter `Result` is what gets built up — it's your "return value"
- Each case is a separate clause (not nested if-then)
- Always put the base case (`[]`) first
- Use `[Head|Tail]` to decompose the list, `[Head|Result]` or `[NewHead|Result]` to construct it

---

### 2.3 The four list-processing patterns

#### Pattern A — Filter (keep matching elements)

```prolog
keepPositives([], []).
keepPositives([H|T], [H|R]) :- H > 0, keepPositives(T, R).
keepPositives([H|T], R)     :- H =< 0, keepPositives(T, R).
```
- First clause: empty list → empty result
- Second clause: if condition is true, include H in result
- Third clause: if condition is false, skip H (result of tail only)

---

#### Pattern B — Map (transform every element)

```prolog
doubleAll([], []).
doubleAll([H|T], [Double|R]) :-
    Double is H * 2,
    doubleAll(T, R).
```
- `is` operator computes arithmetic value
- Every element appears in result (possibly transformed)
- Only two clauses needed (base + recursive)

---

#### Pattern C — Filter+Map (exam favourite — 3-way split)

```prolog
myProp([], []).

% Case 1: omit this element (e.g. zeros)
myProp([H|T], R) :- H =:= 0, myProp(T, R).

% Case 2: transform this element (e.g. double positives)
myProp([H|T], [Double|R]) :-
    H > 0,
    Double is H * 2,
    myProp(T, R).

% Case 3: keep unchanged (e.g. negatives)
myProp([H|T], [H|R]) :-
    H < 0,
    myProp(T, R).
```
> Always make conditions **mutually exclusive** — each element must match exactly one clause.

**Example — omit zeros, negate positives, keep negatives (2025 exam):**
```prolog
getNegativesNegatePositives([], []).
getNegativesNegatePositives([H|T], R) :-
    H =:= 0, getNegativesNegatePositives(T, R).
getNegativesNegatePositives([H|T], [Neg|R]) :-
    H > 0, Neg is -H, getNegativesNegatePositives(T, R).
getNegativesNegatePositives([H|T], [H|R]) :-
    H < 0, getNegativesNegatePositives(T, R).
```

---

#### Pattern D — Accumulate (count or sum into a number)

```prolog
countPositives([], 0).
countPositives([H|T], Count) :-
    H > 0,
    countPositives(T, Rest),
    Count is Rest + 1.
countPositives([H|T], Count) :-
    H =< 0,
    countPositives(T, Count).
```
- Base case: empty list → 0
- Matching case: recurse, then add 1 (or value of H for sum)
- Non-matching case: recurse, pass count unchanged

---

### 2.4 Relational propositions (ST2 style)

These use given facts and build rules. Strategy:

1. **Identify what you need to prove** (the goal)
2. **Chain backwards** — what facts do you need?
3. **Use variables to link propositions** — a shared variable X in two terms means "the same X"
4. **Use `not(X = Y)` to enforce that two variables are different** (the negation problem — but it works practically)

**Example — `nephewNiece(X, Y)` means X is nephew/niece of Y:**
```prolog
parent(P, C) :- father(P, C).
parent(P, C) :- mother(P, C).

sibling(X, Y) :- parent(P, X), parent(P, Y), not(X = Y).

nephewNiece(X, Y) :- parent(P, X), sibling(P, Y).
```

**Key technique — linking propositions with a shared variable:**
- `tenant(X, Tony), address(X, Addr), tenant(Y, Tony), address(Y, Addr), not(X = Y)` 
  means "find two DIFFERENT tenants of Tony who share the same address"

---

### 2.5 Step-by-step approach for Prolog list questions

1. **Write the base case first:** `myProp([], []).`

2. **Count the cases** for each element:
   - How many different outcomes are there for each element? (keep, omit, transform = 3 cases)
   - Write one clause per case

3. **For each non-empty-list clause:**
   ```prolog
   myProp([Head|Tail], ???) :- Condition, ..., myProp(Tail, Rest).
   ```
   - If element is **omitted**: result = `Rest`
   - If element is **kept unchanged**: result = `[Head|Rest]`
   - If element is **transformed**: compute new value `New is ...`, result = `[New|Rest]`

4. **Make conditions explicit and mutually exclusive:**
   - `H > 0`, `H < 0`, `H =:= 0` (use `=:=` for numeric equality in conditions)
   - Never leave gaps — every possible value of H must be covered by some clause

5. **Double-check:**
   - Is `=:=` used for numeric equality (not `=`)?
   - Is `is` used for arithmetic assignment?
   - Is the base case first?
   - Are there no `;` operators or if-then constructs?

---

### 2.6 Arithmetic operator cheat-sheet

| Operation | Prolog syntax |
|-----------|---------------|
| X is positive | `X > 0` |
| X is negative | `X < 0` |
| X is zero | `X =:= 0` |
| X is non-negative | `X >= 0` |
| Compute absolute value | `Abs is abs(H)` |
| Double a value | `Double is H * 2` |
| Negate a value | `Neg is -H` or `Neg is H * -1` |
| X equals Y (arithmetic) | `X =:= Y` |
| X not equals Y (arith.) | `X =\= Y` |

---

### 2.7 Common mistakes to avoid

**Scheme:**
- Returning `()` without quote → `'()` is correct
- Using `positive?` → not in allowed list; use `(> x 0)`
- Printing instead of yielding → no `display`, just `cons`/return
- Forgetting to quote the empty list in base case

**Prolog:**
- Using `=` for arithmetic equality → use `=:=`
- Using `X = expr` for arithmetic → use `X is expr`
- Using `;` for logical or → write separate clauses
- Using if-then `(cond -> then ; else)` → write separate clauses
- Not making conditions mutually exclusive → unexpected backtracking
- Putting recursive case before base case → may cause issues

---

## PART 3 — PATTERN RECOGNITION TABLE

When you read a question description, map it to a pattern:

| Description clue | Pattern | Return structure |
|------------------|---------|-----------------|
| "remove all X" / "without X" | Filter A | `'()` / `[]` base |
| "keep only X" | Filter A | `'()` / `[]` base |
| "transform every element" / "double all" | Map B | `'()` / `[]` base |
| "X unchanged, Y transformed, Z omitted" | Filter+Map C | `'()` / `[]` base |
| "return the count of" | Accumulate D | `0` base |
| "return the sum of" | Accumulate D | `0` base |
| "succeeds if C is the number of..." | Prolog accumulate | `0` base |
