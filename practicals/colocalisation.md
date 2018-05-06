# Colocalisation

## Literature

- [A guided tour into subcellular colocalization analysis in light microscopy. S. B O LT E & F. P. C O R D E L I È R E S Journal of Microscopy, Vol. 224, 2006, pp. 213–232.](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2818.2006.01706.x/epdf)
- [Manders' correlation coefficients](https://imagej.net/_images/2/24/Manders.pdf)

## General considerations

- Draw example images to see what you mean by "colocalisation"
	- Warning: there are tons of possibilities => you have to exactly know what you are doing!
	- You have to chose your point of view: overlap of ch1 with ch2 vs. overlap of ch2 with ch1
	- You can measure pixel- or object-based overlap or some distance criterium (e.g., centroid- or boundary-based)
- Use tetraspec beads to check your microscope
- Diffraction limit depends on wavelength
- Due to the diffraction limit everything can appear to colocalise with ER or tubulin
- The cytoplasm in a cell can be quite small, so proteins might colocalise just by chance
- Create synthetic (simulated or hand-drawn) test images to check if your analysis does what you want

## Practical on pixel- and object-based colocalisation

We will first use manufactured data to keep it simple in terms of interpreting the results:

<img width="314" alt="image" src="https://user-images.githubusercontent.com/2157566/39677022-c8e94670-5174-11e8-8696-f640f65556a2.png">

You are however very welcome to repeat the pratical with real data:

<img width="314" alt="image" src="https://user-images.githubusercontent.com/2157566/39677343-a1995e52-5179-11e8-8744-9c8e5c9e8fce.png">

### Segmentation: Local background subtraction and thresholding

Here, we will only consider pixel- and object-based colocalisation, thus we first segment the images, i.e. we make objects pixels 255 and background pixels 0.

- __[File>Open..] '“../colocalization/synthetic-data-ch1.tif”__
- __[Image>Rename..] 'Title=original'__
- Local background subtraction
	- __[Image>Duplicate] 'Title=median'__
	- __[Process>Filters>Median..] 'radius=20'__ 
	- __[Process>Image Calculator] 'Image1 = original' 'Operation = Subtract' 'Image2 = median' 'Create new window=Check'__ 
- Segmentation:
	- **[Image>Adjust>Threshold..]**
		- choose appropriate threshold values
		- *you don't have to press [Apply] now, the actual 'applying' of the threshold will happen in the next step*
	- **[Analyze>Analyze Particles..]**
		- 'Size = 5-Infinity' 
		- [X] 'Pixel units' 
		- 'Show = Masks' [OK]
			- *selecting 'Show = Masks' generates a binary image in which only 'connected components' of at least 5 pixels are kept, i.e. 'noise' is filtered*
- Save your work:
	- __[File>Save As..] '“../colocalization/synthetic-data-ch1-segmented.tif”__

Repeat above steps for "synthetic-data-ch2.tif".

### Area- and object-based colocalization

First we load the segmented images and compute the overlap (colocalization) image:

- __[File>Open..] '“../colocalization/synthetic-data-ch1-segmented.tif”__
- __[File>Open..] '“../colocalization/synthetic-data-ch2-segmented.tif”__
- __[Process>Image Calculator] 'synthetic-data-ch1-segmented.tif' 'AND' 'synthetic-data-ch2-segmented.tif'__
	- The 'AND' operations keeps pixels that are non-zero in both images, i.e. the 'colocalizing' pixels.
- __[Image>Rename..] 'Title = overlap'__

Now, we can compute an area- and object-based colocalisation using below commands. 

- **[Analyze>Set Measurements..]**	
	- [X] 'Display label'
		- this is nice, because it will associate measurements with the name of the image (and ROI) on which they were computed.
- For all three images...
	- **'synthetic-data-ch1-segmented.tif'**
	- **'synthetic-data-ch2-segmented.tif'**
	- **'overlap'**
- ...perform a particle analysis:
	- **[ Analyze > Analyze Particles ]**
		- Especially for the **overlap** image carefully think about the **Size** filter, which enables you to set a threshold for a minimal overlap for an object to be counted as colocalizing.	
		- [X] 'Display Results' 
		- [X] 'Summarize' 
		- Select: 'Display Labels' 
- Object based colocalization: __Count__
	- coloc1 = overlap / ch1
	- coloc2 = overlap / ch2
- Area based colocalization: __Area__ (e.g., )
	- coloc1 = overlap / ch1
	- coloc2 = overlap / ch2

### Discussion points

- Many parameters influencing the results, thus a tricky business! In general the strategy would be to use the exact same parameters for a treated and a control sample.
- Before you measure colocalization it is very recommended to read the literature mentioned above!
- If you want to include intensities please look at the [Manders' correlation coefficients](https://imagej.net/_images/2/24/Manders.pdf)

## Optional activity: work on real data

Repeat above workflow using the data:

- ../colocalization/real-data-ch1.tif
- ../colocalization/real-data-ch2.tif
