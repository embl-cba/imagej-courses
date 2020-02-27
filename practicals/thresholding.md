# Image thresholding<a name="thresholding"></a> 

- Often essential part of bioimage analysis
- Central dogma of image analysis: Intensity image -> Binary image -> Label mask image
- Intensity image -> Binary image: for fluorescence microscopy can be done via thresholding

## Manual global thresholding followed by connected components labeling

In fluorescence microscopy, image segmentation often is easy, because the objects of interest are simply brighter than the "background". 

Let's try:
 
- [Process > Binary > Options]
	- [X] Black Background
- Open image: "thresholding-neubias-2020/nuclei.tif"
- [Image > Adjust > Threshold]
- Connected components labeling using MorpholibJ

Difference between thresholding and gating!

Changing LUT settings does not change threshold!

## Changing the threshold affects which objects we find

- Open image: "thresholding-neubias-2020/mitotic-and-interphase-cell.tif"
- [Image > Adjust > Threshold]

We can choose to only find the bright cell, however we cannot only find the dark cell. Why?

## Sufficient signal to noise (S/N) is important for thresholding

<img width="885" alt="image" src="https://user-images.githubusercontent.com/2157566/39702229-5a093cc0-5204-11e8-826e-068979e14f6c.png">

- Open image: "thresholding-neubias-2020/hb2-mCherry.tif"

It is difficult to binarise the dim nuclei. Why?

Measure the signal to noise ratio of few nuclei.

One can use signal to noise to compute a threshold value: `threshold = meanBG + N * stdBG`, where in general N can be tuned to balance false positives and false negatives. 

## Manual thresholding may not be practical for automated microscopy

- Open image: "thresholding-neubias-2020/nuclei.tif"  
- Open image: "thresholding-neubias-2020/dimmer-nuclei.tif"  

Finding one threshold for both images is not possible.

- Examine the image histograms to understand the reason.

## Automated global thresholding

- Open image: "thresholding-neubias-2020/nuclei.tif"  
- Open image: "thresholding-neubias-2020/dimmer-nuclei.tif"  
- Open image: "thresholding-neubias-2020/no-nuclei-just-noise.tif"  

- [Image > Adjust > Auto Threshold]
	- https://imagej.net/Auto_Threshold

The images with the nuclei can be auto-thresholded, but the image with noise only presents a challenge!
Look at the histograms to understand why.
To deal with this, e.g., in CellProfiler, one can specify a lower threshold limit.

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

