import cv2

# filename = "images/tiny.png"
filename = "images/yuji_gojo.jpg"

output_path = "outputs/"

image = cv2.imread(filename)

image = image[600:1200, 2700:3200]



nearest = cv2.resize(
    image, (600, 600), interpolation = cv2.INTER_NEAREST
)
linear = cv2.resize(
    image, (600, 600), interpolation = cv2.INTER_LINEAR
)
cubic = cv2.resize(
    image, (600, 600), interpolation = cv2.INTER_CUBIC
)
Lanczos = cv2.resize(
    image, (600, 600), interpolation = cv2.INTER_LANCZOS4
)


cv2.imwrite(output_path+"default_image.jpg", image)
cv2.imwrite(output_path+"nearest_interpolation.jpg", nearest)
cv2.imwrite(output_path+"linear_interpolation.jpg", linear)
cv2.imwrite(output_path+"cubic_interpolation.jpg", cubic)
cv2.imwrite(output_path+"lanczos_interpolation.jpg", Lanczos)



cv2.imshow("Default", image)

cv2.imshow("nearest", nearest)
cv2.imshow("linear", linear)
cv2.imshow("cubic", cubic)
cv2.imshow("Lanczos", Lanczos)




cv2.waitKey(0)
cv2.destroyAllWindows()