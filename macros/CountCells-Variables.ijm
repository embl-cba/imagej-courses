// User input
directory = "/Users/tischi/Documents/imagej-courses/data_new/mitocheck-movie";
threshold = 29;

// General code
run("Image Sequence...", "open=["+directory+"] sort");
run("Set Measurements...", "area display redirect=None decimal=4");
setAutoThreshold("Default dark");
setThreshold(threshold, 255);
setOption("BlackBackground", false);
run("Convert to Mask", "method=Default background=Dark");
run("Analyze Particles...", "  show=Nothing summarize stack");
