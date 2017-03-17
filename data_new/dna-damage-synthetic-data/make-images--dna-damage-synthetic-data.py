#
# Authors: 
# Christian 'Tischi' Tischer; christian.tischer@embl.de
#
# Simluated data of the recruitement of DNA repair enzymes to 
# laser induced DNA damage
# 
# Requirements
# - RandomJ: Add the ImageScience update site.
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

nucleus_area = PI*((d/2)**2)
damage_area = r*l

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


def draw_cell(imp, i, nucleus_total, damage_total, title, noise):
  imp.append(impBG.duplicate()); 
  draw_nucleus( imp[i], nucleus_total / nucleus_area )
  draw_damage( imp[i], damage_total / damage_area )
  imp[i] = blur_and_noise(imp[i], 2, noise)
  imp[i].show()
  imp[i].setTitle(title)
  return(imp)

# Main

# Create background image
impBG = IJ.createImage("Untitled", "16-bit black", 512, 512, 1);
#IJ.run(imp, "RGB Color", "");
#IJ.run(imp, "Radial Gradient", "");
#IJ.run(imp, "16-bit", "");
#IJ.run(imp, "Multiply...", "value="+str(255));
#IJ.run(imp, "Gaussian Blur...", "sigma=30");
#IJ.run(imp, "Divide...", "value="+str(65535/background));
IJ.run(impBG, "Add...", "value="+str(background));



# Intensities
nucleus_total = 1000000

imps = []; 
i = -1;

# No damage

damage_total = 0
i = i + 1; imps = draw_cell(imps, i, nucleus_total, damage_total, "Control", 1)

# With damage, clear signal in the damage region, same total intensity as "No damage"
# => recruitement to damage site

damage_total = nucleus_total * 0.1
nucleus_total_here = nucleus_total - damage_total

i = i + 1; imps = draw_cell(imps, i, nucleus_total_here, damage_total, "Damaged", 1)


# With damage, clear signal in the damage region, less total intensity as "No damage"
# but same ratio of damage/total
# => recruitement to damage site ok, but probably bleaching during the damage
# or overall less expression

bleaching = 0.8
damage_total = nucleus_total * bleaching * 0.1
nucleus_total_here = nucleus_total * bleaching - damage_total

i = i + 1; imps = draw_cell(imps, i, nucleus_total_here, damage_total, "Damaged and treated 01", 1)


# "Treated": with damage, same total intensity as "No damage", but less signal in the damage site
# => the treatment reduced the binding strength of the DNA repair molecule

bleaching = 1.0 # no bleaching
damage_total = nucleus_total * bleaching * 0.05
nucleus_total_here = nucleus_total * bleaching - damage_total
i = i + 1; imps = draw_cell(imps, i, nucleus_total_here, damage_total, "Damaged and treated 02", 1)

# Multiple damage sites close-by
# => Median filter becomes difficult

damage_total = nucleus_total * 0.1
nucleus_total_here = nucleus_total

i = i + 1; imps.append(impBG.duplicate()); 
draw_nucleus( imps[i], nucleus_total / nucleus_area )
## Multiple damage sites

for j in range(-3,4,1):
  ll = l*((10.0-abs(j))/10.0)
  imps[i].setRoi(c+d/2+j*d/9,int(c+(d-ll)/2.0),r,int(ll));
  IJ.run(imps[i], "Add...", "value="+str(0.9*damage_total / damage_area));

imps[i] = blur_and_noise(imps[i], 2, 1)
imps[i].show()
imps[i].setTitle("Multiple damage sites")


# With damage and high noise
# => tophat filter does not work very well

damage_total = nucleus_total * 0.1
nucleus_total_here = nucleus_total - damage_total
i = i + 1; imps = draw_cell(imps, i, nucleus_total_here, damage_total, "Damaged Noisy", 3)

# todo: find a way to add more noise...



