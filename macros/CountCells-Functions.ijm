//
// ../macros/CountCells-Functions.ijm
//

// User input
//
directory = getDirectory("Select a directory");
threshold = getNumber("Enter threshold", 29);

// Main
//
loadImagesIntoStack(directory);
thresholdImages(threshold);
measureCells();

// Functions
// 
function loadImagesIntoStack(directory) {
	run("Image Sequence...", "open=["+directory+"] sort");
}

function thresholdImages(threshold) {
	setAutoThreshold("Default dark");
	setThreshold(threshold, 255);
	setOption("BlackBackground", false);
	run("Convert to Mask", "method=Default background=Dark"); 
}

function measureCells() {
	run("Set Measurements...", "area display redirect=None decimal=4");
	run("Analyze Particles...", "  show=Nothing summarize stack");
}