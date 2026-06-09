This is a fantastic approach to studying. Analyzing the *anatomy* of an examiner’s tests is often more effective than just memorizing the content. Based on the two COS 344 semester tests provided, your lecturer has a very specific, consistent, and rigorous testing style.

Here is an in-depth analytical breakdown of the test formats, question archetypes, and thematic structures to help you build highly accurate mock tests.

---

### I. Overall Test Structure and Format

The tests are meticulously structured to move from lower-order thinking (recall) to higher-order thinking (synthesis and application).

* **Length & Pacing:** Tests are generally out of ~50-60 marks (ST1 is ~60, ST2 is ~51), designed to be completed in a standard test period.
* 
**The "Global Scenario" (Crucial for ST2):** In Test 2, the examiner introduces a single overarching scenario at the very beginning (e.g., "a 3D glass panel on a tiled floor with a light shining through"). Subsequent questions (projections, matrices, texture mapping, culling) constantly refer back to this scenario.


* **The "Motivation" Rule:** The examiner is ruthless about justifications. Across multiple questions, there is an explicit warning: *"Note: No marks will be awarded if no motivation is given"*. Guessing is entirely neutralized.



---

### II. Core Question Archetypes

If you are writing your own mock tests, you must include the following specific question styles:

#### 1. The "Select All That Apply" Nuanced MCQ (Usually Q1)

* **Format:** Multiple choice, but with a twist. The prompt explicitly states: *"Selecting more than one answer, unless specified differently, will result in no marks being awarded"*. However, the options themselves often contain combinations (e.g., "A. i, ii", "D. i, ii, iv").


* 
**What it tests:** Precise definitions, matrix identifications, and tooling knowledge (e.g., knowing ASSIMP vs. RenderDoc).



#### 2. The Visual Annotation / Graphing Problem

* **Format:** The student is given a visual aid and must physically draw the answer on it.
* 
**Examples:** * Plotting vertices and determining the shape/color based on `GL_TRIANGLE_FAN` or `GL_TRIANGLE_STRIP` code.


* Drawing "X"s on a side-profile diagram to indicate which faces/objects are eliminated during Viewvolume, Occlusion, or Backface culling.





#### 3. The "Matrix Pipeline" Derivation

* 
**Format:** The student is given a starting coordinate and an end goal (e.g., "Scale by 3, then rotate by 40 degrees around the global Z-axis," or "Create the orthographic projection matrices").


* **What it requires:** Students cannot just give the final matrix. They must provide the individual 4D homogeneous matrices ($T_1$, $S$, $R$, $T_2$) and state the exact order of multiplication (e.g., $M = T_2 \cdot R \cdot T_1$).



#### 4. The Shader / OpenGL Code Injection

* **Format:** The examiner gives a base program or specific constraints and asks the student to write the GLSL shader code or C++ OpenGL API calls.
* 
**Examples:** * "Write a vertex shader that doubles the x-value if it's negative".


* "Provide the C++ code to enable front-face culling with clockwise winding".




* 
**What it tests:** Memorization of API constants (`GL_CULL_FACE`, `GL_CW`) and understanding of GLSL syntax (`layout`, `in`/`out`, `vec4` for `gl_Position`).



#### 5. Algorithm & Constraint Tracing

* **Format:** Testing the mathematical rules behind rendering algorithms.
* 
**Examples:** * Evaluating Midpoint line algorithm conditions against specific linear equations ($g(x) = 5x + 2$).


* Testing 3D meshes against Strict vs. Relaxed Manifold rules by providing sets of vertex indices.





---

### III. Thematic Weighting & Content Focus

Based on the memos, here is what the examiner cares about most:

* 
**The Math is Non-Negotiable:** You must understand homogeneous coordinates, dot/cross products (used heavily in the camera matrix calculation), and matrix transformations.


* **The Graphics Pipeline is Central:** There is a heavy focus on knowing exactly *where* data goes. From importing an OBJ file, to vertex generation, to shading, to the difference between image-order (ray tracing) and object-order (rasterization).


* **Edge Cases & Artifacts:** The examiner loves asking *what goes wrong*. For example: "What happens if you blend colors on a shared edge?" (Answer: noticeable artifact lines) , or "Why does modulus create texture distortion?" (Answer: discrete jumps) .



---

### IV. Blueprint for Generating Your Mock Tests

To create a highly accurate mock test, use this exact template:

1. **Start with a Scenario:** Invent a specific scene. Example: *"A glowing, rotating 3D pyramid inside a foggy, mirrored room."*
2. **Question 1 (MCQs - 10 marks):** Write 5-8 multiple-choice questions. Include 3D matrix math (give a transformation matrix and ask what it does), tool questions (e.g., What does Glad do?), and ray equation variations.
3. **Question 2 (Conceptual - 5 marks):** Ask a True/False question about the pipeline and demand a motivation. Pick a rendering artifact (like Z-fighting or texture aliasing) and ask them to explain the cause.
4. **Question 3 (The Matrix Problem - 10 marks):** Give the student an arbitrary "center" point for your scenario object. Ask them to scale it, shear it, and rotate it, demanding all 4D matrices and the final equation.
5. **Question 4 (The Visual Problem - 10 marks):** Provide a side-profile diagram of your scene. Ask them to manually cross out faces culled by backface vs. view-volume culling.
6. **Question 5 (The Code Problem - 15 marks):** Ask them to write a custom Fragment Shader that changes the object's color based on its $Y$ height (e.g., gradient from blue to red), followed by the C++ code to bind that buffer.

Which specific topic (e.g., Matrix Transformations, Shaders, Ray Tracing, Culling) do you want to start building mock questions for first?