# Object manipulation

Once you found your objects you often want to split touching object or measure only in certain parts of the object or just close-by the object. 

Example data: 
- [File > Open Samples > Blobs]; [Image > Lookup Tables > Invert LUT]	
- [File > Open Samples > HeLa Cells]; [Color > Split Channels]
- [File > Open Samples > Fluorescent Cells]; [Color > Split Channels]

Convert the image to a binary image ([s.a.](#segmentation)) and then manipluate the object's shape using below methods.

	
## Object growing and shrinking and boundary creation

Workflow:
- Example data:
	- Simply draw some objects yourself
- Dilate (grow, 'maximum') and erode (shrink, 'minimum') the binary image to change the object size
- In addition, by subtracting the eroded image from the original one can generate outlines
- Fiji commands:
	- [File > New Image...]
		- Use Fiji's drawing tools to generate some objects of choice
	- [Process > Filters > Minimum]
	- [Process > Filters > Maximum]
	- [Image > Duplicate]
	- [Process > Image Calculator]
		- Use this to subtract images from each other

Application examples:
- Measure the amount of protein X in the nuclear envelope
	- Data given: Confocal slice with staining for DAPI and protein X 

## Distance transform

The distance transform is a powerful tool for many image analysis tasks, also in biology.
Using the distance transform you can
- measure distances between different objects (from different fluorescence channels) 
- select specific regions within of or close by objects 
- split objects based on a shape criterium (see [below](#object-splitting))

Workflow for measuring distances to nearest object in another channel: 
- Example data: One object in Ch0, many objects in Ch1
	- ../data-new/distance-transform-applications/distances-between-objects.tif
- Split stack into individual channels
- Distance transform Ch0 => DistTrafoCh0
- Measure mean intensity of Ch1 objects in DistTrafoCh0
- Fiji commands:
    - [Image > Stacks > Stack to Images]
    - [Process > Binary > Distance Map]
    - [Image > Rename] 
    - [Analyze > Set Measurements]: [X] Mean gray value; Redirect to 'DistTrafoCh0'
    - [Analyze > Analyze Particles]: [x] Display Results

Workflow for finding circle centers:
- Example data:
	- ../data-new/distance-transform-applications/hollow-tubes.tif
- Compute distance transform
- Find local maxima
- Fiji commands:
    - [Process > Binary > Distance Map]
    - [Process > Find Maxima]

Further reading:
- http://imagej.net/Local_Thickness

## Object splitting <a name="object-splitting"></a>

Often, objects that are very close are idenftied as one object in the connected component analysis. The distance-transform based watershed algorithm is the most commonly way to deal with this.

Workflow:
- Subject the binary image to a (distance-transform based) watershed algorithm
- Fiji commands:
	- [Process > Binary > Watershed]
	
Comments:
- E.g., CellProfiler offers a number of interesting choices for object splitting, which are not only shape but also intensity-based 





