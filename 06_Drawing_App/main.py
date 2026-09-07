import cv2
import numpy as np

canvas = np.zeros((600, 800, 3), dtype=np.uint8)


drawing = False
previous_point = None
color = (255, 255, 255)
brush_size = 3
eraser = False

def mouse_event(event, x, y, flags, param):
    global drawing, previous_point, color, brush_size, eraser

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        previous_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        draw_color = (0, 0, 0) if eraser else color
        cv2.line(canvas, previous_point, (x, y), draw_color, brush_size)
        previous_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        previous_point = None


cv2.namedWindow("Drawing App")
cv2.setMouseCallback("Drawing App", mouse_event)

while True:
    display = canvas.copy()

    cv2.putText(
        display,
        f"Brush Size: {brush_size}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        display,
        f"Mode: {'Eraser' if eraser else 'Brush'}",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow("Drawing App", display)

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

    elif key == ord("e"):
        eraser = not eraser

    elif key == ord("+"):
        brush_size += 2

    elif key == ord("-"):
        brush_size = max(1, brush_size - 2)

    elif key == ord("q"):
        break


cv2.waitKey(0)
cv2.destroyAllWindows()