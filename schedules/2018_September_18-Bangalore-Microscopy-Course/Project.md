## Tasks

1. Practice opening *.czi image files in Fiji.
	1. Use *Bio-Formats* plugin
	2. Check options of the Bio-Formats import
	3. Extract experimental settings (metadata).

2. Change visual representation of the images
	1. different channels with different colors
	2. Both channels visible at the same time.
3. Crop several small regions each containing few cells and save for later data processing as *tiff* files. Big datasets can take a lot of time to process. We will do it later when protocol is created and scripts are assembled. 

4. Check 3D Visualisation options.

5. Project 3D volume data to 2D planes. 
	1. Try sum and max projections
	2. Which information is maintained and what is lost?

6. **Develop 3D image analysis protocol**
	1. Install and use [3D image suite](http://imagejdocu.tudor.lu/doku.php?id=plugin:stacks:3d_ij_suite:start) package. It provides you set of tools for 3D analysis.
	2. Segment nuclei in 3D. Use *Simple segmentation* tool.
	3. Segment foci in 3D. Use *Spot segmentation* tool.
	4. Discard spots which do not belong to any nuclei.
	5. Identify which foci belong to which nuclei.
	6. Count foci in each nucleus
	7. Measure intensity of each foci. When storing intensity values, try to keep information about parent nuclei 

7. **Create a macros or script implementing the developed workflow**
	1. To understand macro recording and scripting principles, you can start with simple workflow such as segmenting cells in 2D.
	2. Create following versions of the macros
		1. Processing image which is currently opened
		2. Selecting individual file to process
		3. Selecting range of files to process
	3. Implement options to save tables with intensity measurements and images with segmentation results.
	4. Modify macros to work with original czi files. 





## Control questions

1. How to extract metadata from the image file. Are metadata maintained when changing image and saving it in the different format?

2. What are the options to represent/visualise 3D datasets?

3. What are the possibilities to represent regions in 2D and 3D?

4. How to identify which secondary object (dot) belongs to which primary object (nucleus)

5. How to change the macros from processing single images to processing multiple images (batch processing), without modifying/changing all code?


## Relevant links
1. [Old ImageJ webpage](https://imagej.nih.gov/ij/). Contains well documented basic functionality and examples
2. [New ImageJ webpage](https://imagej.net/). A lot of materials about more recent developments and advance features
3. [ImageJ forum](https://forum.image.sc/)
4. Google always helps)))
