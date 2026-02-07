A DICOM file =

📷 Pixel image

🏷 Metadata tags

🏥 Patient / study info

⚙ Device parameters

Think:

```
DICOM = { header info + pixel array }
```

🟢 2. Loading a DICOM (Most Basic)
```
import pydicom

ds = pydicom.dcmread("sample.dcm")
```
View all metadata
print(ds)

Access specific fields
```
print(ds.PatientName)
print(ds.Modality)
print(ds.StudyDate)
```
🟢 3. Most Important Functions
A. Read
```
ds = pydicom.dcmread(path)
```

B. Get tags safely
```
ds.get("PatientName", "Not Available")
```

C. Check if tag exists
```
if "PatientID" in ds:
    print(ds.PatientID)
```
D. Pixel array
```
img = ds.pixel_array
print(img.shape)
```
🟢 4. Working with Images
Display DICOM
```
import matplotlib.pyplot as plt

plt.imshow(ds.pixel_array, cmap='gray')
plt.show()

#Normalize
import cv2
img = ds.pixel_array
img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
```

🟢 5. Modify Tags
```
ds.PatientName = "TEST"

ds.save_as("new.dcm")
```

Delete:
```
del ds.PatientName
```
🟢 6. Important DICOM Concepts
VR = Value Representation

Common ones:
```
VR	Meaning
PN	Person Name
DA	Date
UI	Unique ID
LO	Long String
US	Unsigned Short
```

Function / Attribute 	Purpose	Example
```
dcmread()	Loads a DICOM file from disk.	ds = pydicom.dcmread('file.dcm')
pixel_array	Converts raw pixel bytes into a NumPy array for processing. data = ds.pixel_array
save_as()	Saves a modified dataset to a new file.	ds.save_as('updated.dcm')
dir()	        Lists available metadata keywords (e.g., PatientName).	ds.dir("Patient")
decompress()	Unpacks compressed (e.g., JPEG) pixel data in-place.	ds.decompress()
```

Function 	Purpose	Key Parameters
```
imshow()	Displays 2D data as a color-coded image.	cmap (color map), interpolation
colorbar()	Adds a legend showing the scale of values.	shrink, orientation
pcolormesh()	Creates heatmaps for non-regular or large grids.	shading='auto'
matshow()	Specialized version of imshow for matrices.	cmap='viridis'
```
