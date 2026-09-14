import cv2


def edit_image(image):
    # Resize
    resized = cv2.resize(
        image,
        None,
        fx=0.2,
        fy=0.2,
        interpolation=cv2.INTER_AREA
    )

    # Brightness and Contrast
    edited = cv2.convertScaleAbs(
        resized,
        alpha=1.2,
        beta=30
    )

    # Rotate
    height, width = edited.shape[:2]
    center = (width // 2, height // 2)

    matrix = cv2.getRotationMatrix2D(
        center,
        90,
        1
    )

    rotated = cv2.warpAffine(
        edited,
        matrix,
        (width, height)
    )

    # Crop
    cropped = rotated[50:350, 100:500]

    return cropped


image = cv2.imread("09_Image_Editor/images/gojo.jpg")

if image is None:
    print("Could not load image")
    exit()

result = edit_image(image)

cv2.imshow("Image Editor", result)

cv2.imwrite(
    "09_Image_Editor/images/edited_gojo.jpg",
    result
)

cv2.waitKey(0)
cv2.destroyAllWindows()