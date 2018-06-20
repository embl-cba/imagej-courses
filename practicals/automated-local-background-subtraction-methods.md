## Local background subtraction <a name="local-background-subtraction"></a>

In biological fluorescence microscopy one often wants to detect locally bright objects such as vesicular structures on top of a non-uniform background fluorescence, e.g. from unbound cytoplasmic protein. There are different methods to remove such 'background' fluorescence from the image:

- corrected\_image = image - mean\_filter(image, radius) 
- corrected\_image = image - median\_filter(image, radius) 
- corrected\_image = image - morphological\_opening(image, radius) = top\_hat(image, radius)
- corrected\_image = IJs "RollingBall" Algorithm
- *someone knowing other methods?*

In all methods the *radius* parameter should be "quite a bit larger" than the radius of the largest locally bright structure that you want to measure (why that is becomes clear when we discuss the methods in detail).


&nbsp;
	
&nbsp;

&nbsp;


### Local background subtraction using a median filter

<img src="https://github.com/tischi/imagej-courses/blob/master/images/orig__median__subtraction.png" width=700/>

Duplicate image and apply median filter to remove the locally bright spots. Then subtract the median filtered image from the raw image and save the result for later use. 

- __[File>Open..] '../workflow_autophagosomes/autophagosomes_raw.tif'__
- __[Image>Rename..] 'Title=original'__
- __[Image>Duplicate] 'Title=median'__
- Select the 'median' image and __[Process>Filters>Median] 'radius=5'__
- __[Process>Image Calculator]__ 
	- Image1: original 
	- Operation: Subtract
	- Image2: median 
	* [X] 'Create new window' 
	* [X] '32-bit output'
- __[File>Save] 'spots_median.tif'__


&nbsp;
	
&nbsp;

&nbsp;


## Local background subtraction using a top-hat filter 

<img src="https://github.com/tischi/imagej-courses/blob/master/images/orig__open__tophat.png" width=700/>

A morphological opening filter is applied to the image and subtracted from the original. The morphological opening is defined as the dilation of the erosion if the image. Alltogether this reads: top_hat(image) = image - dilation(erosion(image))

- __[File>Open..] '../workflow_autophagosomes/autophagosomes_raw.tif'__
- __[Image>Rename..] 'Title=original'__
- __[Image>Duplicate] 'Title=opened'__
- __[Process>Filters>Minimum..] 'radius=5'__ 
- __[Process>Filters>Maximum..] 'radius=5'__ 
- __[Process>Image Calculator]__
	* Image1: original
	* Operation: Subtract
	* Image2: opened 
	* [X] 'Create new window' 
	* [ ] '32-bit'
		* Top hat filter cannot lead to negative values (which in fact is a problem, because you underestimate your actual background
- __[File>Save] 'spots_tophat.tif'__



&nbsp;
	
&nbsp;

&nbsp;


## Local background subtraction using IJs "Subtract Background"

<img src="https://github.com/tischi/imagej-courses/blob/master/images/orig__bg__rollingball.png" width=700/>

- __[File>Open..] '../workflow_autophagosomes/autophagosomes_raw.tif'__
- __[Process>Subtract Background..] 'radius=5'__

This seems to implement a ['rolling ball'](https://github.com/nearlyfreeapps/Rolling-Ball-Algorithm/blob/master/rolling_ball.py) background estimation (=> Whiteboard). I don't understand the mathematical algorithm how to compute this, but based on the code that i saw it seems not so simple (see also [here](http://dsp.stackexchange.com/questions/10597/uneven-background-subtraction-rolling-ball-vs-disk-tophat) and [here](https://en.wikipedia.org/wiki/Dilation_%28morphology%29#Grayscale_dilation)).


### Comparison of the different BG subtraction methods

Whiteboard session: 

- Difference between median-subtraction and top-hat:
	- top-hat underestimates background in presence of noise
	- median overestimates background in presence of "holes"
- Local background subtraction should only be used for (small) isolated objects
	- e.g., may fail if used to find the background intensity in an image full of cells
- Using the Spheroids image in 3D_Segmentation one can d emonstrate that the top-hat (dramatically) underestimates the background in noisy images


## Further enhancement of spots using a Laplacian of Gaussian filter (optional)

Above local background subtraction methods already helped a lot to enhance the spots; 
however in some cases there might still be some patchy locally bright regions left that are not corresponding to "real" spots. The reason is that the local background subtraction methods cannot distinguish locall bright elongated from locally bright round objects. Convolution of the image with a [Laplacian of Gaussian](https://en.wikipedia.org/wiki/Blob_detection#The_Laplacian_of_Gaussian) filter can help to further enhance spots of a certain size. 

- ...
