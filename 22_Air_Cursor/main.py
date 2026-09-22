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


screen_width, screen_height = pyautogui.size()

clicking = False

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

            thumb = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]


            distance = math.sqrt(
                (thumb.x - index_tip.x) ** 2 +
                (thumb.y - index_tip.y) ** 2
            )


            if distance < 0.05:

                if not clicking:
                    pyautogui.click()
                    clicking = True

            else:
                clicking = False


            height, width = frame.shape[:2]

            x = int(index_tip.x * width)
            y = int(index_tip.y * height)

            control_x1 = 100
            control_y1 = 80
            control_x2 = 540
            control_y2 = 400

            cv2.rectangle(
                frame,
                (control_x1, control_y1),
                (control_x2, control_y2),
                (255, 0, 0),
                2
            )


            mouse_x = int(
                (x - control_x1)
                / (control_x2 - control_x1)
                * screen_width
            )

            mouse_y = int(
                (y - control_y1)
                / (control_y2 - control_y1)
                * screen_height
            )

            mouse_x = max(0, min(screen_width - 1, mouse_x))
            mouse_y = max(0, min(screen_height - 1, mouse_y))

            pyautogui.moveTo(mouse_x, mouse_y)

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