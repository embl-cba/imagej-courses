#@File binary

run("Close All");
open(binary);
rename("binary");

run("Chamfer Distance Map", "distances=[Chessknight (5,7,11)] output=[32 bits] normalize");
run("Invert");
run("Gaussian Blur...", "sigma=10");
rename("inverted_distances");


run("Classic Watershed", "input=inverted_distances mask=binary use min=0 max=255");
rename("split_objects");
