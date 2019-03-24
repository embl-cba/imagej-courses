# Batch analysis in ImageJ

There are several ways to achieve batch analysis of many images in ImageJ:
- Concatenating many images into one image (hyper-)stack 
- Using [Process > Batch]
- Writing scripts, e.g. using the ImageJ Macro language

## More information

- https://imagej.net/How_to_apply_a_common_operation_to_a_complete_directory
- https://imagej.net/Batch_Processing

## Batch analysis using image stacks

If your images have the same dimensions in x,y (and z) and you want to apply the exact same operation to all of them,
 the easiest option for batch analysis is to load all of them into one image (hyper-)stack.

### Concept

( apply operation ) -> [ Image1 ]
( apply operation ) -> [ Image2 ]
[ Image1 ], [ Image2 ], [ ImageN] -> ( concatenate ) -> [ Image Stack ] 
( apply operation ) -> [ Image stack ]

### Activity: Automatically count number of nuclei in many images <a name="AutoCount"></a>

Counting the number of objects in many images is one the most common bio-image analysis application; thus let's start with this!

Workflow:
- Load all images into an image stack
	- [File > Import > Image Sequence] 
		- '../data/mitocheck_movie'
- Threshold all images
	- [Image > Adjust Threshold]
		- [X] Dark background
		- [ ] Calculate threshold for each image
			- Uncheck this, otherwise some auto-thresholding is going on!
		- [Apply]
			- Yes, do it for the whole stack!
- Set measurements
	- [Analyze > Set measurements]
		- [X] Area
		- [X] Display label
			- this will keep track of the filename
- Find and measure the cells in all images
	- [Analyze > Analyze Particles...]
		- [X] Summarize
			- This will give you for each image the average results of all cells

### Dealing with data distributed across different folders

Often your data might not be in one folder. 
For example have a look at the folder:
"../data/data-in-subfolders"
To still load them into one image stack you can use a script that is provided in this repository:

- Drag & Drop onto Fiji: "../macros/import-from-subfolders.py"
- Press [Run]
	- Filename contains: ".tif"
	- Choose as folder: "../data/data-in-subfolders/"

You have all data in one stack and could for instance count the number of cells, as we learned above.

#### Comment

Like this, you cannot change the data and then save it back into the same folder-structure; this would require writing some macro code (see below)

### Good filenames are essential for batch-processing

[ Good filenames ] -- enable --> [ Batch processing ]
[ Good filenames ] -- have --> [ Naming pattern ]
[ Good filenames ] -- are --> [ Sorted properly ]

#### Examples for good filenames

```
ctrl-t-00000-of-00212.tif
ctrl-t-00001-of-00212.tif
ctrl-t-00002-of-00212.tif
```

```
treatment001-T0000-C00.tif
treatment001-T0001-C00.tif
treatment001-T0002-C00.tif
treatment001-T0000-C01.tif
treatment001-T0001-C02.tif
treatment001-T0002-C03.tif
```

#### Good filenames formative assessment

Given below filenames...

```
image-c00-t0000.tif
image-c00-t0001.tif
image-c00-t0002.tif
```
...which one is the correct next one (one answer)?

1. image-c00-t0003.tif
2. Image-c00-t0003.tif
3. image-c0-t3.tif
4. image_c00_t0003.tif


### Computing and saving 3-D maximum projections of many stacks

If you have 3-D data, all having the same x,y,z dimensions, you could implement batch operations using so-called "hyper-stacks"; the challenge here is to actually load the data into a hyperstack; once you have it, batch operations are easy.

### Making a hyperstack from single files, using [Import Image Sequence]

Sometimes data beloning to different image stacks is distributed across several files.
Here, you can see how to rearrange them into a hyper-stack after loading. 

Workflow:
- Load all images
	- [File > Import Image Sequence]
		- "../data/mitosis-5D-single-files/"
- Make a hyperstack
	- [Image > Hyperstack > Stack to Hyperstack]
		- Determine the correct dimensions inspecting the filenames 
		- Solution: 
			- Order: xyczt
			- Channels: 2
			- Time-frames: 51
			- Z-Slices: 5
- Make a maximum projection of all time-frames
	- [Image > Stacks > Z Project]: Projection Type: "Max Intensity"
- Save data as individual files
	- [File > Save as > Image Sequence]

In above workflow we had to manually enter the dimensions of the data.
If the filenames are very well structured those dimensions can be determined automatically as shown in the next workflow.

### Making a hyperstack from many single files using the Bioformats Importer

In order for this to work we need to install the very useful BioFormats plugin:
- [Help > Update]: 
	- [Manage Update Sites]: 
		- [X] Java-8
		- [X] Bio-Formats
		- [Close]
	- [Apply Changes]
- Restart Fiji
 

Workflow:
- Load individual files as hyperstack
	- [Plugins > Bio-Formats > Bio-Formats Importer]:
		- click on one file in the folder "../data/mitosis-5D-single-files/"
		- View stack with: "Hyperstack"
		- [X] Group files with similar names
			- You'll see how it interprets your file-naming scheme
		- [OK]
- Do the processing of your choice and save the data again using [File > Save as > Image Sequence]

### Construct a Hyperstack from individual image stack files

Another frequently occuring scenario is that you have 3-D data, where each file is one image stack.
In the following we will see how to deal with this case. In fact, you can still do the hyperstack trick, because the Bio-Formats plugin can automatically combine data from image stacks into one hyperstack.

##### Concept

[ 3D Image Stack File - 01 ], [ 3D Image Stack File - 02 ], [ .... ] -> ( grouped loading ) -> [ 5D Hyperstack ] 

##### Activity

- Load many stacks into one hyperstack
	- [Plugins > Bio-Formats > Bio-Formats Importer]:
		- click on one file in folder: "../data/mitosis-4D-stacks/"
		- View stack with: "Hyperstack"
		- [X] Group files with similar names
			- You'll see how it interprets your file-naming scheme
		- [OK]
- Do the processing of your choice, e.g. background subtraction
- Save the data again as individual stacks
	- [Plugins > Bio-Formats > Bio-Formats Exporter]
	- Note: the Bio-Formats Exporter has (had) a bug when doing this for multi-channel images

  
## Batch analysis using [Process > Batch]

If your images have different sizes above tricks using an image stack will not work. 
In such cases the next thing you can try is the batch-processing that is built into ImageJ.
 
### Converting various images to Tiff files

Data:
- Diverse images with different file formats and dimensions

Workflow:
- [Process > Batch > Convert]: 
	- Input: "../data/different-file-formats/"
	- Output: you can choose :-)
	- Leave other options at default values

### Display the filename on multiple images

It is good practice to have meaningful filenames, e.g., containing a particular treatment that your images were subjected to. For quick visual inspection of your data it can thus be useful to display the filename in the image.

Workflow:
- Use ImageJ's in-built batch processing, chosing one of the example macros.
	- [Process > Batch > Macro] 
		- Input: "../data/meaningful-filenames/"
		- Output: your choice 
		- Combine code from two of the example macros: "Print index and title", "Label"
			- ```setFont("SansSerif", 18, "antialiased");```
			- ```setColor("red");```
			- ```drawString(getTitle(), 20, 30);``` 
		- [Process]

Don't worry for now too much about the code; we will learn more about it later.

### Macro recording for putting a scale bar on multiple images

It is also very useful to have a scale bar in the images, e.g. for publication on a web-site.
There is no predefined macro for adding a scale bar in Process > Batch; thus we have to record the command on our own.

Workflow:
- Record the macro command for putting a scale bar:
	- [Plugins > Macros > Record..]
		- Record: Macro (not Java)
	- Open some file, e.g. "../data/meaningful_filenames/Treatment_A.tif"
	- Put a scale bar:
		- [Analyze > Tools > Scale Bar..]
			- choose some parameters that you like
			- [OK]
	- Now the window should show some text, such as:
		- ```run("Scale Bar...", "width=50 height=4 font=14 color=White background=None location=[Lower Right] bold");```

- Use the recorded text (copy & paste) to put a scale bar onto multiple images using [Process > Batch > Macro..] (see above)
 

