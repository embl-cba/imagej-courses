# Image segmentation<a name="segmentation"></a> 

https://en.wikipedia.org/wiki/Image_segmentation says: In computer vision, image segmentation is the process of partitioning a digital image into multiple segments (sets of pixels, also known as super-pixels). The goal of segmentation is to simplify and/or change the representation of an image into something that is more meaningful and easier to analyze. Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images. More precisely, image segmentation is the process of assigning a label to every pixel in an image such that pixels with the same label share certain characteristics.

## Applications of image segmentation in biology

- object counting
- object localization measurements
- object shape measurements
- object intensity measurements
- in general: object **feature** measurements

In general, image segmentation typically is a two step process, where you 
1. identify all pixels that potentially belong to an object
2. group pixels together belonging to one object (as you typically have several objects in one image).

## Activity: Manual global thresholding followed by "particle analysis"

In fluorescence microscopy, image segmentation often is easy, because the objects of interest are simply brighter than the "background". 

Let's try:
 
- Configure image segmentation settings [Process > Binary > Options]: 
	- [X] Black Background
- Open image:"../signal-to-noise/hb2-mCherry.tif" [File > Open]
- Manually adjust a threshold value [Image > Adjust > Threshold]
	- You may press [Apply] but you do not have to; it also works with the "red" overlay.
- Perform a "connected component analysis"  [Analyze > Analyze Particles]
	- Other wordings are: "object detection", "particle analysis"
- Run it again and explore the different options of the "Particle Analyzer"

### Discussion

- Single threshold vs. 'gating'
- Object size and shape filtering
- Different types of object representations (pros and cons)


&nbsp;

&nbsp;

&nbsp;

&nbsp;


# The signal to noise (S/N) ratio


<img width="885" alt="image" src="https://user-images.githubusercontent.com/2157566/39702229-5a093cc0-5204-11e8-826e-068979e14f6c.png">


At the microscope, especially setting up a live cell experiment where you want to avoid photo-bleaching of your fluorophore, you typically wonder: "How good does the image need to be in order for me to be able to still segment the objects?"

A very important concept in this regard is the signal to noise ratio (S/N), which, in my humble opinion, is often confused with the much less important signal to background ratio (S/B).

Let's have a look and try to segment nuclei of different intensities:

- Open "../signal-to-noise/hb2-mCherry.tif"  [File > Open]
- Now try to threshold the nuclei  [Image > Adjust > Threshold]
	- You see that this is easy for the bright ones but does not really work for the very dim ones (you may have to adjust the LUT settings [Image > Adjust > Brightness/Contrast] to even see the dark ones).

Let's now try to quantify why it is difficult to segment the dark nuclei by measuring their S/N.

- [Analyze > Set Measurements]: 
	- [X] Mean gray value
	- [X] Standard deviation
- Draw an ROI inside a dim nuclues of your choice, e.g. using the “Oval Selection”
- Save that ROI [Analyze > Tools > ROI Manager > Add]
	- ...and give it a good name [Analyze > Tools > ROI Manager > Rename]
- Now also draw and save an ROI in the background right next to the nucleus
- Select both regions and measure them [ROI Manager > Measure]

Now let's apply below formulas to measure the S/N and S/B: 
- S/N = ( Mean_Nucleus - Mean_Background ) / Sdev_Background
- S/B = Mean_Nucleus / Mean_Background

## Discussion

As mentioned, although sometimes used, I don't understand the use of S/B. For S/N however it is very clear that if you are getting as low as two, you start getting into trouble in terms of being able to still segment this object.


&nbsp;

&nbsp;



# Segmentation of noisy images with the help of filtering

Please first learn the [basics of image filtering.](https://github.com/tischi/imagej-courses/blob/master/practicals/image-filtering.md)


&nbsp;

&nbsp;

&nbsp;


## Activity 

- Open: "../signal-to-noise/noisy-nuclei.tif" [File > Open]
- Try to segment the nuclei:
	- Thresholding: [Image > Adjust > Threshold] 
	- Particle analysis: [Analyze > Analyze Particles]
	- Does not work very well, right?
- Now, let's try to smooth the image first, e.g. using 
	- median filter [Process > Filters > Median]
		- try different radii using the [ ] Preview option
- Now, let's segment the nuclei, using:
	- [Image > Adjust > Threshold]
	- [Analyze > Analyze Particles]

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
