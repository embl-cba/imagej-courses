# Image registration

<img width="732" alt="image" src="https://user-images.githubusercontent.com/2157566/39701434-661922c6-5201-11e8-9978-32e42a1d1406.png">

Image taken from: https://github.com/SuperElastix/elastix/releases/download/4.9.0/elastix-4.9.0-manual.pdf

## Software solutions

- [elastix](https://github.com/SuperElastix/elastix/wiki)
- ImageJ 
  - [stackreg](http://bigwww.epfl.ch/thevenaz/stackreg/)
  - [BigWarp](https://imagej.net/BigWarp)
  - [N-D Sequence Registration](https://github.com/tischi/fiji-plugin-imageRegistration)


## Rotational jitter correction

When acquiring large z-stacks in can happen that a living sample moves during the time it takes to acquire the stack.
This can lead to motion artifacts that can however sometimes be corrected.

- [ Help > Manage Update Sites ] Add BIG-EPFL and restart Fiji
- [ File > Open ] "../registration/rotational-jitter.tif"
- StackReg: Rigid Body


 

