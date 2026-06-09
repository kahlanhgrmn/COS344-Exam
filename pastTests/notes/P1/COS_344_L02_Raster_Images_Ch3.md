COS 344 L2: Chapter 3
Raster Images with file storage format
Cobus Redelinghuys
12/02/2026

- Image:
- Rectangular array of pixels.
- Pixel - picture element
- Colour:
- Mixing different intensities of red, blue, and green light to form
color per pixel.
- Example:
- Displays (output)
- Printer (output)
- Image sensor (input)
Raster display:

- Colour:
- Mixing different intensities of red, blue, and green light to form
color per pixel.
- Example:
- Displays (output)
- Printer (output)
- Image sensor (input)
Raster display:
- Image:
- Rectangular array of pixels.
- Pixel - picture element

- Mixing different intensities of red, blue, and green light to form
color per pixel.
- Example:
- Displays (output)
- Printer (output)
- Image sensor (input)
Raster display:
- Image:
- Rectangular array of pixels.
- Pixel - picture element
- Colour:

- Example:
- Displays (output)
- Printer (output)
- Image sensor (input)
Raster display:
- Image:
- Rectangular array of pixels.
- Pixel - picture element
- Colour:
- Mixing different intensities of red, blue, and green light to form
color per pixel.

Raster display:
- Image:
- Rectangular array of pixels.
- Pixel - picture element
- Colour:
- Mixing different intensities of red, blue, and green light to form
color per pixel.
- Example:
- Displays (output)
- Printer (output)
- Image sensor (input)

- 2D array
- Given an arbitrary image:
- What are the dimensions of the 2D array?
- Each cell in the array is a pixel value.
- RBG values
- How can it be displayed from memory?
- Each pixel of the stored image controls the pixel on the display.
- A type of “naive” mapping.
- What are the advantages and disadvantages?
- Device independent description of the image.
- The display approximates the image.
Raster images:
- What is the underlying data-structure?

- Each cell in the array is a pixel value.
- RBG values
- How can it be displayed from memory?
- Each pixel of the stored image controls the pixel on the display.
- A type of “naive” mapping.
- What are the advantages and disadvantages?
- Device independent description of the image.
- The display approximates the image.
Raster images:
- What is the underlying data-structure?
- 2D array
- Given an arbitrary image:
- What are the dimensions of the 2D array?

- How can it be displayed from memory?
- Each pixel of the stored image controls the pixel on the display.
- A type of “naive” mapping.
- What are the advantages and disadvantages?
- Device independent description of the image.
- The display approximates the image.
Raster images:
- What is the underlying data-structure?
- 2D array
- Given an arbitrary image:
- What are the dimensions of the 2D array?
- Each cell in the array is a pixel value.
- RBG values

- What are the advantages and disadvantages?
- Device independent description of the image.
- The display approximates the image.
Raster images:
- What is the underlying data-structure?
- 2D array
- Given an arbitrary image:
- What are the dimensions of the 2D array?
- Each cell in the array is a pixel value.
- RBG values
- How can it be displayed from memory?
- Each pixel of the stored image controls the pixel on the display.
- A type of “naive” mapping.

- Device independent description of the image.
- The display approximates the image.
Raster images:
- What is the underlying data-structure?
- 2D array
- Given an arbitrary image:
- What are the dimensions of the 2D array?
- Each cell in the array is a pixel value.
- RBG values
- How can it be displayed from memory?
- Each pixel of the stored image controls the pixel on the display.
- A type of “naive” mapping.
- What are the advantages and disadvantages?

Raster images:
- What is the underlying data-structure?
- 2D array
- Given an arbitrary image:
- What are the dimensions of the 2D array?
- Each cell in the array is a pixel value.
- RBG values
- How can it be displayed from memory?
- Each pixel of the stored image controls the pixel on the display.
- A type of “naive” mapping.
- What are the advantages and disadvantages?
- Device independent description of the image.
- The display approximates the image.

- Stores description of shapes instead of pixels.
- Shape: color area bounded by lines or curves.
- Resolution independent.
- Advantages and disadvantages?
- Adv: Perfect for high resolution displays
- DAdv: First be rasterized before displayed.
- Use cases?
Vector image:
- Alternative way of describing images.

- Adv: Perfect for high resolution displays
- DAdv: First be rasterized before displayed.
- Use cases?
Vector image:
- Alternative way of describing images.
- Stores description of shapes instead of pixels.
- Shape: color area bounded by lines or curves.
- Resolution independent.
- Advantages and disadvantages?

Vector image:
- Alternative way of describing images.
- Stores description of shapes instead of pixels.
- Shape: color area bounded by lines or curves.
- Resolution independent.
- Advantages and disadvantages?
- Adv: Perfect for high resolution displays
- DAdv: First be rasterized before displayed.
- Use cases?

Example
03094728/vector-vs-raster.jpg

- It depends on the pixel information.
Section 3.2: Images, Pixels, and Geometry
- Section 3.1 is left to curious students.
- Graphical computations rely on abstraction of the display
device.
- Images in the real world are functions defined over
two-dimensional areas:
- The light of the display is a function of the position on the
display.
- The light on a camera sensor is a function of the position on a
camera sensor.
- etc.
- An image can be abstracted to have the formula:
I(x,y) : R → V
R2
where R ⊂ and V is the set of possible pixel values.
- What is the dimensions of V?

Section 3.2: Images, Pixels, and Geometry
- Section 3.1 is left to curious students.
- Graphical computations rely on abstraction of the display
device.
- Images in the real world are functions defined over
two-dimensional areas:
- The light of the display is a function of the position on the
display.
- The light on a camera sensor is a function of the position on a
camera sensor.
- etc.
- An image can be abstracted to have the formula:
I(x,y) : R → V
R2
where R ⊂ and V is the set of possible pixel values.
- What is the dimensions of V?
- It depends on the pixel information.

Point sample
Local average of the color at a specific point.
Assume the colors in the raster image are the average of all the
colors in a single “cell” when overlaid on the vector image.

2D coordinate convention
- The textbook’s convention:
- The position of a pixel in a raster image is given by: (i,j)
- i is the x-Cartesian coordinate or column.
- j is the y-Cartesian coordinate or row.
- The origin (0,0) is in the bottom left corner.
- If there are n columns and m rows, the top right coordinates
x y
are: (n −1,m −1)
x y

- Recall that V is dependant on the pixel’s information.
- Pixel values are usually bounded between [0,1] due to a finite
maximum intensity.
- Example of 8-bit value:
- Minimum value: 0
- 255
Maximum value: or 1
- 255
Number of possible values: 256.
- Low Dynamic Range (LDR) images.
- Images using integer numbers to represent pixel values.
- High Dynamic Range(HDR) images.
- Images using floating-point numbers to represent pixel values.
- Examples of V’s dimension:
- Grey scale: V =R+
- RGB: V =(R+)3
Section 3.2.1: Pixel Values
- From this formula I(x,y) : R → V, lets investigate V.

- Example of 8-bit value:
- Minimum value: 0
- 255
Maximum value: or 1
- 255
Number of possible values: 256.
- Low Dynamic Range (LDR) images.
- Images using integer numbers to represent pixel values.
- High Dynamic Range(HDR) images.
- Images using floating-point numbers to represent pixel values.
- Examples of V’s dimension:
- Grey scale: V =R+
- RGB: V =(R+)3
Section 3.2.1: Pixel Values
- From this formula I(x,y) : R → V, lets investigate V.
- Recall that V is dependant on the pixel’s information.
- Pixel values are usually bounded between [0,1] due to a finite
maximum intensity.

- Low Dynamic Range (LDR) images.
- Images using integer numbers to represent pixel values.
- High Dynamic Range(HDR) images.
- Images using floating-point numbers to represent pixel values.
- Examples of V’s dimension:
- Grey scale: V =R+
- RGB: V =(R+)3
Section 3.2.1: Pixel Values
- From this formula I(x,y) : R → V, lets investigate V.
- Recall that V is dependant on the pixel’s information.
- Pixel values are usually bounded between [0,1] due to a finite
maximum intensity.
- Example of 8-bit value:
- Minimum value: 0
- 255
Maximum value: or 1
- 255
Number of possible values: 256.

Section 3.2.1: Pixel Values
- From this formula I(x,y) : R → V, lets investigate V.
- Recall that V is dependant on the pixel’s information.
- Pixel values are usually bounded between [0,1] due to a finite
maximum intensity.
- Example of 8-bit value:
- Minimum value: 0
- 255
Maximum value: or 1
- 255
Number of possible values: 256.
- Low Dynamic Range (LDR) images.
- Images using integer numbers to represent pixel values.
- High Dynamic Range(HDR) images.
- Images using floating-point numbers to represent pixel values.
- Examples of V’s dimension:
- Grey scale: V =R+
- RGB: V =(R+)3

- Clipping
- Quantization or banding
Clipping
When the value of a pixel exceeds the fixed-range, the value is
bounded to the minimum or maximum value of the range.
Quantization or banding
The color jumping effect caused by the rounding of values to less
precise values.
- What are examples of each?
- Section 3.2.2 skipped.
- What are the effects of using less bits to store an image
compared to the amount of bits used to create/capture it?

- What are the effects of using less bits to store an image
compared to the amount of bits used to create/capture it?
- Clipping
- Quantization or banding
Clipping
When the value of a pixel exceeds the fixed-range, the value is
bounded to the minimum or maximum value of the range.
Quantization or banding
The color jumping effect caused by the rounding of values to less
precise values.
- What are examples of each?
- Section 3.2.2 skipped.

Example
https:
2020/06/EXPOSURE_CENTER_8-bit-10-bit_Video-Colour.jpg

- RYB are primary colors under subtractive color mixing.
- RGB are primary colors under additive color mixing.
2022/10/additivesubtractivecolour-1024x524.png
Section 3.3: RGB Color
- Colors are formed by blending three primary lights.
- Why is it not RYB?

Section 3.3: RGB Color
- Colors are formed by blending three primary lights.
- Why is it not RYB?
- RYB are primary colors under subtractive color mixing.
- RGB are primary colors under additive color mixing.
2022/10/additivesubtractivecolour-1024x524.png

Color cube
- What if RGB is thought of as a 3D Cartesian coordinate
system:
rgb-color-model-cube-hd-png-download.png

24
possibleLevels(24) = 23
= 28
= 256
- What does this mean, though? R component can have 256
values, G component can have 256 values, B component can
have 256 values
- How to determine the number of possible levels each primary
color has in RGB color system?
n
possibleLevels(n) = 23
where n is the number of color bits of the system.
- Example:
How many possible color levels does each primary color have
in a 24-bit RGB color system?

R component can have 256
values, G component can have 256 values, B component can
have 256 values
- How to determine the number of possible levels each primary
color has in RGB color system?
n
possibleLevels(n) = 23
where n is the number of color bits of the system.
- Example:
How many possible color levels does each primary color have
in a 24-bit RGB color system?
24
possibleLevels(24) = 23
= 28
= 256
- What does this mean, though?

- How to determine the number of possible levels each primary
color has in RGB color system?
n
possibleLevels(n) = 23
where n is the number of color bits of the system.
- Example:
How many possible color levels does each primary color have
in a 24-bit RGB color system?
24
possibleLevels(24) = 23
= 28
= 256
- What does this mean, though? R component can have 256
values, G component can have 256 values, B component can
have 256 values

1. Opaque foreground pixels
- Replaces background pixel.
2. Entirely transparent foreground pixels
- Do not change the background pixel.
3. Partially transparent foreground pixels
- Blending of foreground and background pixel colors.
Section 3.4: Alpha Compositing
Compositing
Effect caused by having two images overlapping each other.
- The possible cases for compositing and their effect on the
background pixel:

Section 3.4: Alpha Compositing
Compositing
Effect caused by having two images overlapping each other.
- The possible cases for compositing and their effect on the
background pixel:
1. Opaque foreground pixels
- Replaces background pixel.
2. Entirely transparent foreground pixels
- Do not change the background pixel.
3. Partially transparent foreground pixels
- Blending of foreground and background pixel colors.

Example

Pixel blending
- In order to blend pixel colors the following equation is used:
c = αc f +(1−α)c b
where:
- c is the resultant color vector
- c f is the color vector of the foreground pixel
- c is the color vector of the background pixel
- b
α is the fraction of the image covered by the foreground layer.
- Think of this as the translucency of the foreground pixel.
- Fun examples:

Alpha channel
- The possible ways to store the alpha value of each pixel:
1. As a separate grey-scale image.
2. A fourth channel on the RGB system which is known as RGBA.
- Modifying the possibleLevels function to account for alpha
values gives:
n
possibleLevelsAlpha(n) = 24

Visual Example

c = αc f +(1−α)c b
   
0 1
= (0.3)1+(1−0.3)1
1 0
 
0.7
= 1
 
0.3
Calculation Example
Assume the foreground pixel has
 
0
the color cyan 1 and the
1
background pixel has the color
 
1
yellow 1. Assume the pixel
0
coverage is 0.3 what would the
resultant color be?

   
0 1
= (0.3)1+(1−0.3)1
1 0
 
0.7
= 1
 
0.3
Calculation Example
Assume the foreground pixel has
c = αc f +(1−α)c b
 
0
the color cyan 1 and the
1
background pixel has the color
 
1
yellow 1. Assume the pixel
0
coverage is 0.3 what would the
resultant color be?

 
0.7
= 1
 
0.3
Calculation Example
Assume the foreground pixel has
c = αc f +(1−α)c b
 
0
the color cyan 1 and the
   
0 1
1
= (0.3)1+(1−0.3)1
background pixel has the color
  1 0
1
yellow 1. Assume the pixel
0
coverage is 0.3 what would the
resultant color be?

Calculation Example
Assume the foreground pixel has
c = αc f +(1−α)c b
 
0
the color cyan 1 and the
   
0 1
1
= (0.3)1+(1−0.3)1
background pixel has the color
  1 0
1
yellow 1. Assume the pixel  
0.7
0
= 1
 
coverage is 0.3 what would the
0.3
resultant color be?

Lossless
No information is lost during the compression of lossless formats.
Lossy
Information is unrecoverably lost during compression of lossy
formats.
- Examples of file formats:
1. JPEG
2. TIFF
3. PPM
4. PNG
Section 3.4.1: Image Storage
- Due to the size of raw RGB images, most image formats have
implemented some form of compression.

1. JPEG
2. TIFF
3. PPM
4. PNG
Section 3.4.1: Image Storage
- Due to the size of raw RGB images, most image formats have
implemented some form of compression.
Lossless
No information is lost during the compression of lossless formats.
Lossy
Information is unrecoverably lost during compression of lossy
formats.
- Examples of file formats:

Section 3.4.1: Image Storage
- Due to the size of raw RGB images, most image formats have
implemented some form of compression.
Lossless
No information is lost during the compression of lossless formats.
Lossy
Information is unrecoverably lost during compression of lossy
formats.
- Examples of file formats:
1. JPEG
2. TIFF
3. PPM
4. PNG

- Note for the homework assignment, as an optional
requirement, you can enable your program to be able to take
a screenshot of the current image displayed to screen.
- This involves using a function like to retrieve
glReadPixels
all the rendered pixels.
- You will also need to investigate a file format other than ppm
in which you will save the images.
- This involves reading the standard for the file format typical in
the same fashion as one would find the RFC for networking
protocols.
Any questions?

It had too many transparency issues!
