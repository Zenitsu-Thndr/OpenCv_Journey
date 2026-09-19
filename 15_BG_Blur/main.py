import cv2
import numpy

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break


    height, width = frame.shape[:2]

    blurred = cv2.GaussianBlur(
        frame,
        (31, 31),
        0
    )


    mask = numpy.zeros((height, width), dtype=numpy.uint8)

    cv2.rectangle(
        mask,
        (width // 4, height // 8),
        (3 * width // 4, 7 * height // 8),
        255,
        -1
    )

    foreground = cv2.bitwise_and(
        frame,
        frame,
        mask=mask
    )

    background_mask = cv2.bitwise_not(mask)

    background = cv2.bitwise_and(
        blurred,
        blurred,
        mask=background_mask
    )

    result = cv2.add(
        foreground,
        background
    )

    # cv2.imshow("Blurred Background", blurred)
    # cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()