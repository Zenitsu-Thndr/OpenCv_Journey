import cv2
import mediapipe as mp
import math


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
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
        print("Failed to capture frame")
        break

    # OpenCV: BGR → MediaPipe: RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            height, width = frame.shape[:2]

            thumb = hand_landmarks.landmark[4]
            index = hand_landmarks.landmark[8]

            thumb_px = (
                int(thumb.x * width),
                int(thumb.y * height)
            )

            index_px = (
                int(index.x * width),
                int(index.y * height)
            )

            distance = math.sqrt(
                (index_px[0] - thumb_px[0]) ** 2 +
                (index_px[1] - thumb_px[1]) ** 2
            )

            
            for hand_landmarks, handedness_data in zip(
                results.multi_hand_landmarks,
                results.multi_handedness
            ):

                handedness = handedness_data.classification[0].label



            cv2.line(
                frame,
                thumb_px,
                index_px,
                (255, 0, 0),
                3
            )

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


            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Hand Landmarks", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
hands.close()