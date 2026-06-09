COS 344 L3: Chapter 4
Introduction to ray tracing
Cobus Redelinghuys
16/02/2026

Practical Schedule
Start By
Assessment Due Marking 1 Marking 2
Date
Practical 1 16/02/2026 27/02/2026 N/A N/A
Practical 2 28/02/2026 23/03/2026 23/03/2026 07/04/2026
Practical 3 24/03/2026 13/04/2026 13/04/2026 20/04/2026
Practical 4 14/04/2026 11/05/2026 11/05/2026 18/05/2026
HW Initial
07/04/2026 28/04/2026 N/A N/A
Report
HW Peer
11/05/2026 13/05/2026 N/A N/A
Review
HW Final
15/05/2026 22/05/2026 N/A N/A
Report
HW Final
23/03/2026 25/05/2026 TBC TBC
Project

Rendering
Process of taking in a set of objects and producing an array of
pixels as output.
- Two types of rendering approaches:
Object-order rendering
Each object is considered in turn, and for each object, all the
pixels that it influences are found and updated.
Image-order rendering
Each pixel is considered in turn, and for each pixel, all the objects
that influence it are found and the pixel value is computed.

- What if the object is translucent?
- Once the object is found, shading is applied to the surface of
the object.
Section 4.1: Basic Ray-Tracing Algorithm
- A ray tracer works by:
- Determining for each pixel which objects are ”seen” by said
pixel.
- Thus, the object must intersect the viewing ray.
Viewing ray
A line that emanates from the viewpoint, in the direction the pixel
is looking in.
- Does the viewing ray stop at the first object it intersects?

- Once the object is found, shading is applied to the surface of
the object.
Section 4.1: Basic Ray-Tracing Algorithm
- A ray tracer works by:
- Determining for each pixel which objects are ”seen” by said
pixel.
- Thus, the object must intersect the viewing ray.
Viewing ray
A line that emanates from the viewpoint, in the direction the pixel
is looking in.
- Does the viewing ray stop at the first object it intersects?
- What if the object is translucent?

Section 4.1: Basic Ray-Tracing Algorithm
- A ray tracer works by:
- Determining for each pixel which objects are ”seen” by said
pixel.
- Thus, the object must intersect the viewing ray.
Viewing ray
A line that emanates from the viewpoint, in the direction the pixel
is looking in.
- Does the viewing ray stop at the first object it intersects?
- What if the object is translucent?
- Once the object is found, shading is applied to the surface of
the object.

- Basic components of ray tracer:
1. Ray generation
- Computes the origin, and direction of each pixel’s viewing ray,
based on camera geometry.
2. Ray intersection
- Finds the closest object intersecting the viewing ray. (*)
3. Shading
- Computes the pixel color based on the results of the
intersection.
Algorithm 1 Basic Ray Tracing Algorithm
for each pixel do
Compute viewing ray
Find the first object that it intersects with
Compute the normal n of the surface of the object the ray hit
Set pixel color to the value computed using n, light, and hit point
end for

https:
pictures/2018/RayTracing/ray-tracing-image-1.jpg

Linear perspective
3D objects are projected onto an image plane, in such a way that
straight lines in the scene become straight lines in the image.
- Types of projection:
- Parallel projection
- Perspective projection
Section 4.2: Perspective
- Many ”approaches” exist for creating 3D shapes on a 2D
shape.
- Cubist Painting
- Fish eye lenses
- Peripheral cameras
- Linear Perspective
- Most common approach and used in computer graphics.

Section 4.2: Perspective
- Many ”approaches” exist for creating 3D shapes on a 2D
shape.
- Cubist Painting
- Fish eye lenses
- Peripheral cameras
- Linear Perspective
- Most common approach and used in computer graphics.
Linear perspective
3D objects are projected onto an image plane, in such a way that
straight lines in the scene become straight lines in the image.
- Types of projection:
- Parallel projection
- Perspective projection

Cubist Painting

Fisheye lens
Sharing_Photography/10351/images/02.jpg

Orthographic
The image plane is perpendicular to the view direction.
Obligue
The image plane is not perpendicular to the view direction.
Parallel Projection
Parallel projection
3D points are mapped to 2D points by moving them parallel along
a projection direction, until they hit the image plane.
- Produced view is constructed by choosing the:
- Projection direction
- Image plane

Parallel Projection
Parallel projection
3D points are mapped to 2D points by moving them parallel along
a projection direction, until they hit the image plane.
- Produced view is constructed by choosing the:
- Projection direction
- Image plane
Orthographic
The image plane is perpendicular to the view direction.
Obligue
The image plane is not perpendicular to the view direction.

- Mechanical and architectural drawings.
- Why?
- Parallel lines stay parallel.
- Size and shapes are preserved.
- Where can parallel projection be used?

- Parallel lines stay parallel.
- Size and shapes are preserved.
- Where can parallel projection be used?
- Mechanical and architectural drawings.
- Why?

- Where can parallel projection be used?
- Mechanical and architectural drawings.
- Why?
- Parallel lines stay parallel.
- Size and shapes are preserved.

Perspective Projection
Perspective projection
3D points are projected to 2D points along lines that pass through
a single point, known as the viewpoint, rather than along parallel
lines.
- Allows objects to appear smaller the further they are from the
viewpoint when projected.
- Produced view is constructed by choosing the:
- Viewpoint
- Image plane

By SharkD - Own work. Download source code., CC BY-SA 4.0,

Section 4.3: Computing Viewing Rays
- Mathematical definition of a ray:
p(t) = e+t(s−e)
p(t) = (1−t)e+t(s)
where:
- p is a point
- e is the start point (eye point)
- s is the end point (surface intersect)
- t is a real value bounded between 0 and 1
- s−e is the direction of the ray.
- Properties:
- p(0)=e
- p(1)=s
- If 0<t <t then p(t ) is closer to e than p(t ).
1 2 1 2

Camera Frame
- Consider an orthonormal (camera frame) defined by:
- e or the viewpoint.
- u pointing rightward from e.
- v pointing upward from e.
- w pointing backward.
- {u,v,w} form a right-handed coordinate system.
- Common camera frame construction:
- viewpoint (e)
- view direction (-w)
- up (v).
- This is used to construct a basis such that v and w are in the
plane defined by the view direction and the up direction.
- See Section 2.4.7

Section 4.3.1: Orthographic views
- Constructing an image plane:
- l and r are the left and right edges of the plane, as measured
from e along the u direction.
- Usually: l <0<r
- b and t are the bottom and top edges of the image as
measured from e along the v direction.
- Usually: b <0<t
- To translate a pixel at position (i,j) in pixel coordinates
(Chapter 3) to (u,v) in the image plane use:
- (r−l)(i+0.5)
u =l +
nx
- (t−b)(j+0.5)
v =b+
ny
- (u,v) are coordinates on the image plane.
- Note the textbook overloads notation!

- Orthographic view ray:
- Direction: -w.
- Starting position: plane defined by e, u, and v.
- s is on the image plane.
- Construct the orthographic viewing ray using:
Algorithm 2 Generating orthographic viewing rays
compute u and v using formulae on previous slide.
Ray origin := e + uu + vv
Ray direction := -w
- To create oblique parallel view:
- Allow the image plane’s normal to be specified separately from
the view direction.
- Use the same approach as Algorithm 2, but with d instead of
w.

Section 4.3.2: Perspective view
- In perspective view rays, all rays have the same origin
(viewpoint), but different directions.
- Image plane is positioned some distance, d, away from e.
- d is referred to as the plane distance or focal length
- Ray direction is defined by the viewpoint and position on the
image plane.
Algorithm 3 Generating perspective viewing rays
compute u and v using formulae on previous slides.
Ray origin := e
Ray direction := -dw + uu + vv

Section 4.4.1: Ray-Sphere Intersection
- To find where a ray (p(t) = e+td) intersects a sphere
centered around c and has a radius of R:
- Find the value of t for which the ray intersects the sphere.
- Use the formula:
(d·d)t2+2d·(e−c)t+(e−c)·(e−c)−R2 =0
- Only unknown is thus t.
- Solve t using the standard quadratic equation.
- The derivation can be found in the textbook for the curious.

Section 4.4.2: Ray-Triangle Intersection
- To find where a ray (p(t) = e+td) intersects a triangle with
vertices a, b, c solve:
e+td = a+β(b−a)+γ(c −a)
- Solve for: t,β, and γ.
- Set up and solve a linear set of equations:
x +tx =x +β(x −x )+γ(x −x )
e d a b a c a
y +ty =y +β(y −y )+γ(y −y )
e d a b a c a
z +tz =z +β(z −z )+γ(z −z )
e d a b a c a
- Textbook shows how to use Cramer’s rule to solve this system
of linear equations.
- If β > 0, γ > 0 and β +γ < 1 then the intersect is inside of
the triangle.

More efficient algorithm to calculate if the ray hits the triangle:
Algorithm 4 Early termination ray-triangle intersection algorithm
Require: Ray r, Vector a, Vector b, Vector c, t , t
0 1
Ensure: If the ray hits the triangle
Compute t
if (t <t ) or (t >t ) then
0 1
return false
end if
Compute γ
if (γ <0) or (γ >1) then
return false
end if
Compute β
if (β <0) or (β+γ >1) then
return false
end if
return true

Remainder of Chapter 4.
- Sections 4.4.3 and 4.4.4 are left out, but can be useful in
practical 4.
- Section 4.5 will be covered in the next lecture as part of
Chapter 5’s discussion.
