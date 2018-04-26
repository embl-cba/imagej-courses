# The meaning of intensities in confocal and widefield microscopy

todo: put images here


# Intensity-based quantifications of BFA-induced Golgi disassembly (confocal)

## Data

- 3D confocal stacks
- ...

## Challenges

- Intensities depend on evertyhing!


## Detector offest (background) subtraction

### Measure and subtract later

Formula for sum intensities: Mean_Background * Area


### Subtract from whole image

32-bit conversion necessary to be truly independent on measurement area.

### Accuracy of background subtraction

Subtracting the wrong background can lead to false biological interpretations of your data.
There will always be a small error in the background subtraction. In order to figure out how much this will influence your sum-intensity measurements you can do the following calculation:

...
### Issues

What to do if you have many data sets? Can I subtract the same background from all?




## Maximum intensity in 3-D maximum intensity projection

Maximum value in a 3-D maximum intensity projection is proportional to the highest local density of observed fluorophores, where local corresponds to the confocal point spread function (~200x200x800 nm^3).

### Workflow

- Maximum projection
- Manual background subtraction
- Draw ROI
- Measure

- Easy to compute readout for the maximal local concentration in a 3-D data set.

#### Normalisation strategies

In a time-lapse experiment one could use the intial maximal local concentration in each cell and then monitor the 

### Pro

### Con

- Only very local readout of whole cell
- 
	- 
	- Measure the average maximal local concentration in a set of control cells and divide by this value


## Sum



# Intensity-based quantifications of H2B-mCherry during the cell-cycle (wide-field)

## Mean intensity
## Maximum intensity
##
 

