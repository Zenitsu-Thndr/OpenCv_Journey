import cv2
import math

points = []


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 2:
            points.append((x, y))


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

cv2.namedWindow("Distance Tool")
cv2.setMouseCallback("Distance Tool", mouse_callback)


while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Draw selected points
    for i, point in enumerate(points):
        cv2.circle(frame, point, 6, (0, 0, 255), -1)
        cv2.putText(
            frame,
            f"P{i + 1}",
            (point[0] + 10, point[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

    # If two points exist
    if len(points) == 2:
        p1 = points[0]
        p2 = points[1]

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Draw measurement line
        cv2.line(frame, p1, p2, (0, 255, 0), 2)

        # Put distance near the middle of the line
        mid_x = (p1[0] + p2[0]) // 2
        mid_y = (p1[1] + p2[1]) // 2

        cv2.putText(
            frame,
            f"{distance:.1f} px",
            (mid_x, mid_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Distance Tool", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        points.clear()

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()