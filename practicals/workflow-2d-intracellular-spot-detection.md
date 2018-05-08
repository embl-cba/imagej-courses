# Workflow: Autophagosome quantification

In the following you will learn all the ingredients to perform a very typical cell biology image analysis workflow.

Your working directory is: __'../data/workflow_autophagosomes'__. This folder contains the two main input files __'autophagosomes_raw.tif'__ and __'nuclei_raw.tif'__. There are also __a lot of other files__ stored, some of which you will generate during the course. You will __overwrite__ most of those files __with your own results__!

If you messed up or missed a step there also is a sub-folder __'teacher'__, form which you can load all files that you need during the practicals :-)


## What to measure?

<img src="https://github.com/tischi/imagej-courses/blob/master/images/bothChannels.jpg" width=400/>

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
		- local background correction needed for spot intensity
- Total cell intensity
	- proportional to total amount of protein (in wide-field microscopy)
- Mean intensity of each cell
	- not clear what the biological meaning in a wide-field images is. 

## Local background subtraction to enhance the vesicles (using a median filter)

<img src="https://github.com/tischi/imagej-courses/blob/master/images/orig__median__subtraction.png" width=700/>

There is a lot of "background" signal from unbound protein which we need to remove to simplify the spot detection.

Duplicate the input image and apply a median filter to remove the locally bright spots, generating a background image, consisting of unbound protein, diffusing in the cell:

- __[File>Open..] '../workflow_autophagosomes/autophagosomes_raw.tif'__
- __[Image>Rename..] 'Title=original'__
- __[Image>Duplicate] 'Title=median'__
- Select 'median' image and __[Process>Filters>Median] 'radius=5'__

Now subtract the median filtered "background" image from the input image to obtain an image where the spots are enhanced:

- __[Process>Image Calculator] 'Image1 = original' 'Operation = Subtract' 'Image2 = median' 'Create new window=Check' '32-bit output=Uncheck'__ 

Save result for later use:
- __[File>Save] 'spots_median.tif'__

### Optional activity

Explore different radii for the median-based background subtraction: e.g., 1 or 50. 
What happens in those cases? Are the spots still nicely highlighted?

## Spot detection using 'Find Maxima'

For spot counting we will now create one binary image with exactly one pixel per spot. This will greatly simplify automated cell-based spot counting later on.

- __[File>Open] 'spots_median.tif'__
- __Draw a line ROI__ across some of the spots and __[Analyze>Plot Profile]__
	- Check how many gray values the spots 'stand out'; use this value as 'Noise tolerance' in the next step
- **[Process>Find Maxima..]**
	- Noise tolerance = ...
	- Output type = Single Points
	- check __'Preview point selection'__ and explore different 'Noise tolerance' values!
- **[Process>Math>Divide..]**
	- Value = 255
	- => spot pixels will have a value of 1 (better for counting them later..)
	- The image will appear white; you have to adjust the contrast to see the dots __[Image>Adjust>Brightness/Contrast]__ 
- __[File>Save] 'spots_points.tif'__	

### Algorithmic details

ImageJ's 'Find Maxima' considers a pixel a maximum if its intensity is higher - by the 'Noise tolerance' - than neighboring pixels; see [Topographic prominence](http://en.wikipedia.org/wiki/Topographic_prominence). 


## Cell detection using a seeded watershed

<img src="https://github.com/tischi/imagej-courses/blob/master/images/cell_segmentation_watershed.png" width=700/>

Since we have the spots, we now need to find the cells in order to count the number of spots per cell:

- __[File>Open] 'autophagosomes_raw.tif'__
- __[Process>Filters>Gaussian Blur..] 'sigma=10'__ (*removes features that  'distract' from the overall cell shape*)
- __[Process>Find Maxima..] 'Noise tolerance=50' 'output=Segmented Particles'__ (*choosing 'Segmented Particles' invokes the Wathershed algorihm*)
- __[File>Save] 'cells_bw.tif'__

### Algorithmic details

The seeded watershed algorithm implemented in ImageJ's 'Find Maxima' first finds local intensity maxima as starting ('seed') points. From these seed points it performs a 'region growing' algorithm, using the intensity information in the image to draw dividing lines at dim parts of the image.  

Explanation for this use-case: Look at the image after blurring it. Then imagine it starts raining. Now imagine where water running down from the different hills (bright pixels) would meet. Those are the dividing lines.

#### Optional activity

Try the same leaving out the 'Gaussian Blur' step. Can you get it to work?


## Generate cell 'objects' that can be used for measurements

We run the 'Particle Analyzer' to convert the binary cell image into 'objects' (i.e., regions of interest = ROIs). This will be handy later for cell-based measurements. 

- __[File>Open] 'cells_bw.tif'__
- __[Analyze>Analyze Particles..] 'Exclude on edges = Check' 'Add to Manager = Check'__ 
- __[File>Open] '../data_course/autophagosomes_raw.tif'__
- Click on the ROIs in the ROI Manager to see them overlayed on the raw data.

#### Optional activity: Getting familiar with the Particle Analzyer

1. Explore all the different output options of the 'Particle Analyzer'!
2. Experiment with different particle exclusion criteria. For example: 

- Close 'ROI Manager' and select image: 'cells_bw.tif'
- __[Analyze>Analyze Particles..] 'Exclude on edges = Do Not Check' 'Add to Manager=Check'__ 
	- Try: '__Size = 15000-Infinity__' and '__Circularity = 0.00-1.00__'
	- Or try: '__Size = 0-Infinity__' and '__Circularity = 0.60-1.00__'
		- Click __[Help]__ to figure out what 'Circularity' is.


## Optional: Improved cell detection by excluding background pixels

<img src="https://github.com/tischi/imagej-courses/blob/master/images/cell segmentation.png" width=400/>

The problem of the seeded watershed algorithm is that it 'grows into the background' (see image). To avoid this one has to threshold the cells and combine this with the results of the watershed:

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

To measure how many spots we have in each cell, we simply measure in each cell ROI the integrated intensity in the 'spots_points.tif' image, where each pixel marking a spot has the value 1 (that is a very typical trick in image analysis :-).

Configure measurements:

- __[Analyze>Set Measurements..] 
	- [X] Area
	- [X] Integrated Density
	- [X] Mean gray value

Perform cell based measurements:

- __[File>Open] 'spots_points.tif'__ 
	- *you may see nothing on this image...do you know why?*
- __[Image>Adjust>Brightness/Contrast..] [Auto]__
- __[Analyze>Tools>ROI Manager..]__
- __[ROI Manager>More>>Open..] 'cells.zip'__
- __[ROI Manager>Measure]__
- Click on Results Table and __[File>Save] 'spot_count.csv'__

The 'RawIntDen' value is the spot count. How many spots did you find?

## Measure intracellular spot location, using a distance map

(=> Whiteboard session on Distance Transform)

<img src="https://github.com/tischi/imagej-courses/blob/master/images/distance map.png" width=400/>

Quite often in biology one wants to know how far a certain structure is away from another (e.g. endocytosis: vesicles from plasma membrane). Such distances can often be quite easily measured using the 'Distance Transform'.

- __[File>Open..] 'nuclei_raw.tif'__
- __[Image>Adjust>Threshold..] 'lower = 500' 'upper = Maximum' [Apply]__
- __[File>Save As>Tiff..] 'nuclei_bw.tif'__
- __[Edit>Invert]__ (*check: nuclei pixels should now be 0 and background 255; needed for Distance Map*)  
- __[Process>Binary>Options..] 'EDM output=32-bit'__ (*enables distances >255*)
- __[Process>Binary>Distance Map]__ (*pixel values are now distances to nearest nucleus*)
- __[File>Save As>Tiff..] 'nuclei_dist.tif'__


## Use nuclear distance map on detected spots

In order to measure the distance of each previously detected spot to the nucleus we (almost) simply multiply the distance map with the spot image. The only problem we have is that a zero in the final image could mean: (i) there was no spot or (ii) there was a spot but its distance to the nucleus was zero. To distinguish these cases we will set non-spot pixels to NaN (Not a Number) before we do the multiplication 

<img src="https://github.com/tischi/imagej-courses/blob/master/images/spots dist2nuc.png" width=400/>


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

## Manual background subtraction on whole image

Usually it is a good idea to normalise the spot intensities to the overall expression level in each cell. If we want to measure total cell intensity properly we have to set the image background intensity to zero. Since cells can grow dense it can be difficult or even impossible to find the correct background value in one image. Thus, sometimes one has to manually subtract a fixed background value from the image. 

- __[File>Open..] 'autophagosomes_raw.tif'__
- __[Image>Adjust>Brightness/Contrast] 'Minimum=190' 'Maximum=230'__
- Measure background intensity: draw a little ROI in the background and __[Analyze>Measure..]__ 
- __[Image>Type>32-bit]__
- __[Process>Math>Subtract..] 'Value=194'__ 
	- *Likely pitfall: if you had a ROI on the image the value was only subtracted in this ROI*
- __[File>Save As>Tiff..] 'autophagosomes_bgcorr.tif'__
- To be sure measure the background intensity again using __[Edit>Selection>Restore Selection..]__ to get the same ROI
	- *it should be zero now*

#### Optional activity: Importance of 32-bit conversion for image-based background subtraction

Do the same but leave out the 32-bit conversion step. Now measure the intensity in the background after correction! What happens? 


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

#### Optional activity: Think about the results

Try to remember the biological interpretation of these measurements. Think about ratios of any of the measured numbers.
