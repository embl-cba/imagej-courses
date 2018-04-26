# Batch analysis in ImageJ

There are several ways to achieve batch analysis of many images in ImageJ:
- Putting images into an image (hyper-)stack 
- Using [Process > Batch]
- Writing scripts, e.g. using the ImageJ Macro language

## More information

- https://imagej.net/How_to_apply_a_common_operation_to_a_complete_directory
- https://imagej.net/Batch_Processing

## Batch analysis using image stacks

If your images have the same dimensions in x,y (and z) and you want to apply the exact same operation to all of them the easiest option for batch analysis is to load all of them into one image (hyper-)stack.

### Automatically counting the number of nuclei in many images <a name="AutoCount"></a>

Counting the number of objects in many images is probably the most classical bio-image analysis application; thus let's start with this!

Workflow:
- Load all images into an image stack
	- [File > Import > Image Sequence] 
		- '../data_new/mitocheck_movie'
- Threshold all images
	- [Image > Adjust Threshold]
		- [X] Dark background
		- [ ] Calculate threshold for each image
			- Uncheck this, otherwise some auto-thresholdin is going on!
		- [Apply]
			- Yes, do it for the whole stack!
- Set measurements, keeping tracking of the file-name
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
"../data_new/data-in-subfolders"
To still load them into one image stack you can use a macro that is provided in this repository:

Workflow:
- Load and run the macro
	- Drag&Drop onto Fij: "../macros/import-from-subfolders.py"
	- Press [Run]
		- Filename contains: ".tif"
		- Choose as folder: "../data_new/data-in-subfolders/"
- You have all data in one stack and could for instance count the number of cells, as we learned above.

Comment:
- Like this, you cannot change the data and then save it back into the same folder-structure; this would require writing some macro code (see below)

### Computing and saving 3-D maximum projections of many stacks

If you have 3-D data, all having the same x,y,z dimensions, you could implement batch operations using so-called "hyper-stacks"; the challenge here is to actually load the data into a hyperstack; once you have it, batch operations are easy.

### Making a hyperstack from single files, using [Import Image Sequence]

Sometimes data beloning to different image stacks is distributed across single files.
Here, you can see how to rearrange them into a hyper-stack after loading. 


Workflow:
- Load all images
	- [File > Import Image Sequence]
		- "../data_new/mitosis-5D-single-files/"
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

### Making a hyperstack from single files using the Bioformats Importer

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
		- click on one file in the folder "../data_new/mitosis-5D-single-files/"
		- View stack with: "Hyperstack"
		- [X] Group files with similar names
			- You'll see how it interprets your file-naming scheme
		- [OK]
- Do the processing of your choice and save the data again using [File > Save as > Image Sequence]

#### Image stacks

Another frequently occuring scenario is that you have 3-D data, where each file is one image stack.
In the following we will see how to deal with this case. In fact, you can still do the hyperstack trick, because the Bio-Formats plugin can automatically combine data from image stacks into one hyperstack.

Workflow:
- Load many stacks into one hyperstack
	- [Plugins > Bio-Formats > Bio-Formats Importer]:
		- click on one file in folder: "../data_new/mitosis-4D-stacks/"
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
	- Input: "../data_new/different-file-formats/"
	- Output: you can choose :-)
	- Leave other options at default values

### Display the filename on multiple images

It is good practice to have meaningful filenames, e.g., containing a particular treatment that your images were subjected to. For quick visual inspection of your data it can thus be useful to display the filename in the image.

Workflow:
- Use ImageJ's in-built batch processing, chosing one of the example macros.
	- [Process > Batch > Macro] 
		- Input: "../data_new/meaningful-filenames/"
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
	- Open some file, e.g. "../data_new/meaningful_filenames/Treatment_A.tif"
	- Put a scale bar:
		- [Analyze > Tools > Scale Bar..]
			- choose some parameters that you like
			- [OK]
	- Now the window should show some text, such as:
		- ```run("Scale Bar...", "width=50 height=4 font=14 color=White background=None location=[Lower Right] bold");```

- Use the recorded text (copy & paste) to put a scale bar onto multiple images using [Process > Batch > Macro..] (see above)
 
## Batch analysis with macro programming

References:
- https://imagej.nih.gov/ij/developer/macro/functions.html
- https://imagej.nih.gov/ij/developer/macro/macros.html

### Even more automated counting of all cells in many images using an IJ-Macro

As our first real example of a macro we will automate above workflow ["Automatically counting the number of cells in many images"](#AutoCount). Even though the trick of loading all images into one stack saved us a lot of work, we still needed to click a lot. If you want to do this workflow for many folders it surely will become boring. Thus, let's record a macro that does the job for us:

Record a macro:
- [Plugins > Macros > Record]
- Repeat all the steps from [above](#AutoCount), including opening the file!
- You should have recorded something like this:

```
//
// ../macros/CountCells.ijm
//
run("Image Sequence...", "open=/Users/tischi/Documents/imagej-courses/data_new/mitocheck-movie sort");
run("Set Measurements...", "area display redirect=None decimal=4");
setAutoThreshold("Default dark");
//run("Threshold...");
//setThreshold(29, 255);
setOption("BlackBackground", false);
run("Convert to Mask", "method=Default background=Dark");
selectWindow("mitocheck-movie");
run("Analyze Particles...", "  show=Nothing summarize stack");
```

If you now [Create] the macro and [Run] it, it should do the job.

- Note: "//" means that a line of code only is a comment
- We have to remove the "//" before the line starting with 'setTreshold', because we actually want to execute it.

##### Activity: Automatically save the results table

Above code does not automatically save the results table, try to add this, using macro recording.


#### Using variables

Some commands in our macro will be the same, but some stuff will be different for different files.
It is good style to put all the things that can change at the top of the code, such that it is easy to modify. For this we need so-called "variables".

**=> Interactive practical on variables: numbers, strings, adding, concatenating.**

##### Activity:

In below code the directory with the images is already a variable (note how string-concatentation was used to paste it into the command).
 
Copy the code into Fiji and also **try to make the threshold a variable**.

```
// User input as variables
directory = "/Users/tischi/Documents/imagej-courses/data_new/mitocheck-movie";

// General code
run("Image Sequence...", "open=["+directory+"] sort");
run("Set Measurements...", "area display redirect=None decimal=4");
setAutoThreshold("Default dark");
setThreshold(29, 255);
setOption("BlackBackground", false);
run("Convert to Mask", "method=Default background=Dark");
run("Analyze Particles...", "  show=Nothing summarize stack");
```

Solution: '../macros/CountCells-Variables.ijm'


#### Making it really nice, with a graphical user interface

It is nice, not to have to type into the macro, but enter the variables with a GUI.
In fact, it is not only nice, but also safer, because it prevents us from breaking the code by typing something wrong there. 

Typically, I use google to find out how to do something related to programming:

Google: imagej macro get variable from user
- http://imagej.1557.x6.nabble.com/Having-a-macro-prompt-for-variable-input-td3694090.html
- getNumber("prompt", defaultValue); 

**=> interactive practical, getting a number via the GUI and printing it**


##### Activity: adding another GUI element

In below code the threshold variable already has its GUI.
Try to also **obtain the directory from the GUI**.

Hint: 
- Google: imagej macro get directory

```
// User input
directory = "/Users/tischi/Documents/imagej-courses/data_new/mitocheck-movie";
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

Solutions:
- https://imagej.nih.gov/ij/macros/GetDirectoryDemo.txt
- getDirectory("Select a directory");
- '../macros/CountCells-GUI.ijm'
 
##### Activity: Saving the results table

Now that we have the input folder as a variable, we can automatically save the results table in a place related to this folder.
Try to add this on your own.

Hints:
- Google: ImageJ Macro save results table
- http://imagej.1557.x6.nabble.com/save-results-table-as-csv-with-custom-name-td5003427.html
- Google: ImageJ Macro create new folder
- https://stackoverflow.com/questions/36144914/imagej-macro-make-new-folder-and-save-output-in-new-folder 



#### The final touch: functions

It is very good for readability and for reusing parts of our code to pack it into small parts that belong together, so-called "functions".

##### Activity

Copy below code into Fiji and try to also **make a function for the thresholding**.

```
// User input
//
directory = getDirectory("Select a directory");
threshold = getNumber("Enter threshold", 29);

// Main
//

loadImagesIntoStack(directory);

// put into a function...
setAutoThreshold("Default dark");
setThreshold(threshold, 255);
setOption("BlackBackground", false);
run("Convert to Mask", "method=Default background=Dark"); 

measureCells();

// Functions
// 
function loadImagesIntoStack(directory) {
	run("Image Sequence...", "open=["+directory+"] sort");
}

function measureCells() {
	run("Set Measurements...", "area display redirect=None decimal=4");
	run("Analyze Particles...", "  show=Nothing summarize stack");
}  
```

Solution:
- ../macros/CountCells-Functions.ijm



### Dealing with data in different folders using macro programming

Once your data is distributed across different folders none of the approaches above currently works (apart from the special script "../macros/import-from-subfolder.py").

Thus, we will learn how to deal with data in different folders. In programming, it is typical not to start from scratch, but modify existing code (everybody does that ;-). Thus, let's just try to understand below IJM (ImageJ-Macro) code. In fact, the way I found this code was like this:

GOOGLE: imagej macro batch process folders

CODE: https://imagej.nih.gov/ij/macros/BatchProcessFolders.txt

```
// "BatchProcessFolders"
//
// This macro batch processes all the files in a folder and any
// subfolders in that folder. In this example, it runs the Subtract 
// Background command of TIFF files. For other kinds of processing,
// edit the processFile() function at the end of this macro.

   requires("1.33s"); 
   dir = getDirectory("Choose a Directory ");
   setBatchMode(true);
   count = 0;
   countFiles(dir);
   n = 0;
   processFiles(dir);
   //print(count+" files processed");
   
   function countFiles(dir) {
      list = getFileList(dir);
      for (i=0; i<list.length; i++) {
          if (endsWith(list[i], "/"))
              countFiles(""+dir+list[i]);
          else
              count++;
      }
   }

   function processFiles(dir) {
      list = getFileList(dir);
      for (i=0; i<list.length; i++) {
          if (endsWith(list[i], "/"))
              processFiles(""+dir+list[i]);
          else {
             showProgress(n++, count);
             path = dir+list[i];
             processFile(path);
          }
      }
  }

  function processFile(path) {
       if (endsWith(path, ".tif")) {
           open(path);
           // 
           // CHANGE HERE: START
           //
           run("Subtract Background...", "rolling=50 white");
           save(path+"--processed.tif");
           // 
           // CHANGE HERE: END
           //
           close();
      }
  }
```

Looks complicated, doesn't it?! 

The really good news however is that the only part you really need to care about is the tiny bit between CHANGE HERE START and END. You can replace that part by anything that you recorded as a macro.

For example, let's try smoothing all the images:

...
