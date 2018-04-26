## Automation using the IJ macro language 

In order to apply the previous measurements to more than one image, we will now automate all the step that we did previously. For this we will use the ImageJ Macro language (http://rsb.info.nih.gov/ij/developer/macro/macros.html) and ImageJ's inbuilt  Macro Recorder [Plugins>Macros>Record].

### Create a macro for automated cell detection

First clean up things, e.g. by restarting ImageJ, and then turn on the Macro Recorder [Plugins>Macros>Record..]

Execute below commands for automated cell detection (these are the same commands we used earlier):

- [File>Open] 'autophagosomes_raw.tif'
- [Process>Filters>Gaussian Blur..] 'sigma=10'
- [Process>Find Maxima..] 'Noise tolerance=100' 'Output type=Segmented Particles'
- [Analyze>Analyze Particles..] 'Size=100-Infinity' 'Exclude on edges=Check' 'Add to Manager=Check' 
- In the Macro Recorder click [Create].
	- The 'Script Editor' with your macro will appear. 
- Close all windows (also the ROI Manager).
- In the Script Editor click [Run].
	- Did it work? If yes: great! Maybe your first code! 
- Script Editor: [File>Save As..] '.../CellDetection.ijm'

#### Advanced task

Look at the macro for the improved cell detection with exclusion of background pixels:
- [File>Open..] '.../teacher/CellDetection2.ijm'
Try to understand the code. Look up commands that you don't know on
http://rsb.info.nih.gov/ij/developer/macro/functions.html

### Create a macro for automated spot detection

First clean up things, e.g. by simply restarting ImageJ, and turn on the Macro Recorder [Plugins>Macros>Record..]

Execute below commands for automated spot detection (same commands we used earlier):

- [File>Open] 'autophagosomes_raw.tif'
- [Image>Rename..] 'Title=raw'
- [Image>Duplicate] 'Title=median_bg'
- Select 'median_bg' image and [Process>Filters>Median] 'radius=5'
- [Process>Image Calculator] 'raw' 'Subtract' 'median_bg' 'Create new window=Check' '32-bit output=Uncheck' 
- [Process>Find Maxima..] 'Noise tolerance=100' 'Output type=Single Points'
- [Process>Math>Divide..] 'Value=255'
- [Image>Rename..] 'spots_points.tif'

- Script Editor: [File>Save As..] '.../SpotDetection.ijm'
- Script Editor: [Run]

### Combine cell- and spot-detection macros and add the spot-per-cell measurement

Open both macros (of course, if you have them both open already you can skip this step) and then simply code and paste the SpotDetection code below the CellDetection code.

- [File>Open] 'CellDetection.ijm' (or 'CellDetection2.ijm')
- [File>Open] 'SpotDetection.ijm'
- Script Editor: Copy code of SpotDetection below CellDetection
- Script Editor: [File>Save] 'CellAndSpotDetection.ijm'
- Script Editor: [Run] 

Now we need to add the spot-per-cell counting by recording the appropriate macro commands:

- Close the Macro Recorder and restart it: [Plugins>Macros>Record..]
- Click on the 'spots_points.tif' image
- Roi Manager: [Measure]
- Results table: [File>Save As..] 'spot_count.csv'
- Macro Recorder: [Create]
- Script Editor: Copy your new code at end of 'CellAndSpotDetection.ijm' 
- Script Editor: [File>Save] 'CellAndSpotDetection.ijm'
- Script Editor: [Run]

#### Exercise 

Run the code twice in a row without closing any windows. Confirm that both the content of the ROI Manager and the content of the Results table get messed up. What happens?

### Close all windows in a macro (help yourself!)

We saw above that we need to automatically close Results Table and ROI Manager before running our macro. Also it would be good to close all image windows. In this case macro recording not always helps (at least on the teachers Mac for a specific version of ImageJ and Fiji). Try to find the right commands using any of the following approaches:

- Have some images, Results Table and ROI Manager open (e.g. run CellAndSpotDetection.ijm) and record yourself closing them all [Plugins>Macros>Record..]; [Create] the macro and try if it works!
- Google: 'imagej macro close results table'
- Google: 'imagej macro close roi manager'
- Google: 'imagej macro close all images'

What did you find?

If you found nothing useful you can see what I found:

- [File>Open..] '../teacher/closeEverything.ijm'

## Adding a function to close all windows

Above we already found the commands to close all windows. Here we will see how to neatly pack them into a "function" such they can be called conveniently from every point of your macro.

- [File>Open..] '../teacher/CellAndSpotDetection_Improved.ijm'
- Script Editor: [Run]
	- run it again: as you see now it works even twice!

=> Discussion of the code with help of teacher.

## Adding code to select an arbitrary image

Right now our 'CellAndSpotDetection_Improved.ijm' only runs on one specific image. Let's look at a slightly modified version that makes it useable for any given input image:

- [File>Open..] '../teacher/CellAndSpotDetection_ChooseImage.ijm'
	- do you understand the code?
- [Run] macro on files in '../data_small/'
- [Run] macro on files in '../data_large/'

=> Discussion of the code with help of teacher.

## Batch me if you can

Of course, we'd like to run a macro on many images. In ImageJ there is the function [Process>Batch>Macro..], which automatically applies a macro to all files in the 'Input..' folder. However, this function is very limited, for instance it cannot handle saving results tables.    

As a more flexible alternative here is some code that handles the batch processing and you (more-or-less) only have to copy and paste your specific macro into it:

- [File>Open..] '../teacher/runAsBatch.ijm'

This code involves some 'real programming' that, in principle, you don't have to understand to use it. We will anyway discuss it together just to give you an idea.

(=> Discussion of the code with teacher.)

## Batch cell and spot detection

Ok, let's have a look the final code, which apart from a few marked changes is just the central part of 'CellAndSpotDetection_ChooseImage.ijm' copied into 'runAsBatch.ijm':

- [File>Open..] '../teacher/CellAndSpotDetection_Batch.ijm'
- [Run] on 'data_small'
- [Run] on 'data_large'
- Examine the output tables in Excel


#### Exercise

Think about the following: Is this code ready to use for a project? What is missing? 


## Batch processing considerations  

The macro 'CellAndSpotDetection_Batch.ijm' is not bad but it is also missing a few things:

- possible: add more measurements; they could be simply added by recording and copying more code into the current script.
- essential: saving of output images for visual quality control!
	- e.g., raw data with overlay of cell boundaries
	- e.g., raw data with overlay of detected spots
- possibly: add graphical user interface for some of the parameters:
	- e.g., minimal cell size
	- e.g., 'noise tolerance' for spot detection
	- e.g., threshold that distinguishes background from cells
- possibly: add more cell filter criteria:
	- e.g., remove cells from analysis that do not express enough protein

It is possible to add all this in ImageJ however I highly recommend to also check the free [CellProfiler](http://cellprofiler.org) software. CellProfiler enables you to perform these operations without actual programming. Note that as of June 2015 CellProfiler only works for 2-D data but this may change.
