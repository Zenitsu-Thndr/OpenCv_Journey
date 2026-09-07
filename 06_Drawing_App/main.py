import cv2
import numpy as np

canvas = np.zeros((600, 800, 3), dtype=np.uint8)


drawing = False
previous_point = None

def mouse_event(event, x, y, flags, param):
    global drawing, previous_point

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        previous_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.line(canvas, previous_point, (x, y), (255, 255, 255), 3)
        previous_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        previous_point = None


cv2.namedWindow("Drawing App")
cv2.setMouseCallback("Drawing App", mouse_event)

while True:
    cv2.imshow("Drawing App", canvas)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cv2.waitKey(0)
cv2.destroyAllWindows()