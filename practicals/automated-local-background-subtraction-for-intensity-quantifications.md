# Intensity measurements with automated local background subtraction  <a name="automated-local-background-subtraction"></a>

This practical discusses how to automate the local background subtraction in the 
practical on [intensity-quantification](https://github.com/tischi/imagej-courses/blob/master/practicals/intensity-quantification.md#image-intensity-measurements-). 

The content of this practial is basically the same as [here](https://github.com/tischi/imagej-courses/blob/master/practicals/workflow-2d-intracellular-spot-detection.md#local-background-subtraction-), but with different images. Although similar, the synthetic input data in this practical allows to examine the pros and cons of the different methods in a more controlled way.

Automated local background subtraction is important for 

- image batch analysis, or 
- uneven local background that is not easy to subtract manually.

In biological fluorescence microscopy one often wants to detect locally bright objects such as vesicular structures on top of a non-uniform background fluorescence, e.g. from unbound cytoplasmic protein. There are different methods to remove such 'background' fluorescence from the image, e.g.:

- corrected\_image = image - mean\_filter(image, radius) 
- corrected\_image = image - median\_filter(image, radius) 
- corrected\_image = image - morphological\_opening(image, radius) = top\_hat(image, radius)
- corrected\_image = IJs "RollingBall" Algorithm
- ...

In all methods the *radius* parameter should be "quite a bit larger" than the radius of the largest locally bright structure that you want to measure (why that is becomes clear when we discuss the methods in detail).


## Local background subtraction using a top-hat filter 

A morphological opening filter is applied to the image and subtracted from the original. The morphological opening is defined as the dilation of the erosion if the image. Alltogether this reads: top_hat(image) = image - dilation(erosion(image))

- [File>Open..] "../dna-damage-synthetic-data/Damaged.tif"
- [Image>Rename..] 'Title=original'
- [Image>Duplicate] 'Title=opened'
- [Process>Filters>Minimum..] 'radius=5' 
- [Process>Filters>Maximum..] 'radius=5' 
- [Process>Image Calculator] 'original' 'Subtract' 'opened' 
	- [X] Create new window 
	- [ ] 32-bit output
		- Note: By construction, the 'opened' image is always lower than the original; thus we cannot get negative pixels. 
- [Image>Rename] 'Tophat.tif'


&nbsp;

&nbsp;

&nbsp;

## Local background subtraction using a median filter

What we'll do here is to duplicate the image and apply median filter to remove the locally bright spots. Then we subtract the median filtered image from the original image: 

- [File>Open..] "../dna-damage-synthetic-data/Damaged.tif"
- [Image>Rename..] 'Title=original'
- [Image>Duplicate] 'Title=median'
- Select the 'median' image and [Process>Filters>Median] 'radius=5'
- [Process>Image Calculator] 'Image1 = original' 'Operation = Subtract' 'Image2 = median' 
	- [X] Create new window 
	- [X] 32-bit output 
- [Image>Rename] "median_subtraction"

&nbsp;

&nbsp;

&nbsp;



## Local background subtraction using IJs "Subtract Background"

- [File > Open..] "../dna-damage-synthetic-data/Damaged.tif" 
- [Process > Subtract Background..] 
	- radius=5

This seems to implement a ['rolling ball'](https://github.com/nearlyfreeapps/Rolling-Ball-Algorithm/blob/master/rolling_ball.py) background estimation (=> Whiteboard). I don't understand the mathematical algorithm how to compute this, but based on the code that i saw it seems not so simple (see also [here](http://dsp.stackexchange.com/questions/10597/uneven-background-subtraction-rolling-ball-vs-disk-tophat) and [here](https://en.wikipedia.org/wiki/Dilation_%28morphology%29#Grayscale_dilation)).


&nbsp;

&nbsp;

&nbsp;


### Discussion: Comparison of the different BG subtraction methods 

- Difference between median-subtraction and top-hat:
	- top-hat underestimates background in presence of noise
	- median overestimates background in presence of "holes"
	- median does not work well along curved egdes
- Local background subtraction should only be used for (small) isolated objects
	- e.g., may fail if used to find the background intensity in an image full of cells



&nbsp;

&nbsp;

&nbsp;
