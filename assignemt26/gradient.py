import cv2
import numpy as np


width, height = 300, 300

gradient = np.zeros ((height, width), dtype=np.uint8)

for i in range(height):
    gradient[i, :] = int(((height - i)/height) *255)

cv2.imshow('Gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()