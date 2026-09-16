import cv2
import numpy as np
import random
import time

def apply_color_matrix(image, matrix, bias=(0, 0, 0)):
    """
    Apply a 3x3 color transformation matrix to an image.

    image: BGR uint8 OpenCV image
    matrix: 3x3 NumPy matrix
    bias: RGB/BGR offset added after transformation
    """

    img = image.astype(np.float32)

    matrix = np.asarray(matrix, dtype=np.float32)
    bias = np.asarray(bias, dtype=np.float32)

    # Apply matrix to every pixel
    result = img @ matrix.T

    # Add color offset
    result += bias

    # Keep values valid
    result = np.clip(result, 0, 255)

    return result.astype(np.uint8)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

effs = ['cyberpunk', 'neon_purple', 'matrix_green', 'cold_blue', 'sunset', 'infrared', 'toxic_yellow', 'night', 'bleach', 'vintage', 'duotone', 'alien']

matrices = {

    # 1. Cyberpunk — cyan/blue shadows + magenta/red highlights
    "cyberpunk": np.array([
        [0.15, 0.05, 0.80],
        [0.10, 0.30, 0.60],
        [0.05, 0.05, 1.20]
    ]),

    # 2. Neon Purple
    "neon_purple": np.array([
        [0.35, 0.05, 0.80],
        [0.10, 0.20, 0.70],
        [0.05, 0.05, 1.35]
    ]),

    # 3. Matrix / Green Terminal
    "matrix_green": np.array([
        [0.05, 0.80, 0.05],
        [0.02, 1.20, 0.02],
        [0.00, 0.60, 0.10]
    ]),

    # 4. Cold Blue / Sci-Fi
    "cold_blue": np.array([
        [0.80, 0.10, 0.10],
        [0.10, 0.90, 0.20],
        [0.05, 0.10, 1.50]
    ]),

    # 5. Warm / Sunset
    "sunset": np.array([
        [0.90, 0.15, 0.05],
        [0.10, 0.80, 0.10],
        [0.05, 0.20, 1.30]
    ]),

    # 6. Infrared-ish
    "infrared": np.array([
        [0.05, 0.05, 1.20],
        [0.05, 0.10, 0.80],
        [0.00, 0.05, 0.30]
    ]),

    # 7. Toxic Yellow
    "toxic_yellow": np.array([
        [0.10, 0.80, 0.20],
        [0.10, 1.00, 0.20],
        [0.05, 0.80, 0.50]
    ]),

    # 8. Purple/Blue Night
    "night": np.array([
        [0.50, 0.05, 0.40],
        [0.05, 0.30, 0.60],
        [0.10, 0.05, 1.10]
    ]),

    # 9. Bleach / High Contrast
    "bleach": np.array([
        [1.30, -0.15, -0.05],
        [-0.10, 1.20, -0.05],
        [-0.05, -0.10, 1.35]
    ]),

    # 10. Vintage / Film
    "vintage": np.array([
        [0.75, 0.15, 0.05],
        [0.10, 0.80, 0.10],
        [0.05, 0.20, 0.90]
    ]),

    # 11. Duotone Cyan/Red
    "duotone": np.array([
        [0.10, 0.20, 0.90],
        [0.10, 0.30, 0.70],
        [0.80, 0.10, 0.10]
    ]),

    # 12. Alien
    "alien": np.array([
        [0.20, 0.80, 0.10],
        [0.10, 0.50, 0.70],
        [0.30, 0.10, 1.10]
    ])
}

x = 0
y = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    '''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 80, 150)

    # Make cyan edges
    neon = np.zeros_like(frame)
    neon[:, :, 0] = edges       # Blue
    neon[:, :, 1] = edges       # Green

    # Glow
    glow1 = cv2.GaussianBlur(neon, (0, 0), 3)
    glow2 = cv2.GaussianBlur(neon, (0, 0), 10)
    glow3 = cv2.GaussianBlur(neon, (0, 0), 25)

    result = cv2.addWeighted(frame, 0.7, glow1, 1.0, 0)
    result = cv2.addWeighted(result, 1.0, glow2, 0.5, 0)
    result = cv2.addWeighted(result, 1.0, glow3, 0.25, 0)
    '''
    
    h, w = frame.shape[:2]

    x, y = np.meshgrid(
        np.arange(w),
        np.arange(h)
    )
    
    wave_x = x + 10 * np.sin(y / 25)
    wave_y = y + 10 * np.sin(x / 35)
    
    result = cv2.remap(
        frame,
        wave_x.astype(np.float32),
        wave_y.astype(np.float32),
        cv2.INTER_LINEAR
    )
    
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # h, s, v = cv2.split(hsv)

    # # Increase saturation
    # s = np.clip(s.astype(np.float32) * 2.0, 0, 255)

    # # Increase brightness
    # v = np.clip(v.astype(np.float32) * 1.2, 0, 255)

    # hsv = cv2.merge([
    #     h,
    #     s.astype(np.uint8),
    #     v.astype(np.uint8)
    # ])

    # result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # result = frame.copy()

    # spacing = 50
    
    # for x in range(0, frame.shape[1], spacing):
    #     cv2.line(
    #         result,
    #         (x, 0),
    #         (x, frame.shape[0]),
    #         (255, 0, 255),
    #         1
    #     )
    
    # for y in range(0, frame.shape[0], spacing):
    #     cv2.line(
    #         result,
    #         (0, y),
    #         (frame.shape[1], y),
    #         (255, 0, 255),
    #         1
    #     )
    
    # result = frame.copy()

    # for _ in range(10):

    #     y = random.randint(0, frame.shape[0] - 5)
    #     height = random.randint(2, 15)
    #     shift = random.randint(-50, 50)

    #     result[y:y+height] = np.roll(
    #         result[y:y+height],
    #         shift,
    #         axis=1
    #     )

    

    cv2.imshow("B&W Camera", result)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

