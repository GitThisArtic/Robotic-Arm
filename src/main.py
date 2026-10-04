import cv2
#import threading
#import time
from ultralytics import YOLO

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

model = YOLO("yolov8n.pt")

# Optimal resolution for processing and performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)


# Checks if the camera opened
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

try:
    is_running = True
    while is_running:
        captured, frame = cap.read()

        # If the frame wasn't grabbed properly, end loop
        if not captured:
            print("Error: Failed to grab frame.")
            is_running = False

        results = model(frame)
        
        annotated_frame = results[0].plot()

        # Display the resulting frame in a window named 'Camera Feed'
        cv2.imshow('Image Detection Feed', annotated_frame)

        # Wait for 1 millisecond and check if the 'q' key is pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            is_running = False

finally: 
    print("Ending program...")
    cap.release()
    cv2.destroyAllWindows()