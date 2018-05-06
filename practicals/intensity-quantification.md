# Image intensity measurements <a name="intensity_measurements"></a> 

## Mean intensity vs. sum intensity

In biology it is crucial to choose the right intensity measurement. In some cases choosing mean instead of sum intensity can give you the opposite biological result!

### Definitions

<img width="243" alt="image" src="https://user-images.githubusercontent.com/2157566/39675856-642a58ae-5161-11e8-977a-e2779ec0e927.png">

- Gray values: 105, 133, 148, 142
- Sum = 105 + 133 + 148 + 142 = 528
- AreaInPixelUnits = 4
- Mean = Sum / AreaInPixelUnits = 132
- Sum = Mean * AreaInPixelUnits   

### Nomenclature

- Alternative wordings for **sum intensity**:
	- total intensity
	- integrated intensity
	- integrated density
	- in ImageJ: 
		- **RawIntDen** = Mean * AreaInPixelUnits
			- This is the one you need!
		- IntDen = Mean * AreaInCalibratedUnits
			- ...I never understood what this is good for...
- Alternative wordings for **mean intensity**:
	- average intensity
	- in ImageJ: 
		- Mean

&nbsp;
	
&nbsp;

&nbsp;


## The biophysical meaning of intensities in fluorescence microscopy images

### Widefield vs. confocal microscopy

<img width="600" alt="image" src="https://user-images.githubusercontent.com/2157566/39675919-da4160a0-5161-11e8-8f65-88a9fff4c209.png">

<img width="600" alt="image" src="https://user-images.githubusercontent.com/2157566/39675923-eaa546dc-5161-11e8-81f1-161cf8973a09.png">

&nbsp;

&nbsp;

&nbsp;

### Comparing mean vs. sum in widefield vs. confocal measuring DNA content during the cell cycle

<img width="526" alt="image" src="https://user-images.githubusercontent.com/2157566/39675959-5c98f978-5162-11e8-86f5-a1761a5ae458.png">

#### Widefield sum intensity

Let's assume:
- the image above are taken with a **widefield** microscope. 
- in each image we draw a region of interest closely around the DNA
- we measure the **sum** intensity

What do you expect?

&nbsp;

&nbsp;

&nbsp;

#### Confocal mean intensity

Now, let's assume:
- the image above are taken with a **confocal** microscope, pinhole at 1 airy unit. 
- in each image we draw a region of interest closely around the DNA
- we measure the **mean** intensity

What do you expect?

&nbsp;

&nbsp;

&nbsp;

#### Answers

<img width="526" alt="image" src="https://user-images.githubusercontent.com/2157566/39675949-45fd1bc2-5162-11e8-8f29-2033b4a542f3.png">


## Activity: Manual intensity measurements

Let's measure the sum intensity of two nuclei in a widefield microscopy image. Assuming that the staining is quantitative this could give us information on the cell cycle state (because the DNA content doubles during the cell cycle).

- Open “../image-inspection/B.tif”
- Record a ROI around one nuclues:
	- Draw a region around a nucleus, e.g. using ImageJ's Polygon Selection
		- We will do sum intensity measurements with background subtraction, thus one should draw this region rather generously not to miss any intensities!
	- Add region to ROI manager [Analyze > Tools > ROI Manager > Add)
	- Name the region “nucleus_1” [Analyze > Tools > ROI Manager > Rename]
- Repeat above steps:
	- Choosing another nucleus (maybe one that clearly appears dimmer or brighter than the first one).
		- "nucleus_2"
	- Now choosing a background region (strongly increase the image brightness to find a clean background region). 
		- "background"
		 
- Select measurements [Analyze > Set Measurements]:
	- [X] Mean gray value
	- [X] Area
	- [X] Integrated density
		- This measures the sum intensity; in fact it will output two values; the "good" one is **RawIntDen**, which really simply adds up the gray values in the measurement ROI.
- Select all regions and measure [ROI Manager > Measure]

Now we need to do the proper background subtraction for the two nuclei ROIs, using below formula:

`Sum_BgCorr = RawIntDen - Area * Mean_Background`

In words, we subtract for each pixel in the ROI the mean value of the background.

Two compare the intensities of the two nuclei, typically computing the ratio of the sum intensities is a good readout.

As mentioned above, given the staining is quantitative, this could be used to infer on the cell cycle state.

&nbsp;

&nbsp;

&nbsp;

## Intensity measurements and their interpretation: Now with local background

Intensity measurements are a **quite tricky business**, not because they are technically difficult, but because one can make many mistakes in the interpretation of the numbers. Thus, they should be done with **utmost care**!

## Activity: Intensity measurements with local background subtraction

In biology, almost always there is some "background" intensity. It is very important to think about what kind of background it is and how to deal with it. Again, wrong decisions here can yield wrong biological conclusions. In this activity we will practice some of the most common issues.

Let's first open the images:

- Open all images in this folder "../dna-damage-synthetic-data/"

These images are made up, such that we know what the result should be! We will pretent that these are **widefield microscopy** images of one nucleus where a GFP-tagged DNA damage repair enzyme is diffusing around. In some of the images a well controlled laser cut was induced and thus the DNA repair enzyme binds the damage site. Some images say "Treated" in their title. The idea is that the scientist added a drug and wanted to find out if this drug enhances or diminishes the binding of the DNA repair enzyme to the damage sites. 

<img width="526" alt="image" src="https://user-images.githubusercontent.com/2157566/39676179-45fa8070-5166-11e8-9a3f-5216bf3670bc.png">

### Examine with line profile

Let's first look at the images using an intensity line profile and discuss what we see.

&nbsp;

&nbsp;

&nbsp;

&nbsp;


### Measure fraction of protein bound to damage site

Ok, now let's try to measure a number that is robust with respect to microscope settings and also has some biological meaning. This is generally challenging and one has to think about it for every project. 

In this case, assuming 

- this is widefield microscopy, and
- the unbound molecule is diffusing fast, and
- the laser cut had the exact same strength in all experiments

it probably makes sense to divide the sum intensity of the bound protein by the sum intensity in the nucleus; i.e. total_bound / total_available. This gives the fraction of protein bound to the damage site, which has the following nice properties, it is:

- independent of microscope settings
- always a number between 0 and 1
- closer to 1 the "stronger" the protein binds to the damage site

One could put even more thought into this and try to relate this to a real binding rate constant (K_A), but this goes beyond the scope of this tutorial. 

To measure the **fraction of bound protein** we need to measure:

- mean intensity outside the nucleus (mean_bg)
- mean intensity next to damage site inside the nucleus (mean_nucleus_diffusive)
- sum intensity of nucleus and area of corresponding ROI (sum_nucleus, area_nucleus_ROI)
- sum intensity of damage site and area of corresponding ROI (sum_damage, area_damage_ROI)

Now we need to compute:

- total_signal_nucleus = sum_nucleus - area_nucleus_ROI * mean_bg
- total_signal_damage = sum_damage - area_damage_ROI * mean_nucleus_diffusive

And finally:

- fraction_bound_to_damage = total_signal_damage / total_signal_nucleus

Hard work, right? And many options to make little mistakes, thus, as said, we only should preform intensity measurements with utmost care!

&nbsp;

&nbsp;

&nbsp;

### Results

- Damage: 
	- 10 percent of protein is recruited to damage site
- Damage and treated 01:
	- 10 percent of protein is recruited to damage site
	- less total intensity than in control:
		- could be due to bleaching,
		- or, if not the same cell as in control, a different expression level 
		- or, a treament induced reduction of the protein level
	- Conclusion: treatment had no effect on binding, but maybe on expression level or on nuclear import
- Damage and treated 02:
	- 5 percent recruitement to damage site
	- Conclusion: Treatment seems to reduce binding


## Discussion points

- Divide by the length (and or width) of the laser damage cut?
	- length makes sense
	- width probably not due to diffraction limit

- How do our observations relate to this: https://en.wikipedia.org/wiki/Binding_constant

- What about using the mean intensity in the nucleus next to the damage site as a biological readout?
	- It is an attractive number, because for measuring a association rate constant (K_A) we need the concentration of the unbound protein.	Thus, if (i) this was a confocal image and (ii) if there are not too many substructures in the nucleus (like nucleoli) the mean intensity gives information about the concentration of the unbound protein.
	- However, it is less obvious how to measure the concentration of the bound protein, as required for a K_A, probably one needs something else?!
	- For a widefield image the PSF is unbounded in 3D and it is thus not clear at all how to measure a concentration.

&nbsp;

&nbsp;

&nbsp;




# Intensity measurements with automated local background subtraction  <a name="automated-local-background-subtraction"></a>

Above we already practiced above how to subtract a local background manually; let's try to automate this. 

This is important for 

- image batch analysis, or 
- uneven local background that is not easy to subtract manually.

In biological fluorescence microscopy one often wants to detect locally bright objects such as vesicular structures on top of a non-uniform background fluorescence, e.g. from unbound cytoplasmic protein. There are different methods to remove such 'background' fluorescence from the image, e.g.:

- corrected\_image = image - mean\_filter(image, radius) 
- corrected\_image = image - median\_filter(image, radius) 
- corrected\_image = image - morphological\_opening(image, radius) = top\_hat(image, radius)
- corrected\_image = IJs "RollingBall" Algorithm
- ...

In all methods the *radius* parameter should be "quite a bit larger" than the radius of the largest locally bright structure that you want to measure (why that is becomes clear when we discuss the methods in detail).

## Local background subtraction using a median filter

What we'll do here is to duplicate the image and apply median filter to remove the locally bright spots. Then we subtract the median filtered image from the original image: 

- [File>Open..] "../dna-damage-synthetic-data/Damaged.tif"
- [Image>Rename..] 'Title=original'
- [Image>Duplicate] 'Title=median'
- Select the 'median' image and [Process>Filters>Median] 'radius=5'
- [Process>Image Calculator] 'Image1 = original' 'Operation = Subtract' 'Image2 = median' 
	- [X] Create new window 
	- [X] 32-bit output 
- [Image>Rename] "median_subtraction"

&nbsp;

&nbsp;

&nbsp;


## Local background subtraction using a top-hat filter 

A morphological opening filter is applied to the image and subtracted from the original. The morphological opening is defined as the dilation of the erosion if the image. Alltogether this reads: top_hat(image) = image - dilation(erosion(image))

- [File>Open..] "../dna-damage-synthetic-data/Damaged.tif"
- [Image>Rename..] 'Title=original'
- [Image>Duplicate] 'Title=opened'
- [Process>Filters>Minimum..] 'radius=5' 
- [Process>Filters>Maximum..] 'radius=5' 
- [Process>Image Calculator] 'original' 'Subtract' 'opened' 
	- [X] Create new window 
	- [ ] 32-bit output
		- Note: By construction, the 'opened' image is always lower than the original; thus we cannot get negative pixels. 
- [Image>Rename] 'Tophat.tif'


&nbsp;

&nbsp;

&nbsp;


## Local background subtraction using IJs "Subtract Background"

- [File > Open..] "../dna-damage-synthetic-data/Damaged.tif" 
- [Process > Subtract Background..] 
	- radius=5

This seems to implement a ['rolling ball'](https://github.com/nearlyfreeapps/Rolling-Ball-Algorithm/blob/master/rolling_ball.py) background estimation (=> Whiteboard). I don't understand the mathematical algorithm how to compute this, but based on the code that i saw it seems not so simple (see also [here](http://dsp.stackexchange.com/questions/10597/uneven-background-subtraction-rolling-ball-vs-disk-tophat) and [here](https://en.wikipedia.org/wiki/Dilation_%28morphology%29#Grayscale_dilation)).


&nbsp;

&nbsp;

&nbsp;


### Discussion: Comparison of the different BG subtraction methods 

- Difference between median-subtraction and top-hat:
	- top-hat underestimates background in presence of noise
	- median overestimates background in presence of "holes"
	- median does not work well along curved egdes
- Local background subtraction should only be used for (small) isolated objects
	- e.g., may fail if used to find the background intensity in an image full of cells



&nbsp;

&nbsp;

&nbsp;
