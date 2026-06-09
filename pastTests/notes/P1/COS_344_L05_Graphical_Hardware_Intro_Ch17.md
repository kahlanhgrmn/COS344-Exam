COS 344: L5 Chapter 17: Using Graphics
Hardware
Cobus Redelinghuys
23/02/2026

- This week’s work starts with what is needed to complete
practicals 2, 3, and 4.
- At the end of next week you will have all the basics to
complete practicals 2, 3, and 4.
- There will be a set of examples to go with this and next
week’s work.

- A set of:
- Chipset
- Transistors
- Busses
- Processors
- Computing cores
- Graphical Processing Units (GPUs)
- Optimized for processing 3D objects and transforming them.
- Supports a high level of parallelism with thousands of
concurrent threads.
- Apart from computer graphics, where else have GPUs been
applied, and why?
Section 17.2: What is Graphics Hardware
- What is graphics hardware?

Section 17.2: What is Graphics Hardware
- What is graphics hardware?
- A set of:
- Chipset
- Transistors
- Busses
- Processors
- Computing cores
- Graphical Processing Units (GPUs)
- Optimized for processing 3D objects and transforming them.
- Supports a high level of parallelism with thousands of
concurrent threads.
- Apart from computer graphics, where else have GPUs been
applied, and why?

- Designed to
display videos
- Release date:
1981
- Could display
text or symbols
in 80 columns
with 25 lines.
- Produced by
IBM.

Bird

- Marketed as
the first real
GPU.
- Release date:
11/10/1999
- OpenGL: 1.2.1
- Transistors 17
million
- Clockspeed:
120 MHz
“a single-chip processor with integrated transform, lighting, triangle
setup/clipping, and rendering engines that is capable of processing a minimum
of 10 million polygons per second.” https://youtu.be/zKH2BXzeQIU

- Newest Nvidia
GPU
- Release date:
30/01/2025
- OpenGL: 4.6
- ®
NVIDIA CUDA
Cores: 21760
- Clockspeed: 2.01
GHz / 2.41 GHz
- Memory: 32 GB
GDDR7
- RTX5090promo
- DemoA
- DemoB

- Newest AMD
GPU.
- Release date:
06/03/2025
- Transistor count:
53.9 billion.
- Clockspeed: 2.4
GHz / 2.97 GHz
- Memory: 16 GB
GDDR6
The remainder of the section is left to the curious student.

- Not the most modern API, but contains the modern trends of
modern APIs.
- OpenGL is implemented in a C-style, and each OpenGL
function starts with “gl”.
- Think of the underlying API as a state machine and OpenGL
function calls change the state.
Section 17.3.1: Programming with OpenGL
- The introduction of the chapter is left for the curious students
interested in hardware as the physical soldering of the board is
discussed.
- So, why OpenGL 3.3?

Section 17.3.1: Programming with OpenGL
- The introduction of the chapter is left for the curious students
interested in hardware as the physical soldering of the board is
discussed.
- So, why OpenGL 3.3?
- Not the most modern API, but contains the modern trends of
modern APIs.
- OpenGL is implemented in a C-style, and each OpenGL
function starts with “gl”.
- Think of the underlying API as a state machine and OpenGL
function calls change the state.

- In C++ code, to ensure that you are using OpenGL 3.3 core
profiles, make sure that the following is set:
glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3); 1
glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3); 2
glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); 3
glfwWindowHint(GLFW_OPENGL_PROFILE, 4
GLFW_OPENGL_CORE_PROFILE);

- Section 17.4.1 Buffers
- Buffers are the primary structure to store data on graphic
hardware.
- Section 17.4.2 Display Buffer
- The final set of pixel colours that will be displayed is a 2D
array of colour values.
- Data is logically a 2D array, but physically a 1D array on the
GPU.
- This is known as the display buffer.
- Rendering involves changing this buffer, such that after
rasterization, the final image is written to the output display
buffer.

- The back buffer is used to alter the model.
- The front buffer is used to display to screen.
- After the rendering loop (discussed later), the two buffers are
“swapped” using a pointer exchange.
- Tearing occurs when the buffer pointer swap is not
synchronized with the windowing system’s refresh rate.
- There is a need to clear the back buffer such that it is “clean”
before writing to it again.
- This can be achieved by setting the background color of the
scene.
glClearColor(0.0f, 0.0f, 0.0f, 1.0f); 1
glClear(GL_COLOR_BUFFER_BIT); 2
- Section 17.4.3 Cycle of Refresh
- Most applications use a two buffer system.
- The buffers are the front and rear buffer.
- Why?

- Section 17.4.3 Cycle of Refresh
- Most applications use a two buffer system.
- The buffers are the front and rear buffer.
- Why?
- The back buffer is used to alter the model.
- The front buffer is used to display to screen.
- After the rendering loop (discussed later), the two buffers are
“swapped” using a pointer exchange.
- Tearing occurs when the buffer pointer swap is not
synchronized with the windowing system’s refresh rate.
- There is a need to clear the back buffer such that it is “clean”
before writing to it again.
- This can be achieved by setting the background color of the
scene.
glClearColor(0.0f, 0.0f, 0.0f, 1.0f); 1
glClear(GL_COLOR_BUFFER_BIT); 2

- void glClearColor(GLclampf red, GLclampf green, GLclampf
blue, GLclampf alpha);
- The first three specify the RGB components of the background
colour, respectively.
- The last property is the alpha value of the background color.
- - void glClear(GLbitfield mask);
- Bitwise OR of masks that indicate the buffers to be cleared.
- The possible inputs:
- GL_COLOR_BUFFER_BIT
- GL_DEPTH_BUFFER_BIT
- GL_STENCIL_BUFFER_BIT
- - To allow OpenGL to draw in 3D space, the Z-buffer algorithm
is used. (Discussed in more depth later in the semester)
- In OpenGL, the z-buffer state can also be enabled and
disabled as needed.
- In OpenGL, this is known as a depth test.
- The z-buffer is enabled as follows:
glEnable(GL_DEPTH_TEST); 1
glDepthFunc(GL_LESS); 2
- void glEnable(GLenum cap);
- cap - Specifies a symbolic constant indicating a GL capability.
- There is a large list of things that can be enabled, which can
be found on the URL below.
- - void glDepthFunc(GLenum func);
- func - Specifies the depth comparison function.
- Symbolic constants are:
- GL_NEVER
- GL_LESS
- GL_EQUAL
- GL_LEQUAL
- GL_GREATER
- GL_NOTEQUAL
- GL_GEQUAL
- GL_ALWAYS
- The default is GL_LESS.
- - At the heart of your OpenGL program, is the display loop.
- It is either faster or equal to the display’s refresh rate.
- The main loop is given below:
do{//Loop to constantly swap buffers 1
2
glClear(GL COLOR BUFFER BIT GL DEPTH BUFFER BIT); 4
5
glfwSwapBuffers(window);//Swap front and back buffers 6
7
glfwPollEvents(); //Poll for events 8
9
} while (glfwGetKey(window, GLFWKEYSPACE) != GLFWPRESS 11
&& glfwWindowShouldClose(window) == 0); 12

- Points
- Lines
- This is used to create your wireframes.
- Triangles
- This is used to create your polygons.
Geometry
- Vertex attributes that are used to describe a geometric object
are stored in an array before passing it off to be rendered.
- On standard GPUs, the basic geometric primitives are?

Geometry
- Vertex attributes that are used to describe a geometric object
are stored in an array before passing it off to be rendered.
- On standard GPUs, the basic geometric primitives are?
- Points
- Lines
- This is used to create your wireframes.
- Triangles
- This is used to create your polygons.
