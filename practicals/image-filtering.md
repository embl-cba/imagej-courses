# Basics of image filtering

Image filtering is a very wide field, where mostly one replaces the intensity of each pixel by some mathematical function of its neighbors. The most simple example is probably the 3x3 mean filter, where each pixel is replaced by the mean value in a 3x3 neighborhood (i.e. inclucing the pixel itself and its 8 neighbors).

## Activity: Manually compute a 3x3 mean and a 3x3 median filter

Mean and median can be almost the same, but, depening on the data, also be very different; thus let's compare them. In fact, the median filter is quite important for local background subtraction, while the mean filter is less useful in this context (see below).

Let's compute a 3x3 mean and a 3x3 median filter for the central pixel in below examples and compare the results.

### Compare 3x3 mean and median filter (behavior with outliers)

|   |   |   |   |   |
|---|---|---|---|---|
| 10  | 11  | 10  | 13  | 12  ||
| 13  | 1000  | 10  | 11  | 14  |
| 21  | 15  | **11**  | 13  | 10  |
| 14  | 13  | 12  | 11  | 10  |
| 11  | 11  | 10  | 13  | 12  |


|   |  Mean  |  Median  |  
|---|---|---|
| Central pixel value after filtering | |   |


### Compare 3x3 mean and median filter (behavior at edges)

|   |   |   |  |   |
|---|---|---|---|---|
| 10  | 11  | 10  | 1 | 1  |
| 13  | 12  | 10  | 1  | 1  |
| 21  | 15  | **11**  | 0  | 0  |
| 14  | 13  | 12  | 0  | 0  |
| 11  | 11  | 10  | 1  | 0  |

|   |  Mean  |  Median  |  
|---|---|---|
| Central pixel value after filtering  | |   |


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
| 1/9  | 1/9 | 1/9 |
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


Sum of the 9 pixels is 11.33333

Convolved image:

|   |   |   |
|---|---|---|
| .  | .  | . |
| .  | **11.333**  | .  | 
|  . | .  | .  | 


Basically, you multiply each pixel in the original image with the number that is written in the kernel and then you replace the center pixel with the sum of all pixels.

### Discussion points

- Issue using 8 bit images for storing convolution results...

&nbsp;

&nbsp;

&nbsp;



## Activity: Try the effect of different convolution kernels

https://en.wikipedia.org/wiki/Kernel_(image_processing)

- Open any image of your choice
- [Process > Filters > Convolve] 

&nbsp;

&nbsp;

&nbsp;

