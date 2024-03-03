import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input\photo_2024-02-22_09-38-32.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape
print (image.shape)

def histogram_cal(image):
    histogram = np.zeros(256)
    for i in range(rows):
        for j in range(cols):
            value = image[i, j]
            histogram[value] += 1
    return histogram

histogram = histogram_cal(image)

#plt.bar(range(256), histogram)
#plt.plot(histogram)
plt.hist(image.ravel(),256,[0,256], facecolor='blue')
plt.title("Image Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Pixel's Number")
plt.show()

