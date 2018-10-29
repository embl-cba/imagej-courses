#
# Main differences of python scripting to macro programming:
# - use # instead of // for comments
# - needs import statements such as: from ij import IJ
# - macro recording should be done using Java instead of Macro, however
#    - recorded null should be replaced by None
#    - recorded true should be replaced by True
# - use IJ.* instead of * for running IJ menu commands
# - string casting need to be done explicitly, using str( )
# - commands generally do not work on the active image but need a imp (ImagePlus) object to operate on.

from ij import IJ;
from ij import Prefs;

# Get input from user
#@File image (label="input image")
#@File (style="directory", label="output directory") outputDirectory

# Open image
IJ.run("Close All");
imp = IJ.openImage( str(image) );
title = imp.getTitle();

# Binarize (Threshold)
IJ.setRawThreshold(imp, 24, 255, None);
Prefs.blackBackground = True;
IJ.run(imp, "Convert to Mask", "");

# Connected components
IJ.run(imp, "Connected Components Labeling", "connectivity=4 type=[16 bits]");

# Measure shape
IJ.run("Region Morphometry");

# Export results
IJ.saveAs("Results", str(outputDirectory) + "/" + title + ".csv");

# Clean up
IJ.run("Close All");
