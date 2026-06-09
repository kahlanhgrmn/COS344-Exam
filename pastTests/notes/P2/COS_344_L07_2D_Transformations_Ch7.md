COS 344: L7 Chapter 7: 2D Shapes and
Transformations
Cobus Redelinghuys
02/03/2026

- Today, we will look at modelling and animations for 2D
objects.
- After today’s lecture, you should be able to start planning
your model for Practical 2.
- Today’s lecture contains a set of examples, which are posted
on ClickUp.
- Not all of this week’s content is in the textbook!

- In order to achieve transformation, a transformation matrix is
needed.
- Why a matrix and not just the formulae?
- For the moment, ignore how the matrix is created.
- This will be discussed later.

Transformation application algorithm
The pseudocode below describes how to apply the transformation
matrix.
Algorithm 1 Pseudo-code for applying a transformation matrix
Require: Matrix T {Transformation matrix}
Require: Object o {Object modeled by a set of vertices}
List vertices = o.getVertices()
for each vertex v in vertices do
v’ = Tv; {Matrix multiplied with a vector}
updatePoint(o, v, v’)
end for
draw(o.getVertices())

Transformation application algorithm
An alternative pseudocode for applying the transformation matrix.
Algorithm 2 Pseudo-code for applying a transformation matrix
Require: Matrix T {Cumulative Transformation matrix}
Require: Object o {Object modeled by a set of vertices}
List vertices = o.getVertices()
List updatedVertices = []
for each vertex v in vertices do
v’ = Tv; {Matrix multiplied with a vector}
append(updatedVertices, v’)
end for
draw(updatedVertices)

Recall
- Going back to Chapter 6, we know the following:
 a a x a x +a y 
11 12 11 12
=
a a y a x +a y
21 22 21 22
- A linear transformation is when we take a 2D vector, apply
some matrix multiplication, and get a 2D vector in return.

Section 7.1.1: Scaling
- Scaling is the most basic transformation.
- Used to change the shape along coordinate axes.
 
s 0
scale(s ,s ) = x
x y
0 s
y
 
x
- Example: Calculate the resultant matrix with the vertex .
y
  
s x 0 x s x x +0y s x x
= =
0 s y 0x +s y s y
y y y
- If s == s , the object’s shape is maintained.
x y
- If s ̸= s , the object is deformed.
x y
Look at Examples/2D/Transformations/Scale example

Illustrations

Section 7.1.2: Shearing
- Shearing causes the ”illusion” of pushing the object sideways
like a deck of cards.
- The top card is further to the side while the bottom card is at
the same position.
  
1 s 1 0
shear (s) = , shear (s) =
x 0 1 y s 1
 
x
- Example: Calculate the resulting matrix with the vertex
y
using shear .
x
  
1 s x x +sy x +sy
= =
0 1 y 0x +y y
Look at Examples/2D/Transformations/Shear example

Alternative form of shearing
- An alternative way to express shearing:
- Is to just rotate the object by a single axis, instead of both like
in standard rotations.
 1 tan(ϕ) 1 0 
shear (s) = , shear (ϕ) =
ϕ 0 1 y tan(ϕ) 1
- shear (ϕ) tilts the object by an angle ϕ clockwise from the
x
vertical axis.
- shear (ϕ) tilts the object by an angle ϕ counterclockwise from
y
the horizontal axis.

Section 7.1.4: Reflection
- Reflection about a coordinate axis by using the scaling matrix
with a negative one scale factor (s or s ).
x y
  
−1 0 1 0
reflect = , reflect =
y 0 1 x 0 −1
 
x
- Example: Calculate the resulting matrix with the vertex
y
using reflect .
y
  
−1 0 x −x +0y −x
= =
0 1 y 0x +y y
Look at example
Examples/2D/Transformations/Reflection

Section 7.1.3: Rotations
- Suppose we want to rotate a by angle ϕ to form b.
- Suppose further that the angle between a and the x-axis is α,

and a has a length r = x2+y2.
a a
Thus, we know
- x =rcos(α)
a
- y =rsin(α)
a
- As b is only a rotation of a,
r remains the same.
- The angle between b and
the x-axis: α+ϕ.

x cos(ϕ)−y sin(ϕ) cos(ϕ) −sin(ϕ) x 
a a a
=
y cos(ϕ)+x sin(ϕ) sin(ϕ) cos(ϕ) y
a a a
  
x cos(ϕ) −sin(ϕ) x
b a
=
y sin(ϕ) cos(ϕ) y
b a
Look at Examples/2D/Transformations/Rotation example
- Using the facts on the previous slide:
- x =rcos(α+ϕ)=rcos(α)cos(ϕ)−rsin(α)sin(ϕ)
b
- y =rsin(α+ϕ)=rsin(α)cos(ϕ)+rcos(α)sin(ϕ)
b
- We can substitute x = rcos(α) and y = rsin(α) which
a a
results:
- x b =x a cos(ϕ)−y a sin(ϕ)
- y =y cos(ϕ)+x sin(ϕ)
b a a
- What does this look like?

- Using the facts on the previous slide:
- x =rcos(α+ϕ)=rcos(α)cos(ϕ)−rsin(α)sin(ϕ)
b
- y =rsin(α+ϕ)=rsin(α)cos(ϕ)+rcos(α)sin(ϕ)
b
- We can substitute x = rcos(α) and y = rsin(α) which
a a
results:
- x b =x a cos(ϕ)−y a sin(ϕ)
- y =y cos(ϕ)+x sin(ϕ)
b a a
- What does this look like?
 x cos(ϕ)−y sin(ϕ) cos(ϕ) −sin(ϕ) x 
a a a
=
y cos(ϕ)+x sin(ϕ) sin(ϕ) cos(ϕ) y
a a a
  
x cos(ϕ) −sin(ϕ) x
b a
=
y sin(ϕ) cos(ϕ) y
b a
Look at Examples/2D/Transformations/Rotation example

Section 7.3: Translation and Affine Transformations
- Say we would like to rotate an object around itself, which is
not at the origin.
- Can the defined rotational matrices work?
- Look at
Examples/2D/Transformations/OffCenterRotation
example.
- How can the defined rotation matrix be used to rotate the
object about itself, when the object is not at the center?
1. Move the object such that the point of rotation is at the origin.
2. Apply the rotation.
3. Move the object back.

Naive approach
- To apply translation using direction d, we can use:
x′
= x +d x
y′
= y +d y
- But this clashes with our current approach of using matrices
to perform transformations.
- How can this be implemented using a matrix?

- To use matrices for transformations, we add an additional
dimension to the transformation matrix.
- Thus, for 2D coordinate spaces, we use a 3×3 matrix.
 
m m x
11 12 t
m 21 m 22 y t
0 0 1
- These are known as homogeneous coordinates (adding an
extra dimension to the matrix).
- We can express the translation as:
 x′ 
m m x

x
 
m x +m y +x

11 12 t 11 12 t
y′  = m 21 m 22 y ty = m 21 x +m 22 y +y t
1 0 0 1 1 1
- This allows a single matrix to apply a linear transformation
followed by a translation!

Translation matrix
- Using the homogeneous coordinates, we can create the
 
x t
following translation matrix in direction :
y
t
 
1 0 x
t
translation(x ,y ) = 0 1 y t
t t
0 0 1
- This can then achieve the following movement:
 x′   
1 0 x x
t
y′  = 0 1 y ty
1 0 0 1 1
- Is the number represented by the 1 significant?

Rule of thumb
   
x x
y y
1 0
is a location or point. is a direction.
- Exercise: Verify that when translating a direction, the
direction remains the same.
- Examples/2D/Transformations/Translation example.
- Remainder of Chapter 7 will be discussed during our next
lecture.

Summary
 
s x 0 0
- Homogeneous scaling matrix: 0 s 0
y
0 0 1
 
1 h 0
xy
- Homogeneous shearing matrix: h 1 0
yx
0 0 1
 
−1 0 0
- Homogeneous y-reflection matrix:  0 1 0
0 0 1
 
cos(ϕ) −sin(ϕ) 0
- Homogeneous rotational matrix: sin(ϕ) cos(ϕ) 0
0 0 1
 1 0 x 
t
- Homogeneous translation matrix: 0 1 y t
0 0 1

- One updates the object and swaps between transformation
matrices.
- In the other, the transformation matrix is updated, and the
object remains the same.
- You can use either of them depending on your preferred way
of thinking.
- This difference will come into effect later in the semester.
Differences between Algorithms
- What is the main difference between the two algorithms
discussed earlier?

Differences between Algorithms
- What is the main difference between the two algorithms
discussed earlier?
- One updates the object and swaps between transformation
matrices.
- In the other, the transformation matrix is updated, and the
object remains the same.
- You can use either of them depending on your preferred way
of thinking.
- This difference will come into effect later in the semester.
