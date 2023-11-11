import cv2
import numpy as np

def invert_image(image):
    inverted_image = cv2.bitwise_not(image)
    return inverted_image

image1 = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)

inverted_image1 = invert_image(image1)
inverted_image2 = invert_image(image2)


cv2.imshow('original image 1', image1)
cv2.imshow('inverted image 1', inverted_image1)

cv2.imshow('original image 2', image2)
cv2.imshow('inverted image 2', inverted_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('invert_image.jpg', inverted_image1)
cv2.imwrite('invert_image.jpg', inverted_image2)
