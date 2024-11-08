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


# def noise_removal(image):
#     # Tăng kích thước kernel cho các bước dilate và erode
#     kernel = np.ones((3, 3), np.uint8)
#
#     # Loại bỏ nhiễu nhỏ hơn và làm dày các đường nét với phép toán morphology
#     image = cv2.dilate(image, kernel, iterations=1)
#     image = cv2.erode(image, kernel, iterations=1)
#     image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
#
#     # Sử dụng Gaussian Blur thay vì Median Blur để làm mờ nhiễu
#     image = cv2.GaussianBlur(image, (5, 5), 0)
#
#     # Thêm Adaptive Threshold để giữ độ tương phản tốt
#     image = cv2.adaptiveThreshold(
#         image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
#     )
#
#     return image


def enhance_text(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def apply_threshold(image, threshold_value=150):
    # Áp dụng threshold để chuyển ảnh thành đen trắng
    _, binary_img = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY_INV)
    return binary_img

def process_image(image_path):
    # Đọc ảnh và chuyển về grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Áp dụng các bước xử lý ảnh
    img_denoised = noise_removal(img)
    img_sharpened = enhance_text(img_denoised)
    img_binary = apply_threshold(img_sharpened)

    return img_binary