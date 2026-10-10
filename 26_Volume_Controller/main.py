
import cv2
import mediapipe as mp
import math

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

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]

        height, width = frame.shape[:2]

        thumb = hand.landmark[4]
        index = hand.landmark[8]

        thumb_px = (int(thumb.x * width), int(thumb.y * height))
        index_px = (int(index.x * width), int(index.y * height))

        distance = math.sqrt(
            (index_px[0] - thumb_px[0]) ** 2
            + (index_px[1] - thumb_px[1]) ** 2
        )

        cv2.line(frame, thumb_px, index_px, (0, 255, 0), 3)
        cv2.circle(frame, thumb_px, 8, (255, 0, 0), -1)
        cv2.circle(frame, index_px, 8, (255, 0, 0), -1)

        cv2.putText(
            frame,
            f"Distance: {distance:.1f} px",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Volume Control", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
