import numpy as np
import cv2

image=cv2.imread("input/1.tif", cv2.IMREAD_GRAYSCALE)

#5x5 0.04
kernel1 = np.array([[ 0.04, 0.04, 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04, 0.04, 0.04]])

# 5x5   1
kernel2 = np.array([[ 1, 1, 1, 1, 1],
                 [ 1, 1, 1, 1, 1],
                 [ 1, 1, 1, 1, 1],
                 [ 1, 1, 1, 1, 1],
                 [ 1, 1, 1, 1, 1]])

#5x5  5
kernel3 = np.array([[ 5, 5, 5, 5, 5],
                 [ 5, 5, 5, 5, 5],
                 [ 5, 5, 5, 5, 5],
                 [ 5, 5, 5, 5, 5],
                 [ 5, 5, 5, 5, 5]])

#3x3  0.04
kernel4 = np.array([[ 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04]])

#3x3  1
kernel5 = np.array([[ 1, 1, 1],
                 [ 1, 1, 1],
                 [ 1, 1, 1]])

#3x3  5
kernel6 = np.array([[ 5, 5, 5],
                 [ 5, 5, 5],
                 [ 5, 5, 5]])


result1 = cv2.filter2D(image, -1, kernel1)      
result2 = cv2.filter2D(image, -1, kernel2)      
result3 = cv2.filter2D(image, -1, kernel3)      
result4 = cv2.filter2D(image, -1, kernel4) 
result5 = cv2.filter2D(image, -1, kernel5)      
result6 = cv2.filter2D(image, -1, kernel6) 

result = np.hstack((image, result1, result2, result3, result4, result5, result6))

# cv2.imshow("r1", result1)
# cv2.imshow("r2", result2)
# cv2.imshow("r3", result3)
# cv2.imshow("r4", result4)
# cv2.imshow("r", result)
# cv2.waitKey()

cv2.imwrite("Output/hidden_things.jpg", result)