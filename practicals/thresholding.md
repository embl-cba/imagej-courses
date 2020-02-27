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

## Automated local tresholding 

### Test image

- open image: "thresholding-neubias-2020/uneven-background-test-image.tif"  

- [Image > Adjust > Auto Local Threshold]
	- http://imagej.net/Auto_Local_Threshold
	- read **Niblack**
		- notice: Parameter 2: `-c` allows to specify a minimal threshold

Reasonable Niblack parameters for "uneven-background-test-image.tif" image: 
- radius: 50 (much larger than objects of interest)
- parameter 1: 2 or 3 (depends on background noise level)

Explore applying a mean filter before thresholding.

### Autophagosome image

- open image: "thresholding-neubias-2020/autophagosomes.tif"  

One cannot find a global threshold to segment the autophagosomes due to uneven background.

Reasonable Niblack parameters for "autophagosomes.tif" image: 
- radius: 15
- parameter 1: 1 

### Nuclei of different intensity image

- open image: "thresholding-neubias-2020/different-intensity-nuclei.tif"  

Choosing a global threshold to also segment the dimmest nucleus causes other nuclei to merge.

- [Image > Adjust > Auto Local Threshold]
	- http://imagej.net/Auto_Local_Threshold
	- read **MidGrey**
		- notice: Parameter 2: `-c` allows to specify a minimal threshold

Reasonable MidGrey parameters for "different-intensity-nuclei.tif" image: 
- radius: 15
- parameter 1: -1 

## Learn more

### Image binarisation by clustering

TODO
