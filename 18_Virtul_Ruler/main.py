import cv2
import math

reference_points = []
measurement_points = []

REFERENCE_LENGTH_CM = 10


def reference_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(reference_points) < 2:
            reference_points.append((x, y))


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

cv2.namedWindow("Virtual Ruler")
cv2.setMouseCallback("Virtual Ruler", reference_callback)

print("Click two points on the reference object.")
print(f"Reference length = {REFERENCE_LENGTH_CM} cm")
print("Press R after calibration to measure another object.")


while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    for i, point in enumerate(reference_points):
        cv2.circle(frame, point, 6, (0, 0, 255), -1)

        cv2.putText(
            frame,
            f"R{i + 1}",
            (point[0] + 10, point[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

    if len(reference_points) == 2:

        p1 = reference_points[0]
        p2 = reference_points[1]

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        reference_pixels = math.sqrt(dx ** 2 + dy ** 2)

        pixels_per_cm = reference_pixels / REFERENCE_LENGTH_CM

        cv2.line(frame, p1, p2, (0, 255, 0), 2)

        cv2.putText(
            frame,
            f"Reference: {REFERENCE_LENGTH_CM} cm",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Pixels/cm: {pixels_per_cm:.2f}",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Virtual Ruler", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        reference_points.clear()

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()