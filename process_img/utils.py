import cv2
import numpy as np

def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image

def sharpen_image(image):
    # Tạo kernel để làm đậm nét
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened

def apply_threshold(image, threshold_value=150):
    # Áp dụng threshold để chuyển ảnh thành đen trắng
    _, binary_img = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY_INV)
    return binary_img

def process_image(image_path):
    # Đọc ảnh và chuyển về grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Áp dụng các bước xử lý ảnh
    img_denoised = noise_removal(img)
    img_sharpened = sharpen_image(img_denoised)
    img_binary = apply_threshold(img_sharpened)

    return img_binary