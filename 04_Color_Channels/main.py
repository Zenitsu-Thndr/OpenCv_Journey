import cv2
import numpy as np

#importing image
image = cv2.imread("03_Image_Translation/images/loki.jpg")


blue, green, red = cv2.split(image)


# cv2.imshow("Original", image)


cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)

cv2.waitKey(0)
cv2.destroyAllWindows()