Perception
COS 344: L20 Chapter 19: Visual Perception
Cobus Redelinghuys
11/05/2026

Perception Section19.2:VisualSensitivity
- Today we will start and end our “hand-wavy” discussion on
visual perception.
- While covering the work, please think about how this can be
applied to computer graphics rendering scenarios.
- This forms part of the human interaction component of
computer graphics and is based on the study of vision science.

- In computer graphics, we strive for physical realism but it is
not possible due to only looking through a 2D screen.
- The best we can hope for is “perceptually effective”.
Perceptually effective
The ability to have a displayed image perceived as intended.
- This chapter will focus on how humans visually perceive
things, with regard to computer graphics.
- Why is it important that we study this?
Perception Section19.2:VisualSensitivity
Chapter 19: Visual Perception
- During our discussion on Computer Animation, we discussed
the importance of scene staging.
- Who can remember why it was important?

Perception Section19.2:VisualSensitivity
Chapter 19: Visual Perception
- During our discussion on Computer Animation, we discussed
the importance of scene staging.
- Who can remember why it was important?
- In computer graphics, we strive for physical realism but it is
not possible due to only looking through a 2D screen.
- The best we can hope for is “perceptually effective”.
Perceptually effective
The ability to have a displayed image perceived as intended.
- This chapter will focus on how humans visually perceive
things, with regard to computer graphics.
- Why is it important that we study this?

Perception Section19.2:VisualSensitivity
Section 19.1: Visual Science
- Vision produces more useful information about the world than
any other sense ∼Textbook
- This is due to the direct consequences of the physical
properties of light:
- Light travels far
- Light travels at high speed
- Light travels in straight lines*
- Interacts with stuff
- Bounces off things
- Is produced in nature
- Has lots of energy
- In a test, you need to be able to explain how you can leverage
each of these properties to create a scene.

Perception Section19.2:VisualSensitivity
- The textbook discusses a brief history of vision science, which
you do not need to know.
- Just an interesting one:
- Computer science has been used recently to great success in
building computational models of the different vision models
which has led to the success of computer vision.
Purpose of vision according to Vision Science
The process of producing/gathering information about objects,
locations and events in the world from viewed patterns of light
reaching the viewer.

Perception Section19.2:VisualSensitivity
Section 19.2: Visual Sensitivity
- The human vision system is predominantly used to identify
patterns rather than pure light.
- Thus, the eye does not work as a photometer; instead, it
detects and recognises patterns.
- Just focus on the introduction of this section, as the
subsections go into detail that is outside the scope of COS344.

- The visual system has been described as inverse optics.
- Think about how we are rendering scenes so far.
- We describe the objects, their positions, colours, etc to form a
scene.
- This is all geometric properties.
- Our vision system does the reverse.
- Takes in a scene and “produces” the geometric properties.
GeometricProperties Examplesofcues
Perception
Section 19.3: Spatial Vision
- One of the critical operations performed by the visual system,
is the estimation of geometric properties of the visible
environment.
- What kind of properties are there?

GeometricProperties Examplesofcues
Perception
Section 19.3: Spatial Vision
- One of the critical operations performed by the visual system,
is the estimation of geometric properties of the visible
environment.
- What kind of properties are there?
- The visual system has been described as inverse optics.
- Think about how we are rendering scenes so far.
- We describe the objects, their positions, colours, etc to form a
scene.
- This is all geometric properties.
- Our vision system does the reverse.
- Takes in a scene and “produces” the geometric properties.

- Our eyes only see objects in the environment that have some
level of light touching them.
- How does the brightness of a scene affect the visual
perception of the scene?
Surface layout
The location and orientation of visible surfaces in the environment
- How is the surface layout used by humans in real life and
when looking at computer rendering?
- In a computer rendering, how can visual cues be used to add
context to the rendering?
GeometricProperties Examplesofcues
Perception
- What role does light play in this?

Surface layout
The location and orientation of visible surfaces in the environment
- How is the surface layout used by humans in real life and
when looking at computer rendering?
- In a computer rendering, how can visual cues be used to add
context to the rendering?
GeometricProperties Examplesofcues
Perception
- What role does light play in this?
- Our eyes only see objects in the environment that have some
level of light touching them.
- How does the brightness of a scene affect the visual
perception of the scene?

- In a computer rendering, how can visual cues be used to add
context to the rendering?
GeometricProperties Examplesofcues
Perception
- What role does light play in this?
- Our eyes only see objects in the environment that have some
level of light touching them.
- How does the brightness of a scene affect the visual
perception of the scene?
Surface layout
The location and orientation of visible surfaces in the environment
- How is the surface layout used by humans in real life and
when looking at computer rendering?

GeometricProperties Examplesofcues
Perception
- What role does light play in this?
- Our eyes only see objects in the environment that have some
level of light touching them.
- How does the brightness of a scene affect the visual
perception of the scene?
Surface layout
The location and orientation of visible surfaces in the environment
- How is the surface layout used by humans in real life and
when looking at computer rendering?
- In a computer rendering, how can visual cues be used to add
context to the rendering?

GeometricProperties Examplesofcues
Perception
- Visual cues are categorized into four categories:
Ocularmotor cues
Involves information about the position and focus of the eye.
Disparity cues
Involves information extracted from viewing the same surface point with
two eyes, beyond that available just from the positioning of the eyes.
Motion cues
Provides information about the world that arises from either the
movement of the observer, or the movement of objects.
Pictorial cues
The result of the process of projecting 3D surface shapes onto a 2D
pattern of light that falls on the retina.

- Why is the measurement scale important, for example, in the
homework assignment?
- Types of reference representations:
Egocentric
Defined with respect to the viewer’s body.
Allocentric/exocentric
Defined with respect to something external to the viewer
- The remaining subsections in Section 19.3 have an in-depth
discussion of the different cues, which is again, outside of our
scope as it tends toward the theory of visual sciences.
GeometricProperties Examplesofcues
Perception
- Why is it important to have a point of reference in your
rendering?

- Types of reference representations:
Egocentric
Defined with respect to the viewer’s body.
Allocentric/exocentric
Defined with respect to something external to the viewer
- The remaining subsections in Section 19.3 have an in-depth
discussion of the different cues, which is again, outside of our
scope as it tends toward the theory of visual sciences.
GeometricProperties Examplesofcues
Perception
- Why is it important to have a point of reference in your
rendering?
- Why is the measurement scale important, for example, in the
homework assignment?

GeometricProperties Examplesofcues
Perception
- Why is it important to have a point of reference in your
rendering?
- Why is the measurement scale important, for example, in the
homework assignment?
- Types of reference representations:
Egocentric
Defined with respect to the viewer’s body.
Allocentric/exocentric
Defined with respect to something external to the viewer
- The remaining subsections in Section 19.3 have an in-depth
discussion of the different cues, which is again, outside of our
scope as it tends toward the theory of visual sciences.

GeometricProperties Examplesofcues
Perception
Examples of cues - Ocularmotor cue
- Example is the motion parallax.
- Motion parallax is a depth cue where objects that are closer,
appear to move faster than objects that are far away.
- https://www.youtube.com/watch?v=SlOxwtR-WV0
- This can also be an example of what other category of cue?

GeometricProperties Examplesofcues
Perception
Examples of cues - Disparity cues
- Example is Virtual Reality (VR).
- VR systems use headsets with built-in displays for each eye.
By tracking the user’s head movements and adjusting the
images displayed to each eye accordingly, VR provides a
realistic sense of depth and immersion.

GeometricProperties Examplesofcues
Perception
Examples of cues - Pictorial cues
- Example is Perspective/Orthographic viewing.
https:
Lectures/Figures/Angel5EjpegChap05/AN05F03.jpg

GeometricProperties Examplesofcues
Perception
Section 19.4: Objects, Locations, and Events
- In the field of vision science there is a big debate about how
exactly this interpretation of the scene is done.
- Vision scientists know how the human brain perceives speed
and heading when moving through the world but, little is
known about the perception of events.
- Visual attention involves the perception of aspects of:
- Objects
- Locations
- Events

GeometricProperties Examplesofcues
Perception
Section 19.4.1: Object Recognition
Object Recognition
Process that involves segregating an image into constituent parts
corresponding to distinct physical entities and determining the
identity of those entities.
- Object recognition consists of two distinct steps:
1. Organizing the visual field into groupings likely to correspond
to objects and surfaces.
2. Interpretation of grouped objects.
- Let’s say for example we are rendering a house but each wall
is about 5 m way from the joining wall. Given the two steps
outlined above what could the possible problem be?

- Say, for example, you want to introduce a new important class
of foreign objects in your render. How would you do it?
GeometricProperties Examplesofcues
Perception
- Our brain ”interprets” recognised objects into descriptions.
- Three general types of object descriptions are:
- Templates:
- Represents object classes in terms of example views of objects
in each class.
- Structural descriptions:
- Represents object classes in terms of unique features of each
class, which are likely to be easily detected in views of objects.
- Invariant features:
- Describe classes of objects in terms of more generic geometric
properties, which are likely to be insensitive to different views
of objects.

GeometricProperties Examplesofcues
Perception
- Our brain ”interprets” recognised objects into descriptions.
- Three general types of object descriptions are:
- Templates:
- Represents object classes in terms of example views of objects
in each class.
- Structural descriptions:
- Represents object classes in terms of unique features of each
class, which are likely to be easily detected in views of objects.
- Invariant features:
- Describe classes of objects in terms of more generic geometric
properties, which are likely to be insensitive to different views
of objects.
- Say, for example, you want to introduce a new important class
of foreign objects in your render. How would you do it?

GeometricProperties Examplesofcues
Perception
Section 19.4.2: Size and Distance
- When there is a lack of a concrete depth scale, objects that
are closer appear to be larger.
- This is called relative size.
- Another depth cue is familiar size,
Familiar Size
A depth cue which uses previous knowledge of objects to
determine their size.
- Familiar size cues are often used in funhouses to create weird
illusions.

GeometricProperties Examplesofcues
Perception
Section 19.4.3 is skipped as it is outside the scope of COS344.

Perception
Section 19.5: Picture Perception
- Up until now, in our discussion of the chapter, we have only
focused on the real world, but tried to apply it to computer
graphics.
- In this section, we will look at how 2D pictures (from a
screen) are depicted
- Looking at rendered images as opposed to the real-world has
some perceptual implications.
- In theory, it should be possible to generate a computer
graphics render that appears indistinguishable from the real
world
- Basically, we are looking at the world through a glass window.
- Problem for computer graphics and other visual arts is that
the real world cannot really be captured onto a flat surface.

- Visual, depth, and perspective cues are compressed, elongated
or distorted.
- The human brain can account for this slightly:
- For example, sitting at different seats in a movie house, we still
see the picture ”approximately” correctly.
Perception
- If we render something using perspective projection the
following is implied:
- There is a specific view-point specified as a position and
direction in model space.
- There is a view frustum which is specified by:
- vertical field of view
- horizontal field of view
- several boundaries
- What would be the problem if we then don’t view the
rendering from the specified viewpoint?

Perception
- If we render something using perspective projection the
following is implied:
- There is a specific view-point specified as a position and
direction in model space.
- There is a view frustum which is specified by:
- vertical field of view
- horizontal field of view
- several boundaries
- What would be the problem if we then don’t view the
rendering from the specified viewpoint?
- Visual, depth, and perspective cues are compressed, elongated
or distorted.
- The human brain can account for this slightly:
- For example, sitting at different seats in a movie house, we still
see the picture ”approximately” correctly.

Perception
