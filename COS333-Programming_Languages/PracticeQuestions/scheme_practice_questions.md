# Scheme Practice Questions
## COS 333 — Exam Style (5 marks each)

---

## Question 1 *(5 points)*

Write a Scheme function named `keepNonNegatives`, which receives one parameter: a simple list containing only numeric atoms. The function should yield (not print) a list containing **only the non-negative values** from the parameter list, in their original order.

*Examples:*
```scheme
(keepNonNegatives '())
; => ()

(keepNonNegatives '(-3 -1 -5))
; => ()   (all values are negative)

(keepNonNegatives '(-4 0 7 -2 3))
; => (0 7 3)   (negative values -4 and -2 removed)
```

**Allowed built-in functions:**
- **Function construction:** `lambda`, `define`
- **Binding:** `let`
- **Arithmetic:** `+`, `-`, `*`, `/`, `abs`, `sqrt`, `remainder`, `modulo`, `min`, `max`
- **Boolean values:** `#t`, `#f`
- **Equality predicates:** `=`, `>`, `<`, `>=`, `<=`, `even?`, `odd?`, `zero?`, `negative?`, `eqv?`, `eq?`
- **Logical predicates:** `and`, `or`, `not`
- **List predicates:** `list?`, `null?`
- **Conditionals:** `if`, `cond`, `else`
- **Quoting:** `quote`, `'`
- **List manipulation:** `list`, `car`, `cdr`, `cons`
- **I/O:** `display`, `printf`, `newline`, `read`

---

### Solution — Question 1

**Pattern:** Filter A — keep elements satisfying a condition (>= 0), skip the rest.

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

**Trace for `(keepNonNegatives '(-4 0 7))`:**
- `lst = (-4 0 7)` → -4 < 0 → skip → recurse on `(0 7)`
- `lst = (0 7)` → 0 >= 0 → `(cons 0 (keepNonNegatives '(7)))`
- `lst = (7)` → 7 >= 0 → `(cons 7 (keepNonNegatives '()))`
- `lst = ()` → base case → `'()`
- Unwind: `(cons 7 '())` = `(7)` → `(cons 0 '(7))` = `(0 7)`

---

## Question 2 *(5 points)*

Write a Scheme function named `absoluteValueAll`, which receives one parameter: a simple list containing only numeric atoms. The function should yield (not print) a list containing the **absolute value of every element** in the parameter list, in their original order.

*Examples:*
```scheme
(absoluteValueAll '())
; => ()

(absoluteValueAll '(-3 -9))
; => (3 9)   (all values negated by abs)

(absoluteValueAll '(-5 0 4 -2 7))
; => (5 0 4 2 7)   (every value replaced by its absolute value)
```

**Allowed built-in functions:** *(same as above)*

---

### Solution — Question 2

**Pattern:** Map B — transform every element (apply `abs`), keep all elements.

```scheme
(define (absoluteValueAll lst)
  (cond
    ((null? lst) '())
    (else
     (cons (abs (car lst)) (absoluteValueAll (cdr lst))))
  )
)
```

**Trace for `(absoluteValueAll '(-5 0 4))`:**
- `(cons (abs -5) (absoluteValueAll '(0 4)))` = `(cons 5 ...)`
- `(cons (abs 0) (absoluteValueAll '(4)))` = `(cons 0 ...)`
- `(cons (abs 4) (absoluteValueAll '()))` = `(cons 4 ...)`
- Base: `'()`
- Unwind: `(4)` → `(0 4)` → `(5 0 4)`

---

## Question 3 *(5 points)*

Write a Scheme function named `doubleNegativesRemoveZeros`, which receives one parameter: a simple list containing only numeric atoms. The function should yield (not print) a list containing the values in the parameter list, in their original order, where **zero values are omitted**, **negative values are doubled**, and **positive values remain unchanged**.

*Examples:*
```scheme
(doubleNegativesRemoveZeros '())
; => ()

(doubleNegativesRemoveZeros '(0 0 0))
; => ()   (all zeros omitted)

(doubleNegativesRemoveZeros '(-3 0 5 -1 0 2))
; => (-6 5 -2 2)   (0s omitted; -3→-6, -1→-2; 5 and 2 unchanged)
```

**Allowed built-in functions:** *(same as above)*

---

### Solution — Question 3

**Pattern:** Filter+Map C — 3-way split: omit zeros, double negatives, keep positives.

```scheme
(define (doubleNegativesRemoveZeros lst)
  (cond
    ((null? lst) '())
    ((zero? (car lst))
     (doubleNegativesRemoveZeros (cdr lst)))
    ((negative? (car lst))
     (cons (* 2 (car lst)) (doubleNegativesRemoveZeros (cdr lst))))
    (else
     (cons (car lst) (doubleNegativesRemoveZeros (cdr lst))))
  )
)
```

**Trace for `(doubleNegativesRemoveZeros '(-3 0 5))`:**
- `-3` is negative → `(cons (* 2 -3) ...)` = `(cons -6 ...)`
- `0` is zero → skip → recurse on `(5)`
- `5` is positive → `(cons 5 (doubleNegativesRemoveZeros '()))` = `(cons 5 '())`
- Unwind: `(5)` → `(-6 5)`

---

## Question 4 *(5 points)*

Write a Scheme function named `countEvens`, which receives one parameter: a simple list containing only numeric atoms. The function should yield (not print) **the count** of even-valued atoms in the parameter list.

*Examples:*
```scheme
(countEvens '())
; => 0

(countEvens '(1 3 5 7))
; => 0   (no even values)

(countEvens '(2 3 4 5 6))
; => 3   (2, 4, and 6 are even)
```

**Allowed built-in functions:** *(same as above)*

---

### Solution — Question 4

**Pattern:** Accumulate D — recurse, count matching elements. Base case is 0.

```scheme
(define (countEvens lst)
  (cond
    ((null? lst) 0)
    ((even? (car lst))
     (+ 1 (countEvens (cdr lst))))
    (else
     (countEvens (cdr lst)))
  )
)
```

**Trace for `(countEvens '(2 3 4))`:**
- `2` is even → `(+ 1 (countEvens '(3 4)))`
- `3` is odd → `(countEvens '(4))`
- `4` is even → `(+ 1 (countEvens '()))`
- Base: `0`
- Unwind: `(+ 1 0)` = 1 → `(+ 1 1)` = 2 (going back up)

---

## Question 5 *(5 points)*

Write a Scheme function named `squareNonNegativesNegateNegatives`, which receives one parameter: a simple list containing only numeric atoms. The function should yield (not print) a list containing the values in the parameter list, in their original order, where **non-negative values are squared** and **negative values are negated** (made positive by multiplying by -1).

*Examples:*
```scheme
(squareNonNegativesNegateNegatives '())
; => ()

(squareNonNegativesNegateNegatives '(-3))
; => (3)   (-3 negated to 3)

(squareNonNegativesNegateNegatives '(-4 0 3 -2))
; => (4 0 9 2)   (-4→4, 0→0, 3→9, -2→2)
```

**Allowed built-in functions:** *(same as above)*

---

### Solution — Question 5

**Pattern:** Map B with conditional transform — every element appears but transformed differently based on sign.

```scheme
(define (squareNonNegativesNegateNegatives lst)
  (cond
    ((null? lst) '())
    ((negative? (car lst))
     (cons (* -1 (car lst)) (squareNonNegativesNegateNegatives (cdr lst))))
    (else
     (cons (* (car lst) (car lst)) (squareNonNegativesNegateNegatives (cdr lst))))
  )
)
```

> Alternative using `abs` for the negative case: `(cons (abs (car lst)) ...)`
> Alternative using `let` to avoid double evaluation of `(car lst)`:

```scheme
(define (squareNonNegativesNegateNegatives lst)
  (cond
    ((null? lst) '())
    (else
     (let ((h (car lst)))
       (cond
         ((negative? h)
          (cons (* -1 h) (squareNonNegativesNegateNegatives (cdr lst))))
         (else
          (cons (* h h) (squareNonNegativesNegateNegatives (cdr lst))))
       )
     )
    )
  )
)
```

**Trace for `(squareNonNegativesNegateNegatives '(-4 0 3))`:**
- `-4` is negative → `(cons 4 ...)`
- `0` is non-negative → `(cons (* 0 0) ...)` = `(cons 0 ...)`
- `3` is non-negative → `(cons (* 3 3) ...)` = `(cons 9 '())`
- Unwind: `(9)` → `(0 9)` → `(4 0 9)`
