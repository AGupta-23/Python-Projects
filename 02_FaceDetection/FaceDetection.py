import cv2
import os

# Get the path of the XML file
xml_path = os.path.join(
    os.path.dirname(__file__),
    "haarcascade_frontalface_default.xml"
)

# Load the Haar Cascade classifier
face_detector = cv2.CascadeClassifier(xml_path)

# Open the webcam
camera = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:

    # Read a frame from the webcam
    ret, frame = camera.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(gray, 1.3, 6)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

    # Display the frame
    cv2.imshow("Face Recognition", frame)

    # Wait for 1 ms
    key = cv2.waitKey(1) & 0xFF

    # Press 'q' to quit
    if key == ord('q'):
        break

    # Close if the window's X button is clicked
    if cv2.getWindowProperty("Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release resources
camera.release()
cv2.destroyAllWindows()