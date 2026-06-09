ASSIMP, Blender
and you
Tristan Potgieter

By the end of this lecture, you should know:
● Basic shader debugging
○ RenderDoc
● How to export a model from Blender.
○ Basic UV unwrapping
○ Texture Baking
○ Asset file types
● How to configure an asset importer to work with OpenGL
○ Downloading Assimp
○ Creating and using an Assimp instance

Does any of this look familiar?

Manual Vertex Specification is painful!
Buzz had approximately 30k faces before the model was subdivided.
Most of it was in the face so that it would look smooth enough.
Digital Animation was difficult. No tools like rigging. Everything was a
slider.
Eben Ostby capturing vertex positions of Buzz
Lightyear’s face for “Toy Story” (1995)

Nowadays it's way easier
3d modelling software has made creating objects
(relatively) more intuitive.
Hardware and software improvements mean
performance is far more forgiving.
Retopology is now a permanent part of the asset
creation pipeline.
Official Capture of the Hi-Poly sculpt for ‘Tracer’ from the 2016 game
“Overwatch”. The in game version runs with around 30k faces. This
sculpt probably has more than 1 million faces.

There is a catch…
Most of the biggest/most successful video games or renderers use custom engines that use different APIs.
Engine: Engine: Engine:
Proprietary Divinity Lightweight
in house Engine 4.0 Java Game
engine Library
Graphics Graphics Graphics
API: API: API:
DirectX 11 Vulkan OpenGL
Graphics APIs by themselves don’t know what to do with 3D Assets!

Asset importers!

ASSIMP
As far as I know, ASSIMP (Open Asset Import Library) is
the only “Plug and play” library around for asset
importing.
Every other is either proprietary, too obscure to be
found, or too buggy to be useful.
Most game dev studios that build their own engines also
build their own asset importers.
This is slowly changing however.
Gadot Engine, an open source competitor to Unreal
Engine and Unity Engine, uses Assimp!

Just some clarification
● This is NOT a 3D modeling lecture
○ There are plenty of tutorials out there that will explain the basics of
Blender better than me.
○ 3D modeling is not something I can explain adequately in a single
lecture.
○ I will cover the major points that are relevant to exporting your model.
● You are not required to use ASSIMP or Blender for your
Homework Assignment
○ Consider this as an extra tidbit of knowledge to hold onto.
○ However, spending some time to learn these tools will make your
Homework Assignment go a lot quicker.
○ That is time you can spend on other subjects… like COS 332 and COS
301 If you know where this doughnut is
● Assimp is designed around workflows from industry from then you are already on the right
track
○ Do not be surprised if you have to do some restructuring to
accommodate for it.

First, an introduction to RenderDoc
RenderDoc is an open source Graphics debugger
released in 2014.
It allows you to capture a single frame of your render,
and then analyse the graphics pipeline that produced
that frame.
Key things to note:
● It’s user interface is structured in a way that
lines up with how you have been taught the
graphics pipeline.
● It allows you to check what data is being
inputted to you shaders.
● It allows you to modify your shaders on the fly
to see how it affects your renders.

Quick Demo!

Lets hop into Blender then

So, you have a beautifully
designed 3D model! Now
what?
Before exporting, we need to know what format we are exporting to.
There are several formats we can export to:
● .OBJ Wavefront
○ Simple, human-readable format
○ Great if you are only interested in using blender for coordinate
mapping
○ Lacks support for modern texture workflows
○ Can be very slow for modern polycounts (> 30k)
● .FBX Filmbox
○ Slightly more modern and better supported (Is developed by
Autodesk)
○ Much faster than OBJ
○ Not human readable
○ Designed for transfer between 3D tools.
○ Still can be slow
● .gltf 2.0
○ Modern open source file format
○ Designed for modern texture workflows
○ Designed for web based projects. Small file sizes and extremely
fast!
○ Not human readable
I advise you use .gltf.

Lets check if we have
GLTF 2.0 installed
Edit > Preferences > Addons > GLTF

Check the model is enclosed and has no loose
geometry.
Not as big of an issue, but is still good practice.
An open mesh will still render, but may produces
unexpected results when viewing from different angles.
To check that your mesh is enclosed, follow these steps:
● Go into edit mode
● Press 3 to go into face select mode
● Press A
● Select > Select Loops > Select Boundary Loop
● If any vertices become highlighted, you’re mesh is
not enclosed!

Checking UVs are unwrapped
UV unwrapping is something that should be done once you have
finished modeling.
Blender’s automatic UV unwrapper should be adequate for what
you will do for your assignment.

Baking Procedural Textures
Pay attention! I’m only going to cover this briefly.
Things to remember:
● You have to give Blender a target image to send the Baked textures to.
● Lower your samples unless you want to melt your GPU

Now we can actually export
Since we are exporting in gltf, we go file > export > gltf 2.0
Then just have the export setting as you see there.
If you choose to export as a .OBJ, the process is quite
similar. Some config settings might be different.

Back to OpenGL
In order to use ASSIMP:
● Organized VAO VBO and EBO into separate classes.
● Have defined classes for the following:
○ Mesh
○ Model
○ Shader
○ Camera
I’m also assuming you have at the very least entertained the idea of adding textures to your
scenes, so you have started exploring the ways to do that.

Installing Assimp
I lied when I said Assimp was plug-and-play.
You actually need to download the source and compile it on your machine using cmake. Then
you have to use Visual Studio to turn it into a usable c++ library on your machine.
This means if you want to use Assimp comfortably, you will have to write and compile an
OpenGL program locally on Windows.
No WSL or Docker Containers.

Importing a I am going to walk through my code and show
how I did it. It should work for you but keep in
model into
mind that I had a bit more time to figure this all
out.
OpenGL
Don’t worry if it doesn’t click that easily.
This will also be demoed

A little caveat about Assimp’s scene structure
Assimp when it imports a model uses a Tree-like structure to map the scene. Each Node is linked
to a root node called the “Scene root”.
● There are many different types of nodes that can be linked to this scene node.
● For our purposes, we are looking at Mesh nodes.
● These nodes then have child nodes which link to other related resources (Textures, bones
etc.)

The loadModel and processNode function
Both classes are in the model class.
LoadModel parses the passed in asset file into a Assimp Tree structure. This is stored in a Assimp
data type called aiScene.
The first invocation of processNode has the root of the tree passed in with the scene data type.
processNode in my implementation only checks for meshes connected to the node.

Process Mesh
This function includes some texture and UV processing, which you have not covered in
lectures yet, so I will only point them out.
Here, we are collecting all the vertices in this mesh node into a vertex array, much like what you
have been doing manually.
We also store the normal in a similar struct.
We also store the indices so OpenGL knows which order to use vertices when drawing triangles.

Questions?
