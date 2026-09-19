import cv2
import math

points = []


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 3:
            points.append((x, y))


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

cv2.namedWindow("Angle Tool")
cv2.setMouseCallback("Angle Tool", mouse_callback)


while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Draw points
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

    # When 3 points are selected
    if len(points) == 3:

        p1 = points[0]
        p2 = points[1]   # vertex
        p3 = points[2]

        # Vectors from vertex P2
        v1 = (
            p1[0] - p2[0],
            p1[1] - p2[1]
        )

        v2 = (
            p3[0] - p2[0],
            p3[1] - p2[1]
        )

        # Dot product
        dot = v1[0] * v2[0] + v1[1] * v2[1]

        # Vector magnitudes
        magnitude1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
        magnitude2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)

        if magnitude1 != 0 and magnitude2 != 0:

            # Calculate cosine of angle
            cosine = dot / (magnitude1 * magnitude2)

            # Protect against tiny floating-point errors
            cosine = max(-1, min(1, cosine))

            # Convert radians to degrees
            angle = math.degrees(math.acos(cosine))

            # Draw the two arms
            cv2.line(frame, p1, p2, (0, 255, 0), 2)
            cv2.line(frame, p2, p3, (0, 255, 0), 2)

            # Display angle near vertex
            cv2.putText(
                frame,
                f"{angle:.1f} deg",
                (p2[0] + 15, p2[1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

    cv2.imshow("Angle Tool", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        points.clear()

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()