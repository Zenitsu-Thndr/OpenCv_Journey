import cv2


image = cv2.imread("04_Color_Channels/shape_images/triangle.jpg")

image = cv2.resize(image, (300,300))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)



contours, _ = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print("Number of contours:", len(contours))


output = image.copy()

cv2.drawContours(output, contours, -1, (0, 255, 0), 2)



cv2.imshow("Gray", gray)

cv2.imshow("Original", image)

cv2.imshow("Binary", binary)

cv2.imshow("Contours", output)



cv2.waitKey(0)
cv2.destroyAllWindows()