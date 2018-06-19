# Handling multi-color images and adding a scale bar

This activity is very similar to the "Image data presentation" above. 

Thus, if you did the "Image data presentation" practical you may not need to do this one.

<img src="https://github.com/tischi/imagej-courses/blob/master/images/color-image.png" width=200>

Aim: make the images look like the image above!

 - __[File>Import>Image Sequence] '../multi-color/'__ (*opens all images in one folder; __Mac__: just click on the folder; __Win__: click on one of the files*)
 - __[Image>Color>Make Composite] 'Display Mode = Composite'__ (*converts to an image type that is good for colors*) 
 - Use the __c__ slider at bottom of image to select a channel and then change its color via __[Image>Lookup Tables]__
 - __[Image>Properties] 'Unit of length = um' 'Pixel width = 0.16' 'Pixel height = 0.16'__ (*changes the scaling to physical distances*)
 - Add scale bar: __[Analyze>Tools>Scale Bar..] 'Overlay = Check'__
 - Save image twice: 
	 - __[File>Save As>Tiff]__
	 - __[File>Save As>Jpeg]__
 - open both images in __PowerPoint__ and compare
 - reopen both in __Fiji__ and compare

What is better for saving? Tiff or Jpeg? 

## Tip for comparing different images

When comparing images it is a good idea to ensure that the LUT settings are the same for all images. This can be achieved with __[Image>Adjust>Brightness/Contrast..]__ clicking __[Set]__ and choosing  __‘Propagate to all other open images = Check’__.


