In data processing and computer vision, Normalization is the process of scaling numeric data into a specific, standard range (usually 0 to 1 or -1 to 1). Think of it like "leveling the playing field." If you have one set of data ranging from 0 to 10 and another ranging from 0 to 10,000, a computer might mistakenly think the larger numbers are "more important." Normalization fixes this. 1. Why do we need it in Computer Vision? Uniformity: Different cameras or medical scanners (DICOM) might save images with different intensity ranges (e.g., 8-bit images go up to 255, while 16-bit DICOMs can go up to 65,535). Normalizing them to a 0–1 range makes them comparable.Faster Learning: For Machine Learning models (like Neural Networks), math works much faster and more accurately when input values are small and centered.Better Contrast: It helps in "stretching" the pixel values so that a dark, low-contrast image becomes easier to see. 2. The Math Behind It The most common form is Min-Max Normalization. It uses a simple formula to squash any value (\(x\)) into a range between 0 and 1: \(x_{norm}=\frac{x-\text{min}(x)}{\text{max}(x)-\text{min}(x)}\)If \(x\) is the minimum value, the result is 0.If \(x\) is the maximum value, the result is 1.Everything else becomes a decimal between 0 and 1. 3. Normalization in Code A. Using OpenCV (cv2.normalize) OpenCV provides a dedicated function to scale images. pythonimport cv2
```
import numpy as np

img = cv2.imread('low_contrast.jpg', 0)

# Normalize to range 0-255 (standard 8-bit image)
normalized_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('Original', img)
cv2.imshow('Normalized', normalized_img)
cv2.waitKey(0)
```
Use code with caution.
B. Using NumPy (Manual) This is the method I used in the previous DICOM example. It is highly flexible. python
```
import numpy as np

# A sample array of random intensities
data = np.array([100, 200, 300, 400, 500], dtype=float)

# Manual Min-Max Normalization to 0-1 range
data_min = np.min(data)
data_max = np.max(data)

normalized_data = (data - data_min) / (data_max - data_min)

print(normalized_data)
# Output: [0.  0.25  0.5  0.75  1. ]
```
Use code with caution.
##4. Normalization vs. Standardization 
Often confused, they are slightly different: Normalization: Squashes data into a fixed range (e.g., [0, 1]). Best when you know the boundaries of your data.Standardization: Rescales data so it has a mean of 0 and a standard deviation of 1. This is used when data follows a "Bell Curve" (Gaussian distribution). 
Summary Table Feature:
 Raw DataNormalized DataRangeVaries (e.g., 0 to 65535)Fixed (usually 0 to 1)Data TypeUsually Integer (uint16)Usually Float (float32)PurposeStorage/CaptureProcessing/ML/Visualization
