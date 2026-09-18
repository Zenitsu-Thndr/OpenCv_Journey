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

    smooth = cv2.bilateralFilter(frame, 9, 75, 75)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    edges = cv2.threshold(
        edges,
        100,
        255,
        cv2.THRESH_BINARY
    )[1]

    # edges = cv2.bitwise_not(edges)

    cartoon = cv2.bitwise_and(smooth, smooth, mask=edges)

    # cv2.imshow("Smooth", smooth)
    # cv2.imshow("Edges", edges)
    cv2.imshow("Cartoon Camera", cartoon)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()