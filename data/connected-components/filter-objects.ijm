
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




