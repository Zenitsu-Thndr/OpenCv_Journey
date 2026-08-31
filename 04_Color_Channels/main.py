import cv2
import numpy as np

#importing image
image = cv2.imread("03_Image_Translation/images/loki.jpg")


blue, green, red = cv2.split(image)


# cv2.imshow("Original", image)


# cv2.imshow("Blue", blue)
# cv2.imshow("Green", green)
# cv2.imshow("Red", red)


# blue[:] = cv2.add(green, 50)
blue[:] = green

# blue[:] = cv2.addWeighted(blue, 0.5, green, 0.5, 0)

modified = cv2.merge([blue, green, red])

cv2.imshow("Modified", modified)

cv2.waitKey(0)
cv2.destroyAllWindows()