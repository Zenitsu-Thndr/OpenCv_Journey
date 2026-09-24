import cv2
import mediapipe as mp
import math
import pyautogui


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

            index_open = (
                hand_landmarks.landmark[8].y <
                hand_landmarks.landmark[6].y
            )

            middle_open = (
                hand_landmarks.landmark[12].y <
                hand_landmarks.landmark[10].y
            )

            ring_open = (
                hand_landmarks.landmark[16].y <
                hand_landmarks.landmark[14].y
            )

            pinky_open = (
                hand_landmarks.landmark[20].y <
                hand_landmarks.landmark[18].y
            )

            open_fingers = sum([
                index_open,
                middle_open,
                ring_open,
                pinky_open
            ])

            if open_fingers == 4:
                gesture = "OPEN HAND"

            elif open_fingers == 0:
                gesture = "FIST"

            else:
                gesture = "OTHER"


            cv2.putText(
                frame,
                gesture,
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )


            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Air Cursor", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
hands.close()