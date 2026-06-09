COS 344: L19 Chapter 16: Computer Animation
Cobus Redelinghuys
11/05/2026

- Where does the term “animation” come from?
- Latin word anima which means: the act, process, or result of
imparting life, interest, spirit, motion, or activity.
- Traditional animation (animation without the use of a
computer) is very time-consuming, why?
- Computers have been used as more than just a tool to aid
animators:
- Modern modelling software makes is easy to create detailed 3d
models.
- Renderingalgorithmscanproduceawiderangeofappearances.
- Powerful numerical simulation algorithms can produce
physics-based motion for objects.
- Motion capture systems can capture real life motion which can
then be used.

- The use cases listed on the previous slide, led to an increased
use of computer animation in the following fields:
- Motion pictures
- Commercials
- Automotive design
- Architecture
- Medicine
- Scientific research
- And many others.
- New domains also appeared, like:
- Fully computer-animated feature films
- Virtual/Augmented reality systems
- Computer Games
- Why is it important for computer graphics students to
understand some of the ideas behind computer animations?

Several computer animation approaches exist, including:
Key-framing
The process where an animator provides the necessary data for select
moments in time and the computer fills in the rest.
Procedural
The process of using specially designed, often empirical, mathematical
functions and procedures whose output resembles some particular motion.
Physics-based
Techniques solve differential equations of motion.
Motion capture
Use of specialised equipment or techniques to record real-world motion,
and then transfer this motion into that of a computer model.

- In 1987 John Lasster defined the following twelve principles of
computer animation:
1. Squash and stretch 7. Arcs
2. Timing 8. Secondary action
3. Anticipation 9. Straight-ahead and
Pose-to-pose action
4. Follow through and overlapping
action 10. Exaggeration
5. Slow-in and slow-out 11. Solid drawing skill
6. Staging 12. Appeal
- In computer animation, the balance of control and flexibility
given to the animator, is vital to take full advantage of the
computer’s abilities.
- We will only focus on a select few of these principles.

Section 16.1.1: Timing
- Why would we need to consider the speed of
animation/timing?
- Let’s assume a character moves their head from left to right.
How can the speed of the rotation affect the “visual
perception” of what the character is doing?
- How can the weight of an object be represented by the speed
of the animation?

Section 16.1.2: Action Layout
- For obvious reasons, it should be clear to the viewer what you
are trying to render.
- Ideal scene staging should lead the viewer’s eye to where they
should look, to effectively convey what you are trying to
render.
- An action can be split into three components:
- Anticipation
- Preparation for the action
- Action itself
- Follow through
- Termination of the action.
- Test question: Given a certain scene, like a soccer penalty
kick, describe each of these components.

Section 16.1.3: Animation Techniques
- Good animation
techniques are required
to make the render
appear more realistic.
- The most important
technique is probably
squash and stretch.
- What can be represented
by squashing the object
and what can be
represented by stretching
the object?

- Straight ahead action, is
when each frame of the
animation is drawn or
plotted by the animator.
- Key framing or
pose-to-pose action, is
when animations are
planned through a series
of relatively sparsely
spaced key frames with
the rest of the frames
completed by the
computer.

Section 16.1.4: Animator Control vs Automatic Methods
- In animations in computer graphics, there is a trade-off:
- Having the animator/programmer plot and plan each frame in
the animation by hand means having more control over the
animation.
- Or relying on automatic processes and procedures by tweaking
input parameters means having little to no control over the
finer details of the animation.
- For example, in a rotation, we can either manually plot out
each point of the rotation, or we can use a matrix to
automatically rotate it for us.

Section 16.2: Key-framing
- The term key-framing is a bit misleading for computer graphics, as
defined so far.
- In OpenGL, we do not have images that we display but rather a
scene defined by different geometric entities, expressed by
mathematical machinery.
- This includes:
- Colours expressed in RGB
- Vertices expressed in 3D
- Camera positions and alignment.
- etc.
- A naive solution is to hard-code the different numerical values for an
animation. This is inefficient. Why?
- You do not need to know the mathematical idea behind key-framing
and curve fitting, just the basic ideas of what key-framing is.

Section 16.3: Deformations
- Examples of an operation that changes an object’s shape?
- Non-uniform scaling.
- We can describe a deformation of a shape as follows:
p′
= f(p,γ)
Where:
- p is the original shape.
- p′ is the new shape.
- γ is a vector of parameters that describes how the object is
deformed.
- Using different f’s we can create interesting formations for
objects.

- Two disadvantages:
1. Choosing the function f.
2. The deformation is applied to the entire object and not a small
part of the object.
- To overcome this, we can choose a single vertex, move it and
adjust the vertices within some neighbourhood to follow the
seed vertex.
- This displacement is controlled by an attenuation function
which decreases with distance from the seed vertex.
- We can thus key-frame the seed vertex’s motion and use the
attenuation function to move the remaining vertices.
- We will skip over free-form deformations.

Section 16.4: Character Animation
- When animating characters, we often need to make use of two
layers:
- Skin:
- Highly detailed surface representing the outer shell of the
character.
- What can we use to create this highly detailed outer shell?
- Skeleton:
- Hierarchical structure (a tree) of joints which provides a
kinematic model of the figure and is used exclusively for
animation.

Note the joint hierarchy

978-3-319-14418-4_14

- Assume we have a local transformation matrix, which relates a
joint to its parent.
- How can we use this fact and the hierarchy of joints to obtain
the world space transformation matrix of any joint?
- Using DFT, we move down the tree and multiply the current
transformation matrix with the stored local one.
- Pass this new matrix onto the next joint down the hierarchy
and repeat the process.
- This is known as Forward Kinematics (FK).

- Why can’t we just use the hierarchy to figure this out for us
and just specify the ends of the joint chain that we want to
transform?
- This is known as inverse kinematics (IK).
- In FK, the animator/programmer needs to specify a set of
parameters for each joint in the joint chain, such that it looks
natural and flows.
- This is inefficient, why?

- This is known as inverse kinematics (IK).
- In FK, the animator/programmer needs to specify a set of
parameters for each joint in the joint chain, such that it looks
natural and flows.
- This is inefficient, why?
- Why can’t we just use the hierarchy to figure this out for us
and just specify the ends of the joint chain that we want to
transform?

- In FK, the animator/programmer needs to specify a set of
parameters for each joint in the joint chain, such that it looks
natural and flows.
- This is inefficient, why?
- Why can’t we just use the hierarchy to figure this out for us
and just specify the ends of the joint chain that we want to
transform?
- This is known as inverse kinematics (IK).

0-S0952197623004852-gr2.jpg
- - Note, just understand the main difference between FK and IK.
The exact calculations of IK do not need to be known.

- Theskinundergoesaspecialtypeofdeformation.
- Skinisthusattachedtotheskeletonbyassigningeachskinvertex:
Rigid skinning
Theskinisfrozenatafixedlocalpositiontoaspecificjoint,whichiseitherthe
closest,orchosenbytheuserandismostlyusedformuscleactionorbreathing.
Smooth skinning
Multiplevertices(displacementvectors)caninfluencethesameskinpositionusinga
setofweightstoachieveasmootheranimation.
- Wecancalculatetheeffectthatthedisplacementvectors,d,hasontheskinby
usingtheformula:

d= ωidi
where:
- ω is the weight associated with the ith displacement vector.
i
- d is the ith displacement vector.
i
- Whathappenstotheskinwhentheskeletonchanges?

- Whathappenstotheskinwhentheskeletonchanges?
- Theskinundergoesaspecialtypeofdeformation.
- Skinisthusattachedtotheskeletonbyassigningeachskinvertex:
Rigid skinning
Theskinisfrozenatafixedlocalpositiontoaspecificjoint,whichiseitherthe
closest,orchosenbytheuserandismostlyusedformuscleactionorbreathing.
Smooth skinning
Multiplevertices(displacementvectors)caninfluencethesameskinpositionusinga
setofweightstoachieveasmootheranimation.
- Wecancalculatetheeffectthatthedisplacementvectors,d,hasontheskinby
usingtheformula:

d= ωidi
where:
- ω is the weight associated with the ith displacement vector.
i
- d is the ith displacement vector.
i

- The remaining sections of Sections 16.4 are outside of the
focus of COS344 and will be skipped.
- Section 16.5 is also skipped due to the high dependency on
differential equations and partial derivatives.

- Physics-based approaches are a special subset of these
functions.
- If we only care about the final result, we can reduce the
complexities introduced in the physics-based approach.
- For example:
- If we want to create the waves on the surface of a lake, we can
just use the well-defined wave function.
- We can just randomise the properties of the wave and create
multiple waves to create a realistic effect of waves on the lake.
- https://www.youtube.com/watch?v=SJSSsItuR0Y
Section 16.6: Procedural Techniques
- Would it not be nice, if we could just have some function f
that does the exact desired motion for us?

Section 16.6: Procedural Techniques
- Would it not be nice, if we could just have some function f
that does the exact desired motion for us?
- Physics-based approaches are a special subset of these
functions.
- If we only care about the final result, we can reduce the
complexities introduced in the physics-based approach.
- For example:
- If we want to create the waves on the surface of a lake, we can
just use the well-defined wave function.
- We can just randomise the properties of the wave and create
multiple waves to create a realistic effect of waves on the lake.
- - We have only been considering a single object.
- How can we work with multiple objects that we would like to
animate together?
- We could simply apply the methods discussed so far, or even
AI.
- Interestingly, the larger the group of objects get, the smaller
the “intelligence” is needed to get them to appear as a group.
- Flocking is one technique and comes from the behaviour of
birds when they fly together.
- Flocking can also be used for other types of animals.
Examples?
Section 16.7: Groups of Objects
- What have we not addressed so far?

- We could simply apply the methods discussed so far, or even
AI.
- Interestingly, the larger the group of objects get, the smaller
the “intelligence” is needed to get them to appear as a group.
- Flocking is one technique and comes from the behaviour of
birds when they fly together.
- Flocking can also be used for other types of animals.
Examples?
Section 16.7: Groups of Objects
- What have we not addressed so far?
- We have only been considering a single object.
- How can we work with multiple objects that we would like to
animate together?

Section 16.7: Groups of Objects
- What have we not addressed so far?
- We have only been considering a single object.
- How can we work with multiple objects that we would like to
animate together?
- We could simply apply the methods discussed so far, or even
AI.
- Interestingly, the larger the group of objects get, the smaller
the “intelligence” is needed to get them to appear as a group.
- Flocking is one technique and comes from the behaviour of
birds when they fly together.
- Flocking can also be used for other types of animals.
Examples?

- As discussed earlier in the chapter, we want objects not to
collide or slice each other.
- This is also true for the motion of multiple objects.
- For example: Unless a bird of prey is present, birds will not fly
into each other.
- Thus, when designing the motion of multiple objects,
collisions should be avoided.
- A simpler implementation is to use a set of velocity vectors.
- The animator is in control of all of the parameters of the
particle system, which include:
- Number of particles
- Particle life span
- Initial velocity
- Location of a particle

- The number of particles in the system is usually much larger
than the number of boids.
- The number of particles can fluctuate as particles can have a
lifespan in which they die or are created during the animation.
- Particles only interact with the environment and ignore other
particles.
- Particles can also collide with other particles but cannot pass
through the particles.
- At each step of the animation the following steps are taken:
1. Creates new particles with some initial parameters.
2. Terminates old particles.
3. Computes necessary forces.
4. Updates velocity and positions of the remaining particles
according to Newton’s law.

- Particle systems have been used for:
- Fireworks
- Explosion
- Spraying liquids
- Smoke and fire
- To increase the level of realism, remember to add randomness.
- Because it was stuck between two frames of mind and couldn’t
interpolate its feelings
