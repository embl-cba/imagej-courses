// Get input from user
#@File (label="Please select an input image") inputImage 
#@File (style="directory", label="Please select an output directory") outputDirectory

// Open image
run("Close All");
open(inputImage);

// Binarize (Threshold)
setThreshold(24, 255);
setOption("BlackBackground", true);
run("Convert to Mask");

// Connected components
run("Connected Components Labeling", "connectivity=4 type=[16 bits]");

// Measure shape
run("Analyze Regions", "area circularity");

// Export results
saveAs("Results", outputDirectory + "/" + Table.title + ".csv");

// Clean up
run("Close All");
close(Table.title + ".csv");
//close("*.csv");
