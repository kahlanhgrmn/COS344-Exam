# COS333 — Exam Cheatsheet
*Content verified against actual lecture slides*

---

## Ch9 — Subprograms (~6 marks)

### Key Terminology
- **Subprogram definition**: defines the interface (name, parameters, return type) and the body
- **Subprogram call**: an explicit execution request
- **Formal parameter**: dummy variable listed in the subprogram header
- **Actual parameter**: value or address used in the call
- **Positional parameters**: matched by order — `greet("Alice", "Hello")` maps left-to-right
- **Keyword parameters**: matched by name — order-independent (Ruby, Python, Ada)
- **Default parameters**: formal parameters with a preset value if no actual is supplied (C++, Python, Ruby, Ada, PHP)

```python
# Python — positional, keyword, and default params
def greet(name, greeting="Hello"):   # greeting has a default
    print(greeting, name)
greet("Alice")                        # positional → Hello Alice
greet(greeting="Hi", name="Bob")      # keyword → Hi Bob (order doesn't matter)
```

- **Parameter profile (signature)**: number, order, and types of parameters
- **Protocol**: parameter profile plus return type
- **Subprogram declaration (prototype)**: provides protocol but no body

### Procedures vs Functions
- **Procedure**: no return value; produces results by modifying parameters or non-local variables
- **Function**: returns a value; modelled on mathematical functions — ideally no side effects

```c
// C procedure (void) vs function
void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }  // procedure: modifies via params
int  square(int x)        { return x * x; }                  // function: returns a value
```

### Local Variables
- Most contemporary languages: local variables are **stack-dynamic** (allocated at block entry, released at exit → supports recursion)
- C/C++: locals are stack-dynamic by default; can be declared `static` (history-sensitive, allocated once)

```c
void counter() {
    static int n = 0;   // allocated once, NOT reset on re-entry
    n++;
    printf("%d\n", n);
}
counter(); // → 1
counter(); // → 2   (n retained between calls)
counter(); // → 3
```

### Parameter Passing Methods
| Method | Mode | How | Caller affected? |
|---|---|---|---|
| **Pass-by-value** | In | Copy actual → formal | No |
| **Pass-by-result** | Out | Copy formal → actual on return | Yes (on return) |
| **Pass-by-value-result** | In-Out | Copy in, copy back on return | Yes (on return) |
| **Pass-by-reference** | In-Out | Access path (alias) | Yes (immediately) |
| **Pass-by-name** | In-Out | Textual substitution | Yes (deferred binding) |

- **Pass-by-value** disadvantage: extra storage, expensive for large objects
- **Pass-by-reference** disadvantage: unwanted side effects, aliasing (`fun(total, total)` → first and second alias the same variable)
- **Pass-by-name** example: `foo(val, arr[val])` — after `a = 1`, `b` becomes `arr[1]`, not `arr[0]`

#### Code Examples

**Pass-by-value** — caller's variable unchanged after call:
```c
void foo(int x) { x = 99; }   // modifies local copy only
int a = 5;
foo(a);
// a is still 5
```

**Pass-by-result** — formal written back to actual only on return (Ada `out`):
```ada
procedure foo(x : out Integer) is
begin
    x := 99;          -- writes to formal; actual unchanged until return
end foo;
-- a receives 99 after the call completes
foo(a);
```

**Pass-by-value-result** — copy in on entry, copy back on return (Ada `in out`):
```ada
procedure foo(x : in out Integer) is
begin
    x := x + 1;       -- reads incoming value (copy-in), writes back on return
end foo;
-- a was 5, becomes 6 after the call returns
foo(a);
```

**Pass-by-reference** — alias to actual; changes visible immediately to caller:
```c
void foo(int &x) { x = 99; }   // x is an alias for a
int a = 5;
foo(a);
// a is now 99 (changed inside the function)
```

**Pass-by-name** — argument expression re-evaluated on every use (textual substitution):
```
// Imagine foo(val, arr[val]) where formal params are a and b
// "a" substitutes for "val", "b" substitutes for "arr[val]"
procedure foo(a, b):
    a = 1          // val becomes 1 — now b re-evaluates as arr[1], not arr[0]
    print b        // prints arr[1], NOT arr[0]
```

#### Language examples
- **C/C++**: pass-by-value (default), pass-by-reference (pointers in C; pointers or references in C++)
- **Java**: all parameters passed by value — objects seem passed by reference, but object *references* are passed by value
- **C#**: pass-by-value (default), pass-by-reference (precede with `ref`)
- **Python/Ruby**: pass-by-assignment — works like pass-by-reference (reference change), except for immutable objects (behaves like pass-by-value)

### Referencing Environment for Passed Subprograms — EXAM IMPORTANT
When a subprogram is passed as a parameter and references a non-local variable, there are three possible bindings:

```
fun sub1() {
   var x = 1
   fun sub2() { print x }
   fun sub3() { var x = 3; call sub4(sub2) }
   fun sub4(subx) { var x = 4; call subx() }
   call sub3()
}
```

| Binding | Referencing environment used | Output |
|---|---|---|
| **Shallow binding** | The call that *enacts* the passed subprogram (sub4) | `4` — natural for dynamic-scoped languages |
| **Deep binding** | The *definition* of the passed subprogram (sub1) | `1` — natural for static-scoped languages |
| **Ad-hoc binding** | The call that *passed* the subprogram (sub3) | `3` |

### Sections 9.6 and 9.7 — Overloaded and Generic Subprograms
- **Overloaded subprogram**: same name, different protocol in same referencing environment — resolved at compile time by parameter profile

```cpp
// C++ overloading — same name, different parameter profile
int    area(int side);              // square: 1 param
int    area(int w, int h);          // rectangle: 2 params
double area(double radius);         // circle: 1 double param
// compiler picks version based on argument count/types at call site
```

- **Generic subprogram** (parametric polymorphism): one definition works for multiple types via a type parameter

```cpp
// C++ template — compiler generates a version per type used
template <typename T>
T maxVal(T a, T b) { return (a > b) ? a : b; }
maxVal(3, 5);       // T = int    — creates int version at compile time
maxVal(3.1, 2.7);   // T = double — creates double version at compile time
```

```java
// Java generics — one Object version at runtime (type erasure)
public <T> T getFirst(ArrayList<T> list) { return list.get(0); }
```

```csharp
// C# generics — new version created at runtime for each primitive type
public T GetFirst<T>(List<T> list) { return list[0]; }
```

#### Generic Subprograms — C++ vs Java vs C#
| Feature | C++ Templates | Java Generics | C# Generics |
|---|---|---|---|
| Mechanism | Compile-time code expansion | Type erasure (single Object version) | Reification — type info kept at runtime |
| When versions created | Compile time | Once at runtime (Object version) | Runtime for primitives; Object version for objects |
| Primitive types | Yes | No (use wrapper classes) | Yes |
| Wildcards | No (SFINAE/concepts) | Yes (`? extends T`) | No |
| Type constraints | Via concepts/SFINAE | `extends` keyword | `where` clause |
| Separate class per type | Yes (code bloat possible) | No | No (but primitives get their own) |

- Java generics: compiler inserts casts automatically, ensuring type misuses caught at compile time (not runtime)
- C# generic methods: if primitive type → new version created at runtime; if object → Object version reused

### Closures (Section 9.12) — VERY IMPORTANT
- A **closure** is a subprogram plus the referencing environment of its *definition*
- Needed when a subprogram accesses variables from an outer scope that is no longer active
- Variables captured by a closure must have **unlimited extent** (lifetime = full program execution)

```javascript
function makeAdder(x) {
    return function(y) { return y + x; }
}
var add10 = makeAdder(10);  // captures x = 10
var add5  = makeAdder(5);   // captures x = 5
add10(20);  // returns 30
add5(20);   // returns 25
```

Each call to `makeAdder` creates a **new closure** with its own captured `x`.

### Coroutines (Section 9.13) — EXAM IMPORTANT
- A **coroutine** is a subprogram with *multiple entry points*, controlling its own entry points
- Also called **symmetric control** — caller and called exist on a more equal basis
- A coroutine **call** is called a **resume**
- First resume → starts from the beginning
- Subsequent resumes → continue after the last executed statement
- Coroutines produce **quasi-concurrent** (interleaved, not overlapping) execution
- Introduced in SIMULA 67; supported in Lua

```
-- Pseudocode coroutine trace (two coroutines A and B)
coroutine A:          coroutine B:
  print "A1"            print "B1"
  resume B              resume A
  print "A2"            print "B2"
  resume B

-- Starting with A:  A1 → (resume B) → B1 → (resume A) → A2 → (resume B) → B2
-- Output: A1, B1, A2, B2
-- Each resume picks up exactly where the other left off
```

---

## Ch12 — OOP (~5 marks)

### Core OOP Terminology
- **Class**: a template/blueprint (an ADT in OOP context)
- **Object / Instance**: a runtime entity created from a class
- **Method**: a subprogram defining operations on objects
- **Message**: a call to a method (e.g. `obj.meth()`)
- **Message protocol / interface**: the entire collection of an object's methods
- **Subclass / derived class**: inherits from a parent
- **Superclass / parent class**: the class inherited from
- **Class variable**: one per class (shared by all instances)
- **Instance variable**: one per object (each instance has its own copy)
- **Encapsulation**: bundling data and methods, hiding internal details
- **Inheritance**: a subclass acquires members of its parent
- **Polymorphism**: same interface applies to different types
- **Dynamic binding / dynamic dispatch**: correct overriding method selected at runtime based on actual object type

```cpp
// C++ — virtual enables dynamic dispatch
class Animal { public: virtual void speak() { cout << "..."; } };
class Dog : public Animal  { public: void speak() { cout << "Woof"; } };
class Cat : public Animal  { public: void speak() { cout << "Meow"; } };

Animal* a = new Dog();
a->speak();   // → "Woof"  (runtime picks Dog::speak, not Animal::speak)
a = new Cat();
a->speak();   // → "Meow"  (runtime picks Cat::speak)
// Without virtual: always "..." — statically bound to Animal::speak
```

- **Abstract method**: declared but not implemented — subclasses must override (C++: pure virtual `= 0`)
- **Abstract class**: contains at least one abstract method — cannot be instantiated
- **Method overriding**: subclass redefines an inherited method with the same signature
- **Overriding** vs **overloading**: overriding = same signature in subclass; overloading = same name, different signature in same class

```java
class Base {
    void foo(int x) { }        // original
}
class Derived extends Base {
    @Override
    void foo(int x) { }        // OVERRIDING — same signature, in subclass
    void foo(String s) { }     // OVERLOADING — same name, different param type
}
```

- **Open recursion**: `this`/`self` allows a method to call the overridden version in a subclass dynamically

```java
class Shape {
    void draw()   { System.out.println("Shape"); }
    void render() { this.draw(); }   // 'this' resolves at runtime
}
class Circle extends Shape {
    @Override void draw() { System.out.println("Circle"); }
}
new Circle().render();   // calls Shape.render(), but this.draw() → Circle.draw() → "Circle"
// Without open recursion (static binding), render() would always print "Shape"
```

### Any OOP Language Must Support
1. Abstract data types (classes)
2. Inheritance
3. Polymorphism via dynamic binding

### Inheritance
- **Single inheritance**: one direct parent (Java, C#, Smalltalk)
- **Multiple inheritance**: more than one direct parent (C++)
- **Diamond problem**: when two parents share a common ancestor → name collision ambiguity

```cpp
// C++ diamond problem
class A { public: void show() {} };
class B : public A {};
class C : public A {};
class D : public B, public C {};   // D inherits show() from both B and C via A

D obj;
obj.show();            // AMBIGUOUS — which show()? compiler error
obj.B::show();         // disambiguate with scope resolution
obj.C::show();
```

- In C++, disambiguate with scope resolution operator (`Drawing::display()`)
- **is-a relationship**: inheritance (a Dog is-a Animal)
- **has-a relationship**: composition (a Car has-a Engine)
- A derived class is a **subtype** of parent if it only adds members and overrides compatibly — a subclass is not a subtype if it removes or restricts inherited members

### Access Control
| Modifier | Visible to |
|---|---|
| `public` | All (class, subclasses, clients) |
| `protected` | Class + subclasses (not clients) |
| `private` | Class only |

### C++ Specific
- Methods are **statically bound by default** (faster)
- For dynamic binding: declare method as `virtual`
- **Pure virtual function** (`virtual void draw() = 0`): defines abstract method → class becomes abstract
- **Public derivation** (common): inherited public/protected members stay public/protected in subclass → subclass is a subtype
- **Private derivation**: inherited public/protected become private → subclass is NOT a subtype

```cpp
class Animal { public: void breathe() {} };
class Dog : public  Animal {};   // public derivation: Dog IS-A Animal (subtype)
class Robot : private Animal {}; // private derivation: breathe() becomes private → Robot is NOT a subtype
```

- If objects on stack (not heap): assignment truncates objects (**object slicing**), binding is not dynamic

```cpp
Dog d;
Animal a = d;    // object slicing: Dog-specific data LOST; a is just an Animal
a.speak();       // static binding → Animal::speak (even if Dog overrides it)

Animal* p = &d;  // pointer: no slicing
p->speak();      // dynamic binding → Dog::speak  (if virtual)
```

- Dynamic binding only through **pointers or references**

### Java Specific
- All data are objects except primitive types (wrapper classes exist)
- All objects heap-dynamic, garbage collected
- Only **single inheritance**
- **Interface**: like an abstract class — only method declarations and named constants; a class can implement multiple interfaces → provides some benefits of multiple inheritance

```java
interface Drawable { void draw(); }
interface Printable { void print(); }
class Report implements Drawable, Printable {   // implements multiple interfaces
    public void draw()  { ... }
    public void print() { ... }
}
```

- All messages dynamically bound EXCEPT: `final`, `private`, or `static` methods (dynamic binding serves no purpose there)

### C# Specific
- Similar to Java; supports both classes and structs
- `struct`: stack-dynamic, no inheritance, simpler than C++ struct
- Base class method marked `virtual`; overriding method marked `override`
- Abstract methods marked `abstract`
- No multiple inheritance; uses interfaces like Java

### Smalltalk (Pure OOP)
- Everything is an object — no primitive types
- All objects are heap-dynamic (slow due to garbage collection)
- All computation is message passing between objects (slow)
- All binding of messages to methods is **dynamic**
- No multiple inheritance; all subclasses are subtypes
- Typeless reference variables; references implicitly dereferenced

### Ruby
- Everything is an object
- Class definitions are **executable** — can add members at runtime
- All data is **private** (cannot change); methods can be public, protected, or private
- Method access is checked at runtime
- No true multiple inheritance; subclasses are not necessarily subtypes (access can change)

---

## Ch1 — Introduction (~4 marks)

### Language Evaluation Criteria
| Criterion | Description | Key factors |
|---|---|---|
| **Readability** | Ease of reading and understanding | Simplicity, orthogonality, data types, syntax |
| **Writability** | Ease of creating programs | Simplicity, orthogonality, abstraction, expressivity |
| **Reliability** | Performs to specification under all conditions | Type checking, exception handling, aliasing, readability/writability |
| **Cost** | Total cost of using the language | Training, writing, compiling, executing, maintaining, reliability |

**Other criteria**: portability, generality, well-definedness

### Readability Sub-factors
- **Simplicity**: manageable feature set; minimal feature multiplicity (multiple ways to do the same thing hurts readability); minimal operator overloading
- **Orthogonality**: see below
- **Data types**: adequate predefined types; absence of required types forces simulation
- **Syntax**: sensible special words; meaningful keywords; block notation; self-descriptive constructs

### Orthogonality — WILL BE TESTED
- A **relatively small set of primitive constructs** that can be combined in a small number of ways, **and every possible combination is legal**
- An orthogonal language feature is **context-independent** — no exceptions to how it can be combined
- Lack of orthogonality = exceptions and special cases
- Example of orthogonality: a single `+` operator for int and float addition — all combinations legal
- Example of non-orthogonality in C: a function cannot return an array (restriction on combining return type with array type)
- **Too much orthogonality** can hurt readability (ALGOL 68) — unrestricted combinations may be nonsensical

```
// Non-orthogonal: C arrays cannot be returned from functions
int[] getArr() { ... }   // ILLEGAL in C
int*  getArr() { ... }   // must use pointer instead — special case / exception

// Orthogonal: pointer types combine uniformly — pointer to any type, pointer to pointer, etc.
int**   pp;   // pointer to pointer to int — all combinations legal
float** fp;   // same rule applies to float — no exceptions
```

### Language Design Trade-offs
- **Reliability vs cost of execution**: Java checks array index bounds (more reliable, but slower)
- **Readability vs writability**: APL has many powerful operators → compact but unreadable
- **Writability vs reliability**: C++ pointers are powerful but reduce reliability

### Reasons for Studying PLs — apply to the scenario given
1. Increased ability to express ideas (can't express what you can't describe)
2. Better background for choosing appropriate languages
3. Increased ability to learn new languages
4. Better understanding of implementation (why languages work as they do)
5. Better use of languages already known
6. Overall advancement of computing

### Language Categories
| Category | Description | Examples |
|---|---|---|
| **Imperative** | Variables, assignment, iteration | C, Java, C++, Python |
| **Functional** | Applying functions to parameters | Scheme, LISP, ML, F# |
| **Logic** | Rule-based, no specified order | Prolog |
| **Markup/hybrid** | Markup extended with programming | JSTL, XSLT |

### Implementation Methods
| Method | Description | Use |
|---|---|---|
| **Compilation** | Translate to machine code | Large commercial apps; fast execution |
| **Pure interpretation** | Execute directly via interpreter | Scripting; easy debugging; 10–100× slower |
| **Hybrid** | Translate to intermediate code (bytecode), then interpret | Java (JVM), Perl |
| **JIT** | Hybrid variant; subprograms compiled to machine code when first called; machine code kept for reuse | Java JIT, .NET |

### Influences on Language Design
- **Von Neumann architecture**: data and programs in memory separate from CPU → basis for imperative languages (variables = memory cells, assignment = piping, iteration is efficient)
- **Programming methodologies**: structured programming (1960s) → data abstraction (1970s) → OOP (1980s)

---

## Ch5 — Names, Bindings, and Scopes (~4 marks)

### Names
- **Reserved word**: cannot be used as a programmer-defined name (`int` in C++ — always means a type)
- **Keyword**: has special meaning only in certain contexts (Fortran: `Real VarName` → Real is a keyword; `Real = 3.4` → Real is a variable)

### Variable Attributes (6)
Name, Address, Value, Type, Lifetime, Scope
- **Alias**: two or more names for the same memory location — created via pointers, references, unions — bad for readability

```c
int x = 5;
int *p1 = &x, *p2 = &x;  // p1 and p2 are aliases — both refer to x's memory
*p1 = 99;
// now x == 99 AND *p2 == 99 — surprising side effect
```

### Binding and Binding Times
- **Binding**: an association between an attribute and an entity
- **Language design time**: meaning of operators (e.g. `*` = multiplication)
- **Language implementation time**: range of `int`
- **Compile time**: type of a variable in C/Java
- **Load time**: address of a `static` C variable
- **Runtime**: value of a variable; address of a stack-dynamic variable
- **Static binding**: occurs before runtime, unchanging
- **Dynamic binding**: occurs at or during runtime, can change

### Type Binding
- **Explicit declaration**: `int myVar;` (C++)
- **Implicit declaration**: type inferred from first use or naming convention (Perl, Ruby, PHP)
  - Advantage: writability; Disadvantage: reduces reliability (typos not caught)
- **Type inferencing**: compiler determines type from context (`var value = 12` in C# → int)
- **Static type binding**: bound at compile time (C, Java, C++)
- **Dynamic type binding**: bound when value assigned at runtime (Python, JavaScript, Ruby, PHP)
  - More flexible; disadvantage: type errors only caught at runtime, slower execution

```python
# Python — dynamic type binding: same variable changes type at runtime
x = 5          # x is int
x = "hello"    # x is now str — type re-bound on assignment
x = [1, 2, 3]  # x is now list
# contrast with Java: int x = 5; x = "hello"; // COMPILE ERROR
```

### Storage Bindings and Lifetimes
| Category | Allocation | Deallocation | Example |
|---|---|---|---|
| **Static** | Before execution begins | End of program | C `static` variables |
| **Stack-dynamic** | At block/subprogram entry | At block/subprogram exit | Normal local variables |
| **Explicit heap-dynamic** | Explicit `new`/`malloc` | Explicit `delete`/`free` | C++ dynamic variables |
| **Implicit heap-dynamic** | By assignment | Garbage collected | All APL variables; Perl/JS strings and arrays |

- Static advantage: efficient direct addressing; history-sensitive subprograms
- Static disadvantage: no recursion; storage cannot be shared
- Stack-dynamic advantage: supports recursion, conserves storage
- Implicit heap-dynamic advantage: maximum flexibility; disadvantage: inefficient (all attributes dynamic), less error detection

### Scope
- **Scope of a variable**: the range of statements in which it is visible
- **Local variables**: declared in the current subprogram
- **Non-local variables**: visible but not declared locally
- **Global variables**: visible throughout the entire program

#### Static (Lexical) Scoping
- Scope determined by **physical structure** of source code
- Search: start at local unit → move to enclosing scopes → stop when declaration found
- A variable in a closer scope **hides** a variable with the same name in an enclosing scope
- Languages that allow nested subprograms (so nested scopes exist): Ada, JavaScript, Common LISP, Scheme, Fortran 2003, F#, Python
- Java/C#: **no variable hiding in blocks** (hiding is an error)

#### Dynamic Scoping
- Scope determined by the **calling sequence** at runtime — search back through the call chain
- Advantage: convenience (no need to pass parameters)
- Disadvantages: harder to read, can't statically type check, slower access to non-local variables

#### Static vs Dynamic — Classic Example
```
Big: declare X
  Sub1: declare X; call Sub2
  Sub2: refer to X
  call Sub1
```
- Static: Sub2 sees `X` in Big (determined by where Sub2 is *defined* in source)
- Dynamic: Sub2 sees `X` in Sub1 (most recent caller on the call stack that declared X)

### Referencing Environments
- **Static scoping**: local variables + all variables in enclosing static scopes
- **Dynamic scoping**: local variables + all variables in all active (started, not terminated) subprograms
- Know how to determine the referencing environment at a given point in a program

### Named Constants
- A name bound to a value only once; improves readability and reliability
- **Static (manifest) constant**: value bound at compile time (`const int SIZE = 10 + 5`)
- **Dynamic constant**: value bound at runtime (`const int SIZE; SIZE = a + 1`) — only assignable once
- C# has both: `const` (compile-time) and `readonly` (runtime, field only, set in constructor)

---

## Ch6 — Data Types (~3 marks)

### Primitive Data Types
- **Integer**: binary representation; multiple sizes (byte, short, int, long in Java)
- **Floating-point**: IEEE 754; approximations of real numbers; float/double precision
- **Decimal**: exact decimal representation (BCD); used in business (COBOL, C# `decimal`); accurate but wastes memory
- **Boolean**: true/false; advantage is readability
- **Character**: stored as numeric codes; ASCII (8-bit), Unicode UCS-2 (16-bit), UCS-4 / UTF-32 (32-bit)
- **Complex**: two floats — real and imaginary parts (C99, Fortran, Python)

### String Types
- C/C++: char arrays + library functions; null-terminated; limited dynamic length
- Java: `String` class (immutable, static length); `StringBuffer`/`StringBuilder` (mutable)
- Python/Fortran: primitive type with operations
- Dynamic length strings: Perl, JavaScript (variable length, no max)

### Array Types
| Category | Subscript range binding | Storage binding |
|---|---|---|
| **Static** | Static | Static |
| **Fixed stack-dynamic** | Static | At declaration (stack) |
| **Stack-dynamic** | Dynamic (runtime) | Dynamic (stack), then fixed |
| **Fixed heap-dynamic** | Dynamic | Heap, then fixed (`new` in C++) |
| **Heap-dynamic** | Dynamic, can change | Heap, can grow/shrink (Python list, JS array) |

- **Rectangular array**: all rows same length (Fortran, Ada)
- **Jagged array**: rows can differ in length — actually arrays of arrays (C, C++, Java)
- **Associative array**: unordered key-value pairs indexed by keys (Python dict, Perl hash)
- **Heterogeneous array**: elements of different types (Perl, Python, JS, Ruby)
- Python array assignment = reference change, not copy

### Record (Struct) Types
- Heterogeneous aggregate of named fields
- COBOL: level numbers for hierarchy; supports elliptical references (can omit record names if unambiguous)
- Other languages: dot notation for field access; records can be nested (Ada)

### Tuple Types
- Like a record but elements are **not named** — Python tuples; immutable
- Useful for returning multiple values from a function

### Union Types
- Variable that can store values of **different types** at different times (one value at a time)
- **Free union** (C, C++, Fortran): no type tag — programmer must track current type; **unsafe**
  ```c
  union flexType { int intEl; float floatEl; };
  union flexType u;
  u.intEl = 42;
  float x = u.floatEl;   // garbage — read wrong field; no error from compiler
  ```
  Accessing wrong field is legal but produces garbage
- **Discriminated union**: includes a **type tag (discriminant)** — type-safe; supported by Ada, ML, Haskell, F#
  - Example: `Form` tag set to `Circle` → can only access `Diameter`, not `Side_1`, etc.

### Pointer and Reference Types
- **Pointer**: stores a memory address; used for dynamic memory management and indirect addressing
- **Dangling pointer**: points to deallocated memory — hazardous (undefined behaviour)

```cpp
int* p = new int(5);
delete p;     // memory freed — p still holds the old address
*p = 10;      // DANGLING POINTER: undefined behaviour (could corrupt memory or crash)
p = nullptr;  // good practice: null the pointer after delete
```

- **Memory leak / lost heap-dynamic variable**: allocated memory no longer accessible — garbage

```cpp
int* p = new int(5);
p = new int(10);   // original int(5) is now unreachable — memory leak
```

- `void*` in C++: can point to any type; cannot be dereferenced without casting → affects type checking
- **Reference** (C++, Java, C#): similar to pointer but safer — always bound to an object, implicitly dereferenced, cannot be reseated in Java
- Java: references only (no raw pointers) — improves reliability; C# has both (unsafe pointers in `unsafe` blocks)

### Type Checking
- **Type checking**: ensures operands of operators are compatible types
- **Coercion**: implicit type conversion — reduces reliability (hides type mismatches)

```c
int   i = 5;
float f = i;            // coercion: int silently widened to float 5.0
float r = i + 3.14;     // i coerced to float before addition
// Danger: int x = 3.9; → x becomes 3 (truncation), no warning in C
```

- **Strongly typed**: ALL type errors always detected (Ada, Java, C# — stronger than C/C++)
- C/C++: not strongly typed (unions not type checked; pre-C99 parameter types not checked)
- Java/C#: more strongly typed than C++ but explicit casts can still cause runtime type errors

### Type Equivalence
- **Name type equivalence**: two variables are compatible only if they share the same **type name** — strict, safe, easy to implement
- **Structure type equivalence**: two variables are compatible if their **structures are identical** — more flexible, harder to implement, may cause unintended compatibility

```ada
-- Ada uses name type equivalence
type Celsius    is new Float;
type Fahrenheit is new Float;
C : Celsius    := 100.0;
F : Fahrenheit;
F := C;         -- COMPILE ERROR: different names, even though both are Float underneath
```

```c
// C uses structure type equivalence for structs
struct Point2D { int x; int y; };
struct Coord   { int x; int y; };   // identical structure to Point2D

struct Point2D p;
struct Coord   c;
p = c;   // legal in C — same structure (structure equivalence)
         // would be illegal under name equivalence
```

---

## Ch15 — Functional PL Theory (~3 marks)

### Core Concepts
- Functional language design is based on **mathematical functions** — unconcerned with machine architecture
- **Pure functional language**: no variables; all repetition through recursion; no side effects

### Side Effects and Referential Transparency
- **Functional side effect**: a function modifies a parameter or a non-local variable
- Problem: `b = a + fun(&a)` — if `fun` changes `a`, result depends on operand evaluation order

```c
int a = 5;
int modify(int *x) { *x = 10; return 1; }
int use(int x)     { return x; }
// modify(&a) + use(a) could be:
//   1 + 5 = 6  (if use(a) evaluated first, before a changes)
//   1 + 10 = 11 (if modify runs first)
// Result is undefined — order-dependent
```

- Two solutions: (1) disallow side effects entirely, (2) require fixed operand evaluation order
- **Referential transparency**: any two equivalent expressions can be substituted for one another without changing program behaviour
  - Only possible if there are **no side effects**
  - `result1 = (fun(a) + b) / (fun(a) – a)` — if `fun` has no side effects, can replace `fun(a)` with `temp` → `result1 = result2`
- Advantage: program semantics much easier to understand

### Scheme Essentials
- Dialect of LISP; mid-1970s; designed for education; uses static scoping
- Everything is a **list**: `(operator operand1 operand2 ...)` — functions and data have same form
- **First-class functions**: can be passed as parameters, returned, applied to other functions
- Repetition is done entirely through **recursion** (no variables, no loops)
- `#t` = true, `#f` = false; `()` can also represent false; any non-null list is true

### Scheme Primitive Functions
| Function | Description | Example |
|---|---|---|
| `car` | First element of list | `(car '(a b c))` → `a` |
| `cdr` | Tail (all but first) | `(cdr '(a b c))` → `(b c)` |
| `cons` | Prepend element to list | `(cons 'a '(b c))` → `(a b c)` |
| `null?` | True if empty list | `(null? '())` → `#t` |
| `list?` | True if parameter is a list | |
| `eqv?` | Equality for atoms (preferred) | `(eqv? 'a 'a)` → `#t` |
| `eq?` | Pointer equality — unreliable for lists/floats | |
| `quote` / `'` | Prevent evaluation | `'(a b c)` = `(quote (a b c))` |
| `list` | Build a list from parameters | `(list 'a 'b 'c)` → `(a b c)` |
| `define` | Bind name to value or function | `(define (square x) (* x x))` |
| `if` | `(if pred then else)` | |
| `cond` | Multi-way selector | |
| `let` | Local name bindings | `(let ((top (+ a b))) (/ top 2))` |
| `display` | Print expression | |
| `not` | Boolean NOT | |

- `cons` second parameter must be a list; `(cons 'a 'b)` → dotted pair `(a . b)` (usually unintended)
- `cdr` of a single-element list → `()`
- `eqv?` preferred over `eq?`; `eqv?` does NOT work for lists

### Scheme List Processing Pattern
```scheme
; member — check if atom is in simple list
(define (member atm lis)
   (cond
      ((null? lis) #f)                    ; base case: empty list
      ((eqv? atm (car lis)) #t)           ; base case: found
      (else (member atm (cdr lis)))       ; recursive: check tail
   ))

; append — concatenate two lists
(define (append lis1 lis2)
   (cond
      ((null? lis1) lis2)                            ; base case
      (else (cons (car lis1) (append (cdr lis1) lis2))) ; recursive
   ))
```

### Tail Recursion
- A **tail recursive** function has the recursive call as the **last operation**
- Scheme converts tail recursive functions to iteration automatically (required by language definition)
- Non-tail recursive factorial: `(* n (factorial (- n 1)))` — multiply is the last op, not the call
- Tail recursive version: pass a partial result accumulator as a parameter

```scheme
; NOT tail recursive — multiply happens AFTER the recursive call returns
(define (fact n)
   (if (= n 0) 1
       (* n (fact (- n 1)))))   ; last op is *, not fact

; Tail recursive — recursive call IS the last operation
(define (fact-tail n acc)
   (if (= n 0) acc
       (fact-tail (- n 1) (* n acc))))   ; last op is the call itself
(fact-tail 5 1)   ; → 120
```

### Functional Forms (Higher-Order Functions)
- **Functional form**: a function that takes functions as parameters or yields a function as result
- **Apply-to-all (mapcar)**: applies a function to every element of a list, building a new list
  ```scheme
  (define (mapcar fun lis)
     (cond
        ((null? lis) ())
        (else (cons (fun (car lis)) (mapcar fun (cdr lis))))
     ))
  (mapcar square '(3 4 2))  ; → (9 16 4)
  ```

### Functional vs Imperative
| Imperative | Functional |
|---|---|
| Efficient execution | Inefficient execution |
| Complex syntax and semantics | Simple syntax and semantics |
| Concurrency is programmer-designed | Programs can automatically be made concurrent |

---

## Ch16 — Logic PL Theory (~2 marks)

### Core Concepts
- Logic programming is **declarative** — specify the *form* of the result, not the procedure
- A program = a set of **facts** and **rules**; execution = proving a **query/goal**
- Based on **first-order predicate calculus** and **resolution**

### Terminology
- **Proposition**: a logical statement that may or may not be true
- **Functor**: the symbol naming a relationship (e.g. `likes`, `parent`)
- **Atom / constant**: lowercase letters — represents a specific object (e.g. `jon`, `bob`)
- **Variable**: starts with uppercase — represents any object (e.g. `X`, `MyVar`)
- **Atomic proposition**: `functor(param1, param2, ...)` — e.g. `like(seth, osx)`
- **Fact statement**: headless Horn clause — assumed true (e.g. `female(shelley).`)
- **Rule statement**: headed Horn clause — `consequent :- antecedent` (read: "if antecedent then consequent")
- **Goal / query**: proposition Prolog must try to prove (e.g. `?- parent(X, mike).`)
- Commas in rules/queries = logical AND

### Horn Clauses
- **Headless Horn clause**: states a fact (`father(bob, jake).`)
- **Headed Horn clause**: states a rule — right side (antecedent), left side (consequent)
  `likes(bob, trout) :- likes(bob, fish), fish(trout).` → "If bob likes fish and trout is a fish, then bob likes trout"

### Unification
- Finding variable bindings that make two terms **identical**
- `father(X, jake)` → "Find X such that X is the father of jake"
- If unification fails → **backtrack** and try a different binding

### Inferencing Process
- **Resolution**: to prove a goal, find a clause whose head unifies with the goal, then prove its body
- **Top-down / backward chaining** (Prolog): start from the goal, find a path to the facts — efficient when few matching facts
- **Bottom-up / forward chaining**: start from facts, try to reach the goal — better for large sets of facts
- **Depth-first search** (Prolog): prove each subgoal completely before moving to the next
- **Backtracking**: when a subgoal fails, undo the last variable binding and try the next matching clause — can be expensive

### Tracing Model (4 events)
| Event | When |
|---|---|
| **Call** | Beginning of attempt to satisfy a goal |
| **Exit** | Goal has been satisfied |
| **Redo** | Backtracking occurs |
| **Fail** | Goal fails |

Example trace: `?- likes(jake, X), likes(darcie, X).`
- Call: `likes(jake, _0)` → Exit: X = chocolate → Call: `likes(darcie, chocolate)` → Fail → Redo → Exit: X = apricots → Call: `likes(darcie, apricots)` → Exit → **X = apricots**

### Prolog Syntax Summary
```prolog
% Facts
female(shelley).
father(bill, jake).

% Rules
parent(X, Y) :- father(X, Y).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Query
?- parent(X, jake).
```

### Prolog Arithmetic
- `is` operator: evaluates RHS expression and binds to LHS variable
  `A is B / 17 + C.` — all RHS variables must be already instantiated; LHS must be uninstantiated
- `Sum is Sum + Number.` — always **illegal** (LHS already instantiated if Sum is; uninstantiated RHS if not)
- Comparison operators: `<`, `>`, `=<`, `>=`, `=` (equality test, not assignment)

### Prolog List Processing
- `[Head | Tail]` — Head = first element, Tail = rest of list
- Anonymous variable `_` — used when we don't care about the value

```prolog
% member
member(Element, [Element | _]).
member(Element, [_ | Lis]) :- member(Element, Lis).

% append
append([], Lis, Lis).
append([Head | Lis_1], Lis_2, [Head | Lis_3]) :-
    append(Lis_1, Lis_2, Lis_3).

% reverse
reverse([], []).
reverse([Head | Tail], List) :-
    reverse(Tail, Result),
    append(Result, [Head], List).
```

- Base case statements must appear **before** recursive cases (Prolog matches top to bottom)
- No need to specify "false" cases — Prolog automatically fails if no clause matches

### Deficiencies of Prolog
- **Resolution order control**: programmer must order clauses carefully for efficiency (more likely to succeed first)
- **Closed-world assumption**: "false" means Prolog *cannot prove* it, not that it *is* false — missing facts cause incorrect "false"
- **Negation problem**: `not(X)` succeeds if Prolog *cannot prove* X — doesn't mean X is logically false
  - `sibling(X,Y) :- parent(M,X), parent(M,Y), not(X=Y).` — works in practice but isn't true logical negation
- **Intrinsic limitations**: some tasks are inherently inefficient (e.g. sorting via permutation checking)

---

## Ch7 — Expressions (~2 marks)

### Operator Precedence and Associativity
- **Precedence**: which operators bind more tightly (parentheses → unary → `**` → `*`/`/` → `+`/`-`)
- **Associativity**: order for equal-precedence operators
  - Left-to-right: most operators (`a - b - c` = `(a - b) - c`)
  - Right-to-left: exponentiation (`a ** b ** c` = `a ** (b ** c)`), unary prefix operators
- APL: only one precedence level — all operators right-to-left associative
- In Scheme/LISP: prefix notation eliminates all precedence/associativity issues (`(+ a (* b c))`)
- Ruby: most operators are implemented as **methods** — can all be overridden by programmer

### Operand Evaluation Order
- Most languages do not specify evaluation order of operands
- Matters when operands have **side effects**: `f(a) + g(a)` — if `f` modifies `a`, result is order-dependent

```c
int a = 5;
int f(int *x) { *x = 10; return 1; }   // side effect: changes a
int g(int  x) { return x; }             // no side effect

// f(&a) + g(a) is undefined:
//   evaluate g first → g(5) = 5, then f → result = 1 + 5 = 6
//   evaluate f first → a becomes 10, then g(10) = 10 → result = 1 + 10 = 11
```

- Java: operands evaluated left-to-right

### Side Effects and Referential Transparency
- **Functional side effect**: a function modifies a non-local variable or parameter
- **Referential transparency**: an expression can be replaced by its value without changing program behaviour — only possible without side effects (see Ch15)
- Short-circuit evaluation can interact with side effects: `(a > b) || (b++ / 3)` — `b++` may not execute if `a > b`

```c
int b = 5;
if (true || (b++ / 3)) { }   // short-circuit: right side never evaluated
// b is still 5 — b++ did NOT execute
```

### Type Conversions
- **Narrowing conversion**: to a type with fewer values (e.g. float → int) — not always safe
- **Widening conversion**: to a type with more values (e.g. int → float) — generally safe, may lose accuracy
- **Coercion**: implicit widening conversion — reduces reliability (can mask typos)

```c
int   i = 5;
float f = i;           // implicit coercion: int → float (widening, safe)
int   x = 3.9;         // implicit coercion: float → int = 3 (narrowing, data lost, no error in C)
float r = i + 3.14;    // i coerced to float before addition
```

- C/C++/Fortran/Perl: coerce any numeric type in any direction
- Java/C#: only widening coercions in mixed-mode assignment (safer)
- ML/F#: no coercions at all

### Overloaded Operators
- Same operator symbol for different purposes (e.g. `+` for int and float)
- C++: `&` overloaded as bitwise AND and address-of — can mask errors
- User-defined overloading: C++, C#, F#, Python, Ruby
- Problems: loss of readability (must find types to understand meaning), nonsensical operations possible

### Short-Circuit Evaluation
- `&&`/`||` in C/C++/Java: standard short-circuit
- `&`/`|` in C/C++: bitwise — NOT short-circuit

```java
// Short-circuit prevents null pointer error:
if (list != null && list.size() > 0) { ... }
// If list is null, second condition never evaluated — no NullPointerException
// With & (non-short-circuit): list.size() still runs → crash
```

### Assignment
- C-based, Perl, JavaScript: assignment produces a result (the assigned value) → can be used as expression
  - Common use: `while ((ch = getchar()) != EOF) {...}`
  - Risk: `if (x = y)` legal (intended `if (x == y)`)
- Perl/Ruby/Lua: multiple-target multiple-source assignment `($a, $b) = ($b, $a)` → easy swap

---

## Ch2 — PL History (~1 mark)

For each language know: **environment → how it affected design → main contribution**

| Language | Environment / Context | Main Contribution |
|---|---|---|
| **Fortran I** | Scientific; IBM 704; machine efficiency paramount; no programming methodology | First compiled HLL; showed compilation was viable; very fast code |
| **LISP** | AI research at MIT; symbolic computation; list processing | First functional language; dynamic typing; garbage collection; recursion |
| **ALGOL 60** | Academic; need for machine-independent, universal language; no I/O standards | Block structure; recursive subprograms; stack-dynamic arrays; first formally defined syntax (BNF); basis for all subsequent imperative languages |
| **COBOL** | Business data processing; non-technical users; English-like design goal | Hierarchical data structures (records); long names; English-like readability; still most-used business language |
| **BASIC** | Timesharing for non-science students; easy to use | First widely-used timesharing language |
| **PL/I** | IBM trying to unify scientific (Fortran) and business (COBOL) users; System/360 | First unit-level concurrency; first exception handling; first pointer data type |
| **APL** | IBM; hardware description; dynamic typing and storage | Highly expressive; very large number of operators; programs very difficult to read |
| **SIMULA 67** | System simulation in Norway; modelling real-world entities | First data abstraction with classes and objects; introduced coroutines |
| **ALGOL 68** | Based on orthogonality; extension of ALGOL 60 | User-defined data structures; reference types; flex arrays — influenced Pascal, C, Ada |
| **Pascal** | Teaching structured programming; Wirth (former ALGOL 68 committee) | Simple, clean educational design; strong typing |
| **C** | Systems programming at Bell Labs; Unix OS | Efficient low-level access + high-level constructs; portability through Unix |
| **Prolog** | AI; automated theorem proving; natural language processing | First logic programming language; declarative semantics |
| **Ada** | US DoD; embedded systems; standardizing 450+ languages; reliability-critical | Packages (data abstraction); elaborate exception handling; generic program units; concurrency |
| **Smalltalk** | Xerox PARC; GUI systems; non-programmer users | First full OOP language (data abstraction + inheritance + dynamic binding); pioneered GUI design |
| **C++** | Bell Labs; extending C with OOP; large-scale systems | OOP on top of C; templates; exception handling; widely adopted; backward-compatible with C |
| **Java** | Sun; embedded devices; C/C++ unreliable for this; web applets | JVM bytecode portability; garbage collection; removed unsafe C++ features; security model |
| **C#** | Microsoft .NET platform; component-based development | IL + JIT for all .NET languages interoperability; combines C++/Java/Delphi features; added delegates, properties |
| **Python** | Scripting; CGI; system administration; data science | OO interpreted scripting; garbage collection; large library; dynamic typing with type checking |
| **Ruby** | Replacement for Perl/Python; pure OOP | Everything is an object; operators as methods; classes/objects modifiable at runtime |

---

## Ch8 — Control Structures (~1 mark)

### Selection Statements
- **Dangling else**: `if (a) if (b) s1 else s2` — which if gets the else?

```c
// The else matches the NEAREST unmatched if — so this binds to inner if:
if (a)
    if (b) s1;
    else s2;    // else belongs to inner if(b), NOT outer if(a)
// To attach else to outer if:
if (a) {
    if (b) s1;
} else s2;      // braces force the intended grouping
```

- Java/C/C++: else matches nearest preceding unmatched if
- Perl: forces compound statements (braces required) → no ambiguity
- Python: indentation removes ambiguity
- **switch/case** (C/C++/Java): falls through by default → needs `break`
- **C#**: disallows implicit fall-through (each segment must end with `break` or `goto`) — increases reliability
- **Selector expressions** (ML, F#, LISP): `if` is an expression, evaluates to a value

### Iterative Statements
- **Counter-controlled** (`for`): loop variable, initial/terminal/stepsize; C-based loop has no explicit loop variable — full expressions used
- **Logically-controlled**: pretest (`while`) vs posttest (`do-while`)
- Python `for`: `for var in object` — optional `else` clause executes if loop terminates normally (not via `break`)
- **Ruby blocks**: a block is code passed to a method — defined with `{ }` or `do...end`
  - Method uses `yield` to execute the block and pass values to it
  - Block has formal parameter(s): `list.each {|value| puts value}`
  - Ruby `for` statements are converted to `upto` calls

```ruby
# yield — method executes the block passed by the caller
def repeat(n)
    n.times { yield }         # yield: run the block each iteration
end
repeat(3) { puts "Hello" }   # → Hello  Hello  Hello

# yield with argument — passes a value into the block
def double_it(x)
    yield(x * 2)              # passes x*2 into the block
end
double_it(5) { |n| puts n }  # → 10
```

### Guarded Commands (Dijkstra) — PAY SPECIAL ATTENTION
Designed to support **formal program verification** (correctness proofs)
- Basic idea: if order of evaluation does not matter, the program should not specify an order

**Selection (if...fi):**
```
if Boolean_exp_1 -> statement_1
[] Boolean_exp_2 -> statement_2
...
[] Boolean_exp_n -> statement_n
fi
```
- Evaluate **all** Boolean expressions
- If **more than one** is true → choose one **non-deterministically**
- If **none** are true → **runtime error**

```
-- Concrete example: absolute value (non-deterministic when x=0 is avoided)
if x > 0 -> result := x
[] x < 0 -> result := -x
fi
-- If x=3:  only first guard true → result = 3
-- If x=-2: only second guard true → result = 2
-- If x=0:  NEITHER guard is true → runtime error
```

**Repetition (do...od):**
```
do Boolean_exp_1 -> statement_1
[] Boolean_exp_2 -> statement_2
...
[] Boolean_exp_n -> statement_n
od
```
- Evaluate all guards each iteration
- If more than one true → choose one non-deterministically, **repeat**
- If none are true → **exit loop**

```
-- Concrete example: sort two variables so x <= y
do x > y -> temp := x; x := y; y := temp
od
-- If x=7, y=3: guard true → swap → x=3, y=7 → guard false → exit
-- Loop always terminates because each swap reduces disorder
```

- Supports: verification is relatively simple if only guarded commands used
- Basis for CSP and Ada concurrency models

---

## Quick Revision — Things Guaranteed or Strongly Flagged

| Topic | Chapter | Evidence |
|---|---|---|
| **Orthogonality** | Ch1 | Lecturer said "will definitely be tested" |
| **Closures / MakeAdder output tracing** | Ch9 | "Very important", must provide output |
| **Coroutines output tracing** | Ch9 | Must provide output of pseudocode; "easy, will probably come up" |
| **Shallow/deep/ad-hoc binding** | Ch9 | Slides say "important for examination purposes" (×3) |
| **Parameter passing methods** | Ch9 | "Important" |
| **Sections 9.6 and 9.7 (generics)** | Ch9 | Explicitly flagged "very important" |
| **Generic subprograms C++ vs Java vs C#** | Ch9 | Slides say "most important part... important for the exam" |
| **OOP terminology** | Ch12 | "Very important" |
| **Guarded commands** | Ch8 | Slide note: "Pay attention... probably a question in test/exam" |
| **Ruby blocks** | Ch8 | "Make sure you understand" |
| **Referential transparency / side effects** | Ch7 + Ch15 | Mentioned across two chapters |
| **Discriminated unions** | Ch6 | "Pay attention" |
| **Name vs structure type equivalence** | Ch6 | Highlighted in scope |
| **Prolog backward chaining + depth-first** | Ch16 | Core mechanism of the whole chapter |
| **Prolog tracing model (Call/Exit/Redo/Fail)** | Ch16 | With example in slides |
| **Prolog deficiencies** | Ch16 | Whole chapter is examinable |
| **Scheme list functions (car/cdr/cons/null?)** | Ch15 | Needed for both MCQ and implementation question |
