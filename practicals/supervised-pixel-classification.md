# Supervised pixel classification

## Software solutions

- http://ilastik.org/
- https://imagej.net/Trainable_Weka_Segmentation

## Practical 

<img width="189" alt="image" src="https://user-images.githubusercontent.com/2157566/39700776-c31fdd46-51fe-11e8-8d2d-c82340c8b27a.png">

- Open “../supervised_segmentation/scanningEM_flyEye.tif”
- Perform supervised pixel classification
  - Run [Plugins > Segmentation > Trainable Weka Segmentation]
  - Add labels using the freehand line tool:
  - Mark regions on the eye [Add to class 1]
  - Mark regions outside the eye [Add to class 2]
  - Try the prediction: [Train classifier]
  - Add more labels to regions where the prediction is not yet satisfactory
  - If you are satisfied export results: [Get probability]
- Perform particle analysis to segment the eye
  - [Image> Adjust..Threshold] 
  - [Analyze..Analyze Particles] 


<img width="134" alt="image" src="https://user-images.githubusercontent.com/2157566/39700789-ce4401a2-51fe-11e8-9fbc-c8941e2a7039.png">
