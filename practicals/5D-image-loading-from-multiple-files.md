## Constructing a 5D hyperstack from single plane files

Sometimes data belonging to one 5D image data set is distributed across several files.
Here, you can see how to deal with this situation.

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

In above workflow we had to manually enter the dimensions of the data.
If the filenames are very well structured those dimensions can be determined automatically as shown in the next workflow.

### Construction a 5D hyperstack from single plane files using the Bioformats Importer

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
