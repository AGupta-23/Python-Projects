import cv2

print("Version:", cv2.__version__)
print("File:", cv2.__file__)
print("CascadeClassifier exists:", hasattr(cv2, "CascadeClassifier"))
print("VideoCapture exists:", hasattr(cv2, "VideoCapture"))
print("First 20 names:")
print(dir(cv2)[:20])