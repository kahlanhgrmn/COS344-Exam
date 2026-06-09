COS 344: L15 Chapter 11: Texture Mapping
Cobus Redelinghuys
16/04/2026

- Today, we will start our discussion on texture mapping and
will continue it on Thursday.
- For Practical 4, note a relaxed requirement. Texture mapping
and related operations, such as bump mapping, can be done
in the shaders.
- All transformations, camera (if being used), and any other
operations should still be done in the CPP file.

Given these apparent smooth surfaces, what do you notice?
They are smooth, but are they smooth smooth?

Spatially varying surface properties
Attributes of surfaces that vary from place to place but do not
alter the shape of the surface.
- Spatially varying surface properties are usually achieved using
some type of image.
- These images are called:
- Texture mapping
- Texture image
- Texture
- Idea behind texture mapping:
- Store the texture in a type of image, and then mathematically
map this image to a set of surfaces.

- Texture mapping can also be used to create:
- Shadows
- Reflections
- Provide illumination
- Define surface shapes
- And even store data
- We will specifically look at using texture maps to represent:
- Detail
- Shadows
- Reflection

- Consider the following scene:
- A room with a wooden floor.
- The diffuse color of the floor is controlled by an image showing
floorboards with wood grain.
- We need to know the color of the surface to calculate the
shading.
- To retrieve this color, the shader performs a texture lookup.
Texture lookup
The process of finding out the location, in the coordinate system
of the texture image, that corresponds to the shading point, and
reads out the color at that location.
Texture sample
The output color that was obtained from a texture lookup.

Texture coordinate function
A function that maps from the surface to the texture which is
easily computable for every pixel.
- Mathematically, a texture coordinate function is a mapping
from the surface S, to the domain of the texture, T.
ϕ : S → T
: (x,y,z) → (u,v)
- Set T is often called the “texture space”.
- T is usually a rectangle that contains the image.
- It is even common practice to have T use the unit square
[0,1]2.
(u,v) ∈
- The textbook uses the convention that (u,v) is coordinates
on the texture map for this chapter.

Automatic-3D-face-texture-mapping-framework-from-He-Yuk/
f56157cd90f547f1f45adc6586b32956b98966b3/figure/2

- Thus, π maps a coordinate on the surface in world space to a
coordinate on the image space, and ϕ maps a coordinate on
the surface in world space to a coordinate on the texture
space.
- Therefore, both π and ϕ are 3D to 2D mappings.
- Where else did we see this?
- π is a view projection and is almost always either an
orthographic or perspective projection.
- ϕ can take on many forms, due to each object in the scene
likely having different texture functions.
- Note that ϕ is a mapping from the surface to the texture,
which is reversed but the correct order of doing it.

- Getting back to the wooden floor example.
- Assume the floor is at a constant z position and axis aligned
with the x and y axes.
- We could then use the mappings:
u = ax
v = by
- Where a and b are “suitably” chosen scale factors.
 
u
- This allows us to assign texture coordinates , to the point
v
 
x
y and then use the value of the texture pixel (known as
z
floor
  
u x
a texel) closest to as the texture value at
v y

- Obviously, this simple mapping is very limited.
- We have two problems in basic texture mapping:
- Defining texture coordinate functions (Section 11.2).
- Looking up texture values without introducing too much
aliasing (Section 11.3).
- We will only discuss Section 11.2 as Section 11.3 requires
knowledge of Chapter 10, which is outside the pre-requisites
for this module.

Fig 11.3 contains aliasing artefacts (stairsteps in the foreground,
wavy and glittery patterns in the distance).

Section 11.2: Texture Coordinate Functions
- Intuitively designing the texture coordinate function, is
deciding how you are going to deform a rectangular 2D flat
surface, to fit around a 3D object.
- As previously stated, there are many different ways to design
the texture coordinate function, but the following points
should be taken into consideration:
- Bijectivity
- Size distortion
- Shape distortion
- Continuity
- We can define texture coordinates in two ways:
- Compute them geometrically.
- Or from mesh surfaces.

Bijectivity:
- Consider a function f(a) = b.
- Function f is bijective i.f.f. ∀a ∈ A, f(a) maps to a unique b
and ∀b ∈ B there is a unique a such that f(a) = b.
- In other words, there is a one-to-one mapping between a and
b in f(a) = b.
- Ideally, we would like each coordinate in the world space to
map to a unique coordinate in the texture space.
- Is there a case for when we would like a set of coordinates in
the world space to map to the same place in texture space?

Size distortion:
- The scale of the texture should be approximately constant
across the surface.
- i.e. points that are close to each other on the texture space
should be relatively close to each other on the geometric
object.
Shape distortion:
- The texture should not be distorted.
- i.e. small circles on the texture should appear as relatively
circular patterns on the geometric object.
Continuity
- There should not be too many seams.
- Points that are next to each other on the surface should map
to points that are next to each other in the texture.

- Geometrically determined texture coordinates are usually used
for simple objects, or as starting points for hand tweaked
texture coordinate maps.
- There are many different ways to calculate these coordinates:
- Planar projection:
- Utilises parallel projection and the same machinery developed
for orthographic viewing.
- Spherical coordinates:
- Used to map textures to a sphere and uses the idea of
latitudes and longitudes to accomplish this mapping.
- Cylindrical coordinates:
- Used for cylindrical objects when the object is more columnar
than spherical.
- Cubemaps:
- Spherical projection allows for high amounts of distortion
around the poles of the sphere.
- An alternative is to rather map the texture to a square, and
then map each face of the square to a section of the sphere.

Section 11.2.2: Interpolated Texture Coordinates
- For a bit more of a fine grain control over the texture
coordinate function on a triangle mesh surface, explicitly store
the texture coordinates at each vertex.
- Using these stored coordinates, interpolate across the triangles
using barycentric interpolation.

- What could scaling the texture coordinates up be used for?
- If the machinery is already set up to use the texture map using
the unit square coordinate system, scaling the texture map up
will ensure that a smaller portion of the texture map is used.
- What should we return if the texture coordinate function
needs to return a texture coordinate that is outside of the unit
square?
- Return a constant color, like black.
- When can it be useful to use a wrap-around coordinate system
for texture coordinate lookup?
- Say we have a chess board with repeated black and white tiles.
- We could use a wrap-around coordinate system, where lookups
that are outside of the unit square, is wrapped around back
into the unit square.
- Why would it be useful to have the texture coordinates extend
further than the texture coordinate function will ever use?

- If the machinery is already set up to use the texture map using
the unit square coordinate system, scaling the texture map up
will ensure that a smaller portion of the texture map is used.
- What should we return if the texture coordinate function
needs to return a texture coordinate that is outside of the unit
square?
- Return a constant color, like black.
- When can it be useful to use a wrap-around coordinate system
for texture coordinate lookup?
- Say we have a chess board with repeated black and white tiles.
- We could use a wrap-around coordinate system, where lookups
that are outside of the unit square, is wrapped around back
into the unit square.
- Why would it be useful to have the texture coordinates extend
further than the texture coordinate function will ever use?
- What could scaling the texture coordinates up be used for?

- Return a constant color, like black.
- When can it be useful to use a wrap-around coordinate system
for texture coordinate lookup?
- Say we have a chess board with repeated black and white tiles.
- We could use a wrap-around coordinate system, where lookups
that are outside of the unit square, is wrapped around back
into the unit square.
- Why would it be useful to have the texture coordinates extend
further than the texture coordinate function will ever use?
- What could scaling the texture coordinates up be used for?
- If the machinery is already set up to use the texture map using
the unit square coordinate system, scaling the texture map up
will ensure that a smaller portion of the texture map is used.
- What should we return if the texture coordinate function
needs to return a texture coordinate that is outside of the unit
square?

- Say we have a chess board with repeated black and white tiles.
- We could use a wrap-around coordinate system, where lookups
that are outside of the unit square, is wrapped around back
into the unit square.
- Why would it be useful to have the texture coordinates extend
further than the texture coordinate function will ever use?
- What could scaling the texture coordinates up be used for?
- If the machinery is already set up to use the texture map using
the unit square coordinate system, scaling the texture map up
will ensure that a smaller portion of the texture map is used.
- What should we return if the texture coordinate function
needs to return a texture coordinate that is outside of the unit
square?
- Return a constant color, like black.
- When can it be useful to use a wrap-around coordinate system
for texture coordinate lookup?

- Why would it be useful to have the texture coordinates extend
further than the texture coordinate function will ever use?
- What could scaling the texture coordinates up be used for?
- If the machinery is already set up to use the texture map using
the unit square coordinate system, scaling the texture map up
will ensure that a smaller portion of the texture map is used.
- What should we return if the texture coordinate function
needs to return a texture coordinate that is outside of the unit
square?
- Return a constant color, like black.
- When can it be useful to use a wrap-around coordinate system
for texture coordinate lookup?
- Say we have a chess board with repeated black and white tiles.
- We could use a wrap-around coordinate system, where lookups
that are outside of the unit square, is wrapped around back
into the unit square.

- These two methods of handling out-of-bounds are examples of
“wrapping modes”.
- Other examples are:
- Tiling
- Clamping
- Other variations.

Section 11.2.4: Continuity and Seams
- To obtain a perfect texture coordinate function is often very
difficult and a compromise is needed.
- Usually the best resulting compromise is to introduce seams.
- In many of the geometrically determined mappings discussed,
seams are already present.
- Spherical and cylindrical coordinates have seams where the
angle computed by atan2 wraps around from −π to π.
- Cubemaps have seams along the edges of the faces.

- In interpolated texture coordinates, we need to account for
the case where the texture mesh contains triangles whose
vertices are on either side of the seem.
- This causes high levels of distortion, or fold over.
- The only solution is to ensure that the triangles that are on
the seam avoid sharing coordinates.
- Section 11.2.5 is left to the curious student.
