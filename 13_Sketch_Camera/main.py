import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    inverted = cv2.bitwise_not(gray)

    blurred = cv2.GaussianBlur(inverted, (31, 31), 0)

    sketch = cv2.divide(gray, blurred, scale=256)

    cv2.imshow("Sketch", sketch)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()