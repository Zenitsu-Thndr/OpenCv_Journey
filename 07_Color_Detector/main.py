import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()



colors = {
    "RED": [
        (np.array([0, 50, 50]), np.array([10, 255, 255])),
        (np.array([170, 50, 50]), np.array([179, 255, 255]))
    ],

    "GREEN": [
        (np.array([35, 50, 50]), np.array([85, 255, 255]))
    ],

    "BLUE": [
        (np.array([90, 50, 50]), np.array([130, 255, 255]))
    ],

    "BLACK": [
        (np.array([0, 0, 0]), np.array([179, 255, 50]))
    ]
}


def detect_color(frame, hsv, color_name, ranges, box_color):
    for lower, upper in ranges:
        mask = cv2.inRange(hsv, lower, upper)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:
            area = cv2.contourArea(contour)

            if area > 500:
                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    box_color,
                    2
                )

                cv2.putText(
                    frame,
                    color_name,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    box_color,
                    2
                )



while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    detect_color(
        frame,
        hsv,
        "RED",
        colors["RED"],
        (0, 0, 255)
    )

    detect_color(
        frame,
        hsv,
        "GREEN",
        colors["GREEN"],
        (0, 255, 0)
    )

    detect_color(
        frame,
        hsv,
        "BLUE",
        colors["BLUE"],
        (255, 0, 0)
    )

    detect_color(
        frame,
        hsv,
        "BLACK",
        colors["BLACK"],
        (0, 0, 0)
    )


    cv2.imshow("Color Detector", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()