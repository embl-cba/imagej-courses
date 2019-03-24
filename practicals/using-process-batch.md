# Using [ Process > Batch ]

This documents contains few examples on how to use [ Process > Batch ]

## Activity: Paint filenames into images

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

## Activity: Macro recording for putting a scale bar on multiple images

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
 
