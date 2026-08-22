import cv2
import numpy as np


image = cv2.imread("03_Image_Translation/images/loki.jpg")


matrix = np.float32([
    [1, 0, -200],
    [0, 1, -100]
])

translated = cv2.warpAffine(
    image,
    matrix,
    (image.shape[1], image.shape[0])
)

cv2.imshow("Normal Image", image)
cv2.imshow("Translated", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()