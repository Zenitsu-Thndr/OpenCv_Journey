import cv2
import numpy as np

#importing image
image = cv2.imread("03_Image_Translation/images/loki.jpg")




cv2.imshow("Original", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

