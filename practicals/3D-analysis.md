# Automated 3-D object detection

## Aim

Count the number of spot-like objects in 3D volume. 

## Motivation

Segmentation of spot structures can be performed by generating maximum projections from 3D datasets. However, in the regions with high object density maximum projections can not represent each object individually, leading to underestimation of the number of structures. Therefore, 3D analysis has to be performed.

## Installation of 3D-ImageJ-Suite (mcib3d) plugins

1. Start Fiji update [ Help > Update > Manage Update Sites ]
2. Select following Fiji update sites
	1. *3D ImageJ Suite*
	2. *ImageScience*
	3. *Java8*
3. Restart Fiji after update (installation process is complete)
Instructions can also be found here:
http://imagejdocu.tudor.lu/doku.php?id=plugin:stacks:3d_ij_suite:start

## Workflow

1. Load input dataset dataset in Fiji
	- "../3D-spot-detection/cell-3d-vesicles-crop.tif"
	- Note: *3D ImageJ Suite* plugins currently can not work with hyperstacks. If you have multicolor or multi-timepoint 3D datasets, you should extract individual 3D stacks for processing
	
2. Switch image format to 32 bit (*Image->Type->32-bit*)
3. Remove the pixel scaling to define all following analysis parameters in pixel units
4. Suppress the noise
	1. Select original stack
	2. Apply 3D median filter to suppress noise:
		1. *Plugins->3D->3D Fast Filters*
		2. then select *Median* as *Filter*
		3. Select 2 pixels smoothing radius in XY (Kernel_XY) and 1 pixel smoothing radius in Z(Kernel_Z)
		4. Press *OK*
	3. Rename newly created image to **Filtered** (*Image->Rename...*)
5. Create background image
	1. Select original stack
	2. Apply 3D median filter to suppress noise:
		1. *Plugins->3D->3D Fast Filters*
		2. Select **Median** as *Filter*
		3. Select 10 pixels Kernel_XY and 3 pixels Kernel_Z
		4. Press *OK*
	3. Rename newly created image to **Background** (*Image->Rename...*)
6. Create background subtracted denoised image:
	1. *Process->Image Calculator*
	2. *Image1*=**Filtered**;*Image2*=**Background**;*Operation*=**Subtract**;
	3. Select *Create new window* and *32-bit result* options
	4. Rename newly created image to **Cleaned** (*Image->Rename...*)
7. Create image with the seed points of the spots
	1. *Plugins->3D->3D Fast Filters*
	2. Select **MaximumLocal** as *Filter*
	3. Select 3 pixels Kernel_XY and 2 pixels Kernel_Z
	4.  Rename newly created image to **Seeds** (*Image->Rename...*)
8. Only brightest pixels on this image will correspond to centers of real spots. Examine values of positive pixels to define thresholds on the seeds
	-Hint: use *Syncronize Windows* tool (*Analyze->Tools->Syncronize Windows*) to correlate positions of spots and identified seeds.
9. Run spot segmentation:
	1. *Plugins->3D->3D Spot Segmentation*
	2. Set identified seed threshold
	3. *Local Threshold method*=**Gaussian fit**
	4. *Radius max*=**10**
	5. *Volume min*=**10**
	6. *Volume max*=**1000**
	7. *Seeds*=**Seeds**
	8. *Spots*=**Cleaned**
	9. *Output*=**Both**
10. Inspect the outputs
	1. 16-bit mask with different pixel values assigned to different spots
	2. 3D RoiManager to select spots and overlay them on raw or processed (**Filtered**, **Cleaned**, etc.) images. Multiple objects can be selected and overlaid at the same time.

# Challenge task: Count spots in nuclei

## Description

- Dataset `spots-in-nuclei.tif` has two channels 
	- Nuclear stain (channel 1)
	- Spots inside nuclei (channel 2)
	- 
- Aim: identify how many spots belong to each nucleus

## Workflow

- Segment nuclei
	- Isolate nuclei channel
	- Smooth to reduce the noise
	- Use `3D simple segmentation` function
	- Produce count mask
- Segment spots
	- Isolate spots channel
	- Use workflow above for spot detection in the whole image
	- Add identified 3D spots to 3D ROI Manager
- Identify which spots belong to which nucleus
	- Measure minimum and maximum values of 3D spots on the nuclear count mask
	- Measured values indicate index of target nucleus 
