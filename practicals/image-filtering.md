# Image filtering (convolution)

Image filtering is a very wide field, where mostly one replaces the intensity of each pixel by some mathematical function of its neighbors. The most simple example is probably the 3x3 mean filter, where each pixel is replaced by the mean value in a 3x3 neighborhood (i.e. inclucing the pixel itself and its 8 neighbors).

## Activity: Manually compute a 3x3 mean and a 3x3 median filter

Mean and median can be almost the same, but, depening on the data, also be very different; thus let's compare them. In fact, the median filter is quite important for local background subtraction, while the mean filter is less useful in this context (see below).

Let's compute a 3x3 mean and a 3x3 median filter for the central pixel in below examples and compare the results.

|   |   |   |   |   |
|---|---|---|---|---|
| 10  | 11  | 10  | 13  | 12  ||
| 13  | 1000  | 10  | 11  | 14  |
| 21  | 15  | **11**  | 13  | 10  |
| 14  | 13  | 12  | 11  | 10  |
| 11  | 11  | 10  | 13  | 12  |

What do you get for mean and median?


|   |   |   |  |   |
|---|---|---|---|---|
| 10  | 11  | 10  | 1 | 1  |
| 13  | 12  | 10  | 1  | 1  |
| 21  | 15  | **11**  | 0  | 0  |
| 14  | 13  | 12  | 0  | 0  |
| 11  | 11  | 10  | 1  | 0  |

And what do you get here for mean and median?

### Discussion

From above examples, it should have become clear why a median filter is called both:
- robust to outliers
- edge preserving

&nbsp;

&nbsp;

&nbsp;

## Image convolution

The 3x3 mean filter that we applied above can also be expressed in terms on a "convolution", with a "convolution kernel" as show below:

Kernel:

|   |   |   |
|---|---|---|
| 1/9  | 1/9  | 1/9 |
| 1/9  | **1/9**  | 1/9 |
| 1/9  | 1/9  | 1/9 |


Original image:

|   |   |   |
|---|---|---|
| 15  | 11  | 5 |
| 14  | **13**  | 12  | 
| 11  | 11  | 10  | 

Intermediate step:

|   |   |   |
|---|---|---|
| 15 * 1/9  | 11 * 1/9  | 5 * 1/9 |
| 14 * 1/9   | **13** * 1/9   | 12 * 1/9   | 
| 11 * 1/9   | 11 * 1/9   | 10 * 1/9   | 


Sum is 11.33333

Convolved image:

|   |   |   |
|---|---|---|
| ?  | ?  | ? |
| ?  | **11.333**  | ?  | 
| ?  | ?  | ?  | 


Basically, you multiply each pixel in the original image with the number that is written in the kernel and then you replace the center pixel with the sum of all pixels.

&nbsp;

&nbsp;

&nbsp;



## Activity: Try the effect of different convolution kernels

- Open any image of your choice
- [Process > Filters > Convolve] 

&nbsp;

&nbsp;

&nbsp;

### Spot enhancement using the Difference of Gaussian

The Difference of Gaussian (DoG) is a very popluar method for object detection when there is uneven background or also an uneven object brightness distribution.

Workflow:
- Blur image with a small Gaussian (about the size of the objects)
- Blur image with a large Gaussian (about two-three times the object size)
- Subtract the large blur from the small blur; this is the DoG!
- Threshold the resulting image to find the object centers
- Fiji commands:
	- [Process > Filters > Gaussian]
	- [Process > Image Calculator]
	- [Analyze > Analyze Particles] or [Process > Find Maxima]

Discussion:
- The object shape is not preserved with this method

	- Workflow:
		- Find object centers using DoG
		- Find object volumes growing from the object centers
