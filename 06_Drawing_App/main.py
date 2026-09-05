import cv2
import numpy as np

canvas = np.zeros((600, 800, 3), dtype=np.uint8)



cv2.imshow("Drawing App", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()