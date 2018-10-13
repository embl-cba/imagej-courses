// get file from user (see also: https://imagej.net/Script_Parameters)
#@File (label="Please select file") file

// open file
open(file);
rename("input");

// threshold
run("Duplicate...", "title=binary");
setThreshold(21, 255);
run("Convert to Mask");

// connected components labeling
run("Connected Components Labeling", "connectivity=4 type=[8 bits]");

// display on input
run("Merge Channels...", "c2=binary-lbl c4=input create ignore");
run("glasbey_inverted");