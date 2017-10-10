from ij import IJ;
from ij.plugin import ImageCalculator;

imp1 = IJ.getImage();
imp2 = imp1.duplicate();
IJ.run(imp2, "Minimum...", "radius=10");
IJ.run(imp2, "Maximum...", "radius=10");
ic = ImageCalculator();
imp3 = ic.run("Subtract create", imp1, imp2);
imp3.show();
