# 3D image inspection

There are many ways of looking at 3D data in ImageJ. In this pratical we will explore a number of them.

- Hyperstack viewer
- Ortho-slicing
- Projections
- 3D Viewer
- ClearVolume
- BigDataViewer
- 3DScript
	- https://bene51.github.io/3Dscript/gallery.html

## Example data 

- Please open, e.g., “../3D-data/???” [File > Open]

## Hyperstack viewer

The hyperstack viewer enables browsing of 5-D (3D + channel + time ) data in a slice mode.

<img width="595" alt="image" src="https://user-images.githubusercontent.com/2157566/38975745-4d8c71c8-43af-11e8-887c-
033aebc2ad84.png">

### Multi-color viewing options

There are different ways to look at multi-color images, you can switch between them:

- [ Image > Color > Channels Tool ]
	- Grayscale
	- Color
	- Composite

![image](https://user-images.githubusercontent.com/2157566/38928439-24556630-4309-11e8-87e6-56d4f85cdbfd.png)

#### Usage of the channel slider

The meaning of the channel slider in composite mode is fantastic, but confusing:

- It does **not** change what you see!
- It changes however what channel you work on and measure!

## Ortho-slicing

Ortho-slicing also is a good way of looking at 3-D data and typically is available in all softwares, including microscope acquisition softwares.

- [ Image > Stacks > Orthogonal Views ]

![image](https://user-images.githubusercontent.com/2157566/38928505-5af4e8c8-4309-11e8-859d-148d3dad1a54.png)

## Non-orthogonal slicing

You can also slice your data at an angle.

- Draw a line on the image, indicating the slicing plane
- [ Image > Stacks > Reslice ]

## Projections

Another way to inspect (and sometimes even analyse) images are projections of your data.

- [ Image > Stacks > Z Project ]

In general, maximum projections are the best for looking at the data.
For quantification however, sum projections can be biologically more meaningful.

You can also realise projections along different axes but z by first running a "reslicing" without specifying a particular plane.

- [ Image > Stacks > Reslice ]
- [ Image > Stacks > Z Project ]

## 3D Viewer

The 3D Viewer provides volume rendering; however, we feel that ClearVolume (see below) is more user-friendly.

- [ Plugins > 3D Viewer ]
	- Resampling factor: This is how much you downsample (more => faster rendering)
- Examine data by
	- Rotating (left mouse button)
	- Zooming (mouse wheel)
- Change Display Settings
	- Edit...Change Color
	- Edit...Transfer Function
	
![image](https://user-images.githubusercontent.com/2157566/38928558-7f5a455a-4309-11e8-93cd-dbb09cc0c2ca.png)

## ClearVolume

ClearVolume provides volume rendering with a nice user interface.

- Install ClearVolume update site:
	- [ Help > Update > Manage Update Sites > [X] ClearVolume ]
		- Click [ Close ]
		- Click [ Apply Changes ]
	- Restart Fiji to finish the installation
- Open “../psf/beads_p_open.tif” [File > Open]
- Fiji Search Bar: ClearVolume => Open in ClearVolume

![image](https://user-images.githubusercontent.com/2157566/38928602-9ea40b1c-4309-11e8-84cc-b67bc5188960.png)

## BigDataViewer

The BDV provides 3-D slicing in arbitrary orientations and support big image data, which does not fit into the RAM of your computer.

- [ Plugins > BigDataViewer > Open current image ]

![image](https://user-images.githubusercontent.com/2157566/38928635-cd32d968-4309-11e8-9432-d4ef5fc93680.png)

## 3Dscript

There also is a way in ImageJ to make professional 3D rotation animations:

- Update Site: https://romulus.oice.uni-erlangen.de/updatesite/
- Introduction: https://bene51.github.io/3Dscript/
- Manual: https://bene51.github.io/3Dscript/Manual.pdf
- Examples: https://bene51.github.io/3Dscript/gallery.html

## Other (also commercial) solutions

There are of course many other software to look at 3D image data.
On the commerical side Imaris and Arivis are popular in Biology. 
In terms of open-source, Chimera is probably worth exploring: https://www.cgl.ucsf.edu/chimera/

# Point spread function examination

For microscopy, it is very important to understand the point spread function (PSF) very well. 
Thus, in this practical, we will closely examine PSFs, acquired at different wavelengths.

- Open “../psf/beads_p_close.tif” [File > Open]
	- This is a so-called hyperstack with two channels: green (c1) and red (c2)
- Generate side views [Image > Stacks > Reslice]
	- Don't avoid interpolation
- Project into 2-D  [Image > Stacks > Z-Project]
	- Projection Type: Sum Slices
- Repeat above steps for “../psf/beads_p_open.tif”

## Activity

1. Visually comparing the PSFs of closed and open pinhole, what is the main difference?
2. Can you also see a difference between the green and the red PSF? What would you expect?

<img width="800" alt="image" src="https://user-images.githubusercontent.com/2157566/38828012-00cd084e-41b5-11e8-9ed6-488641015eed.png">

## Optional activity: measure the width of the PSFs

Quantify the width of the green and red PSFs in the x/y-direction.

- Choose a central z-plane in the original file
	- Using the channel slider of the hyperstack viewer, select the green channel.
- Draw a line profile across the signal 
- Get the profile [Analyze > Plot Profile]
- Measure the profile's shape and width [Analyze > Tools > Curve Fitting (gaussian)]
	- You need to copy the list from the profile plot into the fitting tool
- Repeat with the red channel.

<img width="800" alt="image" src="https://user-images.githubusercontent.com/2157566/38828149-678479c8-41b5-11e8-99b0-1141413d0b33.png">
