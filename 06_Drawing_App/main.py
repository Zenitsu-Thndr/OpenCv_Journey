import cv2
import numpy as np

canvas = np.zeros((600, 800, 3), dtype=np.uint8)


drawing = False
previous_point = None
color = (255, 255, 255)

def mouse_event(event, x, y, flags, param):
    global drawing, previous_point, color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        previous_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.line(canvas, previous_point, (x, y), color, 3)
        previous_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        previous_point = None


cv2.namedWindow("Drawing App")
cv2.setMouseCallback("Drawing App", mouse_event)

while True:
    cv2.imshow("Drawing App", canvas)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        color = (0, 0, 255)
    
    elif key == ord("g"):
        color = (0, 255, 0)
    
    elif key == ord("b"):
        color = (255, 0, 0)
    
    elif key == ord("w"):
        color = (255, 255, 255)
    
    elif key == ord("c"):
        canvas[:] = 0
    
    elif key == ord("q"):
        break


cv2.waitKey(0)
cv2.destroyAllWindows()