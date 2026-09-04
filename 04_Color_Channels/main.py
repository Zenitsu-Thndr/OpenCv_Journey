import cv2
import numpy as np

#importing image
image = cv2.imread("03_Image_Translation/images/loki.jpg")


blue, green, red = cv2.split(image)


# cv2.imshow("Original", image)

##BGR

# cv2.imshow("Blue", blue)
# cv2.imshow("Green", green)
# cv2.imshow("Red", red)


# blue[:] = cv2.add(green, 50)
# blue[:] = green

# blue[:] = cv2.addWeighted(blue, 0.5, green, 0.5, 0)

# modified = cv2.merge([blue, green, red])

##HSV

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

'''
h, s, v = cv2.split(hsv)

cv2.imshow("Hue", h)
cv2.imshow("Saturation", s)
cv2.imshow("Value", v)
'''

##HSV MASK


lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)

# kernal = np.ones((5,5), np.uint8)


# mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel= kernal)
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel= kernal)

# result = cv2.bitwise_and(image, image, mask=mask)

# cv2.imshow("Original", image)
# cv2.imshow("Mask", result)


##CONTOURS
contours, hierarchy = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# print("Number of contours:", len(contours))

''' DRAWING CONTOURS and BOUNDING BOX

output = image.copy()

# cv2.drawContours(
#     output,
#     contours,
#     -1,
#     (0, 255, 0),
#     2
# )


for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    cv2.rectangle(
        output,
        (x, y),
        (x + w, y + h),
        (0, 0, 255),
        2
    )


cv2.imshow("Contours", output)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()
