import cv2
import os

folder = "images/"
filename = "loki.jpg"

image = cv2.imread(folder + filename)


# image[50:500, 400:900] = [255, 255, 255]

# crop = image[0:550, 350:950]

height, width, channels = image.shape
total_values = image.size
total_pixels = height * width
image_type = os.path.splitext(filename)[1]


info = f"Image Width: {width}\nImage Height: {height}\nNumber of Channels: {channels}\nSize of image: {total_values}\nTotal Pixels: {total_pixels}\nImage type: {image_type}"


cv2.putText(
    image,
    info,
    (60, 60),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    (255, 255, 255),
    1
)

# cv2.imwrite("output.png", image)


cv2.imshow("My Image", image)


cv2.waitKey(0)


cv2.destroyAllWindows()