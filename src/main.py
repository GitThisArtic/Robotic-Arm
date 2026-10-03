import cv2

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Optimal resolution for processing and performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# Checks if the camera opened
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

isRunning = True
while isRunning:
    ret, frame = cap.read()

    # If the frame wasn't grabbed properly, end loop
    if not ret:
        print("Error: Failed to grab frame.")
        isRunning = False

    # Display the resulting frame in a window named 'Camera Feed'
    cv2.imshow('Camera Feed', frame)

    # Wait for 1 millisecond and check if the 'q' key is pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        isRunning = False

cap.release()
cv2.destroyAllWindows()