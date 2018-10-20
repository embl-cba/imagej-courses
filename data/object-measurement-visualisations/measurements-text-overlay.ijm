run("Close All");
open("/Users/tischer/Documents/imagej-courses/data/object-measurement-visualisations/nuclei-2d.tif");

setThreshold(23, 255);
run("Convert to Mask");
run("Connected Components Labeling", "connectivity=4 type=[16 bits]");
run("Region Morphometry");


// https://imagej.nih.gov/ij/developer/macro/functions.html
// Search: "Overlay"
// Search: "Table"


for ( i = 0; i < Table.size; ++i )
{
	area = Table.get( "Area", i );
	// ACTIVITY: change Font size
	Overlay.drawString( area, 30, 30, 0.0);	
}

Overlay.show();




