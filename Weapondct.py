import numpy as np
import cv2
import imutils
import datetime

# Load the gun detection cascade
gun_cascade = cv2.CascadeClassifier('cascade.xml')

# Initialize the camera
camera = cv2.VideoCapture(0)

Frame_1 = None  # Initialize the first frame as None
Gun_exist = False  # Variable to track gun detection

while True:  # Infinite loop until the user exits
    # Read frame from the camera
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture frame from camera. Exiting...")
        break

    # Resize the frame
    frame = imutils.resize(frame, width=500)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns in the frame
    Gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    # Update Gun_exist flag
    Gun_exist = len(Gun) > 0

    # Draw rectangles around detected guns
    for (X, Y, w, h) in Gun:
        frame = cv2.rectangle(frame, (X, Y), (X + w, Y + h), (255, 0, 0), 2)

    # Display the frame
    cv2.imshow("Security Feed", frame)

    # Print gun detection status
    if Gun_exist:
        print("Weapon detected")
    else:
        print("No weapon detected")

    # Check for user input to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        break

# Release the camera and close windows
camera.release()
cv2.destroyAllWindows()
