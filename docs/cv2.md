cv2 is the Python binding library for OpenCV (Open Source Computer Vision Library), designed to solve computer vision problems. It provides a fast, optimized interface to over 2,500 algorithms, enabling real-time image processing, video analysis, feature detection, and machine learning applications. 
It is commonly used to process visual data—treating images as NumPy arrays—and is essential for tasks like object tracking, face recognition, and image manipulation. 

##Key Categories of cv2 Functions

While cv2 has too many functions to list individually (over 2,500), they are organized into major modules. Here are the most important functions categorized by purpose: 

1. Image I/O (Input/Output) & Display

cv2.imread(): Loads an image from a specified file.
cv2.imshow(): Displays an image in a window.
cv2.imwrite(): Saves an image to a specified file.
cv2.waitKey(): Waits for a key event (essential for imshow).
cv2.destroyAllWindows(): Closes all opened OpenCV windows. 

2. Image Processing (imgproc)

cv2.cvtColor(): Converts an image from one color space to another (e.g., BGR to Gray, HSV).
cv2.resize(): Resizes an image.
cv2.flip(): Flips an image.
cv2.threshold(): Applies thresholding to create binary images.
cv2.GaussianBlur() / cv2.medianBlur() / cv2.blur(): Smoothes/blurs images (noise reduction).
cv2.Canny(): Detects edges in an image.
cv2.erode() / cv2.dilate(): Erosion and dilation of images.
cv2.copyMakeBorder(): Adds borders (padding) to images.
cv2.warpAffine() / cv2.warpPerspective(): Applies affine/perspective transformations.
cv2.getRotationMatrix2D(): Calculates the transformation matrix for rotation. 

3. Video Analysis (video / videoio)
cv2.VideoCapture(): Captures video from a camera or a video file.
cv2.VideoWriter(): Saves video files.
cv2.calcOpticalFlowPyrLK(): Calculates optical flow (motion tracking).
cv2.createBackgroundSubtractorMOG2(): Detects motion by subtracting the background. 

4. Drawing Functions
cv2.line(): Draws a line.
cv2.circle(): Draws a circle.
cv2.rectangle(): Draws a rectangle.
cv2.ellipse(): Draws an ellipse.
cv2.putText(): Writes text on an image. 

5. Object Detection & Features (objdetect / features2d) 
cv2.CascadeClassifier(): Loads pre-trained classifiers (like Haar Cascades for face detection).
cv2.findContours(): Finds contours (object boundaries) in a binary image.
cv2.drawContours(): Draws contours.
cv2.SIFT_create() / cv2.ORB_create(): Feature detector constructors. 

6. User Interface (HighGUI) 
cv2.setMouseCallback(): Registers a callback function for mouse events.
cv2.createTrackbar(): Creates a slider control. 

##How to Find All Functions
Since cv2 is a massive library, you can list all available functions in your current environment using Python's dir() function: 
python
```
import cv2
print(dir(cv2))
```

##Main Modules
The library is structured into modules, which can be explored via documentation: 

core: Basic data structures and functions.
imgproc: Image processing.
videoio: Video input/output.
highgui: High-level GUI.
objdetect: Object detection.
dnn: Deep Neural Network module. 

##Basic File Operations (I/O)

These functions handle loading, viewing, and saving image data. 

import cv2

# Load an image (IMREAD_COLOR is the default)
img = cv2.imread('input.jpg')

# Display the image in a window titled 'My Image'
cv2.imshow('My Image', img)

# Keep the window open until a key is pressed
cv2.waitKey(0) 

# Save the image as a PNG
cv2.imwrite('output.png', img)

# Cleanup
cv2.destroyAllWindows()
Use code with caution.

2. Video Stream Handling
Use these for webcam access or processing video files. 
python
# Open the default webcam (0)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # Read a single frame
    if not ret: break       # Exit if no frame is captured
    
    cv2.imshow('Webcam Feed', frame)
    
    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # Close the webcam
cv2.destroyAllWindows()
Use code with caution.

3. Image Transformation & Processing
Essential for prepping images for machine learning or analysis. 
python
# Convert to Grayscale (reduces data complexity)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize to exactly 500x500 pixels
resized = cv2.resize(img, (500, 500))

# Gaussian Blur to remove noise (using a 5x5 kernel)
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)
Use code with caution.

4. Drawing & Annotating
Useful for highlighting detected objects or adding data labels. 
python
# Draw a red rectangle (BGR format: 0,0,255)
# Parameters: (image, top-left, bottom-right, color, thickness)
cv2.rectangle(img, (50, 50), (200, 200), (0, 0, 255), 3)

# Add white text to the image
cv2.putText(img, 'Object Detected', (55, 45), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
Use code with caution.

5. Advanced Analysis (Contours)
Used to find boundaries of shapes in an image. 
python
# 1. Threshold to binary (Black & White)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 2. Find external contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 3. Draw all detected contours in green
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
