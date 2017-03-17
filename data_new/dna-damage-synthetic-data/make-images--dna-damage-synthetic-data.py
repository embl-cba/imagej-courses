#
# Author: Christian 'Tischi' Tischer, christian.tischer@embl.de
#
# Time-lapse data of laser induced nuclear damage
# 
# Requirements
# - RandomJ: RandomJ is available from the ImageScience update site.
#

from ij import IJ
from ij.gui import OvalRoi, Line

# Globals

c = 256
d = 80
l = int(d*0.8)
r = 3
n = 8
background = 200
blur = 1
PI = 3.141 

# Functions

def draw_nucleus(imp, value):
  imp.setRoi(OvalRoi(int(c),int(c),d,d));
  IJ.run(imp, "Add...", "value="+str(value));

def draw_damage(imp, value):
  imp.setRoi(c+d/2,int(c+(d-l)/2.0),r,l);
  IJ.run(imp, "Add...", "value="+str(value));

def blur_and_noise(imp, blur, noise):
  IJ.run(imp, "Select None", "");
  # Blur
  IJ.run(imp, "Gaussian Blur...", "sigma="+str(blur));
  # Noise
  IJ.run(imp, "RandomJ Poisson", "mean="+str(noise)+" insertion=Modulatory");
  imp.close()
  imp = IJ.getImage()
  IJ.run(imp, "16-bit", "");
  IJ.resetMinAndMax(imp);
  return(imp)

# Main

# Create background image
imp = IJ.createImage("Untitled", "16-bit black", 512, 512, 1);
#IJ.run(imp, "RGB Color", "");
#IJ.run(imp, "Radial Gradient", "");
#IJ.run(imp, "16-bit", "");
#IJ.run(imp, "Multiply...", "value="+str(255));
#IJ.run(imp, "Gaussian Blur...", "sigma=30");
#IJ.run(imp, "Divide...", "value="+str(65535/background));
IJ.run(imp, "Add...", "value="+str(background));

# Areas
nucleus_area = PI*((d/2)**2)
damage_area = r*l

# Intensities
nucleus_total = 1000000

# No damage
imp2 = imp.duplicate()
draw_nucleus(imp2, nucleus_total / nucleus_area)
imp2 = blur_and_noise(imp2, 2, 1)
imp2.show()

# With damage, clear signal in the damage region, same total intensity as "No damage"
# => recruitement to damage site
damage_total = nucleus_total * 0.1
nucleus_total = nucleus_total - damage_total
damage_mean = damage_total / damage_area
nucleus_mean = nucleus_total / nucleus_area
imp3 = imp.duplicate()
draw_nucleus( imp3, nucleus_total / nucleus_area )
draw_damage( imp3, damage_total / damage_area )
imp3 = blur_and_noise(imp3, 2, 1)
imp3.show()

# With damage, clear signal in the damage region, less total intensity as "No damage"
# but same ratio of damage/total
# => recruitement to damage site ok, but probably bleaching during the damage

# "Treated": with damage, same total intensity as "No damage", but less signal in the damage site
# => the treatment reduced the binding strength of the DNA repair molecule

# Same signal in damage site but less in total ("treated")
# => increased binding strength and less expression

# With damage and high noise
# => tophat filter does not work very well



# With damage, same total intensity as "No damage", low noise



# Rename
