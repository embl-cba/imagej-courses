# Basic Image Analysis Concepts

## Location

EMBL Rome

## Date(s)

- Wednesday, Feb. 12, whole day, 2020
- Thursday, Feb. 13, whole day, 2020
- Friday, Feb. 14, half day, 2020 

## Teachers

Christian Tischer

## Computers

Participants use own laptops.

## Software

Fiji (is just ImageJ)

## Interactive course document

....

## Prerequisites

- Please print the [handout](https://github.com/tischi/imagej-courses/blob/master/handouts/image-analysis-basics.pdf).
- Please download the [example data](https://github.com/embl-cba/imagej-courses/archive/master.zip).
- Please install [Fiji](https://imagej.net/Fiji/Downloads)
- Please install several Fiji Update Sites: 
  - [Fiji > Help > Update... > Manage Update Sites]
    - [X] IJPB Plugins
       - This installs MorpholibJ
    - [X] 3D ImageJ Suite
    - [X] ImageScience
    - [X] ClearVolume 
    - Click [ Close ]; the updates sites will be installed...
    - Restart Fiji
  - Check that the update sites are installed! E.g., you should now find
    - [ Fiji > Plugins > MorpholibJ > ... ]
    - [ Fiji > Plugins > 3D > ... ]
    - [ Fiji > Plugins > FeatureJ > ... ]

## Course content

### Basic concepts of image analysis:

- Images are made of pixels
- Lookup tables (LUTs)
- Calibration of pixel sizes
- Image (pixel) data types
- Image math
- Data type conversions
- Image binarisation (thresholding)
- Connected component analysis (object detection)
- Object shape measurements
- Object shape measurement workflow
- Results visualisations
- Object filtering
- Intensity measurements
- Global background subtraction workflow
- Convolution filters (mean, gauss, edge)
- Typical image analysis workflow

### Advanced concepts of image analysis:

- Rank filters
- Rank filter sequences (morphological filtering)
- Local background subtraction using a median filter
- Local background subtraction using a tophat filter
- Object splitting by intensity based watershed
- Object splitting by intensity based watershed workflow
- Distance map
- Distance measurement workflow
- Object splitting by distance transform based watershed
- Automated global thresholding
- Automated local thresholding
- Machine learning based pixel classification

### Image analysis automation:

- IJ macro recording and scripting


## Course schedule

- Wednesday, Feb. 12, whole day, 2020
	- Basic concepts of image analysis
- Thursday, Feb. 13, whole day, 2020
	- Advanced concepts of image analysis
- Friday, Feb. 14, half day, 2020
	- Image analysis automation using IJ Macro scripting
