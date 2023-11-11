import cv2

image_path = ('3.jpg')
image = cv2.imread(image_path)

rotated_image = cv2.rotate(image, cv2.ROTATE_180)

cv2.imshow('original image', image)
cv2.imshow('rotated image', rotated_image)
cv2.waitKey()

cv2.imwrite('rotated_image.jpg', rotated_image)
