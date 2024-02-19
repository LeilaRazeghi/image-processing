import cv2
import numpy as np

img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")

#resize images to have samr dimension
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

img1 = img1.astype(np.float32)
img2 = img2.astype(np.float32)

img1img2_1 = img1 * (1/4) + img2 * (3/4)
img1img2_2 = img1 * (1/2) + img2 * (1/2)
img1img2_3 = img1 * (3/4) + img2 * (1/4)

img1img2_1 = img1img2_1.astype(np.uint8)
img1img2_2 = img1img2_2.astype(np.uint8)
img1img2_3 = img1img2_3.astype(np.uint8)

img1img2 = np.concatenate((img1, img1img2_1, img1img2_2, img1img2_3, img2), axis=1)

cv2.imwrite("output/img1img2.jpg", img1img2)
