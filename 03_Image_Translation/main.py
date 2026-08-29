import cv2
import numpy as np

#importing image
image = cv2.imread("03_Image_Translation/images/loki.jpg")

#TRANSLATION
'''
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
'''


#ROTATION

# height, width = image.shape[:2]

# center = (width // 2, height // 2)
# # center = (0, 0)

# matrix = cv2.getRotationMatrix2D(
#     center,
#     -90,
#     1
# )

# cos = abs(matrix[0, 0])
# sin = abs(matrix[0, 1])

# new_width = int((height * sin) + (width * cos))
# new_height = int((height * cos) + (width * sin))

# matrix[0, 2] += (new_width / 2) - center[0]
# matrix[1, 2] += (new_height / 2) - center[1]

# rotated = cv2.warpAffine(
#     image,
#     matrix,
#     (new_width, new_height)
# )

# cv2.imshow("Original", image)
# cv2.imshow("Rotated", rotated)


# Flipping 

flipped = cv2.flip(image, 0)

cv2.imshow("Original", image)
cv2.imshow("Flipped", flipped)


cv2.waitKey(0)
cv2.destroyAllWindows()

