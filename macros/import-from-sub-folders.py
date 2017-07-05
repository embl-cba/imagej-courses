# Walk recursively through an user-selected directory
# and add all found filenames that end with ".tif"
# to a VirtualStack, which is then shown.
#
# It is assumed that all images are of the same type
# and have the same dimensions.

# todo: replace by reg-exp matching
# todo: make it optional whether to load as real or as virtual stack

from ij import IJ
from ij.io import DirectoryChooser
from ij import VirtualStack, ImagePlus, ImageStack
import os
import re

def run():
  sId = IJ.getString("Filenames contain:", "T0000");
  srcDir = DirectoryChooser("Choose!").getDirectory()
  if not srcDir:
    # user canceled dialog
    return
  # Assumes all files have the same size
  stack = None
  for root, directories, filenames in os.walk(srcDir):
    for filename in filenames:
      # Skip non-TIFF files
      if not (sId in filename):
        continue
      print(filename)
      path = os.path.join(root, filename)
      # Upon finding the first image, initialize the VirtualStack
      imp = IJ.openImage(path)
      if stack is None:
        # stack = VirtualStack(imp.width, imp.height, None, srcDir)
        stack = ImageStack(imp.width, imp.height)
      # Add a slice to the virtual stack, relative to the srcDir
      #
      #stack.addSlice(path[len(srcDir):])
      
      # Add a slice to the real stack
      #
      stack.addSlice(filename, imp.getProcessor())
      
  # Make a ImagePlus from the stack
  ImagePlus("Stack from subdirectories", stack).show()
  
run()