import cv2

image = cv2.imread("bat.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(image.shape)

threshold = 120
_, image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
cv2.putText(image, "Batman", (370, 500), cv2.FONT_HERSHEY_COMPLEX, 2, 255, thickness=3)

cv2.imshow("", image)
cv2.waitKey()
cv2.imwrite('BatmanLogo.png', image)