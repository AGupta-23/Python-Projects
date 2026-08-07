# Face Detection using OpenCV (Haar Cascade)

## 🎯 Project Goal

Build a real-time face detection system using Python and OpenCV that:

- Opens the webcam
- Reads live video frames
- Detects faces
- Draws a rectangle around every detected face
- Closes properly when 'Q' is pressed or the window is closed

---

# 📚 Things I Learned

## Python

- Importing libraries
- Infinite loops using `while True`
- Using `for` loop to iterate through tuples
- Variables and object creation
- Using functions and methods
- Conditional statements (`if`)
- Reading frames continuously from webcam
- Using `break`
- File handling using the `os` module
- Creating absolute file paths using `os.path.join()`

---

## OpenCV

- Opening webcam
- Capturing frames
- Converting color image to grayscale
- Loading pre-trained XML models
- Detecting faces
- Drawing rectangles
- Showing images continuously
- Reading keyboard input
- Closing OpenCV windows safely

---

# 🧠 New Concepts Learned

## XML File

- XML = Extensible Markup Language
- Used for storing structured data.
- In this project it stores the trained Haar Cascade model.
- OpenCV loads this model to detect faces.

---

## Haar Cascade

A classical machine learning face detection algorithm.

Instead of understanding a face like humans, it looks for patterns like:

- Dark eyes
- Bright nose bridge
- Face edges
- Hairline

using thousands of learned features stored inside the XML file.

---

## Face Detection Workflow

```
Load XML Model
      ↓
Open Webcam
      ↓
Read Frame
      ↓
Convert to Grayscale
      ↓
Detect Faces
      ↓
Draw Rectangle
      ↓
Display Frame
      ↓
Repeat
```

---

# 📂 Project Structure

```
02_FaceRecognition/
│
├── FaceRecognition.py
├── haarcascade_frontalface_default.xml
└── README.md
```

---

# ⚙️ Functions & Code Reference

| Code / Function | Purpose |
|-----------------|---------|
| `import cv2` | Imports OpenCV library. |
| `import os` | Imports OS module for file paths. |
| `os.path.dirname(__file__)` | Gets folder where the script is located. |
| `os.path.join()` | Joins folder path and filename. |
| `cv2.CascadeClassifier()` | Loads Haar Cascade XML model. |
| `cv2.VideoCapture(0)` | Opens default webcam. |
| `camera.isOpened()` | Checks if webcam opened successfully. |
| `camera.read()` | Captures one frame from webcam. |
| `cv2.cvtColor()` | Converts BGR image to grayscale. |
| `detectMultiScale()` | Detects faces in the image. |
| `cv2.rectangle()` | Draws rectangle around detected face. |
| `cv2.imshow()` | Displays image/window. |
| `cv2.waitKey()` | Waits for keyboard input. |
| `cv2.getWindowProperty()` | Checks whether window is still open. |
| `camera.release()` | Releases webcam resource. |
| `cv2.destroyAllWindows()` | Closes every OpenCV window. |

---

# 🔍 Understanding Important Lines

## 1.

```python
faces = face_detector.detectMultiScale(gray, 1.3, 6)
```

### Meaning

Detects all faces present in the grayscale image.

### Parameters

`gray`

- Image in grayscale.

`1.3`

- Scale Factor.
- Image is reduced to about 77% each time.
- Smaller → More accurate but slower.
- Larger → Faster but may miss faces.

`6`

- Minimum Neighbors.
- At least 6 nearby detections must agree before considering it a real face.
- Larger value → Fewer false detections.

Returns:

```python
[(x,y,w,h), ...]
```

---

## 2.

```python
for (x, y, w, h) in faces:
```

Loops through every detected face.

Meaning of each variable:

- `x` → Left coordinate
- `y` → Top coordinate
- `w` → Width
- `h` → Height

---

## 3.

```python
cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)
```

Draws rectangle around the face.

| Parameter | Meaning |
|-----------|---------|
| `frame` | Image on which rectangle is drawn |
| `(x,y)` | Top-left corner |
| `(x+w,y+h)` | Bottom-right corner |
| `(255,0,0)` | Blue color (BGR format) |
| `3` | Rectangle thickness |

---

## 4.

```python
key = cv2.waitKey(1) & 0xFF
```

### `waitKey(1)`

- Waits 1 millisecond.
- Updates OpenCV window.
- Detects keyboard input.

### `& 0xFF`

- Keeps only the lowest 8 bits of the returned key value.
- Makes keyboard detection work consistently across operating systems.

---

# 📝 Program Flow

```
Start Program
      ↓
Load XML Model
      ↓
Open Webcam
      ↓
Read Frame
      ↓
Convert to Grayscale
      ↓
Detect Faces
      ↓
Draw Rectangle
      ↓
Display Frame
      ↓
User presses Q or closes window?
      ↓
Yes
      ↓
Release Webcam
      ↓
Destroy Windows
      ↓
End Program
```

---

# 💡 Errors I Faced & Solutions

### 1. `AttributeError: module 'cv2' has no attribute 'CascadeClassifier'`

**Cause**

Broken OpenCV installation.

**Solution**

Uninstalled the broken package and installed a stable OpenCV version.

---

### 2. XML file not found

**Cause**

Python searched in the current working directory instead of the script's folder.

**Solution**

Used:

```python
xml_path = os.path.join(os.path.dirname(__file__),
                        "haarcascade_frontalface_default.xml")
```

---

### 3. Webcam window didn't close

**Cause**

Closing the window didn't stop the infinite loop.

**Solution**

Used:

```python
cv2.getWindowProperty()
```

to detect window closure.

---

# 🚀 Next Improvements

- Face Recognition
- Eye Detection
- Smile Detection
- Face Blur
- Face Attendance System
- Deep Learning Face Detection (YOLO / FaceNet / MediaPipe)
