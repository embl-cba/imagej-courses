
# Microscopy image file formats

Microscopy image files contain information about:
- pixel values;
- various metadata - scaling (pixel size), microscope settings;

Different microscope vendors have their proprietary data formats, which differ how data are structured. ImageJ/Fiji can open most of the common formats by using dedicated import functions (e.g. Bio-Formats).

***Important note***: if possible, store image data in the original file format it contains non-modified pixel values and metadata that can be essential for data processing and interpretation.  

## 1. Simple image format

1 file = 1 image window in ImageJ. All channels and Z-slices and time points are saved in the same file.

## 2.One dataset saved in multiple files

Filename will often contain information about channel scile and timepoint in a structured way. Import functions can analyse these filenames to open muplitpel files as one dataset.

![image](https://user-images.githubusercontent.com/6419504/39753827-730e1530-52c0-11e8-832d-f7eb65a2fd23.png)

---

### Using BioFormats  
*File->Import->Bio-Formats*
![image](https://user-images.githubusercontent.com/6419504/39753042-bb6fe78e-52bd-11e8-9396-da01b1146059.png)

---
### Import result

![image](https://user-images.githubusercontent.com/6419504/39754026-1a31f700-52c1-11e8-8187-0915c82fe85c.png)

---

## 3. Multiple datasets saved in the same file
Can contain images that belong to the different positions in the sample

![image](https://user-images.githubusercontent.com/6419504/39753500-5183f6a6-52bf-11e8-811a-4ef2c4e4a672.png)


---

