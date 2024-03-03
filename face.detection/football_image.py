import cv2
import numpy as np

length = 700
width = 400
pitch_image = np.ones((width, length, 3), dtype=np.uint8)
pitch_image = np.array(pitch_image, dtype=np.uint8)

green1 = (0, 128, 0)
green2= (0, 180, 0)

stripe_width= 50
for i in range(0, 700, stripe_width):
    if i // stripe_width %2 == 0:
        cv2.rectangle(pitch_image, (i, 0), (i + stripe_width, 400), green1, -1)
    else:
        cv2.rectangle(pitch_image, (i, 0), (i + stripe_width, 400), green2, -1)

# Draw white lines for the pitch
cv2.rectangle(pitch_image, (30,30), (length - 30,width - 30), (255,255,255),4)
cv2.rectangle(pitch_image, (30,110), (140,width - 110), (255,255,255),4)
cv2.rectangle(pitch_image, (30,150), (80,width - 150), (255,255,255),4)
cv2.rectangle(pitch_image, (length - 30,110), (length - 140,width - 110), (255,255,255),4)
cv2.rectangle(pitch_image, (length - 30,150), (length - 80,width - 150), (255,255,255),4)
cv2.circle(pitch_image, (length//2,width//2), 70, (255,255,255),4)
cv2.circle(pitch_image, (length//2,width//2), 0, (255,255,255),15)
cv2.line(pitch_image, (length//2,30), (length//2,width-30), (255,255,255),4)
      


cv2.imshow("football ground image", pitch_image)
cv2.imwrite("football_ground_image.jpg", pitch_image)
cv2.waitKey(0)

