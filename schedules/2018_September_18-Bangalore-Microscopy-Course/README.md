# Bangalore Microscopy Course 2018
# Image analysis module

## Schedule

|             Day                |           Time             |                Activity           |
|--------------------------------|----------------------------|-----------------------------------|
|         Tuesday 18.09          |        11.45-12:45         | ***Lecture***: Image Analysis     |
|         Tuesday 18.09          |        17.00-19:00         | ***Practicals***: Basic image analysis operations |
| Saturday 22.09<br>Sunday 23.09 | 11.15-18:15<br>09.00-18:00 | ***Project***: 3D Image Processing|

## Lecture

Lecture slides can be downloaded after the course. Link will be provided later here

## Practical

### Exercises

|  N  |  Exercise  |
|-----|------------|
|  1  |[Image inspection](https://github.com/tischi/imagej-courses/blob/master/practicals/basic-image-inspection-and-handling.md#activity-image-content-inspection)|
|  2  |[Basics of intensity measurements](https://github.com/tischi/imagej-courses/blob/master/practicals/intensity-quantification.md)|
|  3  |[Image segmentation: Manual thresholding, Signal to noise, Image filtering](https://github.com/tischi/imagej-courses/blob/master/practicals/image-segmentation.md)|
|  4  |Automated [global](https://github.com/tischi/imagej-courses/blob/master/practicals/image-segmentation.md#automated-global-thresholding) and [local](https://github.com/tischi/imagej-courses/blob/master/practicals/image-segmentation.md#automated-local-tresholding-under-development) thresholding 

### Homework (advanced exercises)

| N | Exercise |
|------|-------|
|  1  |[3D image inspection](https://github.com/tischi/imagej-courses/blob/master/practicals/3D-image-inspection.md)|
|  2  |[Intensity quantification: Automated local background subtraction](https://github.com/tischi/imagej-courses/blob/master/practicals/automated-local-background-subtraction-for-intensity-quantifications.md#intensity-measurements-with-automated-local-background-subtraction--) |
|  3  |[Workflow for intracellular object quantification](https://github.com/tischi/imagej-courses/blob/master/practicals/workflow-2d-intracellular-spot-detection.md#workflow-autophagosome-quantification) | 
|  4  |[Colocalization](https://github.com/tischi/imagej-courses/blob/master/practicals/colocalisation.md#colocalisation) |
|  5  |[Tracking using TrackMate](https://github.com/tischi/imagej-courses/blob/master/practicals/tracking-with-trackmate.md)  |
|  6 |[Macro recording and scripting in ImageJ](https://github.com/tischi/imagej-courses/blob/master/practicals/macro-recording.md) |




## Project

### Abstract

During the first part of the project students will implement the workflow for analyzing confocal microscopy data in 3D using ImageJ/Fiji. We will work on images of cells stained for nuclei and nuclear foci. We will segment nuclei and foci in 3D and visualize segmentation results. To separate touching objects advanced analysis techniques such as local maxima detection and seeded watershed will be applied. Volume, intensity, and shape parameters will be then computed for each object. Then we will determine which foci belong to which nucleus and calculate distribution of foci quantities in nuclei. In the second part of the project we will use Fiji scripting capabilities to automate the workflow for batch processing of large number of images. 
