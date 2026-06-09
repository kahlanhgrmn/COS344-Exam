COS 344: L21 Chapter 14: Physics-Based
Rendering
18/05/2026

- All of the rendering we have done up until now is to some
extent or another “physics-based”.
- But the term physics-based implies in practice something
different.
Physics-based rendering (PBR)
The use of physics-based models to create a render.
- In this chapter, a very high level discussion will be had about
PBR due to the sheer amount of different approaches and
algorithms that have been created.

- A particle representing a quantum of light or other
electromagnetic radiation.
- What is a photon to computer graphic programmers?
- A photon is a packet of light that has a position, direction of
propagation, and a wavelength λ.
- A photon also has a speed c that depends only on the
refractive index n of the medium it is propagating through.
- What is a photon?

- What is a photon to computer graphic programmers?
- A photon is a packet of light that has a position, direction of
propagation, and a wavelength λ.
- A photon also has a speed c that depends only on the
refractive index n of the medium it is propagating through.
- What is a photon?
- A particle representing a quantum of light or other
electromagnetic radiation.

- A photon is a packet of light that has a position, direction of
propagation, and a wavelength λ.
- A photon also has a speed c that depends only on the
refractive index n of the medium it is propagating through.
- What is a photon?
- A particle representing a quantum of light or other
electromagnetic radiation.
- What is a photon to computer graphic programmers?

- What is a photon?
- A particle representing a quantum of light or other
electromagnetic radiation.
- What is a photon to computer graphic programmers?
- A photon is a packet of light that has a position, direction of
propagation, and a wavelength λ.
- A photon also has a speed c that depends only on the
refractive index n of the medium it is propagating through.

- We can also use the following formula to calculate the
frequency of light:
c
f =
λ
- This is useful as f does not change when a photon refracts
into a medium with a new n.
- Another invariant measure is the amount of energy q a
photon has:
hc
q = hf =
λ
- Where h = 6.63×10−34 Js (Planck’s constant)

- In Chapter 4 we discussed how smooth metals reflect light.
- Two options exist:
1. Specular reflection
2. Refracted into the surface and then quickly absorbed.
- The amount of light that is reflected is determined by the
Fresnel equations.
- These are a set of straightforward but cumbersome equations
and their values differ when polarization is taken into account.
- In computer graphics, polarization is often ignored.
- The main visual effect of the Fresnel equation, is that the
reflectance increases with the incident angle, particularly near
grazing angles where it goes to 100%.

- In computer graphics, we use a simple approximation for the
Fresnel equations:
(λ))(1−cos(θ))5
R(θ,λ) = R 0 (λ)+(1−R 0
where:
- λ is the wavelength
- θ is the angle between the direction of light propagation and
the surface normal.
- R (λ) is the reflectance at normal incidence
0

- “Clear” materials that refract light.
- It is not a “bad” assumption to make, that if something is not
a metal it is a dielectric.
- Examples?
- Skin
- Milk
- Hair
- Cloth
- These examples are tricky as they can be seen as fully opaque
since they are a mixture of different refractive indices and
light-absorbing impurities.
- Examples of smooth homogeneous dielectrics:
- Pure Water
- Pure Glass
- Eye lens (Eyeball 1.0)
- What are dielectrics?

- Skin
- Milk
- Hair
- Cloth
- These examples are tricky as they can be seen as fully opaque
since they are a mixture of different refractive indices and
light-absorbing impurities.
- Examples of smooth homogeneous dielectrics:
- Pure Water
- Pure Glass
- Eye lens (Eyeball 1.0)
- What are dielectrics?
- “Clear” materials that refract light.
- It is not a “bad” assumption to make, that if something is not
a metal it is a dielectric.
- Examples?

- Pure Water
- Pure Glass
- Eye lens (Eyeball 1.0)
- What are dielectrics?
- “Clear” materials that refract light.
- It is not a “bad” assumption to make, that if something is not
a metal it is a dielectric.
- Examples?
- Skin
- Milk
- Hair
- Cloth
- These examples are tricky as they can be seen as fully opaque
since they are a mixture of different refractive indices and
light-absorbing impurities.
- Examples of smooth homogeneous dielectrics:

- What are dielectrics?
- “Clear” materials that refract light.
- It is not a “bad” assumption to make, that if something is not
a metal it is a dielectric.
- Examples?
- Skin
- Milk
- Hair
- Cloth
- These examples are tricky as they can be seen as fully opaque
since they are a mixture of different refractive indices and
light-absorbing impurities.
- Examples of smooth homogeneous dielectrics:
- Pure Water
- Pure Glass
- Eye lens (Eyeball 1.0)

- Smooth Dielectrics have the following properties:
1. How much light is reflected at each incident angle and
wavelength.
2. What fraction of light is absorbed as it travels through the
material for a given distance and wavelength.
3. What are the directions of the reflected and refracted light?

- How light bends geometrically and what fraction is
reflected/transmitted, depends on the refractive index n(λ).
- When air is one of the materials light moves through, we can
set R (λ) in terms of n(λ).
0

n(λ)−1
2
R (λ) =
0
n(λ)+1
- In cases where the material on either side is not air, or a
vacuum (when the refractive indices are not 1.0), use this
formula:

n (λ)−n (λ)
2
t i
R (λ) =
0
n (λ)+n (λ)
t i
where:
- i is associated with the incoming ray
- t is associated with the transmitted ray

- Typically n does not change depending on wavelength.
- Some useful values for n:
- water: 1.33
- glass: 1.4-1.7
- diamond: 2.4

- Dielectrics also filter and refract light.
- Some glass types filter out more red and blue light than green
light.
- When light travels from one medium with a refractive index n,
to another medium with a refractive index n , some light is
t
transmitted and bent.
- Snell’s law is defined as:
nsin(θ) = n sin(ϕ)
t
- We can rewrite this in terms of cosines:
n2(1−cos2(θ))
cos2(ϕ) = 1−
n2
t
- This will exploit the dot product between two vectors for us.

The remainder of the subsection discusses how to convert cos(ϕ)
and sin(ϕ) into a 3D vector.

- Sections 14.4, 14.5, 14.6, 14.7, and 14.8 are skipped.
- Section 14.5 introduces a brute-force photon tracing
algorithm, which is able to generate amazing and realistic
renders at a high execution cost.

- At the start of the semester, we said that we can look up a
material’s BRDF function for the lighting and shadow
calculations.
- There are many BRDF models in industry and literature.
- There are also many fields that use BRDF models including:
- remote sensing
- heat transfer
- material science
- computer graphics
- Unfortunately, as with many things in tech, there is no
standard set of terms for BRDF.
- The taxonomy on the next page are a somewhat summary of
the consensus of BRDF terms in industry and practice.
- Section 14.10 is also skipped due to Monte Carlo Integration

traditionalvspbr01.jpg
Video: https://www.youtube.com/watch?v=iXHZlqp3X6U

And with this, we conclude the theory for COS 344 2026.
Good luck with your exams and the rest of your 3rd year.
