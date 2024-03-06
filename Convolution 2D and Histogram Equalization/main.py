import cv2
import numpy as np

image = cv2.imread("input\circle_noisy.png", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((3, 3)) / 9

result = cv2.filter2D(image, -1, kernel)

cv2.imwrite("output/result1.jpg", result)
