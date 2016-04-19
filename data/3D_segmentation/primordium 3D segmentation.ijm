// duplicate subset
selectWindow("C1-primordium.tif");
run("Duplicate...", "title=C1-primordium-1.tif duplicate range=1-26");
selectWindow("C2-primordium.tif");
run("Duplicate...", "title=C2-primordium-1.tif duplicate range=1-26");
// gray LUTs
selectWindow("C1-primordium-1.tif"); run("Grays");
selectWindow("C2-primordium-1.tif"); run("Grays");

// convert to probability maps
selectWindow("C1-primordium-1.tif");
setMinAndMax(103, 1135);
run("8-bit");
run("Invert", "stack");

selectWindow("C2-primordium-1.tif");
setMinAndMax(125, 1574);
run("8-bit");

// multiply
imageCalculator("Multiply create 32-bit stack", "C1-primordium-1.tif","C2-primordium-1.tif");
setMinAndMax(230, 50000);
run("8-bit");

// erode
run("3D Fast Filters","filter=Minimum radius_x_pix=1 radius_y_pix=1 radius_z_pix=1 Nb_cpus=4");

// smooth 
run("Gaussian Blur...", "sigma=2 stack");

// find objects
run("3D Objects Counter", "threshold=51 slice=13 min.=1000 max.=263952 objects statistics summary");
run("005-random");

