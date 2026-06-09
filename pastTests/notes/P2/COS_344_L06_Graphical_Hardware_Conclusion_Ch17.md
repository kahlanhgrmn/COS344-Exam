Extra
COS 344: L6 Chapter 17: Using Graphics
Hardware
Cobus Redelinghuys
26/02/2025

Extra
- Modern OpenGL requires shaders to process vertices and
fragments.
- Thus, no render will properly work without:
- At least one vertex shader to process the incoming primitive
vertices.
- At least one fragment shader to process the rasterized
fragment.
- OpenGL supports two advanced shader types:
- Geometry shaders
- Computer shaders

Extra
- Geometry shaders are designed to:
- Process primitives.
- Potentially creating additional primitives.
- Can support geometric instancing operations.
- Computer shaders are designed for:
- Performing general computation on the GPU.

Extra
Section 17.8.1: Vertex Shader Example
- Code in vertex shaders determines how vertices are
transformed and prepared before use in fragment shaders.
- Another use is to perform calculations on the GPU.
- Example of a simple vertex shader:
#version 330 core
layout(location=0) in vec3 in_Position;
void main(void)
{
gl_Position = vec4(in_Position, 1.0);
}
- This simple vertex shader just passes the incoming vertex
position (in Position) out as the gl Position that
OpenGL uses to rasterize the fragment.

Extra
- Note that gl Position is a reserve variable, that signifies one
of the key outputs required from a vertex shader.
- The #version 330 core instructs GLSL compiler to use
version 3.3 of the GLSL Core profile.
- Note that vertex and fragment shaders operate on all vertices
and fragments respectively, in the graphics pipleline.
- The in keyword indicates that data is being passed into the
shader.
- layout(location=0) in vec3 in Position:
- Indicates that the input variable in Position is of type vec3
(Vector of size 3).
- The source of the data is at the 0th index of the array of
attributes assigned to the vertex.
- All shaders need a main function, where the calculations are
performed.

Extra
- Matrices and Vectors in vertex shaders:
- Vectors: - Matrices:
- ▶
vec2 mat2
- ▶
vec3 mat3
- ▶
vec4 mat4
- Standard data types also exist:
- int
- float
- Example of how to access the elements in the vector:
vec4 v;
/*Do something to populate v*/
int x = v.x;
int y = v.y;
int z = v.z;
int w = v.w;

Extra
Swizzling
- We can also access elements in vectors as follows:
vec3 position = vec3(1.0, 2.0, 3.0);
vec2 xy = position.xy;
vec3 xxy = position.xxy;
vec4 xyzw = vec4(position, 1.0);
- This method of accessing the elements is known as swizzling.

- Light green.
- The out keyword denotes the output that is written to the
color buffer.
- Thus the in and out keywords denote the data flow in and
out of shaders.
Extra
Section 17.8.2: Fragment Shader Example
- The following simple fragment shader accompanies the simple
vertex shader.
#version 330 core
layout(location=0) out vec4 out_FragmentColor;
void main(void){
out_fragmentColor = vec4(0.49,0.87,0.59,1.0);
}
- What is the color that each fragment will be set to?

Extra
Section 17.8.2: Fragment Shader Example
- The following simple fragment shader accompanies the simple
vertex shader.
#version 330 core
layout(location=0) out vec4 out_FragmentColor;
void main(void){
out_fragmentColor = vec4(0.49,0.87,0.59,1.0);
}
- What is the color that each fragment will be set to?
- Light green.
- The out keyword denotes the output that is written to the
color buffer.
- Thus the in and out keywords denote the data flow in and
out of shaders.

Extra
- layout(location=0) out vec4 out FragmentColor;
- layout and location keywords makes an explicit connection
between the geometric data in the vertex shader, and the
output color buffers in the fragment shader.
- Fragment shaders can output to multiple buffers, but that is
left to the curious student
- Section 17.8.3 is left to the curious student, as we will be
using a provided file to compile and use the shaders.

glGenBuffers
glBufferData
Extra Recap
Section 17.9: Vertex Buffer Objects
- Vertices of geometric objects are stored in buffers known as
Vertex Buffer Objects (VBO).
- VBOs also store other vertex attributes such as color or
texture coordinates.
- Geometric primitives coordinates are specified in a GLfloat
array.
- Below is an example of a static primitive:
GLfloat vertices[] = {
-0.5f, -0.5f, 0.0f,
0.5f, -0.5f, 0.0f,
0.0f, 0.5f, 0.0f
}
- What is the shape?

- Thus we could use 2D coordinates to represent the triangle.
- Which shader will change and how?
#version 330 core
layout(location=0) in vec2 in_Position;
void main(void)
{
gl_Position.xy = in_Position;
gl_Position.z = 0;
gl_Position.w = 1.0;
}
glGenBuffers
glBufferData
Extra Recap
- If the simple shaders that were defined earlier are used, the
triangle will be rendered.
- Is the Z value important if it is rendered as a 2D scene?

#version 330 core
layout(location=0) in vec2 in_Position;
void main(void)
{
gl_Position.xy = in_Position;
gl_Position.z = 0;
gl_Position.w = 1.0;
}
glGenBuffers
glBufferData
Extra Recap
- If the simple shaders that were defined earlier are used, the
triangle will be rendered.
- Is the Z value important if it is rendered as a 2D scene?
- Thus we could use 2D coordinates to represent the triangle.
- Which shader will change and how?

glGenBuffers
glBufferData
Extra Recap
- If the simple shaders that were defined earlier are used, the
triangle will be rendered.
- Is the Z value important if it is rendered as a 2D scene?
- Thus we could use 2D coordinates to represent the triangle.
- Which shader will change and how?
#version 330 core
layout(location=0) in vec2 in_Position;
void main(void)
{
gl_Position.xy = in_Position;
gl_Position.z = 0;
gl_Position.w = 1.0;
}

glGenBuffers
glBufferData
Extra Recap
- In order to render a geometric primitive, the following order
should be followed:
1. Create a vertex buffer
2. Transfer the vertices into the buffer
3. Reference the buffer when needed to render the primitive.
- For efficiency, VBOs are created before the rendering loop,
such that they are not continuously re-created.
- Example of creating a VBO.
GLuint triangleVBO[1];
glGenBuffers(1, triangleVBO);
glBindBuffer(GL_ARRAY_BUFFER, triangleVBO[0]);
glBufferData(GL_ARRAY_BUFFER, 9 *
sizeof(GLfloat), vertices, GL_STATIC_DRAW);
glBindBuffer(GL_ARRAY_BUFFER, 0);

glGenBuffers
glBufferData
Extra Recap
void glGenBuffers(GLsizei n, GLuint * buffers);
- Creates a handle that can be used to refer to the VBO, once
it is stored on the device.
- Multiple handles to VBOs can be created using a single
glGenBuffers call.
- n - Specifies the number of buffer object names to be
generated.
- buffers - Specifies an array in which the generated buffer
object names are stored.
glGenBuffers
glBufferData
Extra Recap
void glBindBuffer(GLenum target, GLuint buffer);
- Binds a named buffer object.
- target - Specifies the target to which the buffer object is
bound.
- The symbolic constant can be found:
- buffer - Specifies the name of a buffer object.

glGenBuffers
glBufferData
Extra Recap
void glBufferData(GLenum target, GLsizeiptr size,
const GLvoid* data, GLenum usage);
- This function call copies the data of the array to the currently
bounded VBO.
- target - Specifies the target buffer object.
- The symbolic constant can be found:
- size - Specifies the size, in bytes, of the buffer object’s new
data store.
- data - Specifies a pointer to data that will be copied into the
data store for initialization, or NULL if no data is to be copied.
- usage - Specifies the expected usage pattern of the data
store.
- The symbolic constant can be found:

glGenBuffers
glBufferData
Extra Recap
GLuint triangleVBO[1];
glGenBuffers(1, triangleVBO);
glBindBuffer(GL_ARRAY_BUFFER, triangleVBO[0]);
glBufferData(GL_ARRAY_BUFFER, 9 * sizeof(GLfloat),
vertices, GL_STATIC_DRAW);
glBindBuffer(GL_ARRAY_BUFFER, 0);
1. triangleVBO array is created of size 1.
2. One VBO is created and bounded to the memory reference of
triangleVBO.
3. The current VBO object is bounded to the first triangleVBO
index.
4. The VBO is populated with the data in the vertices.
5. Unbind the current VBO as no more data will be read or
written to it.

glDrawArrays
Extra
Section 17.10: Vertex Array Objects
- VBOs are the storage containers for vertices.
- Vertex Array Objects (VAOs) represent OpenGL’s mechanism
to bundle vertex buffers together.
- These bundled buffers can then be communicated and linked
with shaders in graphics hardware.

glDrawArrays
Extra
- The following code segment shows how to create a VAO to
contain the triangleVBO previously created:
GLunit VAO;
glGenVertexArrays(1, &VAO);
glBindVertexArray(VAO);
glEnableVertexAttribArray(0);
glBindBuffer(GL_ARRAY_BUFFER, triangleVBO[0]);
glVertexAttribPointer(0,3,GL_FLOAT, GL_FALSE,
3*sizeof(GLfloat), 0);
glBindVertexArray(0);
- glGenVertexArrays and glBindVertexArray works similar
to the VBO and can be further explored at:
and

glDrawArrays
Extra
- Recall from the vertex shader discussion, the line:
layout(location=0) in vec3 in_Position
- Data is in Position at index 0 in the bounded VAO.
- Thus, we focus on the extract of the code snippet:
glEnableVertexAttribArray(0);
glBindBuffer(GL_ARRAY_BUFFER, triangleVBO[0]);
glVertexAttribPointer(0,3,GL_FLOAT, GL_FALSE,
3*sizeof(GLfloat), 0);

glDrawArrays
Extra
void glEnableVertexAttribArray(GLuint index);
- Enables vertex attribute array.
- Can be disabled using: void
glDisableVertexAttribArray(GLuint index);
- index - Specifies the index of the generic vertex attribute to
be enabled or disabled.
- glBindBuffer has been defined previously.

glDrawArrays
Extra
void glVertexAttribPointer(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei
stride, const GLvoid* pointer);
- index - Specifies the index of the generic vertex attribute to
be modified.
- size - Specifies the number of components per generic vertex
attribute and must be 1, 2, 3, 4.
- type - Specifies the data type of each component in the array.
- The symbolic constant can be found:
- normalized - Specifies whether fixed-point data values should
be normalized or converted directly as fixed-point values.
- stride - Specifies the byte offset between consecutive generic
vertex attributes
- pointer - Specifies an offset of the first component of the
first generic vertex attribute in the array.

- first
- Specifies the starting index in the enabled arrays.
- count
- Specifies the number of indices to be rendered.
glDrawArrays
Extra
- The last code segment we need to discuss is to start the
pipeline process.
- The code segment is given below:
glBindVertexArray(VAO);
glDrawArrays(GL_TRIANGLES, 0, 3);
glBindVertexArray(0);
- void glDrawArrays(GLenum mode, GLint first,
GLsizei count);
- mode - Specifies what kind of primitives to render.
- The symbolic constant can be found, but will also be covered
later in the lecture: https://docs.gl/gl3/glDrawArrays
- What primitives can we draw?

glDrawArrays
Extra
- The last code segment we need to discuss is to start the
pipeline process.
- The code segment is given below:
glBindVertexArray(VAO);
glDrawArrays(GL_TRIANGLES, 0, 3);
glBindVertexArray(0);
- void glDrawArrays(GLenum mode, GLint first,
GLsizei count);
- mode - Specifies what kind of primitives to render.
- The symbolic constant can be found, but will also be covered
later in the lecture: https://docs.gl/gl3/glDrawArrays
- What primitives can we draw?
- first
- Specifies the starting index in the enabled arrays.
- count
- Specifies the number of indices to be rendered.

glDrawArrays
Extra
- Section 17.11 is left to students. Reminder you are not
allowed to use GLM in practicals but only in the homework
assignment!!!
- Sections 17.12 and 17.13 gives examples of how to perform
pre-vertex and pre-fragement shading. Note for practical 4,
you need to do the shading calculations in the application, not
the shader.
- Section 17.15 will only be useful after covering texture
mapping.
- Section 17.16 can be useful for designing your practicals.

- Simplicity:
- Most basic polygon.
- Triangles are the least amount of points needed to create an
area.
- Planarity:
- Three non-collinear points always define a unique plane in 3D
space.
- Which ensures that triangles are always flat.
- why-do-3d-engines-use-triangles-to-draw-object-surfaces
Section17.8:AFirstLookAtShaders 2DShapes
Extra
2D Shapes
- Before animating an object we need to model said object.
- In computer graphics, triangles are used to create more
shapes.
- Why triangles?

Section17.8:AFirstLookAtShaders 2DShapes
Extra
2D Shapes
- Before animating an object we need to model said object.
- In computer graphics, triangles are used to create more
shapes.
- Why triangles?
- Simplicity:
- Most basic polygon.
- Triangles are the least amount of points needed to create an
area.
- Planarity:
- Three non-collinear points always define a unique plane in 3D
space.
- Which ensures that triangles are always flat.
- why-do-3d-engines-use-triangles-to-draw-object-surfaces

- Yes, the triangle needs to be created such that the normal of
the plane created by the triangle faces outward.
- Open COS344 L6 Normals in
- Why must the normal face outward?
Section17.8:AFirstLookAtShaders 2DShapes
Extra
- Triangles, thus, consists out of three vertices.
- Is the order in which we “connect” the vertices to form the
triangle important?

Section17.8:AFirstLookAtShaders 2DShapes
Extra
- Triangles, thus, consists out of three vertices.
- Is the order in which we “connect” the vertices to form the
triangle important?
- Yes, the triangle needs to be created such that the normal of
the plane created by the triangle faces outward.
- Open COS344 L6 Normals in
- Why must the normal face outward?

Section17.8:AFirstLookAtShaders 2DShapes
Extra
- Now that we can create triangles correctly, how can we use
them to create other shapes?
- For each of the following shapes describe how to model them
using triangles.
- Rectangle
- Pentagon
- Hexagon
- Circle

Section17.8:AFirstLookAtShaders 2DShapes
Extra
- Note that not all of the methods are explicitly covered in the
textbook, although Section 12.1.3 covers a part of this.
- OpenGL defined a set of primitive rendering modes, in which
we can define how OpenGL must draw the vertices that are
passed to it.
- The three main categories:
- Point
- Line
- Triangle
- GLStart/Tut3
- Some of these methods have been deprecated since OpenGL
3.0 and removed since OpenGL 3.1.

Section17.8:AFirstLookAtShaders 2DShapes
Extra
Points
- All the vertices in the vertex array are rendered as points.
b2/Glstart_tut3_4.jpg

Section17.8:AFirstLookAtShaders 2DShapes
Extra
Lines
All the vertices in the vertex array are rendered as lines.
- GL Lines
- Each pair of vertices represents a line.
- Say a line is formed between points a and b, then the next line
will be formed between c and d.
- GL Line Strip
- The vertices are connected to make a loop, excluding
connecting the first and last vertex.
- GL Line Loop
- The vertices are connected to make a loop, including the first
and last vertex.

Section17.8:AFirstLookAtShaders 2DShapes
Extra
Triangles
All the vertices in the vertex array, are rendered as triangles.
- GL Triangles
- A tuple of vertices from the array is drawn as a triangle.
- Say a triangle is formed with points a, b, and c, then the next
triangle will be formed using d, e, and f.
- GL Triangle Strip
- Triangles are formed in a strip.
- Say a triangle is formed with points a, b, and c, then the next
triangle will be formed using b, c, and d.
- GL Triangle Fan
- Triangles are formed in a fan.
- Say a triangle is formed with points a, b, and c, then the next
triangle will be formed using a, c, and d.

Section17.8:AFirstLookAtShaders 2DShapes
Extra
v0 v2 v4 v0 v2 v4
v1 v3 v6 v1 v3 v6
GL_POINTS GL_LINES
v0 v2 v4 v0 v2 v4
v1 v3 v6 v1 v3 v6
GL_LINE_STRIP GL_LINE_LOOP
v0 v2 v4 v0 v2 v4
v1 v3 v6 v1 v3 v6
GL_TRIANGLES GL_TRIANGLE_STRIP
v4 v3
v5 v2
v1
GL_TRIANGLE_FAN

Section17.8:AFirstLookAtShaders 2DShapes
Extra
Test type question. Given a set of points, apply the primitive
drawing method, or combine the points using the minimum
amount of triangles to cover the entire polygon.
