# Batch analysis using IJ macro programming

References:
- https://imagej.nih.gov/ij/developer/macro/functions.html
- https://imagej.nih.gov/ij/developer/macro/macros.html

## Introduction

Software can often be ran by either

- Graphical User Interface (GUI) 
- Scripting 

Have you done scripting before?

[ Script ] --- is ---> [ Executable text ]

Think about pros and cons of GUI vs scripting.

## Script recording concept

[ GUI actions ] --- record as ---> [ Script ]

## Smoothing an image

Let's record our first macro!

- Turn on the macro recorder:
	- [Plugins > Macros > Record]
- Execute below UI commands
	- [ File > Open... ]
		- "/imagej-courses/data/convolution-filters/noisy-nuclei.tif" 
	- [ Process > Filters > Mean... ]
		- Radius: 2
		- [ OK ]

You should now see below text in the **Recorder** window:

```
open("/imagej-courses/data/convolution-filters/noisy-nuclei.tif");
run("Mean...", "radius=2");
```

In order to run the code we have to
- [Create] the macro
	- This opens up the **Script** editor window
- Now you can [Run] it!

## Concepts

### Recorder

- [ Recorder window ] -> ( Records code )
- [ Recorder window ] -> ( Choose language )

### Script editor window

- [ Script editor window ] -> ( Run code )
- [ Script editor window ] -> ( Edit code )
- [ Script editor window ] -> ( Save code )
- [ Script editor window ] -> ( Open code )

### Recorded code content

open( ... );
- [ open ] -> [ Function ]
- [ open ] --- has ---> [ Parameter ]


Parameter
[ Parameter(s) ] --- configure ---> [ Function ]


run( ... );
- [ run ] -> [ Function ]
- [ run ] --- has ---> [ 2 text parameters ]
	1. Name of menu command
	2. Command parameter(s) as a "key value" pair(s)


radius=2
- [ Key value pair ] --- has ---> [ Key (name) ]
- [ Key value pair ] --- has ---> [ Value ] --- can be ---> [ Number ]
- [ = ] -> [ Operator ] 
- [ = ] --- assigns ---> Value to key


"radius=2"
- [ Text parameters ] --- enclosed by ---> [ Quotation marks " " ]


Function
- [ Function ] --- has ---> [ Name ]
- [ Function ] --- can have ---> [ Parameters ]

;
- [ ; ] -> indicates the end of one "block of code"


## Automated counting of all cells in an image stack using a macro

As our first really useful example of a macro we will automatically count the number of cells in an image.

Turn on macro recorder:

- [Plugins > Macros > Record]

Record workflow for cell counting:

- Open the first time-point of the time-series:
	- [ File > Open ] 
		- '../mitocheck_movie/EMBO_2012_Group3--empty--empty--W0002--P001--T00000--Z000--C.tif'
- Threshold
	- [Image > Adjust Threshold]
		- [X] Dark background
		- [Apply]
- Set measurements, keeping tracking of the file-name
	- [Analyze > Set measurements]
		- [X] Area
		- [X] Display label
			- this will keep track of the filename
- Find and measure the cells
	- [Analyze > Analyze Particles...]
		- [X] Summarize
			- This will give you for a given image the average results of all objects
    - Show: Nothing

Your recorded macro should look somewhat similar to the text shown below:

```
open("H:\\imagej-courses-master\\data\\mitocheck-movie\\EMBO_2012_Group3--empty--empty--W0002--P001--T00000--Z000--C.tif");
run("Set Measurements...", "area display redirect=None decimal=3");
setAutoThreshold("Default dark");
//run("Threshold...");
setThreshold(18, 255);
setOption("BlackBackground", false);
run("Convert to Mask");
run("Analyze Particles...", "  show=Outlines summarize");
```

### Comment concept

- [ // ] --- starts a ---> [ Comment ]
- [ Comment ] --- is ---> [ Not executed text ]


Before we can run the code we have to:

- Remove the "//" before the line starting with 'setTreshold', because we actually want to execute it.
- [Create] the macro
- Save it [ File > Save as .. ].
- Now you can [Run] it and it should do the job :-)

### Cleaning up and adding comments

In fact there a number of lines recorded that are not really needed, below code is sufficient.

In addition, it is good style to add comments '//' and visually separate code belonging together.

```
// close all images
run("Close All"); 

// open file
open("C:/Users/teach/Desktop/imagej-courses-master/data/mitocheck-movie/EMBO_2012_Group3--empty--empty--W0002--P001--T00000--Z000--C.tif");

// threshold
setThreshold(18, 255);
run("Convert to Mask");

// configure measurements
run("Set Measurements...", "area display redirect=None decimal=3");

// perform particle analysis
run("Analyze Particles...", "  show=Nothing summarize");
```

### Activity: Automatically save the results table

Above code does not automatically save the results table, try to add this, using macro recording.

&nbsp;

&nbsp;

#### Solution:

```
saveAs("Results", "C:\\Users\\teach\\Desktop\\Summary.csv");
```

## Using variables

Reusing a macro for different data set might require adapting some parameters.
It is good style to put all the things that can change at the top of the code, such that it is easy to modify. For this we need so-called "variables".

### Variable concept

- [ Variable ] --- has ---> [ Name ]
- [ Variable ] --- has ---> [ Content ]
- [ Content ] --- can be ---> [ Text ] --- has ---> [ Quotation marks ] 
- [ Content ] --- can be ---> [ Numeric ] 
- [ String ] --- is another name for ---> [ Text ]
 
### Activity: Interactive practical on variables: numbers, strings, adding, concatenating.

### Combining variables concept

- [ + ] --- combines ---> [ Variables ]
- [ + ] --- adds ---> [ Numeric variables ]
- [ + ] --- concatenates ---> [ Text variables ] 

### Activity: Make filepath and threshold variables

In below code, the directory with the images is already a variable (note how string-concatentation was used to paste it into the command).
 
- Copy below code into Fiji's script editor [ File > New > Script ]
- Adapt the content of the `filepath` **variable**.
- Also make the lower threshold (`18`) a **variable**, with 
	- name: `threshold`
	- content: `18` 

```
// variables
filepath = ".../imagej-courses-master/data/mitocheck-movie/EMBO_2012_Group3--empty--empty--W0002--P001--T00000--Z000--C.tif";

// close all images
run("Close All"); 

// open file
open( filepath );

// threshold
setThreshold( 18, 255 );
run( "Convert to Mask" );

// configure measurements
run("Set Measurements...", "area display redirect=None decimal=3");

// perform particle analysis
run("Analyze Particles...", "  show=Nothing summarize");

// save results table
saveAs("Results", "C:\\Users\\teach\\Desktop\\Summary.csv");

```

&nbsp;

&nbsp;

#### Solution

```
threshold = 18;
...
setThreshold( threshold, 255 );
```

### Activity: Name results table after input image

In above macro, try to make the filename of the results table resemble the image name, using "String concantenation".

Hints:
- image_filename = "image.tif";
- table_filename = image_filename + ".csv";


&nbsp;

&nbsp;


#### Solution

```
table_filepath = filepath + ".csv";
saveAs( "Results", table_filepath + ".csv" );
```

### Combined solutions

```
// user input
filepath = "C:/Users/teach/Desktop/imagej-courses-master/data/mitocheck-movie/EMBO_2012_Group3--empty--empty--W0002--P001--T00000--Z000--C.tif";
threshold = 18;

// close all images
run("Close All"); 

// open file
open( filepath );

// threshold
setThreshold( threshold, 255 );
run( "Convert to Mask" );

// configure measurements
run("Set Measurements...", "area display redirect=None decimal=3");

// perform particle analysis
run("Analyze Particles...", "  show=Nothing summarize");

// save results table
table_filepath = filepath + ".csv";
saveAs( "Results", table_filepath );
```

##### Note

It is not ideal to have the results in the same folder as the image. 
To avoid this we would have to split the filepath into a directory and filename...

## Adding graphical user interface (GUI) for variables

Sometimes, it can be nice not to have to type into the macro, but enter the variables with a GUI.
In fact, it is not only nice, but also safer, because it prevents us from breaking the code by typing something wrong there. 

### Concept

[ GUI element ] --- fetches content for ---> [ Variable ]

### Hints

Typically, I use internet search to find out how to do something related to programming:

- Search the internet: `imagej macro get variable from user`
	- You should find:
		- http://imagej.1557.x6.nabble.com/Having-a-macro-prompt-for-variable-input-td3694090.html
		- getNumber("prompt", defaultValue); 

### Activity: Fetching a number via a GUI element

Interactive activity: fetching a number via a GUI element and print it

### Activity: Fetching a file path via a GUI element

In below code, the threshold variable already has its GUI.

- Try to also **obtain the filepath from a GUI element**.

Hint: 
- https://imagej.nih.gov/ij/macros/OpenDialogDemo.txt

```
// User input
filepath = "H:\\imagej-courses-master\\data\\mitocheck-movie\\EMBO_2012_Group3--empty--empty--W0002--P001--T00000--Z000--C.tif";
threshold = getNumber("Enter threshold", 29);

// General code
run("Image Sequence...", "open=["+directory+"] sort");
run("Set Measurements...", "area display redirect=None decimal=4");
setAutoThreshold("Default dark");
setThreshold(threshold, 255);
setOption("BlackBackground", false);
run("Convert to Mask", "method=Default background=Dark");
run("Analyze Particles...", "  show=Nothing summarize stack");
```

&nbsp;

&nbsp;



#### Solution

```
filepath = File.openDialog( "Select a File" );
```
 
### Activity: Saving the results table at a good place and with a good name

Now that we have the input file as a variable, we can automatically save the results table with a name related to this file.
Try to do this on your own.

Hints:
- Google: ImageJ Macro save results table
- http://imagej.1557.x6.nabble.com/save-results-table-as-csv-with-custom-name-td5003427.html
- Google: ImageJ Macro create new folder
- https://stackoverflow.com/questions/36144914/imagej-macro-make-new-folder-and-save-output-in-new-folder 

#### Solution

...

## Functions

It is very good for ithe readability and for reusing parts of our code to refactor it into small parts that belong together, so-called "functions".

### Function concept

- [ Function ] --- has ---> [ Name ]
- [ Function ] --- contains ---> [ Code ]
- [ Code ] -> [ Executable via name ]   
- [ Function ] --- can have ---> [ Parameters ] 
- [ Parameters ] --- are ---> [ Variables ]

### Activity

- Copy below code into Fiji.
- Note how everything related to measure the cells was wrapped into a function.
- Try to also make a function for the thresholding.

```
// User input
//

filepath = File.openDialog("Select a File");
threshold = getNumber("Enter threshold", 29);

// Main
//

open( filepath );

// TODO: put into a function...
setAutoThreshold("Default dark");
setThreshold(threshold, 255);
setOption("BlackBackground", false);
run("Convert to Mask", "method=Default background=Dark"); 

// a function
measureCells();

// Functions
// 

function measureCells() {
	run("Set Measurements...", "area display redirect=None decimal=4");
	run("Analyze Particles...", "  show=Nothing summarize stack");
}  
```

Solution:
- ../macros/CountCells-Functions.ijm


## Analyzing multiple images in one folder

```
dir = getDirectory("Choose a Directory ");

files = getFileList( dir );
   
for (i = 0; i < files.length; i++) 
{
   path = dir + files[i];
   processFile( filePath );
}

function processFile( filePath ) 
{
	print( "Processing file: " + path );
        open( path );
         
        //
        // ADD OWN CODE HERE
        //
}
```

- Copy above code into the Script editor
- ...and run it!


### Concepts

#### Arrays (Lists)

- [ Array ] --- has ---> [ Name ]
- [ Array ] --- contains ---> [ Variables ]
- [ Array ] --- has ---> [ Length ]
- [ Name[index] ] --- retrieves ---> [ Variable ]

#### For loop

- [ For loop ] --- iterates ---> [ Numeric variable ]
- [ For loop ] --- has ---> [ Start ]
- [ For loop ] --- has ---> [ Ending condition ]
- [ For loop ] --- has ---> [ Increment ]


### Activity

Add your own cell counting code!



## Batch mode

Execute code much faster by suppressing any output.

```
setBatchMode( true );
```

## Analyzing multiple images in one folder, including sub-folders

Sometimes you have your image files distributed in sub-folders. Below code deals with this.

```
dir = getDirectory("Choose a Directory ");

list = getFileList(dir);
for ( i = 0; i < list.length; i++) 
{
	if ( endsWith(list[i], "/") ) {
		// recursively go into sub-folders
		processFiles( "" + dir + list[i] );
	}
	else 
	{
		path = dir + list[i];
		processFile( path );
	}
    }
}

function processFile( path ) 
{     
	print( "Processing file: " + path );

	open( path );
         
         //
         // ADD OWN CODE HERE
         //   
    }
}
```
