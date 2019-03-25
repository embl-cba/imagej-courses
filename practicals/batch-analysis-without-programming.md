# Batch analysis in ImageJ

There are several ways to achieve batch analysis of many images in ImageJ:

- Concatenating many images into one image (hyper-)stack 
- Using [Process > Batch]
- Writing scripts, e.g. using the ImageJ Macro language

## More information

- https://imagej.net/How_to_apply_a_common_operation_to_a_complete_directory
- https://imagej.net/Batch_Processing

## 2D Batch analysis using image stacks

If your images have the same dimensions in x,y (and z) and you want to apply the exact same operation to all of them,
 the easiest option for batch analysis is to load all of them into one image (hyper-)stack.

### Concept

- ( apply operation ) -> [ Image1 ]
- ( apply operation ) -> [ Image2 ]
- [ Image1 ], [ Image2 ], [ ImageN] -> ( concatenate ) -> [ Image Stack ] 
- ( apply operation ) -> [ Image stack ]

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

## Good filenames are essential for batch-processing

- [ Good filenames ] -- enable --> [ Batch processing ]
- [ Good filenames ] -- have --> [ Naming pattern ]
- [ Good filenames ] -- are --> [ Sorted properly ]

### Examples for good filenames

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

### Good filenames formative assessment

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


## 3D Batch analysis using Hyperstacks

### Concept

( apply operation ) -> [ Image stack 0 ]
( apply operation ) -> [ Image stack 1 ]
[ Image stack 0 ], [ Image stack 1 ], [ ... ] -> ( concatenate ) -> [ Image Hyperstack ] 
( apply operation ) -> [ Image Hyperstack ]

### Construct a Hyperstack from individual image stack files

A frequently occuring scenario is that you have 5D data distributed across several 3D image files.
In the following we will see how to deal with this case. 

#### Concept

[ 3D image file 0 ], [ 3D image file 1 ], [ .... ] -> ( grouped loading ) -> [ 5D Hyperstack ] 

#### Activity

Load many 3D stacks into one Hyperstack and preform a maximum projection for each 3D stack.

In order for this to work we first need to **install the BioFormats plugin**:

- [Help > Update]: 
	- [Manage Update Sites]: 
		- [X] Java-8
		- [X] Bio-Formats
		- [Close]
	- [Apply Changes]
- Restart Fiji
 

- Load many stacks into one hyperstack
	- [Plugins > Bio-Formats > Bio-Formats Importer]:
		- click on one file in folder: "../data/mitosis-4D-stacks/"
		- View stack with: "Hyperstack"
		- [X] Group files with similar names
			- You'll see how it interprets your file-naming scheme
		- [OK]
- Perform an operation on the whole hyperstack, e.g. 
	- Compute a maximum projection of all channels and time-points
		- [ Image > Stacks > Z Project ...]
	- Note: Unfortunately not many ImageJ functions and plugins work on hyperstacks :-(
  

## Batch analysis using [ Process > Batch ]

If your images have different sizes above tricks using an image stack will not work. 
In such cases you can try the `[ Process > Batch ]` batch-processing, built into ImageJ.
 
### Activity: Convert various images to Tiff files using [ Process > Batch ]

- [ Process > Batch > Convert ]: 
	- Input: "../data/different-file-formats/"
	- Output: `Tiff`
	- Leave other options at default values

