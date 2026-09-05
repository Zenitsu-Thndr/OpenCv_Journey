import cv2
import numpy as np

#importing image
image = cv2.imread("05_Webcam_Viewer/images/loki.jpg")




cv2.imshow("Original", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

