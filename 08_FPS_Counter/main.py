import time
import numpy
import cv2

prev_time = time.time()
frame_count = 0
fps = 0



cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    frame_count += 1

    current_time = time.time()
    elapsed_time = current_time - prev_time
    
    if elapsed_time >= 1:
        fps = frame_count / elapsed_time
        frame_count = 0
        prev_time = current_time

    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("FPS Counter", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
