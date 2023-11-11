import cv2
import numpy as np

image_size = 300
canvas = np.ones((image_size, image_size, 3), dtype= np.uint8) * 255

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 6
font_thickness = 18
font_color = (0, 0, 0)

text = "L"
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_position = ((image_size - text_size[0])// 2, (image_size + text_size[1])// 2)
 
cv2.putText(canvas, text, text_position, font, font_scale, font_color, font_thickness)

cv2.imshow('Leila', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()