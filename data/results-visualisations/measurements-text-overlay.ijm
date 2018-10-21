run("Particle Analysis 3D", "volume inertia surface_0=[Crofton (13 dirs.)] euler_0=C26");

// TODO: change font size: setFont

for ( i = 0; i < Table.size; ++i )
{
	volume = Table.get( "Volume", i );
	x = Table.get( "Elli.Center.X", i );
	y = Table.get( "Elli.Center.Y", i );
	z = Table.get( "Elli.Center.Z", i );
	
	// TODO: change to unscaled coordinates: toUnscaled

	Overlay.drawString( volume, x, y );
	Overlay.setPosition( z );	
}

Overlay.show();




