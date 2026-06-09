COS 344: L9 Chapter 9: The Graphics Pipeline
Cobus Redelinghuys
09/03/2026

Chapter 9: Introduction
- Ray tracing is part of image-order rendering.
- This chapter will look at object-order rendering.
- Ray tracing is easier, as no “complicated” mathematics is
required to render a simple scene.
- But is inefficient, as each pixel is considered in turn and
objects are repeatedly visited.
- Instead, the object-order rendering considers each geometric
object in turn and finds the pixels that the object could affect.
Rasterization
The process of finding all the pixels in an image that are occupied
by a geometric primitive.
- Object-order rendering is more efficient, due to only visiting
each geometric object once.

The graphics pipeline outline will be used for the remainder of
Chapter 9.
- Geometric objects are fed into the pipeline from
an application, or scene description file, as a set
of vertices.
- In the vertex processing stage, the vertices are
operated on.
- After this, the vertices that represent the
geometric primitives are sent off to be rasterized.
- The rasterizer breaks the primitive into
fragments that correspond to the pixels covered
by the primitive.
- The fragment processing stage processes the
fragment before they are combined together in
the fragment blending stage.

Section 9.1: Rasterization
- Terminology:
- Rasterization - operation.
- Rasterizer - performs the operation.
- Rasterizer performs two jobs for each primitive it receives:
1. Iterates over the pixels that are covered by the primitive and
marks them as covered by the primitive.
2. Interpolates values (attributes) across the primitive.
- The outcome of rasterization is a set of fragments, one for
each pixel covered by the primitive.

Section 9.1.1: Line Drawing
  
- x 0 x 1
Given two points: and .
y y
0 1
- The rasterizer should draw some “reasonable” pixels such that
an approximate line is displayed.
- Why approximate?
- Two types of line equations can be used:
- Implicit will be used for the remainder of the section.
- Parametric
- Implicit line equation:
f(x,y) ≡ (y −y )x +(x −x )y +x y −x y = 0
0 1 1 0 0 1 1 0
- Assume that x < x . If this is not the case, swap the points.
0 1
- The algorithm that we will use is the midpoint algorithm.

Midpoint algorithm
y
- The midpoint algorithm m = 2
considers four distinct
cases using the gradient m
of the line:
m = 0.5
Case 1: m∈(0,1] x
m = −0.5
Case 2: m∈(−∞,−1]
Case 3: m∈(−1,0]
Case 4: m∈(1,∞) m = 2
- What is special about each case?

- We will only look at m ∈ (0,1], as the others can be formed
similarly.
Algorithm 1 Midpoint algorithm for m ∈ (0,1]
y =y
0
for x =x to x do
0 1
draw(x,y)
if some condition then
y =y +1
end if
end for

- The some condition determines the
“realisticness” of the line.
- The textbook suggests using the condition:
f(x +1,y +0.5) < 0
- This is the midpoint between the two possible
pixels to the right of the current pixel.
  
x+1 x+1
- or
y y +1
- Note x and y are integers.
- Why?
- Test type question:
- Given some a line, and a condition, color the
pixels that will be covered by the line as Fig 9.2.
- The remainder of the section discusses an
efficiency improvement for the discussed line
algorithm.

Section 2.9: Barycentric
Given a triangle with points a, b, and c.
- Let a be the origin.
- Let the vector going from a to b (i.e. b−a) be the first axis and
the vector going from a to c (i.e. c−a) be the second axis.
- i.e. we have a non-orthogonal set of basis vectors.
- This yields:
p(α,β,γ)=αa+βb+γc
With the constraint that α+β+γ =1
where α≡1−β−γ
- Warning: Standard linear algebra does not work as expected with
barycentric basis vectors
- See Section 2.9 of the textbook.

Properties
- A given point p can only be inside the triangle formed by a,
b, and c i.f.f:
- 0<α<1
- 0<β <1
- 0<γ <1
- α+β+γ =1
- If one component is 0, it is on the edge of the triangle.
- If two components are 0, it is at a corner.

Section 9.1.2: Triangle Rasterization
- Triangles are defined by three points, and we would like to
connect these points.
- We encountered similar problems with lines but these have a
few twists.
- Coloring:
- Say we would like to have one corner of the triangle blue, the
next red and the last green.
- How to interpolate the colors?
c=αc +βc +γc
0 1 2
- Where:
- c 0 to c 2 are colors.
- α,β,γ are barycentric coordinates.
- Known as Gourand interpolation.

- Another possible problem is that two adjacent triangles that
share an edge, should not have a gap between them.
- This can be avoided by the following constraint:
- Only draw a pixel i.f.f. the center of the pixel is inside the
triangle.
- i.e. the barycentric coordinates are between 0 and 1.
- What if the centre of the pixel is perfectly on the edge?
- Discussed later.
- Thus, the problem boils down to finding barycentric
coordinates for the centre of pixels.

- The brute force algorithm is described by:
Algorithm 2 Bruteforce triangle rasterization algorithm
for all x do
for all y do
compute(α,β,γ) for x,y
if α∈[0,1] and β ∈[0,1] and γ ∈[0,1] then
c=αc +βc +γc
0 1 2
drawPixel(x,y,c)
end if
end for
end for
- The textbook gives more optimised algorithm.

- Draw the pixel twice?
- Don’t draw the pixel?
- Only draw the pixel once?
- How?
- Textbook suggests that one way is with an offscreen point.
- Choose a point such that it will always be only on one side of
the edge.
- Whichever side the point is on gets to draw the pixel.
- Still has one weakness, what is it?
- Add a test for the case where the edge goes through the
off-screen point.
- Textbook gives a more complex extension of the algorithm to
account for the above discussion.
- Section 9.1.3 and Section 9.1.4 are skipped for now.
- What about if the center of the pixel is on the edge between
two triangles?
- Options?

- Textbook suggests that one way is with an offscreen point.
- Choose a point such that it will always be only on one side of
the edge.
- Whichever side the point is on gets to draw the pixel.
- Still has one weakness, what is it?
- Add a test for the case where the edge goes through the
off-screen point.
- Textbook gives a more complex extension of the algorithm to
account for the above discussion.
- Section 9.1.3 and Section 9.1.4 are skipped for now.
- What about if the center of the pixel is on the edge between
two triangles?
- Options?
- Draw the pixel twice?
- Don’t draw the pixel?
- Only draw the pixel once?
- How?

- Add a test for the case where the edge goes through the
off-screen point.
- Textbook gives a more complex extension of the algorithm to
account for the above discussion.
- Section 9.1.3 and Section 9.1.4 are skipped for now.
- What about if the center of the pixel is on the edge between
two triangles?
- Options?
- Draw the pixel twice?
- Don’t draw the pixel?
- Only draw the pixel once?
- How?
- Textbook suggests that one way is with an offscreen point.
- Choose a point such that it will always be only on one side of
the edge.
- Whichever side the point is on gets to draw the pixel.
- Still has one weakness, what is it?

- What about if the center of the pixel is on the edge between
two triangles?
- Options?
- Draw the pixel twice?
- Don’t draw the pixel?
- Only draw the pixel once?
- How?
- Textbook suggests that one way is with an offscreen point.
- Choose a point such that it will always be only on one side of
the edge.
- Whichever side the point is on gets to draw the pixel.
- Still has one weakness, what is it?
- Add a test for the case where the edge goes through the
off-screen point.
- Textbook gives a more complex extension of the algorithm to
account for the above discussion.
- Section 9.1.3 and Section 9.1.4 are skipped for now.

Section 9.2.1: Simple 2D Drawing
- In the simplest possible pipeline:
- Nothing happens in the vertex or fragment stages.
- In blending, the previous pixel color is just overwritten.
- Application supplies primitives directly in pixel coordinates and
the rasterizer does the rest.
- Solid color is achieved by giving each vertex in the primitive
the same color.

Section 9.2.2: A Minimal 3D Pipeline
- To modify our 2D pipeline to draw a 3D object, the following
change needs to be made:
- The vertex-processing stage does the following multiplication:
- Incoming vertex position
- Product of the modeling, camera, projection and viewpoint
matrices.
- Painters algorithm:
- Algorithm that determines the order that primitives need to be
drawn, such that the objects at the back are behind the other
objects, and the objects in front are in front of other objects.
- Limitation: Intersections between objects and occlusion cycles.

Section 9.2.3: Using a z-Buffer for Hidden Surfaces
- Painter’s algorithm is rarely used due to its inefficiency.
- Alternative: use z-buffer
- At each pixel, keep track of the distance to the closest surface
drawn.
- If another fragment is further away then discard.
- If another fragment is closer update the value.
- The z-buffer algorithm is implemented in the fragment
blending phase.
- What is the initial value for each pixel at the start of the
algorithm?
- The precision issues section are left to the curious student.

Section 9.2.4: Pre-vertex Shading
- Perform shading during the vertex stage.
- The application provides the:
- Normals to the surfaces
- Light position.
- Light color.
- For each vertex, compute:
- Viewer direction.
- Light direction.
- The color is computed and then passed to the rasterizer as a
vertex color.
- Called Gouraud shading.

Section 9.2.5: Pre-fragment Shading
- Perform shading during the fragment stage.
- Geometric information needed for shading, is passed through
the rasterizer as attributes.
- Thus, coordination is needed between the vertex and fragment
stages to prepare data.
- One approach:
- Interpolate the eye-space surface normal and the eye-space
vertex position.
- Then it is used identically to pre-vertex shading
- The remainder of Section 9.2 will be covered later.

Comparison
blogs.dir/4779/files/2021/10/5-1.png

Section 9.3: Simple Anti-aliasing
- The simple rasterization algorithms we discussed are also
called standard or aliased rasterization.
- Basic idea is to allow pixels to be partly covered by primitives
to create a blurry effect.
- Helps the visual quality.
- Box filtering:
- Take the average of all the colors assigned to a pixel.
- Happens when a primitive partly covers the pixel.
- Super-sampling:
- Create a higher resolution image then down-sample.

- Section 9.4: Culling Primitives for Efficiency will be discussed
later.
- The reason for this is that viewing has not been discussed yet.
