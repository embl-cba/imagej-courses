from ij import IJ
from ij.gui import OvalRoi, Line

# Requirements
# - RandomJ: RandomJ is available from the ImageScience update site.

r = 3
c = 256
dc = 30
n = 8
SNR = 3
blur = 1 

imp = IJ.createImage("Untitled", "8-bit black", 512, 512, 1);
IJ.run(imp, "RGB Color", "");
IJ.run(imp, "Radial Gradient", "");
IJ.run(imp, "8-bit", "");
IJ.run(imp, "Divide...", "value="+str(SNR));

for i in range(n):
  imp.setRoi(OvalRoi(c-i*dc,c-i*dc,r,r));
  IJ.run(imp, "Multiply...", "value="+str(SNR));


# Line with dots
for i in range(n):
  imp.setRoi(OvalRoi(80+i*dc,50,r,r));
  IJ.run(imp, "Multiply...", "value="+str(SNR));
imp.setRoi(80,50,int(3/2*c),r);
IJ.run(imp, "Add...", "value=80");
  
# Crossing lines
imp.setRoi(230,150,100,r);
IJ.run(imp, "Add...", "value=80");
imp.setRoi(250,100,r,100);
IJ.run(imp, "Add...", "value=80");
imp.setRoi(270,100,r,100);
IJ.run(imp, "Add...", "value=30");
imp.setRoi(300,100,r,100);
IJ.run(imp, "Add...", "value=10");


# Nuclear Envelope
rc = 70
imp.setRoi(OvalRoi(int(c),int(c/2+c),rc,rc));
IJ.run(imp, "Properties... ", "  width="+str(r));
IJ.run(imp, "Draw", "slice");

# Full Nucleus
imp.setRoi(OvalRoi(int(c/2),int(c/2+c),rc,rc));
IJ.run(imp, "Multiply...", "value="+str(SNR));

# Empty hole
imp.setRoi(OvalRoi(int(c/2+c),int(c/2+c),rc,rc));
IJ.run(imp, "Multiply...", "value=0.5");

# Blur
IJ.run(imp, "Select None", "");
IJ.run(imp, "Gaussian Blur...", "sigma="+str(blur));

# Noise
IJ.run(imp, "RandomJ Poisson", "mean=1.0 insertion=Modulatory");

# Rename
imp.setTitle("test-image");
#imp.show();
