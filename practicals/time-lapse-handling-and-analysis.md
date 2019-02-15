# Basic time-lapse data annotation and movie generation

- [ File > Open ] “../tracking/TransportOfEndosomalVirus.tif”
- Add time stamps: [ Image > Stacks > Time Stamper] (dt=2s)
- Save as movie: [File > Save As > AVI…] (jpeg compression)

# Manual tracking

There are multiple tracking plugins in ImageJ.
Noteworthy is [Mastodon](https://github.com/fiji/TrackMate3), which is very good for really big data.
Here, we will use a very simple manual tracking plugin.

To determine the motility of (not too many) particles manual tracking can be a good option.

- Open “../tracking/ TransportOfEndosomalVirus.tif”
- Start tracker: [ Plugins > Tracking > Manual Tracking ]
	- Enter scaling: [X] Show Parameters
	- Time interval: 2 s
	- x/y calibration: 0.129 um
- Track a few (e.g., 3) different particles
	- [X] Use centering correction? Local Maximum
- Track particles: [Add track] click..click… [End track]
- Try different drawing options, e.g. [Overlay Dots & Lines]

Examine the results table: what are the fastest speeds that you measured?

![image](https://user-images.githubusercontent.com/2157566/38928238-6c991366-4308-11e8-8fcd-1df408223676.png)

# Kymograph analysis

Kymographs are a very useful way of visualising and quantifying motion in movies. The are used in many biological publications.

- Open “../kymograph/tubulin-tirf-dt500ms-dxy106nm.avi”
- Enhance microtubules [ Process > Subtract Background ]
	- 5 pixel radius (no “light background”)
- Trace a dynamic microtubule (Segmented Line Tool)
	- Optional Trick:  Make a max-projection of the movie 
- Make a kymograph [ Image > Stacks > Reslice ]
	- Accept all default values
- Measure the growth and shrinkage speed of the microtubule

![image](https://user-images.githubusercontent.com/2157566/38929198-dbb6e41e-430b-11e8-8e3b-0fe238209086.png)
