run("Image Sequence...", "open=/Users/tischi/Documents/imagej-courses/data_new/mitocheck-movie sort");
run("Set Measurements...", "area display redirect=None decimal=4");
setAutoThreshold("Default dark");
//run("Threshold...");
setThreshold(29, 255);
setOption("BlackBackground", false);
run("Convert to Mask", "method=Default background=Dark");
run("Analyze Particles...", "  show=Nothing summarize stack");
