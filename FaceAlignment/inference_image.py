import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time  
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


fd = UltraLightFaceDetecion("RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel( "coor_2d106.tflite")

image = cv2.imread("photo_2024-02-22_09-38-19.jpg")
color = (0, 0, 255)

#start_time = time.perf_counter()
boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    for i,p in enumerate(np.round(pred).astype(int)):
        cv2.circle(image, tuple(p), 2, color, -1)
        cv2.putText(image, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0))


    lips_landmarks = []
    for i in [52, 55, 56, 53, 59, 58, 61, 63, 64, 68, 67, 71]:
        lips_landmarks.append(pred[i])
    lips_landmarks = np.array(lips_landmarks, dtype=int)

    x, y, w, h = cv2.boundingRect(lips_landmarks)   
    mask = np.zeros(image.shape, dtype= np.uint8)
    cv2.drawContours(mask, [lips_landmarks], -1, (255, 255, 255), -1)
    mask = mask // 255

    result =image * mask
    result = result[y:y+h, x:x+w]
    #print(lips_landmarks)

    #result_big = cv2.resize(result, (0, 0), fx=2 , fy=2)
    #return result_big

#print(time.perf_counter() - start_time)

cv2.imshow("result", image)
cv2.waitKey(0)
cv2.imwrite("output/result.jpg", image)
