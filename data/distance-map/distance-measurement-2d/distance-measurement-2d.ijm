//
// INPUT
//

// define variables such that the code below becomes independent of specific inputs
objects = "binary-nucleus.tif";
labels = "vesicles-label-map.tif";

//
// COMPUTATION
//

// select the binary image with the object(s) to which we want to compute the distances to 
selectWindow(objects);

// we need to invert this, because the distance map measures distances to background pixels
run("Invert");

// run the distance map computation
run("Chamfer Distance Map", "distances=[Quasi-Euclidean (1,1.41)] output=[32 bits] normalize");
rename("distances");

// measure "intensity" ( = distance ) of objects in the distance map image 
selectWindow(labels);
rename("labels");
run("Intensity Measurements 2D/3D", "input=distances labels=labels mean");
