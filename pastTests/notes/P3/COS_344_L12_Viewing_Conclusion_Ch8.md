COS 344: L12 Chapter 8: Viewing
Cobus Redelinghuys
26/03/2026

- Today we continue our discussion on Chapter 8: Viewing, and
we will focus on perspective projection.
- What do you think is the problem if t and g are scalar
multiples of each other?

- What do you think is the problem if t and g are scalar
multiples of each other?
 
0
- For example, what if the up vector is 1 and the gazing
0
 0 
vector is 2?
0
- How can we solve this?

Section 8.2: Projective Transformations
- Let us assume the following:
- Viewpoint is at the origin.
- Camera is looking along the z-direction.
- The key property of perspective that we will use is:
- That the size of the object on the screen is proportional to 1
z
for an eye at the origin looking in the negative z-axis.
- We can then use: y = dy
s z

- We would like to just multiply some matrix and achieve this
projection as it aligns with our process we have build up until
now.
- Assume we have a point at (x,y,z) and we represent it as
 x 
 y
follows:   or (x,y,z,1)T
z
1
- The last value, w, is always equal to 1.
- (0,0,0,1)T
We can enforce this by always using as the fourth
row in an affine transformation matrix.
- What if we think of the w as the denominator of the xyz
coordinates?
 
x x
w
-  y y
In other words,   represents the point as  .
z w
z
w w

- Affine transformations allows us to compute:
x′ =ax +by +cz +d
- Using w we can compute the following:
ax +by +cz +d
x′
=
ex +fy +gz +h
- This is known as a linear rotational function.
- We need to add another constraint:
- For each coordinate the denominator is the same.
- To summarize:
- Linear transformations allows us to compute:
x′
=ax +by +cz

- Using w we can compute the following:
ax +by +cz +d
x′
=
ex +fy +gz +h
- This is known as a linear rotational function.
- We need to add another constraint:
- For each coordinate the denominator is the same.
- To summarize:
- Linear transformations allows us to compute:
x′
=ax +by +cz
- Affine transformations allows us to compute:
x′ =ax +by +cz +d

- To summarize:
- Linear transformations allows us to compute:
x′
=ax +by +cz
- Affine transformations allows us to compute:
x′ =ax +by +cz +d
- Using w we can compute the following:
ax +by +cz +d
x′
=
ex +fy +gz +h
- This is known as a linear rotational function.
- We need to add another constraint:
- For each coordinate the denominator is the same.

- We can express this as a matrix transformation:
    
x˜ a b c d x
1 1 1 1
y˜ a b c d y
  2 2 2 2 
 =    
z˜ a b c d 3z
3 3 3
w˜ e f g h 1
- Which leads to:
x˜ y˜ z˜
(x′,y′,z′)
= ( , , )
w˜ w˜ w˜
- This looks as follows:
a x +b y +c z +d
x′ 1 1 1 1
=
ex +fy +gz +h
a 2 x +b 2 y +c 2 z +d 2
y′ =
ex +fy +gz +h
a x +b y +c z +d
z′ 3 3 3 3
=
ex +fy +gz +h

- This looks as follows:
a x +b y +c z +d
x′ 1 1 1 1
=
ex +fy +gz +h
a 2 x +b 2 y +c 2 z +d 2
y′ =
ex +fy +gz +h
a x +b y +c z +d
z′ 3 3 3 3
=
ex +fy +gz +h
- We can express this as a matrix transformation:
    
x˜ a b c d x
1 1 1 1
y˜ a b c d y
  2 2 2 2 
 =    
z˜ a b c d 3z
3 3 3
w˜ e f g h 1
- Which leads to:
x˜ y˜ z˜
(x′,y′,z′)
= ( , , )
w˜ w˜ w˜

- Transformations like this are known as a projective
transformation or a homography.
- Examples 17 and 18 are left as self-study.

Section 8.3: Perspective Projection
- Projective transformations simplify the implementation of the
key property of perspective, i.e. the division by z.
- Using the simple 2D example from Figure 8.8, we can
implement the perspective projection as follows:
 y 
  
y d 0 0
s ∼ z
1 0 1 0
1
 
y
- This transforms the 2D homogeneous vector: z to the 1D
1
 
dy
homogeneous vector .
z
- dy.
This represents the point
z

- For a 3D perspective projection matrix, let us assume the
following:
- Camera is at the origin and facing in the negative z-axis
direction.
 
x
- The distance to the point positioned at y is −d
p
z
- Note the textbook has it as −z referring to the z as with Fig
8.8.
- Just as with orthographic projection, we limit the near and far
planes of what can be seen.
- The image plane is therefore at a distance of −n.
- Why is −d p and −n negative?
- The desired mapping is thus: y = ( n )y and the same can be
s dp
found for x.

- Thus we obtain the perspective matrix (P) as:
 
n 0 0 0
0 n 0 0 
P =
 
0 0 n+f −fn
0 0 1 0
- The first, second, and fourth rows simply implement the
perspective equation.
- Third row, as with orthographical and viewport matrices, is
just to carry over the z value for later use.
- Note the z component of coordinates are distorted in an effort
to manipulate the x and y components.
- We thus choose to keep the z value unchanged for points on
the near and far point.

- There are many different matrices that can work as
perspective matrices, and all of them nonlinearly distort the z
component.
- P has the following properties:
- Leaves points on the z =n plane alone.
- Leaves points on the z =f plane, but, squashes the x and y
components by the appropriate amount.
 
x
- The effect of P on y is thus:
z
 x   nx   nx 
z
y  ny   ny 
P  =   ∼  z 
z (n+f)z −fn n+f − fn 
z
1 z 1

- The inverse of P is:
1 
0 0 0
n
1
 0 0 0 
P−1 =  n 
0 0 0 1

0 0 −1 n+f
fn fn
- A nice benefit of the perspective matrix is that once applied,
the orthographic transforms can be used to create the
canonical view volume.
- If we take the perspective matrix in the context of the
orthographic projection matrix, the perspective matrix simply
maps the perspective view volume to the orthographic view
volume.
- The shape of the perspective view volume is:
- Slice, or frustrum, of a pyramid.
- The shape of the orthographic view volume:
- Axis-aligned box

perspective-matrix/canonical1.png?

- We can thus obtain the perspective projection matrix (M )
per
M = M P
per orth
- The remaining problem is how we define l,r,b,t for perspective.
- Since the perspective matrix does not alter the values of x
and y on the (z = n)-plane, we specify (l,r,b,t) on the
(z = n)-plane.
- How can we integrate this perspective matrix into our
previously defined formula: M M M ?
vp orth cam
- We simply replace M with M .
orth per
- This gives us two options:
M = M M M M = M M PM
vp per cam vp orth cam

- If we multiply the M per out we obtain:
 2n l+r 
0 0
r−l l−r
2n b+t
 0 0 
M =  t− b b − t 
per 0 0 f + n 2fn
 
n−f f−n
0 0 1 0
- Section 8.4 is left to the curious students and deals with the
properties of the perspective transformations

We can now extend Algorithm 2 to use M .
per
Algorithm 1 Drawing 3D lines
Construct M
vp
Construct M
per
Construct M
cam
M := M ×M ×M
vp per cam
for each line segment (a ,b ) do
i i
p := Ma i
q := Mb
i
p q
drawLine( , )
wp wq
end for

- This implies the constraint that:
- l =−r
- b =−t
- Now add the constraint that the pixels are square, i.e. there is
no distortion of the shape in the image.
- We obtain that the ratio of r to t must be the same as the
number of horizontal pixels to the number of vertical pixels:
n r
x =
n t
y
Section 8.5: Field-of-View
- We saw that we can specify any viewing window using
(l,r,b,t) and n values.
- What if we would like to simplify this, where we look through
the center of a window?

Section 8.5: Field-of-View
- We saw that we can specify any viewing window using
(l,r,b,t) and n values.
- What if we would like to simplify this, where we look through
the center of a window?
- This implies the constraint that:
- l =−r
- b =−t
- Now add the constraint that the pixels are square, i.e. there is
no distortion of the shape in the image.
- We obtain that the ratio of r to t must be the same as the
number of horizontal pixels to the number of vertical pixels:
n r
x =
n t
y

- Once n and n have been chosen, this leaves only one degree
x y
of freedom left.
- This is known as the field-of-view angle or the vertical
field-of-view angle.
- Why the need to specify the vertical?

- From Fig 8.14 we can see that:
 
θ t
tan =
2 |n|
- Thus, if we define n and θ we can derive t and use it to code
a general viewing system.
