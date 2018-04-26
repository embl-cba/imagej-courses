# Workflow: Autophagosome quantification

In the following you will learn all the ingredients to perform a very typical cell biology image analysis workflow.

Your working directory is: __'../data/workflow_autophagosomes'__. This folder contains the two main input files __'autophagosomes_raw.tif'__ and __'nuclei_raw.tif'__. There are also __a lot of other files__ stored, some of which you will generate during the course. You will __overwrite__ most of those files __with your own results__!

If you messed up or missed a step there also is a sub-folder __'teacher'__, form which you can load all files that you need during the practicals :-)


## What to measure?

<img src="https://github.com/tischi/imagej-courses/blob/master/presentation/bothChannels.jpg" width=200/>

- __[File>Open..] 'bothChannels.jpeg'__

- Number of spots per cell
	- autophagosome initiation
	- not a 3-D image, but you could squeeze your cells...
- Size of spots
	- diffraction limit!
- Average intensity of one spot
	- diffraction limit!
	- how large should i draw my ROI?
- Sum intensity of one spot
	- autophagosome maturation
	- technical considerations:
		- microscope settings change intensities
		- total expression level changes intensities
		- good to divide by total cell intensity => fraction of protein localized to one autophagosome
		-  local background correction needed for spot intensity
- Total cell intensity
	- proportional to total amount of protein (in wide-field microscopy)
- Mean intensity of each cell
	- not clear what the biological meaning in the wide-field images is. 



## Local background subtraction <a name="local-background-subtraction"></a>

In biological fluorescence microscopy one often wants to detect locally bright objects such as vesicular structures on top of a non-uniform background fluorescence, e.g. from unbound cytoplasmic protein. There are different methods to remove such 'background' fluorescence from the image:

- corrected\_image = image - mean\_filter(image, radius) 
- corrected\_image = image - median\_filter(image, radius) 
- corrected\_image = image - morphological\_opening(image, radius) = top\_hat(image, radius)
- corrected\_image = IJs "RollingBall" Algorithm
- *someone knowing other methods?*

In all methods the *radius* parameter should be "quite a bit larger" than the radius of the largest locally bright structure that you want to measure (why that is becomes clear when we discuss the methods in detail).

### Local background subtraction using a median filter

<img src="https://github.com/tischi/imagej-courses/blob/master/presentation/orig__median__subtraction.png" width=700/>

Duplicate image and apply median filter to remove the locally bright spots. Then subtract the median filtered image from the raw image and save the result for later use. 

- __[File>Open..] 'autophagosomes_raw.tif'__
- __[Image>Rename..] 'Title=original'__
- __[Image>Duplicate] 'Title=median'__
- Select the 'median' image and __[Process>Filters>Median] 'radius=5'__
- __[Process>Image Calculator] 'Image1 = original' 'Operation = Subtract' 'Image2 = median' 'Create new window=Check' '32-bit output=Uncheck'__ 
- __[File>Save] 'spots_median.tif'__


## Local background subtraction using a top-hat filter 

<img src="https://github.com/tischi/imagej-courses/blob/master/presentation/orig__open__tophat.png" width=700/>

A morphological opening filter is applied to the image and subtracted from the original. The morphological opening is defined as the dilation of the erosion if the image. Alltogether this reads: top_hat(image) = image - dilation(erosion(image))

- __[File>Open..] 'autophagosomes_raw.tif'__
- __[Image>Rename..] 'Title=original'__
- __[Image>Duplicate] 'Title=opened'__
- __[Process>Filters>Minimum..] 'radius=5'__ 
- __[Process>Filters>Maximum..] 'radius=5'__ 
- __[Process>Image Calculator] 'original' 'Subtract' 'opened' 'Create new window=Check' '32-bit output=Uncheck'__ 
- __[File>Save] 'spots_tophat.tif'__


## Local background subtraction using IJs "Subtract Background"

<img src="https://github.com/tischi/imagej-courses/blob/master/presentation/orig__bg__rollingball.png" width=700/>

- __[File>Open..] 'autophagosomes_raw.tif'__
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

Above local background subtraction methods already helped a lot to enhance the spots; however in some cases there might still be some patchy locally bright regions left that are not corresponding to "real" spots. The reason is that the local background subtraction methods cannot distinguish locall bright elongated from locally bright round objects. Convolution of the image with a [Laplacian of Gaussian](https://en.wikipedia.org/wiki/Blob_detection#The_Laplacian_of_Gaussian) filter can help to further enhance spots of a certain size. 

- ...


## Spot detection using 'Find Maxima'

ImageJ's 'Find Maxima' considers a pixel a maximum if its intensity is higher - by the 'Noise tolerance' - than neighboring pixels; see [Topographic prominence](http://en.wikipedia.org/wiki/Topographic_prominence). 

- __[File>Open] 'spots_median.tif'__
- __Draw a line ROI__ across some of the spots and __[Analyze>Plot Profile]__
	- Check how many gray values the spots 'stand out'; use this value as 'Noise tolerance' in the next step
- __[Process>Find Maxima..] 'Noise tolerance=20' 'Output type=Single Points'__
	- check __'Preview point selection'__ and explore different 'Noise tolerance' values!
- __[Process>Math>Divide..] 'Value=255'__
	- => spot pixel will have a value of 1 (better for counting them later..)
	- The image will appear white; you have to adjust the contrast to see the dots __[Image>Adjust>Brightness/Contrast]__ 
- __[File>Save] 'spots_points.tif'__	


#### Exercise: Explore influence of local background removal   

- __[File>Open..] 'autophagosomes_raw.tif'__
- __[Process>Filters>Gaussian Blur..] 'sigma=15'__ (this removes the spots)
- __[Process>Find Maxima..] 'Noise tolerance=100'__

As you can see there are maxima detected only due to the cellular background. If you do the same using 'spots_median.tif' - where the background was removed - as input image there should be no maxima (for this 'Noise tolerance').


## Cell detection using seeded watershed

<img src="https://github.com/tischi/imagej-courses/blob/master/presentation/cell_segmentation_watershed.png" width=700/>

The seeded watershed algorithm implemented in ImageJ's 'Find Maxima' first finds local intensity maxima as starting ('seed') points.  From these seed points it performs a 'region growing' algorithm, using the intensity information in the image to draw dividing lines at dim parts of the image.   

- __[File>Open] 'autophagosomes_raw.tif'__
- __[Process>Filters>Gaussian Blur..] 'sigma=10'__ (*removes features that  'distract' from the overall cell shape*)
- __[Process>Find Maxima..] 'Noise tolerance=50' 'output=Segmented Particles'__ (*choosing 'Segmented Particles' invokes the Wathershed algorihm*)
- __[File>Save] 'cells_bw.tif'__

Explanation for this use-case: Look at the image after blurring it. Then imagine it starts raining. Now imagine where water running down from the different hills (bright pixels) would meet. Those are the dividing lines.

#### Exercise

Try the same leaving out the 'Gaussian Blur' step. Can you get it to work?


## Generate cell 'objects' that can be used for measurements

We run the 'Particle Analyzer' to convert the binary cell image into 'objects' (i.e., regions of interest = ROIs). This will be handy later for cell-based measurements. 

- __[File>Open] 'cells_bw.tif'__
- __[Analyze>Analyze Particles..] 'Exclude on edges = Check' 'Add to Manager = Check'__ 
- __[File>Open] '../data_course/autophagosomes_raw.tif'__
- Click on the ROIs in the ROI Manager to see them overlayed on the raw data.

#### Exercise: Exclude cells based on their shape 

1. Explore all the different output options of the 'Particle Analyzer'!
2. Experiment with different particle exclusion criteria. For example: 

- Close 'ROI Manager' and select image: 'cells_bw.tif'
- __[Analyze>Analyze Particles..] 'Exclude on edges = Do Not Check' 'Add to Manager=Check'__ 
	- Try: '__Size = 15000-Infinity__' and '__Circularity = 0.00-1.00__'
	- Or try: '__Size = 0-Infinity__' and '__Circularity = 0.60-1.00__'
		- Click __[Help]__ to figure out what 'Circularity' is.


## Improved cell detection by excluding background pixels

<img src="https://github.com/tischi/imagej-courses/blob/master/presentation/cell segmentation.png" width=400/>


The problem of the seeded watershed algorithm is that the 'grows into the background' (see image). To avoid this one has to threshold the cells and combine this with the results of the watershed:

- __[File>Open] 'autophagosomes_raw.tif'__
- __[Process>Filters>Gaussian Blur..] 'sigma=5'__ (*just to get rid of some noise*)
- __[Image>Adjust>Threshold..] 'lower th=230' 'upper th=Max' [Apply]__
- __[Image>Rename..] 'foreground'__ (*all background pixels are zero*)
- __[File>Open] 'cells_bw.tif'__ (*this is the image that we got from the watershed*)
- __[Process>Image Calculator..] 'foreground' 'AND' 'cells_bw.tif' [OK]__ (*we combine both...*)
- __[File>Save] 'cells_bw_improved.tif'__ (*...and get an image where we removed the background pixels and still have dividing lines between the cells*)
- __[Analyze>Analyze Particles..] 'Size=100-Infinity' 'Exclude on edges=Check' 'Add to Manager=Check'__  (*simply finds the cell objects*)
- __[ROI Manager>More>>Save..] 'cells_improved.zip'__

## Measure spots per cell

ImageJ can measure lots of features. To have our readout more "to-the-point" we will first only select a small subset: 

- __[Analyze>Set Measurements..] 'Area = Check' 'Integrated Density = Check' 'Mean gray value = Check'__

To measure how many 'spots' (vesicular structures) we have in each cell, we simply measure in each cell ROI the integrated intensity in the 'spots_points.tif' image, where each pixel marking a spot has the value 1 (that is a very typical trick in image analysis :-).

- __[File>Open] 'spots_points.tif'__ (*you may see nothing on this image...do you know why?*)
- __[Image>Adjust>Brightness/Contrast..] [Auto]__
- __[Analyze>Tools>ROI Manager..]__
- __[ROI Manager>More>>Open..] 'cells.zip'__
- __[ROI Manager>Measure]__
- Click on Results Table and __[File>Save] 'spot_count.csv'__

The 'RawIntDen' value is the spot count. How many spots did you find?

#### Exercise
Manually draw a region on the image, add it to the ROI Manager __[ROI Manager>Add]__ and measure the number of spots in this region.

## Manual background subtraction on whole image

If we want to measure total cell intensity in a biophysically meaningful way we have to set the image background intensity to zero.  Since cells can grow dense it can be difficult or even impossible to find the correct background value in one image. Thus, sometimes one has to manually subtract a fixed background value from the image. 

(=> Whiteboard session: why background subtraction; why convert to 32-bit.)

- __[File>Open..] 'autophagosomes_raw.tif'__
- __[Image>Adjust>Brightness/Contrast] 'Minimum=190' 'Maximum=230'__
- Measure background intensity: draw a little ROI in the background and __[Analyze>Measure..]__ 
- __[Image>Type>32-bit]__
- __[Process>Math>Subtract..] 'Value=194'__ (*Possible pitfall: if you had a ROI on the image the value was only subtracted in this ROI*) 
- __[File>Save As>Tiff..] 'autophagosomes_bgcorr.tif'__
- Measure background intensity again using __[Edit>Selection>Restore Selection..]__ to get the same ROI (*should be zero now*)

#### Exercise
Do the same but leave out the 32-bit conversion step. Now measure the intensity in the background after correction! What happens? 

## Compute nuclear distance map
(=> Whiteboard session on Distance Transform)

<img src="https://github.com/tischi/imagej-courses/blob/master/presentation/distance map.png" width=400/>

Quite often in biology one wants to know how far a certain structure is away from another (e.g. endocytosis: vesicles from plasma membrane). Such distances often can be quite easily measured using the 'Distance Transform'.

- __[File>Open..] 'nuclei_raw.tif'__
- __[Image>Adjust>Threshold..] 'lower = 500' 'upper = Maximum' [Apply]__
- __[File>Save As>Tiff..] 'nuclei_bw.tif'__
- __[Edit>Invert]__ (*check: nuclei pixels should now be 0 and background 255; needed for Distance Map*)  
- __[Process>Binary>Options..] 'EDM output=32-bit'__ (*enables distances >255*)
- __[Process>Binary>Distance Map]__ (*pixel values are now distances to nearest nucleus*)
- __[File>Save As>Tiff..] 'nuclei_dist.tif'__

#### Exercise
...

## Use nuclear distance map on detected spots

In order to measure the distance of each previously detected spot to the nucleus we (almost) simply multiply the distance map with the spot image. The only problem we have is that a zero in the final image could mean: (i) there was no spot or (ii) there was a spot but its distance to the nucleus was zero. To distinguish these cases we will set non-spot pixels to NaN (Not a Number) before we do the multiplication 

<img src="https://github.com/tischi/imagej-courses/blob/master/presentation/spots dist2nuc.png" width=400/>


- __[File>Open..] 'spots_points.tif'__ (*pixel values: 1 = spot; 0 = no spot*)

Set non spot pixels to NaN (Not a Number):
- __[Image>Type>32-bit]__ (*necessary to enable NaN values*)
- __[Image>Adjust>Threshold..] [Set] 'lower=0.5' 'upper=1' [Apply]__
	- When asked: __Check 'Set background pixels to NaN'__

Multiply spot image with distance image:
- __[File>Open..] 'nuclei_dist.tif'__ (*pixel values: distances to nearest nucleus*)
- __[Process>Image Calculator..] 'Image1 = nuclei_dist.tif' 'Operation = Multiply' 'Image2 = spots_points.tif' '32-bit result = Check'__ 
	- *the value of each pixel is now distance of the spot to nearest nucleus or NaN if there was no spot*
- __[File>Save As>Tiff..] 'spots_dist2nuc.tif'__


## Measure intensity inside autophagosomes
(=> Whiteboard session on intensity measurements in diffraction limited objects in the presence of local background (unbound protein))

Often one wants quantify the intensity of objects as it reports the amount of bound labelled protein. Here, we use the 'spots_median.tif' image, where the cytoplasmic background has already been subtracted. In order to restrict the intensity measurement to the region of the spots, we use the 'spots_point.tif' image, where the center of each spot has the value 1 and the other pixels are 0. In order to measure the whole spot intensity we will dilate this image and then multiply (mask) onto the 'spots_median.tif' image (for the masking we need to set pixels outside spots to NaN (Not a Number)).

- __[File>Open..] 'spots_points.tif'__ (*pixel values: 1 = spot; 0 = no spot*)
- __[Process>Filters>Maximum..] 'radius=2'__   (*enlarge spots to include all fluorescence*)
- __[File>Open..] 'spots_median.tif'__ (*pixel values: background corrected autophagosome intensities*)
- __[Process>Image Calculator..] 'Image1 = spots_points.tif' 'Operation = Multiply' 'Image2 = spots_median.tif' '32-bit result = Check'__ 
	- *pixel values: inside spots: background corrected spot intensity; outside spots: NaN*
- __[File>Save As>Tiff..] 'spots_intensity.tif'__

## Perform all kinds of cell based measurements 

Once we have the cell ROIs we can measure many cell-based features, simply loading different input images for the measurement: 

- __[Analyze>Tools>ROI Manager..]__ 
- __[ROI Manager>More>>Open..] 'cells.zip'__ or 'cells_improved.zip'

- __[File>Open] 'spots\_points.tif', 'autophagosomes\_bgcorr.tif', 'spots\_intensity.tif', and 'spots\_dist2nuc.tif'__ (*if you did not generate all these images yourself you can load them from the 'teacher' folder*) 
-  For each of above input images: 
	- Select the input image (i.e., click on it once)
	- __[ROI Manager>Measure]__ 
	- Click on the Results Table and __[File>Save] '*a good name*.csv'__
	- Close Results Table! (*otherwise the next measurement values will be appended in case you want to measure another image*)

#### Exercise
Try to remember the biological interpretation of these measurements. Think about ratios of any of the measured numbers.
