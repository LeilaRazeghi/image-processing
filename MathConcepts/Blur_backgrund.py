import cv2
import numpy as np


image = cv2.imread("input/flower_input.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape
result = np.zeros((rows, cols), dtype=np.uint8)
n= 30
filter = np.ones((n*2+1, n*2+1))/ ((n*2+1)*(n*2+1))

for i in range(n, rows-n):
    for j in range(n, cols-n):
        small = image[i-n:i+n+1, j-n:j+n+1]
        if image[i,j] < 125:
            average = np.sum(filter * small)
            result[i, j] = average
        else:
            result[i, j] = image[i, j]
        
    
cv2.imwrite("output/blur_background.png", result)
cv2.imshow('', result)
cv2.waitKey(0)