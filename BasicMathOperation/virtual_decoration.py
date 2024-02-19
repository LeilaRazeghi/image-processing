import cv2
import numpy as np

room_background = cv2.imread("room_background.jpg")
room_foreground = cv2.imread("room_foreground.jpg")
room_mask = cv2.imread("room_mask.jpg")


room_background = cv2.cvtColor(room_background, cv2.COLOR_BGR2GRAY)
room_foreground = cv2.cvtColor(room_foreground, cv2.COLOR_BGR2GRAY)
room_mask = cv2.cvtColor(room_mask, cv2.COLOR_BGR2GRAY)

room_mask = room_mask / 255
room_background = room_background * (1 - room_mask)
room_foreground = room_foreground * room_mask
result = room_foreground + room_background


cv2.imshow("virtual decoration", result)
cv2.imwrite("output/VirtualDecoration.jpg", result)
cv2.waitKey()
