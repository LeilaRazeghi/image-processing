import random
import cv2

image = cv2.imread("ashkan.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

image_sticker1 = cv2.imread("input\sticker1.png")
#image_sticker2 = cv2.imread("sticker2.png")
#image_sticker3 = cv2.imread("sticker3.png")

#stickers = [image_sticker1, image_sticker2, image_sticker3]

faces = face_detector.detectMultiScale(image_gray, 1.3)

for face in faces:
    x, y, w, h = face 
    #cv2.rectangle(image, [x, y], [x+w, y+h], [0,0,0], 8)
    sticker = cv2.resize(image_sticker1, [w, h])
    image[y:y+h, x:x+w] = sticker

cv2.imshow("result", image)
cv2.imwrite("face_detection.jpg", image)
cv2.waitKey()
