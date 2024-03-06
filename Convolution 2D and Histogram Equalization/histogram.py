import cv2
import numpy as np
import matplotlib.pyplot as plt

#image1 = cv2.imread("input\plainview.jpg", cv2.IMREAD_GRAYSCALE)
#image2 = cv2.imread('input\citysky.png', cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread("input/tsukuba_l.png", cv2.IMREAD_GRAYSCALE)

#image1_eq = cv2.equalizeHist(image1)
#image2_eq = cv2.equalizeHist(image2)
image3_eq = cv2.equalizeHist(image3)

#hist1 =cv2.calcHist([image1_eq], [0], None, [256], [0, 256])
#hist2 =cv2.calcHist([image2_eq], [0], None, [256], [0, 256])
hist3 =cv2.calcHist([image3_eq], [0], None, [256], [0, 256])

clahe = cv2.createCLAHE(clipLimit=2.0 , tileGridSize=(8,8))
res = clahe.apply(image3)

#image1_eq = np.hstack((image1, image1_eq))
#image2_eq = np.hstack((image2, image2_eq))
image3_eq = np.hstack((image3, image3_eq, res))

#plt.plot(hist1)
#plt.plot(hist2)
plt.plot(hist3)
plt.show()
#cv2.imwrite("output/image1_eualized.jpg", image1_eq)
#cv2.imwrite("output/image2_eualized.jpg", image2_eq)
cv2.imwrite("output/image3_eualized.jpg", image3_eq)
cv2.imwrite("output/image3_clahe_eualized.jpg", image3_eq)