import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

points = []

smooth_x = 0
smooth_y = 0
smoothing = 0.3

while True:

    ret, frame = cap.read()

    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        # Index fingertip
        index_tip = hand.landmark[8]

        height, width = frame.shape[:2]

        x = int(index_tip.x * width)
        y = int(index_tip.y * height)


        # Check finger state
        index_up = hand.landmark[8].y < hand.landmark[6].y
        middle_down = hand.landmark[12].y > hand.landmark[10].y

        drawing = index_up and middle_down

        smooth_x = smooth_x + (x - smooth_x) * smoothing
        smooth_y = smooth_y + (y - smooth_y) * smoothing
        
        smooth_point = (int(smooth_x), int(smooth_y))
        
        if drawing:
            points.append(smooth_point)

        

        # Draw fingertip
        cv2.circle(
            frame,
            (x, y),
            8,
            (0, 0, 255),
            -1
        )

        if drawing:
            cv2.putText(
                frame,
                "DRAWING",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    # Draw the path
    for i in range(1, len(points)):
        cv2.line(
            frame,
            points[i - 1],
            points[i],
            (0, 255, 0),
            3
        )

    cv2.imshow("Air Drawing", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        points.clear()

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()