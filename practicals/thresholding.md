# Image thresholding<a name="thresholding"></a> 

- Often essential part of bioimage analysis
- Central dogma of image analysis: Intensity image -> Binary image -> Label mask image
- Intensity image -> Binary image: for fluorescence microscopy can be done via thresholding

## Manual global thresholding followed by connected components labeling

In fluorescence microscopy, image segmentation often is easy, because the objects of interest are simply brighter than the "background". 

Let's try:
 
- Configure image segmentation settings [Process > Binary > Options]: 
	- [X] Black Background
- Open image: "thresholding-neubias-2020/nuclei.tif" [File > Open]
- Manually adjust a threshold value [Image > Adjust > Threshold]
	- You may press [Apply] but you do not have to; it also works with the "red" overlay.
- Connected components labeling using MorpholibJ

## Changing the threshold affects which objects we find

- Open image: "thresholding-neubias-2020/mitotic-and-interphase-cell.tif" 

We can choose to only find the bright cell, however we cannot only find the dark cell. Why?

- Difference between thresholding and gating!
- Changing LUT settings does not change threshold!

# The signal to noise (S/N) ratio

<img width="885" alt="image" src="https://user-images.githubusercontent.com/2157566/39702229-5a093cc0-5204-11e8-826e-068979e14f6c.png">

- Open "thresholding-neubias-2020/hb2-mCherry.tif"  [File > Open]

It is difficult to binarise the dim nuclei. Why?

Make line profiles to inspect the intensities.

Measure the signal to noise ratio of few nuclei.

## Manual thresholding may not be practical for automated microscopy

- Open image: "thresholding-neubias-2020/nuclei.tif"  
- Open image: "thresholding-neubias-2020/dimmer-nuclei.tif"  

Finding one threshold for both images is not possible.


## Automated global thresholding

Sometimes, if you have many images to analyse, you may need automated methods that find the threshold for you. There are many good methods, but it is dangerous to apply them, and you always need to check if it worked! 

Workflow:
- Apply automated thresholding

Example data within Fiji: 
- [File > Open Samples > Blobs]
	- [Image > Lookup Tables > Invert LUT]
- [File > Open Samples > Hela cells]
	- [Image > Color > Split Channels]
- [File > New Image]
	- [Process > Noise > Add Noise]

Fiji commands:
- [Image > Adjust > Auto Threshold]

Documentation: 
- https://imagej.net/Auto_Threshold

### Discussion

- Many automated thresholding methods always find a threshold, even if there is only noise.

&nbsp;

&nbsp;

&nbsp;

## Automated local tresholding (under development)

Automated local thresholding is another method to segment objects in the prescence of a locally varying background. In fact, the results can be both mathematically and practically very similar to applying a global threshold to an image after local background subtraction.

Workflow:
- Threshold using a local thresholding algorithm
- Connected component analysis
- Fiji commands:
	- [Image > Adjust > Auto Local Threshold]
	- [Analyze > Analyze Particles]
- Documentation:
	- http://imagej.net/Auto_Local_Threshold
	
&nbsp;

&nbsp;

&nbsp;

## Segmentation in the prescence of uneven background

If there is an uneven background in your image segmenting the objects with just one threshold will not work.

Ways to combat this challenge are:

- **Local background subtraction**
	- If possible, this might be the best method, because 
		- it also corrects the intensities in your image.
		- you actually see how the image looks like that you finally threshold.
- **Automated local tresholding**
	- Works, but
		- does not correct intensities.
		- can be hard to debug, because, in contrast to local background subtraction, there is no visual feedback on what happens.
- **Edge enhancement combined with 'fill holes' (not shown)**
	- Also can work, but alters your intensities in a bad way.

## Local background subtraction practical

Please see here: [local background subtraction](https://github.com/tischi/imagej-courses/blob/master/practicals/workflow-2d-intracellular-spot-detection.md#local-background-subtraction-).

Once local background subtraction has been sucessfully applied it simply is a matter of applying a global threshold as discussed above.

&nbsp;

&nbsp;

&nbsp;

