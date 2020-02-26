#@File labelImage

// open image
run("Close All");
open(labelImage);

// perform measurements
run("Analyze Regions 3D", "volume surface_area mean_breadth sphericity euler_number centroid inertia_ellipsoid ellipsoid_elongations max._inscribed surface_area_method=[Crofton (13 dirs.)] euler_connectivity=C26");

// TODO: change font size: setFont
setFont("SansSerif", 4);

for ( i = 0; i < Table.size; ++i )
{
	volume = Table.get( "Volume", i );
	x = Table.get( "Centroid.X", i );
	y = Table.get( "Centroid.Y", i );
	z = Table.get( "Centroid.Z", i );

	toUnscaled(x, y, z);
	print(x);

	Overlay.drawString( volume, x, y );
	Overlay.setPosition( z );	
}

Overlay.show();




