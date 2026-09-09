import time
import numpy
import cv2

perv_time = 0

current_time = time.time()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    cv2.imshow("FPS Counter", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
