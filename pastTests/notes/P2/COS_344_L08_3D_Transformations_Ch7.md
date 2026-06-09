3Dshapes
COS 344: L8 Chapter 7: 3D Shapes and
Transformations
Cobus Redelinghuys
06/03/2024

3Dshapes
- Today, we will look at modelling and animations for 3D
objects.
- After today’s lecture, you should be able to start planning
your model for Practical 3 and 4.
- Today’s lecture contains a set of examples, which will be
posted on ClickUp at a later stage.
- Not all of this week’s content is in the textbook!

- Assume that we have the following matrices:
- T 1 which moves the object to the origin.
- R which is the rotation matrix.
- T which moves the object back to its original position.
2
- Assume the object we want to rotate has n vertices.
3Dshapes
Section 7.1.5: Composition and Decomposition of
Transformations
- Back in L7, we discussed how to rotate an object about itself
when it is not at the origin.
- What were the steps?

3Dshapes
Section 7.1.5: Composition and Decomposition of
Transformations
- Back in L7, we discussed how to rotate an object about itself
when it is not at the origin.
- What were the steps?
- Assume that we have the following matrices:
- T 1 which moves the object to the origin.
- R which is the rotation matrix.
- T which moves the object back to its original position.
2
- Assume the object we want to rotate has n vertices.

- We multiply four matrices (assuming the point is a D×1
matrix) together n times.
- Is there a way we can improve this?
- Note, the three transformation matrices (T 1 ,R,T 2 ) do not
change from point to point.
- Why not calculate all the transformations once, and then
apply them to all of the n vertices?
- This gives us how many calculations?
- Multiplying three matrices once.
- Then multiplying two matrices n times.
- Example:
- Consider that the object has a 100 vertices:
- Inefficient: Multiply four matrices 100 times.
- Efficient: Multiply three matrices once and two matrices 100
times.
3Dshapes
- Assume that each matrix is multiplied sequentially to each of
the n vertices. How many multiplications do we perform?

- Note, the three transformation matrices (T 1 ,R,T 2 ) do not
change from point to point.
- Why not calculate all the transformations once, and then
apply them to all of the n vertices?
- This gives us how many calculations?
- Multiplying three matrices once.
- Then multiplying two matrices n times.
- Example:
- Consider that the object has a 100 vertices:
- Inefficient: Multiply four matrices 100 times.
- Efficient: Multiply three matrices once and two matrices 100
times.
3Dshapes
- Assume that each matrix is multiplied sequentially to each of
the n vertices. How many multiplications do we perform?
- We multiply four matrices (assuming the point is a D×1
matrix) together n times.
- Is there a way we can improve this?

- Multiplying three matrices once.
- Then multiplying two matrices n times.
- Example:
- Consider that the object has a 100 vertices:
- Inefficient: Multiply four matrices 100 times.
- Efficient: Multiply three matrices once and two matrices 100
times.
3Dshapes
- Assume that each matrix is multiplied sequentially to each of
the n vertices. How many multiplications do we perform?
- We multiply four matrices (assuming the point is a D×1
matrix) together n times.
- Is there a way we can improve this?
- Note, the three transformation matrices (T 1 ,R,T 2 ) do not
change from point to point.
- Why not calculate all the transformations once, and then
apply them to all of the n vertices?
- This gives us how many calculations?

3Dshapes
- Assume that each matrix is multiplied sequentially to each of
the n vertices. How many multiplications do we perform?
- We multiply four matrices (assuming the point is a D×1
matrix) together n times.
- Is there a way we can improve this?
- Note, the three transformation matrices (T 1 ,R,T 2 ) do not
change from point to point.
- Why not calculate all the transformations once, and then
apply them to all of the n vertices?
- This gives us how many calculations?
- Multiplying three matrices once.
- Then multiplying two matrices n times.
- Example:
- Consider that the object has a 100 vertices:
- Inefficient: Multiply four matrices 100 times.
- Efficient: Multiply three matrices once and two matrices 100
times.

- Yes, you multiply the matrices in the order of transformations
applied, starting from the right.
- Firstly T is applied, then R, and lastly T
1 2
- Note: T RT ̸= T T R for arbitrary matrices.
2 1 1 2
- Section 7.1.6 is skipped.
3Dshapes
- Using the efficient method, we obtain:
M = T RT
2 1
- Is the order of matrix multiplication important?

3Dshapes
- Using the efficient method, we obtain:
M = T RT
2 1
- Is the order of matrix multiplication important?
- Yes, you multiply the matrices in the order of transformations
applied, starting from the right.
- Firstly T is applied, then R, and lastly T
1 2
- Note: T RT ̸= T T R for arbitrary matrices.
2 1 1 2
- Section 7.1.6 is skipped.

3Dshapes
Matrices: Scale
- The scale matrix is expanded from 2D to 3D by adding a third
dimension and an extra parameter.
scale(s ,s ) → scale(s ,s ,s )
x y x y z
which implies:
 s 0 0 
  x
s 0
x → 0 s 0
y
0 s y
0 0 s
z

3Dshapes
- In 2D, the rotation was around the z-axis.
- In 3D, we can rotate around three distinct axes.
- Z-axis:
cos(ϕ) −sin(ϕ) 0
rotate z (ϕ) = sin(ϕ) cos(ϕ) 0
0 0 1
- X-axis:
1 
0 0
rotate (ϕ) = 0 cos(ϕ) −sin(ϕ)
x
0 sin(ϕ) cos(ϕ)
- Y-axis:
cos(ϕ) sin(ϕ)
0
rotate (ϕ) = 0 1 0
y
−sin(ϕ) 0 cos(ϕ)

3Dshapes
Matrices: Shear
- In 3D, you can shear along the coordinate axes, just as with
2D.
- Z-axis:
1 0 0
shear z (d x ,d y ) = 0 1 0
d d 1
x y
- X-axis:
1 
d d
y z
shear (d ,d ) = 0 1 0
x y z
0 0 1
- Y-axis:
1 0
0
shear (d ,d ) = d 1 d
y x z x z
0 0 1

3Dshapes
- The normals of surfaces do not transform correctly when the
standard transformation matrix M is applied.
- An alternative representation is required to transform the
normal, such that it stays orthogonal to the surface.
- The textbook covers the derivation in Section 7.2.2.
- Use the formula:
n = (M−1)Tn
N
where:
- n is the new normal.
N
- M is the transformation matrix.
- n is the old normal.
- As the length of the new normal can change, just remember
to normalize the new normal for lighting/shading calculations.

3Dshapes
Section 7.3: Translation and Affine Transformations
- Just as with 2D translations, we can create homogeneous
coordinates for 3D translations.
 1 0 0 d 
x
 0 1 0 d y
T(d) =
 
0 0 1 d z
0 0 0 1

3Dshapes
Section 7.4: Inverses of Transformation matrices
- Often times, it is needed to undo transformations.
- For example, T , from our rotation example.
2
- Two methods exist:
- Option 1: Taking the inverse of the transformation matrix M.
MM−1 =I
- Thus, if we have a vertex v and we transform and undo the
transformation, we obtain:
v′ =M−1Mv
v′
=Iv
v′
=v

3Dshapes
Section 7.4: Inverses of Transformation matrices
- Often times, it is needed to undo transformations.
- For example, T , from our rotation example.
2
- Two methods exist:
- Option 2: Creating a transformation matrix that will undo the
operation.
- Example:
- If T(d) was applied then to undo it we can apply T(−d)
- IfR (45◦)wasappliedthentoundoitwecanapplyR (−45◦)
x x

3Dshapes
 1 
- Consider we have a sphere centred at 0.5 . We want to
−0.25
rotate this sphere by 25◦ around its x-axis.
- We construct the transformation matrix as follows:
- First we need to translate the sphere such that the centre of
the sphere is at the origin:
 
   1 0 0 −1
1
0 1 0 −0.5
T− 0.5 =
0 0 1 0.25 
−0.25
0 0 0 1
- Next the rotation matrix:
 
1 0 0 0
0 c o s ( 2 5 ◦ ) − s in ( 2 5 ◦ ) 0
(25◦)=  
R x  
 0 s in ( 2 5 ◦ ) co s ( 2 5 ◦ ) 0 
0 0 0 1

3Dshapes
- Lastly, we need the matrix that will move the sphere back to
the origin.
- ▶
Option A: Option B:
  −1    
1 1
T−− 0.5 =
T− 0.5  = 
−0.25 −0.25
 1 0 0 1   1 0 0 1 
0 1 0 0.5 0 1 0 0.5 

   
0 0 1 −0.25 0 0 1 −0.25
0 0 0 1
0 0 0 1

3Dshapes
- Pulling it all together:
 −1   
1 1
(25◦)×T−
M = T 0.5  ×R x 0.5 
−0.25 −0.25
 1 0 0 1  1 0 0 0  1 0 0 −1 
0 1 0 0.5 0 cos(25◦) −sin(25◦) 0 0 1 0 −0.5
M =    
0 0 1 −0.250 sin(25◦) cos(25◦) 00 0 1 0.25
0 0 0 1 0 0 0 1 0 0 0 1
- Then multiply M with every vertex of the sphere.

3Dshapes
- This part is not explicitly clear in the textbook.
Figure: Rotation about an arbitrary axis

3Dshapes
- We require:
- The center of the object, P .
0
- The vector along which to rotate, V.
- The angle of rotation, θ.
- V can be obtained by:
V = P 1 −P 0
.
- Always choose V such that θ is positive.
- We need to normalize V:
 
α
V x
u = = α y
V
α
z

3Dshapes
- We need two translation matrices:
- T(−P 0 )
- T(P )
0
- What is the purpose of each?
- Strategy:
- Perform two rotations to align u with the z-axis.
- Rotate by θ.
- Undo the alignment rotations.
- Final result:
R = R (−θ )R (−θ )R (θ)R (θ )R (θ )
x x y y z y y x x
- All we need now is θ and θ .
x y

3Dshapes
- Since u is a unit-length vector, we can exploit the following:
α2 +α2 +α2 = 1
x y z
- Now draw u and draw perpendicular lines from the point
(α ,α ,α ) to each axis.
x y z
- In Figure 16 (Slide 16), these are represented by c , c and c .
x y z
- The directional angles between u and each axes is expressed
as: ϕ , ϕ and ϕ .
x y z
- The directional cosines are:
- cos(ϕ )=α
x x
- cos(ϕ y )=α y
- cos(ϕ )=α
z z

3Dshapes
- As cos(ϕ )2+cos(ϕ )2+cos(ϕ )2 = 1, we can calculate θ
x y z x
and θ using the line segment.
y
- First, we need to rotate line segment into plane y=0.
- Before rotation, if the line segment is projected onto the x =0
plane, the line segment has a length of d.
- We can calculate d as follows:

d = α2 +α2
y z
- As such, we don’t need to calculate θ or θ , we can rather use
x y
simple trigonometry.

3Dshapes
This yields the following matrix:
 
1 0 0 0
αz −αy
0 0
R (θ ) =  d d 
x x α y α
0 z 0 
d d
0 0 0 1

3Dshapes
Rotate the line into the plane x=0.
This yields the following matrix:
 
d 0 −α 0
x
 0 1 0 0
R (θ ) =
y y  
α x 0 d 0 
0 0 0 1
This produces the final complete matrix concatenation as:
R = T(P )R (−θ )R (−θ )R (θ)R (θ )R (θ )T(−P )
0 x x y y z y y x x 0

- Using a set of 2D shapes.
- How would we draw the following shapes:
- Pyramid
- Cube
- Rectangle
3Dshapes
3D shapes
- How can we draw 3D shapes?

3Dshapes
3D shapes
- How can we draw 3D shapes?
- Using a set of 2D shapes.
- How would we draw the following shapes:
- Pyramid
- Cube
- Rectangle
