# Advanced image filtering

Please first check out the (basic image filtering)[https://github.com/tischi/imagej-courses/blob/master/practicals/image-filtering.md#basics-of-image-filtering] section.

## Spot enhancement using the Difference of Gaussian

The Difference of Gaussian (DoG) is a very famous method for enhancement of blob=like structures. It works well even when there is uneven background and also in noisy images.

Workflow:
- Blur image with a small Gaussian (about the size of the objects)
- Blur image with a large Gaussian (about two-three times the object size)
- Subtract the large blur from the small blur; this is the DoG!
- Threshold the resulting image to find the object centers
- Fiji commands:
	- [Process > Filters > Gaussian]
	- [Process > Image Calculator]
	- [Analyze > Analyze Particles] or [Process > Find Maxima]

Discussion:
- The object shape is not preserved with this method

	- Workflow:
		- Find object centers using DoG
		- Find object volumes growing from the object centers
		
    
## Hessian matrix eigenvalues

...

## Structure tensor eigenvalues

...

