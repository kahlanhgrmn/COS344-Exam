COS 344: L11 Chapter 8: Viewing
Cobus Redelinghuys
23/03/2026

- Moving, deforming, and rotating geometric objects.
- Another use case is to deal with the moving of objects from
the 3D world to 2D views.
- This 3D to 2D mapping is called viewing transformations.
- Used extensively in object order rendering.
- In chapter 4, we discussed the different types of projections
and how to generate the viewing rays.
- In this chapter, we will do the reverse:
- Using transformation matrices to form parallel or perspective
views.
- Ensure that you revise chapter 4 when studying for this
chapter!
- Up till now, what have we used transformation matrices for?

- Up till now, what have we used transformation matrices for?
- Moving, deforming, and rotating geometric objects.
- Another use case is to deal with the moving of objects from
the 3D world to 2D views.
- This 3D to 2D mapping is called viewing transformations.
- Used extensively in object order rendering.
- In chapter 4, we discussed the different types of projections
and how to generate the viewing rays.
- In this chapter, we will do the reverse:
- Using transformation matrices to form parallel or perspective
views.
- Ensure that you revise chapter 4 when studying for this
chapter!

- The transformations in this chapter will take 3D points (in
world space) and project them onto 2D points (on the image
plane).
- For the remaining discussion of this chapter assumes that we
are working with a wireframe.
- i.e. a 3D line segment denoted by the 3D coordinates of the
two end points.

Section 8.1: Viewing Transformations
The viewing transformations responsibility
Mapping 3D locations (represented as 3D coordinates in canonical
coordinate systems) to coordinates in the image (expressed in units
of pixels).
- The following things affect the above mentioned mapping:
- Camera position
- Field of view
- Camera orientation
- Image resolution
- Projection type
- To overcome this list of considerations, we will break the
transformation into a series of simpler transformations.

Most graphics system do this by using a sequence of three
transformations:
Camera transformation (eye transformation)
Definition: Rigid body transformation that places the camera at
the origin in a convenient orientation.
Dependency: Position and orientation of the camera.
Input: Points in canonical coordinates (world space).
Output: Points in camera coordinates (points in camera space).
Rigid body transformations
Transformations that preserve the shape and size of an object.

Most graphics system do this by using a sequence of three
transformations:
Projection transformation
Definition: Projects points from camera space, so that all visible
points fall in the range [−1,1] for all x and y values.
Dependency: Type of projection.
Input: Points in camera space.
Output: Points in canonical view volume.
Canonical
Something arbitrary chosen for the sake of convenience.
For example, the unit circle could be called a canonical circle.

Most graphics system do this by using a sequence of three
transformations:
Viewport transformation (window transformation)
Definition: Maps this unit image rectangle to the desired
rectangle in pixel coordinates.
Dependency: Size and position of the output image.
Input: Points in canonical view volume.
Output: Points in screen space.
Each transformation is relatively simple. We will focus on
orthographic case in great detail and discuss later how to change
them for perspective projection.

Section 8.1.1: The Viewport Transformation
- Let us assume what we want to view is in the canonical view
volume and we want to view it with an orthographic camera
looking in the −z direction.
- Canonical view volume is a 3D cube whose Cartesian
coordinates are defined as: (x,y,z) ∈ [−1,1]3.
- x = −1 is to the left of the screen and x = 1 is to the right.
- y = 1 is to the top of the screen and y = −1 is to the bottom.
- In Chapter 3 we discussed:
- A pixel “owns” a unit square centred at integer coordinates.
- Image boundaries have a half-unit overshoot from the pixel
centres.
- Smallest pixel center coordinates are (0,0).
- The amount of pixels in the screen is defined by: n ×n .
x y

- Using this, we need to map the square [−1,1]2 to the
rectangle [−0.5,n −0.5]×[−0.5,n −0.5].
x y
- For the sake of simplicity, we introduce the following
restriction: All line segments are drawn inside the canonical
view volume.
- Since the viewport transformation maps one axis-aligned
rectangle to another, we obtain:
 x  nx 0 nx−1 x 
screen 2 2 canonical
y screen = 0 n y ny −1 y canonical
2 2
1 0 0 1 1
- Why do we ignore the z-value?
- The final form of the viewport matrix (M ):
vp
nx nx−1
0 0
2 2
ny ny−1
0 0 
M =  2 2 
vp
0 0 1 0 
0 0 0 1

Section 8.1.2: The Orthographic Projection
Transformation
- Sometimes we want to render things that are not inside the
canonical view volume.
- We use two constraints to perform this:
1. View volume is an axis-aligned box.
2. Name the coordinates of its sides so
that the view volume is:
[l,r]×[b,t]×[f,n]
- We call this box, the orthographic view volume.

- The orthographic view volume refers to the bounding planes
as follows:
- x =l ≡ left plane - y =b ≡ bottom plane - z =n≡ near plane
- - ▶
x =r ≡ right plane y =t ≡ top plane z =f ≡ far plane
- Note, z might feel unnatural as we are looking in the −z
direction.

- Thus, the orthographically view matrix (M orth ) is:
 2 −r+l 
0 0
r−l r−l
2 −t+b
 0 0 
M =  t− b t− b 
orth 0 0 2 −n + f
 
n−f n−f
0 0 0 1
- In order to draw the 3D line segments in orthographic view
volume, we project them onto the x and y screen-coordinates.
- Again, why do we ignore the z-value?
- In order to perform this projection, we multiply M with
vp
M orth and then with the point as follows:
   
x pixel x
y y
 p ix e l   
  = (M vp M orth )  
z   z 
c an o n i cal
1 1

Thus, we can use the following algorithm to draw 3D lines.
Algorithm 1 Drawing 3D lines
Construct M
vp
Construct M
orth
M := M vp ×M orth
for each line segment (a ,b ) do
i i
p := Ma
i
q := Mb
i
drawLine(p, q)
end for

- We will now discuss changing the viewpoint in 3D and look in
any direction.
We will use the following
convention:
- We can now create a coordinate system using e as the origin,
and uvw as the basis as discussed in Section 2.4.7 (and listed
on page 163)

- We need to now translate the coordinates of geometric
objects from the coordinate system generated by the Cartesian
origin, and xyz axis to the coordinate system generated by the
origin e and uvw axis.
- In order to do this, we use the following matrix:
  
x y z 0 1 0 0 −x
u u u e
 −1
u v w e  x v y v z v 0   0 1 0 − y e
M = =    
cam 0 0 0 1 x y z 0 0 0 1 − z
w w w   e 
0 0 0 1 0 0 0 1

We can now extend Algorithm 1 to include M .
cam
Algorithm 2 Drawing 3D lines
Construct M
vp
Construct M
orth
Construct M
cam
M := M ×M ×M
vp orth cam
for each line segment (a ,b ) do
i i
p := Ma i
q := Mb
i
drawLine(p, q)
end for
