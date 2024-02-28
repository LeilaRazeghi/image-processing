import os
import cv2
import numpy as np

counter = 1
for i in range(4):
    images_path = os.listdir(f"input/{i+1}")
    images = []
    
    for image_path in images_path:
        image = cv2.imread(f"input/{counter}/" + image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = image.astype(np.float32)
        images.append(image)

    result = np.zeros(image.shape)

    for image in images:
        result += image

    result = result / len(images)
    result = result.astype(np.uint8)

    counter += 1
    cv2.imwrite(f"{i+1}.jpg", result)



#concatenating
img1 = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")
img3 = cv2.imread("3.jpg")
img4 = cv2.imread("4.jpg")

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)

result1 = np.concatenate((img1, img2), axis=1)
result2 = np.concatenate((img3, img4), axis=1)
result= np.concatenate((result1, result2), axis=0)

cv2.imshow("BlackHole", result)
cv2.imwrite("output/BlackHole.jpg", result)
cv2.waitKey()