COS 344: L14 Chapter 9: Rasterization: Viewing
Cobus Redelinghuys
06/04/2025

- Today we will finish up the parts of Chapter 9 that was
skipped previously.
- We needed to skip these sections as we had not discussed
viewing yet.

- During the rasterization process, if we simply transform
primitives into screen space and rasterize them, what could be
the problem?
- Primitives that are behind the camera will also be rasterized,
leading to incorrect rendering.
- For this reason, the clipping operation needs to be applied
before the rasterization process.
- Clipping is a common process in computer graphics, and is
used whenever one geometric entity cuts another.
- What is a geometric entity?
- Is it just objects?
Section 9.1.4: Clipping
- In our discussion on Viewing, we made the assumption that
everything we want to render is “seen” by the camera.
- In real life, this is not always possible.
- Examples?

- Primitives that are behind the camera will also be rasterized,
leading to incorrect rendering.
- For this reason, the clipping operation needs to be applied
before the rasterization process.
- Clipping is a common process in computer graphics, and is
used whenever one geometric entity cuts another.
- What is a geometric entity?
- Is it just objects?
Section 9.1.4: Clipping
- In our discussion on Viewing, we made the assumption that
everything we want to render is “seen” by the camera.
- In real life, this is not always possible.
- Examples?
- During the rasterization process, if we simply transform
primitives into screen space and rasterize them, what could be
the problem?

- Is it just objects?
Section 9.1.4: Clipping
- In our discussion on Viewing, we made the assumption that
everything we want to render is “seen” by the camera.
- In real life, this is not always possible.
- Examples?
- During the rasterization process, if we simply transform
primitives into screen space and rasterize them, what could be
the problem?
- Primitives that are behind the camera will also be rasterized,
leading to incorrect rendering.
- For this reason, the clipping operation needs to be applied
before the rasterization process.
- Clipping is a common process in computer graphics, and is
used whenever one geometric entity cuts another.
- What is a geometric entity?

Section 9.1.4: Clipping
- In our discussion on Viewing, we made the assumption that
everything we want to render is “seen” by the camera.
- In real life, this is not always possible.
- Examples?
- During the rasterization process, if we simply transform
primitives into screen space and rasterize them, what could be
the problem?
- Primitives that are behind the camera will also be rasterized,
leading to incorrect rendering.
- For this reason, the clipping operation needs to be applied
before the rasterization process.
- Clipping is a common process in computer graphics, and is
used whenever one geometric entity cuts another.
- What is a geometric entity?
- Is it just objects?

- The view volume.
- Why is it safe to always discard
geometric objects that is outside of
the view volume?
- For example, take a triangle that is
cut into two portions by a plane.
- In most graphic applications, the
part of the triangle that is on the
wrong side of the plane is
discarded.
- In computer graphics, what is an
example of a set of planes, that
when a geometric object is on the
wrong side of the plane, is
discarded?

- For example, take a triangle that is
cut into two portions by a plane.
- In most graphic applications, the
part of the triangle that is on the
wrong side of the plane is
discarded.
- In computer graphics, what is an
example of a set of planes, that
when a geometric object is on the
wrong side of the plane, is
discarded?
- The view volume.
- Why is it safe to always discard
geometric objects that is outside of
the view volume?

- Two common approaches exist:
- Using the world coordinates and the size bounding planes of
the truncated viewing pyramid.
- In the 4D transformed space, before the homogeneous divide.
- You are only expected to know, on a high level, how these
methods work.

- Only visits each object once.
- As with most things, this is also a weakness. How?
- Why do objects need to be visited if they are not seen?
Culling
Identifying and ignoring invisible geometry, for the sake of
efficiency.
Section 9.4: Culling Primitives for Efficiency
- Who can remember what object order rendering’s strength is?

- Why do objects need to be visited if they are not seen?
Culling
Identifying and ignoring invisible geometry, for the sake of
efficiency.
Section 9.4: Culling Primitives for Efficiency
- Who can remember what object order rendering’s strength is?
- Only visits each object once.
- As with most things, this is also a weakness. How?

Section 9.4: Culling Primitives for Efficiency
- Who can remember what object order rendering’s strength is?
- Only visits each object once.
- As with most things, this is also a weakness. How?
- Why do objects need to be visited if they are not seen?
Culling
Identifying and ignoring invisible geometry, for the sake of
efficiency.

- Three commonly implemented culling strategies are:
View volume culling (View frustum culling)
The removal of geometry that is outside the view volume
Occlusion culling
The removal of geometry that may be within the view volume, but
is obscured, or occluded, by other geometry closer to the camera.
Backface culling
The removal of primitives facing away from the camera.
We will only briefly consider view volume culling and backface
culling.

- When they lie outside of the view volume.
- Why?
- The trade-off:
- Being able to decide if a primitive can be culled or not, using a
quick test, will speed up the render.
- But visiting each primitive to test if they need to be rendered,
can be more computationally expensive than just leaving it to
the rasterizer to remove.
- View volume culling can be useful if we can find a bounding
volume for an object.
- If the bounding volume is outside the view volume, we can
ignore all the primitives used in the object.
Section 9.4.1: View Volume Culling
- When can a primitive be safely culled?

Section 9.4.1: View Volume Culling
- When can a primitive be safely culled?
- When they lie outside of the view volume.
- Why?
- The trade-off:
- Being able to decide if a primitive can be culled or not, using a
quick test, will speed up the render.
- But visiting each primitive to test if they need to be rendered,
can be more computationally expensive than just leaving it to
the rasterizer to remove.
- View volume culling can be useful if we can find a bounding
volume for an object.
- If the bounding volume is outside the view volume, we can
ignore all the primitives used in the object.

Section 9.4.2: Backface Culling
Closed polygon
Polygons that bound a closed space with no holes
- Polygons that are closed polygons, have a normal that faces
outward from the surface of the polygon.
- If the normal faces away from the camera, it is often safe to
assume that another polygon is in front of this polygon.
- This other polygon will probably have a normal that faces the
camera.
- The polygon with the “backwards” normal can be culled.
- In basic wording: Culling the back of polygons

Culling+Techniques+Fall+2006+revised.jpg

- We would like to create some matrix U that take in a point in
world space, apply some transformation to it, then change it
such that it is projected using the correct projection.
- In other words:
v = Uv
clip world
- We thus need three matrices:
- Model (M)
- This is the transformation matrix that will change the
geometric object.
- View (M or V)
cam
- This is the view matrix that alters the camera position and
looking direction.
- Projection (M or M )
per orth
- This is the matrix that will project the geometric objects
according to the correct projection type.
- U can thus be formed as:
U = PVM
U = M M M
orth cam

- This part of the work is not in the textbook.
- In order to perform back face culling in OpenGL, the following
is used:
1. Winding order
2. Enabling culling
3. Specifying what needs to be culled.

- This order is also known as the winding order.
- Two possibilities exist:
- Clockwise
- Counter-clockwise
- OpenGL uses this information to determine what the back
face is and what the front face is.
- By default, OpenGL uses counter-clockwise, why?
Winding Order
- When drawing triangles, why was the order of the vertices
important?

Winding Order
- When drawing triangles, why was the order of the vertices
important?
- This order is also known as the winding order.
- Two possibilities exist:
- Clockwise
- Counter-clockwise
- OpenGL uses this information to determine what the back
face is and what the front face is.
- By default, OpenGL uses counter-clockwise, why?

float vertices[] = {
vertices[0], // vertex 1
vertices[1], // vertex 2
vertices[2], // vertex 3
vertices[0], // vertex 1
vertices[2], // vertex 3
vertices[1] // vertex 2
};
windingorder.png

frontback.png

Code
In order to enable culling, the following functions are needed:
1. glEnable(GL CULL FACE);
2. glCullFace(GL FRONT);
3. glFrontFace(GL CCW);
What do you think the purpose is of glEnable(GL CULL FACE)?

glCullFace
void glCullFace(GLenum mode)
- Specifies whether front- or back-facing facets are culled
- mode
- Specifies which mode of culling is used:
- Types are:
- GL FRONT
- GL BACK
- GL FRONT AND BACK
- Default is GL BACK

BC-01-1024x536.jpg

glFrontFace
void glFrontFace(GLenum mode);
- Specifies the winding order of the front face of the polygon.
- mode
- Specifies the winding order that will be used:
- Options are:
- GL CW (Clockwise)
- GL CCW (Counter clockwise)
- GL CCW is the default value.
