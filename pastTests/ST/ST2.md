Here are the questions and their associated visual content extracted from the second semester test document:

### **Scenario**

Consider the following scenario when answering the majority of the questions in this test: You have been contracted to create a render to illustrate how the resulting colour of a beam of light is affected by a panel of coloured glass when shone onto a coloured floor. The render should be set up as follows:

* A floor consisting of a variable number of a series of smaller rectangles, which are of the same size.


* The floor also has a series of rectangles running along the sides to create the illusion that the floor is a 3D cuboid and not a flat 2D plane.


* A 3D glass panel, which has a variable thickness, is positioned in the middle of the floor.


* A light that shines through the glass panel onto the floor.



> 
> **Visual Content:** Two reference render images - Figure 1: A and Figure 2: В are shown in the exam paper.
> 
> 

---

### **Question 1**

**1.1** Which of the following allows you to import assets created in Blender into OpenGL? 

* A. Asset Importer 


* B. ASSIMP 


* C. GoDot 


* D. GLFW 



**1.2** Which of the following programs can assist you with debugging your graphic assignments, specifically with regard to the graphics pipeline? 

* A. GDB 


* B. Blender 


* C. RenderDoc 


* D. Glad 



**1.3** Which of the following drawbacks is specific to the obj wavefront file format? 

* A. Lacks support for modern texture workflows 


* B. Not human-readable 


* C. Open source 


* D. Designed for transfer between 3D tools 



**1.4** Consider the following texture lookup function $f(x,y,z)=(u,v)$ where $u=2x^2 \bmod z$ and $v=\log(y) \bmod z$. Answer the following questions:

**a)** What is the primary issue with its bijectivity? 

* A. The function always returns zero values for u and v.


* B. The function is not defined for all combinations of x, y, and z.


* C. The square term $x^2$ in $u=2x^2 \bmod z$ can cause multiple input coordinates to map to the same output texture coordinates.


* D. The logarithm function $\log(y)$ is undefined for negative values of y.



**b)** Which of the following best describes the distortion of size within the texture lookup function? 

* A. Only the v component is subject to distortion, leading to size changes.


* B. Both the u and v components are equally affected, resulting in overall size distortion.


* C. The function maintains perfect size preservation.


* D. The function always increases the size of the texture.



**c)** How does the use of the modulus operator in the texture lookup function affect the shape of the resulting textures? 

* A. The modulus operator has no effect on the shape of the texture.


* B. It creates a perfectly regular and predictable shape distortion.


* C. The modulus operator only distorts textures when z is a large number.


* D. The non-linear nature of the modulus operation (creating discrete jumps) leads to significant shape distortion.



---

### **Question 2**

**2.1** For each of the two images (Figure 1 and Figure 2), name the projection that was used to create the image, and justify your answer.

* Figure 1: 


* Figure 2: 



---

### **Question 3**

To create and present the scene orthographically, a series of matrices is needed. Given the following information, provide all of the required 4D matrices to create the scene:

* A screen that is 1920 pixels wide and 1080 pixels high.


* A view volume with the following bounding planes: Left = -10, Right = 10, Top = 8, Bottom = -8, Near = -2, $Far = -10$.


* A camera described by the following vectors:
* Camera position: $[2, 2, 2]^T$ 


* Camera gazing direction: $[-2, 0, 0]^T$ 


* Camera top direction: $[2, 2, 0]^T$ 



If a matrix can be expressed in its inverse form, you can provide that form as well. For each matrix that you create, provide its name and its purpose. Show all steps performed to create each of the matrices.

---

### **Question 4**

**4.1** For each of the following culling techniques, using an 'X', indicate on the side profile drawing which faces of the objects will be culled. If the entire object is culled, draw a big 'X' over the entire object. Motivate your answer to the right of the image.

**a)** Viewvolume Culling 

> 
> **Visual Content:** Side profile diagram with Camera, View volume, Floor, Glass, Ball, and Decor objects provided in exam paper.
> 
> 

**b)** Occlusion Culling 

> 
> **Visual Content:** Side profile diagram provided in exam paper.
> 
> 

**c)** Backface Culling 

> 
> **Visual Content:** Side profile diagram provided in exam paper.
> 
> 

**4.2** Explain why the winding order of the triangles used to create the faces of shapes is important, especially for backface culling.

**4.3** Provide the C++ code that will allow the culling of the front faces of objects. The winding order that should be used is clockwise.

---

### **Question 5**

Consider the following texture image is used for the floor of the scenario:

> 
> **Visual Content:** Figure 3: Texture Image a small 2-tile image with a dark and a light grey square.
> 
> 

**5.1** Explain which of the geometrically determined coordinate techniques that were discussed in class will be the most appropriate for the scenario. Motivate your answer.

**5.2** Together with the geometrically determined coordinate technique, tiling can also be used. Explain how.

**5.3** Assume that a C++ program has been correctly configured to load the texture, and pass all the following information to the vertex shader:

* Vertex positions as a vec3 at position 0.


* Surface normals for each vertex as a vec3 at position 1.


* Texture coordinates as a vec2 at position 2.


* The texture as a uniform sampler2D known as "customTexture".



Consider as well that the result of a texture lookup returns a float between the values of -1 and 1. The colour associated with each vertex position should be a vec3 with all three components set to the result of the texture lookup function. Answer the following questions:

**a)** Provide the vertex shader that will scale the vertex position along the passed-through surface normal by the result of the texture lookup for the passed-through texture coordinate.

**b)** What is the name for this application of texture mapping? Provide a reason for your answer.

---

### **Question 6**

**6.1** Assume the centre of the scene is situated at the position described by $[1, 1, 1]^T$. You would like to perform the following transformations on the scene, in this order:

* Scale the scene by 2 units along the x-direction and 3 units along the y-direction.


* Rotate by $30^\circ$ units around the centre of the scene in both the x and y axis.



Provide the required matrices, and explain the purpose of each of the matrices.

---

### **Question 7**

**7.1** Consider that the glass contains lots of tiny scratches and deformities. Answer the following questions:


**a)** Explain how you would apply a level of detail algorithm to improve the performance of the render.
**b)** If this render were ported over to work on mobile devices, explain why it is important to develop it for a computationally weak platform compared to a computationally strong platform.
**c)** Explain how computer games that were developed on older hardware can run on hardware that was not yet invented at the time of the games' development.

**7.2** Consider we have the following vertices, which can be combined to create index-based meshes: 

| Vertex number | Position |
| --- | --- |
| 0 | (1,0,0) 

 |
| 1 | (0,1,0) 

 |
| 2 | (0,0,1) 

 |
| 3 | (1,1,0) 

 |
| 4 | (0,1,1) 

 |
| 5 | (1,1,1) 

 |

**a)** State whether the following triangle combinations violate the strict manifold restrictions. Provide a motivation for your answer.

* i) (2, 4, 1), (4, 1, 0), (4, 5, 1) 


* ii) (2, 4, 1), (4, 5, 1), (2, 5, 1), (1, 0, 3) 



**b)** State whether the following triangle combinations violate the relaxed manifold restrictions. Provide a motivation for your answer.

* i) (1, 0, 3), (1, 3, 5), (0, 1, 2) 


* ii) (2, 1, 4), (4, 5, 1), (4, 2, 5), (1, 3, 0) 



---

### **Question 8**

Visualisation is one of the applications of computer graphics. Answer the following questions on visualisation.

**8.1** Explain how clipping through a geometric object in a render can be seen as a negative experience for the user, but in visualisation, it can be used to aid the user's understanding.

**8.2** Often, it is needed to reduce the complexity of the data. Contrast the derived dimensionality technique with another data dimensionality reduction method that was discussed in class by discussing the following points:

* Explain what derived dimensionality is, as well as the technique of your choosing.


* Explain one advantage and one disadvantage of each method.


* Provide a use case for both methods.