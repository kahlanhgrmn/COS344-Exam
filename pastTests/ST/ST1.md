
Question 1 

**1.1** Given that a raster display has the dimensions of 1300 by 1100, how many pixels is the display comprised of? 

* A. 1300 


* B. 1100 


* C. 2400 


* D. 13001100 


* E. None of the above 



**1.2** Consider the homogeneous matrix below is applied to a point to transform the point. 

$$\begin{bmatrix} 1 & 0 & 0.5 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$$

Which of the following vector representation(s) of the point is valid such that the point will be transformed? 

* A. $[2 \quad 1]$ 


* B. $[2 \quad 1 \quad 0]$ 


* C. $[2 \quad 1 \quad 1]$ 


* D. $[2 \quad 1 \quad 1]^T$ 


* E. $[2 \quad 1 \quad 0]^T$ 


* F. $[2 \quad 1]^T$ 


* G. None of the above 



**1.3** Consider the transformation matrix below is applied to the following vector. Which of the following descriptions best describes the resulting transformation? 

$$\begin{bmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

 applied to 

$$\begin{bmatrix} e \\ e^2 \\ 0 \end{bmatrix}$$



* A. No transformation 


* B. Translation 


* C. Scaling 


* D. Shearing 


* E. Rotation 


* F. A transformation not mentioned in the other options 



**1.4** Ambient lighting is primarily used to: 

* A. Simulate directional light sources such as the sun 


* B. Provide a uniform base illumination independent of object position 


* C. Create shadows and highlights based on surface orientation 


* D. Enhance specular reflections on shiny surfaces 



**1.5** Consider a general ray can be described by: $r(e,d,t)=e+td$, where $e$ is the origin of the ray and $d$ is the direction of the ray. Which of the following rays are examples of parallel projection? i) $r(e_1,d_1,t)$ ii) $r(e_2,d_1,t)$ iii) $r(e_1,d_2,t)$ iv) $r(e_3,d_3,t)$ Assume that $e_1 \neq e_2 \neq e_3$ and $d_1 \neq d_2 \neq d_3$. 

* A. i, ii 


* B. i, iii 


* C. i, iv 


* D. i, ii, iv 


* E. ii, iii, iv 


* F. More than one of the above, but not all of the above 


* G. All of the above 


* H. None of the above 



**1.6** Consider a general ray can be described by: $r(e,d,t)=e+td$, where $e$ is the origin of the ray and $d$ is the direction of the ray. Which of the following rays are examples of perspective projection? i) $r(e_1,d_1,t)$ ii) $r(e_2,d_1,t)$ iii) $r(e_1,d_2,t)$ iv) $r(e_3,d_3,t)$ Assume that each of the $e$s and $d$s is different. 

* A. i, ii 


* B. i, iii 


* C. i, iv 


* D. i, ii, iv 


* E. ii, iii, iv 


* F. More than one of the above, but not all of the above 


* G. All of the above 


* H. None of the above 



**1.7** OpenGL is an example of which Computer Graphics API: 

* A. Integrated 


* B. Web 


* C. Library 


* D. Practical 



**1.8** Consider the following render of a scenario, where the tiles on the floor are perfectly square: 

> 
> **Visual Content:** Orthographic-style render of a floor with a box. 
> 
> 

Which of the following projections best describes the projection used in the render of the scenario? 

* A. Orthographic projection 


* B. Perspective projection 


* C. Oblique projection 


* D. Fish Eye projection 



**1.9** Consider the following render of a scenario, where the tiles on the floor are perfectly square: 

> 
> **Visual Content:** Angled render of a floor with a box. 
> 
> 

Which of the following projections best describes the projection used in the render of the scenario? 

* A. Orthographic projection 


* B. Perspective projection 


* C. Oblique projection 


* D. Fish Eye projection 



---

Question 2 

**2.1** Explain why a camera sensor is an example of a 2D raster image input. 

**2.2** Consider an RGB colour cube, where each colour component is bounded between the values 0 and 1, i.e., blue has the coordinate $[0, 0, 1]^T$. What is the name given to the scale of colours produced by the line going from the origin to the coordinate $[1, 1, 1]^T$? 

**2.3** Consider the following C++ function definition: `Colour determine Final Colour (Colour foreground, Colour background, float alpha)` 
This function needs to determine the final colour after alpha compositing has occurred. The Colour data type is defined as follows: 

```cpp
struct Colour {
    float r;
    float g;
    float b;
    Colour(float r, float g, float b): r(r), g(g), b(b) {};
};

```

Provide the implementation for the determine Final Colour function. 

**2.4** Consider that we have a ray from a point light source, positioned at $[4, 4, 4]^T$, that intersects the surface at a position described by $[2, 1, 3]^T$. The normal of the surface where the light intersects with said surface is $[0, 1, 0]^T$. 
If the direction of the reflected light is $[-2, 3, -1]^T$, what can be assumed by the type of reflection caused by the material of the surface? Provide a motivation for your answer. 

---

Question 3 

**3.1** State whether the following statement is true or false, and provide a motivation. Note: No marks will be awarded if no motivation is given. "Rendering is the process by which the object is moved around the screen" 

**3.2** In Computer Graphics, there exist two types of methods for determining how an object influences the final result a pixel shows. Answer the following questions. 

* 
**a)** Name each of these two methods, and explain how they differ. 


* **b)** OpenGL is an example of which method? Provide a reason for your answer. Note: No marks will be awarded if no motivation is given. 



**3.3** As part of any ray-tracing algorithm, explain why it is important to know how to calculate if a viewing ray intersects a triangle, specifically. As part of your discussion, explain why triangles play a vital role in Computer Graphics. 

---

Question 4 

Consider the following C++ program: 

```cpp
/* required correct pre-amble and setup goes here */
int main()
{
    GLFWwindow *window = setUp();
    glClearColor(0.2, 0.2, 0.2, 0.2);
    GLuint VertexArrayID;
    glGenVertexArrays(1, &VertexArrayID);
    glBindVertexArray(VertexArrayID);
    GLuint programID = LoadShaders("vertexShader.glsl", "fragmentShader.glsl");
    GLuint vertexbuffer;
    glGenBuffers(1, &vertexbuffer);
    GLuint colorbuffer;
    glGenBuffers(1, &colorbuffer);
    GLfloat vertices[] = {
        -0.5, 0,
        -0.7, 0.2,
        -0.5, 0.3,
        -0.3, 0.2,
        0.0, 0.0,
        -0.1, 0.3,
        0.0, 0.4,
        0.0, 0.0,
        0.1, 0.3,
        0.0, 0.4,
        0.2, 0.2,
        0.2, 0.4,
        0.4, 0.2,
        0.4, 0.4,
        0.8, 0.2,
        0.8, 0.4
    };
    GLfloat colors[] = {
        1,0,0,
        1,0,0,
        1,0,0,
        1,0,0,
        0,1,0,
        0,1,0,
        0,1,0,
        0,1,0,
        0,1,0,
        0,1,0,
        0,0,1,
        0,0,1,
        0,0,1,
        0,0,1,
        0,0,1,
        0,0,1,
    };
    do
    {
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        glUseProgram(programID);
        glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
        glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
        glBindBuffer(GL_ARRAY_BUFFER, colorbuffer);
        glBufferData(GL_ARRAY_BUFFER, sizeof(colors), colors, GL_STATIC_DRAW);
        glEnableVertexAttribArray(0);
        glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, (void *)0);
        glEnableVertexAttribArray(1);
        glBindBuffer(GL_ARRAY_BUFFER, colorbuffer);
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, (void *)0);
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4);
        glDrawArrays(GL_TRIANGLES, 4, 6);
        glDrawArrays(GL_TRIANGLE_STRIP, 10, 6);
        glDisableVertexAttribArray(0);
        glDisableVertexAttribArray(1);
        glfwSwapBuffers(window);
        glfwPollEvents();
    } while (glfwGetKey(window, GLFW_KEY_SPACE) != GLFW_PRESS && glfwWindowShouldClose(window) == 0);
}

```

**4.1** Using the graph below, draw the resulting shapes that are produced by this program, as well as indicating what colour each of the shapes will have. You can assume that the shaders do not alter the shapes or colours. 

> 
> **Visual Content:** Graph with axes from -1 to 1 provided in exam paper. 
> 
> 

**4.2** Consider now that the shaders are modified to perform the following tasks: 

* If the vertex has a negative $x$ value, the value should be doubled. 


* If the vertex has a negative $y$ value, the value should be halved. 


* All the colours should be more pastel colours (i.e. more white). This is done by adding 0.5 to each of the colour channels. 



Provide the modified vertex and fragment shaders. Clearly indicate which shader is which. 

---

Question 5 

**5.1** Assume a function `void rotateScene()` has been declared for you, which will rotate the scene. Provide the valid C++ code that will invoke this function when the R key is pressed. You can assume that `GLFWwindow *window` is the GLFWwindow pointer to the active window, and all the required boiler code has been correctly configured. 

**5.2** Assuming that the centre of the scene is located at $[1, 2, 1]^T$, provide the transformation matrices that will allow the following transformations. If multiple matrices are required, provide each matrix as well as the order in which they will need to be multiplied to achieve the desired effect. Provide the matrices as 4D homogeneous matrices. 

* 
**a)** Scaling the scene along all three axes by 3 units. 


* 
**b)** Rotation about the global Z-axis by $40^{\circ}$. 



**5.3** Explain what the purpose of the code statement is: `gl.enable(gl.GL_BLEND)` 

---

Question 6 

**6.1** Consider the following possible conditions for the midpoint algorithm: 

* i) $f(x+1, y+0.5) < 0$ 


* ii) $f(x+1, y-0.5) > 0$ 


* iii) $f(x+0.5, y+1) > 0$ 


* iv) $f(x+0.5, y-1) < 0$ 



State which condition will be best suited for each of the following lines: 

* 
**a)** $g(x) = 5x+2$ 


* 
**b)** $g(x) = -0.2x-5$ 


* 
**c)** $g(x) = 0.2x+8$ 


* 
**d)** $g(x) = -10x$ 



**6.2** During the rasterisation process, complications arise when colouring two connected triangles with a pixel that lies perfectly on the edge between the two triangles. For each of the following solutions to the complications, explain a possible problem that may arise if the solution is used. 

* 
**a)** Blend the colours assigned to a pixel. 


* 
**b)** If the pixel is on the edge, do not give it any colour. 


* 
**c)** Use an offscreen point to determine the colour of the pixel.