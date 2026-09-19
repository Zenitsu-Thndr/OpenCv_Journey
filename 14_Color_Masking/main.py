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

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = (35, 80, 50)
    upper_green = (85, 255, 255)

    mask = cv2.inRange(
        hsv,
        lower_green,
        upper_green
    )

    result = cv2.bitwise_and(
        frame,
        frame,
        mask=mask
    )

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    background = cv2.bitwise_and(
        gray,
        gray,
        mask=cv2.bitwise_not(mask)
    )

    color_splash = cv2.add(
        background,
        result
    )

    cv2.imshow("Color Splash", color_splash)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()