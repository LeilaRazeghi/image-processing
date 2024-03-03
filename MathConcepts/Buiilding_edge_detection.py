import cv2
import numpy as np

image = cv2.imread("input/building.png", cv2.IMREAD_GRAYSCALE)


rows, cols = image.shape
#result_v = np.zeros((rows, cols), dtype=np.uint8)
result_h = np.zeros((rows, cols), dtype=np.uint8)

#filter_v = np.array([[-1, 0, 1],
#                   [-1, 0, 1],
#                    [-1, 0, 1]])

filter_h = np.array([[-1, -1, -1],
                     [0, 0, 0],
                    [1, 1, 1]])

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_neighbor = image[i-1:i+2, j-1:j+2]
        average_h = np.abs(np.sum(small_neighbor * filter_h))
        #average_v = np.abs(np.sum (small_neighbor * filter_v))
        result_h[i,j] = average_h
        #result_v[i, j] = average_v


cv2.imshow('result', result_h)
#cv2.imshow('result', result_v)
cv2.waitKey()

cv2.imwrite('output/Building_h.png', result_h)
#cv2.imwrite('output/Building_v.png', result_v)


