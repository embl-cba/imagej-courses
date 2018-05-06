# Colocalisation: Pixel-, distance- and object-based

Literature: [A guided tour into subcellular colocalization analysis in light microscopy. S. B O LT E & F. P. C O R D E L I È R E S Journal of Microscopy, Vol. 224, 2006, pp. 213–232.](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2818.2006.01706.x/epdf)

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

## Segmentation: Local background subtraction and thresholding

First we segment the images, i.e. we make objects pixels 255 and background pixels 0.

- __[File>Open..] '“../colocalization/stain1.tif”__
- __[Image>Rename..] 'Title=original'__
- __[Image>Duplicate] 'Title=median'__
- __[Process>Filters>Median..] 'radius=20'__ 
	- 3D: [Process>Filters>Median 3D..]
- __[Process>Image Calculator] 'Image1 = original' 'Operation = Subtract' 'Image2 = median' 'Create new window=Check'__ 
- __[Image>Adjust>Threshold..] 'lower th=30' 'upper th=255'__ (*you don't have to press [Apply] now, the actual 'applying' of the threshold will happen in the next step*)
- __[Analyze>Analyze Particles..] 'Size = 5-Infinity' 'Pixel units = Check' 'Show = Masks' [OK]__ (*selecting 'Show = Masks' generates a binary image in which only 'connected components' of at least 5 pixels are kept, i.e. 'noise' is filtered*)
	- for 3D use [Analyze>3D Objects Counter]  
- __[File>Save As..] '“../colocalization/stain1_segmented.tif”__
- You also have to do this "stain2.tif"...

## Area, object and distance-based colocalization

First we load the data and compute the overlap image:

- __[File>Open..] '“../colocalization/stain1_segmented.tif”__
- __[File>Open..] '“../colocalization/stain2_segmented.tif”__
- __[Process>Image Calculator] 'stain1_segmented.tif' 'AND' 'stain2_segmented.tif'__
- __[Image>Rename..] 'Title = overlap'__

Now, you can compute an area-based, object-based or distance-based colocalisation:


- __[Analyze>Set Measurements..] 'Centroid = Check'  'Display label = Check'__ *('Display label = check': this will associate measurements with the name of the image (and ROI) on which they were computed.)*
- For all three images, i.e. __'stain1_segmented.tif', 'stain2_segmented.tif', 'overlap'__, run the following command : 
	- __[Analyze>Analyze Particles] 'Display Results = Check' 'Summarize =Check' 'Display Labels__ 
		- for 3D use [Analyze>3D Objects Counter] 
		- choose particle selection criteria that make sense for your project... 
- Object based colocalization: __Count__ (e.g., divide overlap by stain1) 
- Area based colocalization: __Area__ (e.g., divide overlap by stain1)
- Distance based colocalization: you have to write some code to find particles that are next to each other in the Results tables

