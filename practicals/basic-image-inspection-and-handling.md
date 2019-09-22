# Inspection of the numerical content of images

An image essentially is an array of numbers with some metadata. For scientific image analysis it is very important to constantly inspect the numeric content of our images, for instance to check whether the image was acquired properly, or whether a mathematical operation such as background subtraction had the desired effect.

## Activity: Image inspection <a name="image_inspection"></a> 

Let's open an image and explore different tools to inspect the numbers in this image.
We start by inspection an 8-bit image, where the numbers range from 0 to 255 (2^8-1); we'll explore different bit depths later.

- Open image "data/image-inspection/B.tif"  [File > Open]

### Mouse over

Simply move with the mouse over the image; the intensity will be shown in ImageJ's menu bar.

&nbsp;

&nbsp;

### Pixel inspection tool

- Menu bar: [Px]

&nbsp;

&nbsp;


### Intensity line profile

- Menu bar: Select the line profile tool
- [Analyze > Plot Profile]

&nbsp;

&nbsp;


		
### Histogram

- [Analyze > Histogram]

&nbsp;

&nbsp;

# Lookup tables (LUTs)

LUTs assign a certain color to each numerical value. Intensity differences are best seen using a grayscale LUT. Choosing the LUT color similar to the emission color of the imaged fluorophore can also make sense. LUTs with multiple colors (e.g., "Fire" in ImageJ) are good for simultaneously seening very dim and very bright images. Finally, LUTs where only the lowest and highest value have a certain color are useful for microscopy, e.g. to indicate saturated pixels.

## Activity: Adjust Brightness & Contrast

While the colors in a given LUT are fixed, one can change how these colors are mapped onto the numbers in the image.

- Open image "data/image-inspection/B.tif"  [File > Open]
- Change the LUT settings:
	- [Image > Adjust > Brightness/Contrast]

Note that this does not change the numbers but only the appearance on your screen.

**Important: Don't press [Apply] as this will in fact change the pixel values.** 


&nbsp;

&nbsp;



## Activity: Explore different LUTs 

- Open image "data/image-inspection/B.tif"  [File > Open]
- Explore different LUTs [Image > Lookup Tables], e.g.
	- Grays
		- If you have no specific other reason, this is the "go-to" LUT
	- HiLo
		- Good for seeing saturated pixels
		- Red: highest, Blue: lowest
		- Important note: "highest" and "lowest" depend on your Brightness&Contrast settings!
	- Fire
		- Good for seeing dim and bright values at the same time


&nbsp;

&nbsp;


# Image data presentation

<img width="1056" alt="image" src="https://user-images.githubusercontent.com/2157566/41596158-b7dea420-73c9-11e8-95e6-4837fd6f222c.png">

- Open all files in “../image-presentation” 
- Generate above figure in PowerPoint, using the following Fiji commands:
	- [ Image > Color > Merge Channels ]
		- This combines two single channel images into one so called *Composite* image
	- [ Image > Rename ]
		- After merging the images their names will always be "Composite". Thus, not to loose track, you should immediately rename to, e.g. "treated" or "untreated".
	- [ Analyze > Tools > Scale Bar ]
	- [ Image > Adjust > Brightness&Contrast ]
		- After adjusting the LUT for one image, click [ Set ] and
		* [X] “Propagate to all other open images”
			- This is __super important__ as it will ensure that the same LUT is used for all open images, which is critical for a scientifically meaningful presentation of your data.
			- All pairs of images that were acquired with the same microscope settings should be treated this way. In above example figure all images in the same column must have the same LUT settings. On the other hand, it does typically not make sense to use the same LUT for, e.g., a DAPI signal and a GFP signal.
			- This also works for *Composite* images 
	- [ Edit > Copy to System ] 
		- Copies the active image to the clip-board of your computer from where you can paste it, e.g. into PowerPoint.
		- The good thing about this command is that the image (in terms of the LUT settings) will look the same in PowerPoint as it did on your screen in ImageJ. In other words, the LUT settings are "burned into" the image.

 
&nbsp;

&nbsp;

&nbsp;


# Image format conversion

Unfortunately there are many different image formats and since not all software can open all formats you most likely will have to sometimes save your images in different formats. It is of utmost importance that you check what happens to the numerical content of your images when you are doing this! So let's practice!

## Activity: Save an image in different formats and inspect how this affects its numerical content and file size

- Open “../image-format-conversion/16bit.tif” [File > Open]
	- Adjust the display such that you actually see something [Image > Adjust > Brightness/Contrast]
- Save as **Jpeg** using different levels of compression (quality)
	- Adjust Jpeg quality (0-100) to 10 [Edit > Option > Input/Output]
	- save as "quality_10.jpg"  [File > Save As > Jpeg]
	- repeat for Jpeg qualities 75, and 100
- Save as **Png** "image.png" [File > Save As > PNG]
- Save as **Zip** "image.zip" [File > Save As > ZIP]
- Now, adjust the display such that the image **appears saturated** [Image > Adjust > Brightness/Contrast]
	- Save as "saturated.tif" [File > Save As > Tiff]
	- Save as "saturated.jpg" [File > Save As > Jpeg]
	- Save as "saturated.png" [File > Save As > PNG]

Now, let's inspect what happened to the image when saving it in the different formats.

1. Go to the folder where they have been saved an observe the file sizes
2. Open them again in Fiji and check what happened to the gray values

To document your findings, you may make a table like below and fill in columns:

 Image       | File size | Gray values (min, max) 
-------------|-----------|------------------------ 
 16bit.tif   |           |
 quality_10.jpg    |       |
 quality_75.jpg      |          |
 quality_100.jpg    |                |
 image.png     |                            |
 image.zip     |                            |
 saturated.tif |   |
 saturated.jpg |   |
 saturated.png |   |


&nbsp;

&nbsp;

&nbsp;

Take home message: Always check what happens to your image when you save it! 

&nbsp;

&nbsp;

&nbsp;



# Important numerical properties of microscopy images

## Background (offset)

&nbsp;

&nbsp;

## Dynamic range

&nbsp;

&nbsp;

## Saturation

&nbsp;

&nbsp;

## Activity: Image content inspection

In this activity we will open several images and find out which "issues" they have.
The aim is to assign each image to one of the following issues:
- no problem
- high background
- clipping (too low background)
- low dynamic range
- too much saturation

Use below workflow to inspect the images:
- Open “data/image-inspection/A.tif”  [File > Open]
- Also open B.tif, C.tif, D.tif, E.tif 
- Use the following [image inspection methods](#image_inspection) to check above the images and find their "issues", e.g, inspect the values in the images by
	- Adjusting the display [Image > Adjust > Brightness/Contrast]
	- Examining gray values in whole image [Analyze > Histogram]
	- Analyzing gray values along a line [Analyze > Plot Profile]

What did you find?

 Image |  This image has the following issue |
-------|-------------------------------------|
A      |                                     |
B      |  no problem     |
C      |                                     |
D      |                                     |
E      |                                     |

&nbsp;

&nbsp;

&nbsp;

## Image bit depths in ImageJ

- 8-bit
	- integers from 0-255 (2^8-1)
- 16-bit
	- integers from 0-65535 (2^16-1)
- 32-bit floating point
	- can have negative numbers, such as -1
	- can have non-integer numbers, such as 1.5 or -3.2
	- this format is generally recommended as soon as you do any kind of mathematical operations on your images
	- disadvantage: needs more memory and disk space 

Although ImageJ does not specifially support it, your images could also have been acquired with cameras of different bit depth such as 12 or 14 bit; such images will be stored and dealt with as 16-bit. 

&nbsp;

&nbsp;


## Image bit depth conversions

Image bit depth conversion is something that you should generally avoid, but sometimes you can't; either because you need to save disk space or because certain operations or plugins only work with certain bit depths. Let's thus explore what happens if you do convert between different bit depths.


## Activity: Conversion from 8-bit to 32-bit floating point

- Open image "../image-inspection/B.tif" [File > Open]
- Duplicate the image and rename it to "32-bit" [Image > Duplicate]
- Convert to 32-bit floating point [Image > Type > 32 bit]
- Inspect the gray values! Did they change after the conversion?

&nbsp;

## Activity: Conversion from 16-bit to 32-bit floating point
 
- Open image "../image-format-conversion/16bit.tif" [File > Open]
- Duplicate the image and rename it to "32-bit" [Image > Duplicate]
- Convert to 32-bit floating point [Image > Type > 32 bit]
- Inspect the gray values! Did they change after the conversion?

&nbsp;

## Activity: 16-bit to 8-bit conversion

OK! Now comes the **tricky part**, where several projects were going very wrong in the past!

- Open "data/image-format-conversion/16bit.tif" [File > Open]
- Inspect the gray values: What are the minimum and maximum? Note them down.
- Adjust the display such that it looks nice [Image > Adjust > Brightness/Contrast]
- Convert to 8-bit [Image > Type > 8bit]
- Inspect the gray values again: What are the minimum and maximum now?

Hopefully you are **shocked** that we all got different results! How can this be?

&nbsp;

### Discussion: How to convert 16-bit to 8-bit

- 0, 65535 => 0, 255
	- Preserves intensities but looses dynamic range
- min, max => 0, 255
	- Maximizes dynamic range, but looses intensity information
- minLUT, maxLUT => 0, 255 
	- Leave it up to the user!
	- This is what ImageJ is doing!

&nbsp;

&nbsp;

&nbsp;


# Image bit depths

Images can have different bit depths. Let's start by exploring some of the limitations of the 8-bit image that we were dealing with until now.

## Activity: Exploring the limitations of an 8-bit image <a name="8bit_limitations"></a> 

### Adding numbers

- Open image "data/image-inspection/B.tif" [File > Open]
- Copy image [Image > Duplicate]
	- Title: "after math"
- Add 100 to each pixel in the image [Process > Math > Add]
- Inspect the gray values!
- Find (two) pixels for which the result is correct and incorrect

| x  | y  | original value  | value after math   | correct?  |
|---|---|---|---|---|
| &nbsp;  |   |   |   |   |
| &nbsp;  |   |   |   |   |


### Subtracting numbers

- Open image "data/image-inspection/B.tif" [File > Open]
- Copy image [Image > Duplicate]
	- Title: "after math"
- Subtract 100 from each pixel in the image [Process > Math > Subtract]
- Inspect the gray values!

### Dividing numbers

- Open image "data/image-inspection/B.tif" [File > Open]
- Copy image [Image > Duplicate]
	- Title: "after math"
- Copy the image [Image > Duplicate]
- Divide each pixel in the image by 2 [Process > Math > Divide]
- Inspect the gray values!
 

### Conclusions

- Obviously this is not what we want since it is all wrong :-).
- If possible try to avoid mathematical operations on a pixel level
- If you need to change the values in an image consider changing it to a "floating point image" (see below).


&nbsp;

&nbsp;

&nbsp;

## Activity: Exploring floating point images

Floating point images are there to solve the issues that you encountered in above activity, because they allow for numbers like -1.2 and 0.55, which are not allowd in integer images.

- Open image "data/image-inspection/B.tif" [File > Open]
- Duplicate the image and already name "32-bit" [Image > Duplicate]
- Convert to 32-bit floating point [Image > Type > 32 bit]
- Inspect the gray values! Did they change after the conversion to 32 bit?
- Now let's repeat [above activity](#8bit_limitations)

Much better, right?!

&nbsp;

&nbsp;

&nbsp;





