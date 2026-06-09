COS 344: L17 Chapter 22: Computer Graphics
in Games
Cobus Redelinghuys
20/04/2026

- In this chapter, we will look at the specific considerations that
apply to graphics in games.
- https://www.youtube.com/watch?v=HcMm6TJoYL0
- Computer games have been and still are the major motivation
in improvements made in Computer Graphics.
- Why?

- Computer games have been and still are the major motivation
in improvements made in Computer Graphics.
- Why?
- In this chapter, we will look at the specific considerations that
apply to graphics in games.
- https://www.youtube.com/watch?v=HcMm6TJoYL0

- In the past games were designed for a single platform.
- Nowadays games are developed to be multiplatform.
- Why this change?
Platform
For this chapter platform refers to a specific combination of
hardware, operating system, and API for which the game is
designed.
- Games run on a large range of platforms.
- Examples?

Platform
For this chapter platform refers to a specific combination of
hardware, operating system, and API for which the game is
designed.
- Games run on a large range of platforms.
- Examples?
- In the past games were designed for a single platform.
- Nowadays games are developed to be multiplatform.
- Why this change?

09/types-of-gaming-platforms.webp

- On Windows specifically, the use of abstracted APIs has been
the main reason old games are still able to “run” on modern
platforms.
- Why do computer games have a graphics settings tab?
- This allows for the scaling of the graphics requirements such
that the game is able to run on a wider range of platforms
with different computing power capabilities.
- It is also possible that the computing power of a platform is
too weak to be able to play the game at its lowest setting,
which is why minimum requirements for games are released
with the game.
- Games need to be able to run on platforms that were not yet
developed when the game was designed.
- Examples?

- This allows for the scaling of the graphics requirements such
that the game is able to run on a wider range of platforms
with different computing power capabilities.
- It is also possible that the computing power of a platform is
too weak to be able to play the game at its lowest setting,
which is why minimum requirements for games are released
with the game.
- Games need to be able to run on platforms that were not yet
developed when the game was designed.
- Examples?
- On Windows specifically, the use of abstracted APIs has been
the main reason old games are still able to “run” on modern
platforms.
- Why do computer games have a graphics settings tab?

- Games need to be able to run on platforms that were not yet
developed when the game was designed.
- Examples?
- On Windows specifically, the use of abstracted APIs has been
the main reason old games are still able to “run” on modern
platforms.
- Why do computer games have a graphics settings tab?
- This allows for the scaling of the graphics requirements such
that the game is able to run on a wider range of platforms
with different computing power capabilities.
- It is also possible that the computing power of a platform is
too weak to be able to play the game at its lowest setting,
which is why minimum requirements for games are released
with the game.

https:

- Yet developing for console platforms is not a breeze in the
park either, why?
- Console APIs are less abstract and closer to the actual
hardware implementations.
- It can be argued that multiplatform game development is the
hardest of all the development options.
- - - - Why are console platforms easier to develop for, as compared
to PC platforms?

- Console APIs are less abstract and closer to the actual
hardware implementations.
- It can be argued that multiplatform game development is the
hardest of all the development options.
- - - - Why are console platforms easier to develop for, as compared
to PC platforms?
- Yet developing for console platforms is not a breeze in the
park either, why?

- Why are console platforms easier to develop for, as compared
to PC platforms?
- Yet developing for console platforms is not a breeze in the
park either, why?
- Console APIs are less abstract and closer to the actual
hardware implementations.
- It can be argued that multiplatform game development is the
hardest of all the development options.

09/types-of-gaming-platformsC.OwSe3b44p:L17Chapter22:ComputerGraphicsinGames

- Thus browser-based games need to be able to run on a wider
range of platforms than say a multi-platform game.
- Browser-based games also need to operate with less
computing power as not all platforms with browsers have a
GPU for example.
- Often times games developed for these platforms are designed
on the weakest common denominator in the range of possible
platform configurations.
- Example: https://chromedino.com/
- Browser-based virtual machines such as Adobe Flash are an
interesting class of platform.
- What are all the platforms a browser can use?

- Browser-based virtual machines such as Adobe Flash are an
interesting class of platform.
- What are all the platforms a browser can use?
- Thus browser-based games need to be able to run on a wider
range of platforms than say a multi-platform game.
- Browser-based games also need to operate with less
computing power as not all platforms with browsers have a
GPU for example.
- Often times games developed for these platforms are designed
on the weakest common denominator in the range of possible
platform configurations.
- Example: https://chromedino.com/

- The platform used has a great influence in the overall
experience of the user.
- PC users may use keyboard and mouse.
- Console typically uses controllers.
- Other examples?

08/Set-Up-Flight-Simulator-Airbus-Cockpit.jpg

- A major problem for computer graphics programmers is the
management of limited resources.
- These limited resources include:
- Hardware:
- Processing time
- Storage
- Memory bandwidth
- Development resources:
- Developers
- Artists
- Game designers with limited time
- The remainder of the section is left as self-study.

- Due to the limited resources always being a constant problem,
various optimisation techniques have been developed.
- Pixel shader process is the primary bottleneck.
- Most GPUs contain hierarchical depth-culling hardware, which
can avoid executing pixel shaders on occluded surfaces.
- Thus, which type of culling is this?
- To fully utilise this hardware, opaque objects can be rendered
back-to-front.
- An alternative is to perform a depth prepass.
Depth prepass
Rendering all the opaque objects into the depth buffer (without any
colour output or pixel shaders) before rendering the scene normally.
- Why optimise?

- To fully utilise this hardware, opaque objects can be rendered
back-to-front.
- An alternative is to perform a depth prepass.
Depth prepass
Rendering all the opaque objects into the depth buffer (without any
colour output or pixel shaders) before rendering the scene normally.
- Why optimise?
- Due to the limited resources always being a constant problem,
various optimisation techniques have been developed.
- Pixel shader process is the primary bottleneck.
- Most GPUs contain hierarchical depth-culling hardware, which
can avoid executing pixel shaders on occluded surfaces.
- Thus, which type of culling is this?

- Why optimise?
- Due to the limited resources always being a constant problem,
various optimisation techniques have been developed.
- Pixel shader process is the primary bottleneck.
- Most GPUs contain hierarchical depth-culling hardware, which
can avoid executing pixel shaders on occluded surfaces.
- Thus, which type of culling is this?
- To fully utilise this hardware, opaque objects can be rendered
back-to-front.
- An alternative is to perform a depth prepass.
Depth prepass
Rendering all the opaque objects into the depth buffer (without any
colour output or pixel shaders) before rendering the scene normally.

- Thus, any method that can help perform occlusion culling
early can be beneficial.
- This saves on the aspects:
- Pixel processing
- Vertex processing
- CPU time
- View frustum culling is universally employed, but is often not
enough.
- High-level occlusion culling algorithms often use data
structures like Potentially Visible Sets (PVS) or Binary Spatial
Partitioning (BSP) trees to quickly determine a set of visible
objects.
- “The fastest way to render an object is to not render it at all”

- “The fastest way to render an object is to not render it at all”
- Thus, any method that can help perform occlusion culling
early can be beneficial.
- This saves on the aspects:
- Pixel processing
- Vertex processing
- CPU time
- View frustum culling is universally employed, but is often not
enough.
- High-level occlusion culling algorithms often use data
structures like Potentially Visible Sets (PVS) or Binary Spatial
Partitioning (BSP) trees to quickly determine a set of visible
objects.

- Level-of-detail algorithms render different representations of
an object based on distance or other factors such as:
- Importance
- Screen coverage
- Another option is to perform optimisation before the game
even starts.
- The result of this preprocessing can be stored and just recalled
when needed during runtime.
- What if an object can be seen but is at such a far distance
that finer details are not identifiable?

- What if an object can be seen but is at such a far distance
that finer details are not identifiable?
- Level-of-detail algorithms render different representations of
an object based on distance or other factors such as:
- Importance
- Screen coverage
- Another option is to perform optimisation before the game
even starts.
- The result of this preprocessing can be stored and just recalled
when needed during runtime.

- https://www.youtube.com/watch?v=IsPPWWlV-T8
- This concludes our brief discussion on Computer Graphics in
Games
- The remainder of the chapter can be omitted.

Playing a game
- Replicube
- Marbles on Stream
