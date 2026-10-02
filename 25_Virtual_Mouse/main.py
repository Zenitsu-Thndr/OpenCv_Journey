import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

screen_width, screen_height = pyautogui.size()

smooth_x = 0
smooth_y = 0
smoothing = 0.3

clicking = False
right_clicking = False

screen_width, screen_height = pyautogui.size()
control_x1 = 150
control_y1 = 60
control_x2 = 500
control_y2 = 350

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    height, width = frame.shape[:2]

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]
        

        thumb_tip = hand.landmark[4]
        index_tip = hand.landmark[8]

        middle_tip = hand.landmark[12]

        distance = (
            (thumb_tip.x - index_tip.x) ** 2 +
            (thumb_tip.y - index_tip.y) ** 2
        ) ** 0.5


        right_distance = (
            (thumb_tip.x - middle_tip.x) ** 2 +
            (thumb_tip.y - middle_tip.y) ** 2
        ) ** 0.5

        if distance < 0.06:

            if not clicking:
                pyautogui.click()
                clicking = True

                cv2.putText(
                    frame,
                    "CLICK",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

            else:
                clicking = False


        if right_distance < 0.05:

            if not right_clicking:
                pyautogui.rightClick()
                right_clicking = True

        else:
            right_clicking = False


        # MediaPipe normalized coordinates → camera pixels
        x = int(index_tip.x * width)
        y = int(index_tip.y * height)

        # Camera coordinates → screen coordinates
        screen_x = int(
            (x - control_x1)
            / (control_x2 - control_x1)
            * screen_width
        )

        screen_y = int(
            (y - control_y1)
            / (control_y2 - control_y1)
            * screen_height
        )

        screen_x = max(0, min(screen_width - 1, screen_x))
        screen_y = max(0, min(screen_height - 1, screen_y))

        cv2.rectangle(
            frame,
            (control_x1, control_y1),
            (control_x2, control_y2),
            (255, 0, 0),
            2
        )

        # Smooth movement
        smooth_x = smooth_x + (screen_x - smooth_x) * smoothing
        smooth_y = smooth_y + (screen_y - smooth_y) * smoothing

        pyautogui.moveTo(
            int(smooth_x),
            int(smooth_y)
        )

        cv2.circle(
            frame,
            (x, y),
            8,
            (0, 0, 255),
            -1
        )
    
    if not results.multi_hand_landmarks:
        clicking = False
        right_clicking = False
    cv2.imshow("Virtual Mouse", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()