import cv2
import math

reference_points = []
measurement_points = []

REFERENCE_LENGTH_CM = 10


def mouse_callback(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        # First select reference
        if len(reference_points) < 2:
            reference_points.append((x, y))

        # Then select measurement
        elif len(measurement_points) < 2:
            measurement_points.append((x, y))


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

cv2.namedWindow("Virtual Ruler")
cv2.setMouseCallback("Virtual Ruler", mouse_callback)


while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # -------------------------
    # Reference
    # -------------------------

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

    # -------------------------
    # Measurement
    # -------------------------

    for i, point in enumerate(measurement_points):

        cv2.circle(frame, point, 6, (255, 0, 0), -1)

        cv2.putText(
            frame,
            f"P{i + 1}",
            (point[0] + 10, point[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

    if len(measurement_points) == 2 and len(reference_points) == 2:

        p1 = measurement_points[0]
        p2 = measurement_points[1]

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        measurement_pixels = math.sqrt(dx ** 2 + dy ** 2)

        measured_length = measurement_pixels / pixels_per_cm

        cv2.line(frame, p1, p2, (255, 0, 0), 2)

        mid_x = (p1[0] + p2[0]) // 2
        mid_y = (p1[1] + p2[1]) // 2

        cv2.putText(
            frame,
            f"{measured_length:.2f} cm",
            (mid_x, mid_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

    cv2.imshow("Virtual Ruler", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        reference_points.clear()
        measurement_points.clear()

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()