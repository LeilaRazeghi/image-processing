import cv2
import numpy as np
import matplotlib.pyplot as plt

image_xray = cv2.imread("input/xray_noisy.png", cv2.IMREAD_GRAYSCALE)
image_board = cv2.imread("input/board_noisy.png", cv2.IMREAD_GRAYSCALE)
image_circle = cv2.imread("input\circle_noisy.png", cv2.IMREAD_GRAYSCALE)
image_face = cv2.imread("input\Medianfilterp.png", cv2.IMREAD_GRAYSCALE)
image_ballons = cv2.imread("input/balloons_noisy.png")
image_5 = cv2.imread("input/5.png", cv2.IMREAD_GRAYSCALE)

#result_xray = np.zeros(image_xray.shape)

#for i in range (1, image_xray.shape[0]-1):
    #for j in range(1, image_xray.shape[1]-1):
        #small = image_xray[i-1: i+2, j-1: j+2]
        #sorted_array = np.sort(small, axis=None)
        #result_xray[i,j] = sorted_array[4]

result_xray = cv2.medianBlur(image_xray, 5)
result_board = cv2.medianBlur(image_board, 5)
result_circle = cv2.medianBlur(image_circle, 5)
result_face = cv2.medianBlur(image_face, 5)
result_ballons = cv2.medianBlur(image_ballons, 5)
result_5 = cv2.medianBlur(image_5, 5)

result_xray = np.hstack((image_xray, result_xray))
result_board = np.hstack((image_board, result_board))
result_circle = np.hstack((image_circle, result_circle))
result_face = np.hstack((image_face, result_face))
result_ballons = np.hstack((image_ballons, result_ballons))
result_5 = np.hstack((image_5, result_5))


cv2.imwrite('output/xray.png', result_xray)
cv2.imwrite('output/board.png', result_board)
cv2.imwrite('output/circle.png', result_circle)
cv2.imwrite('output/face.png', result_face)
cv2.imwrite('output/ballons.png', result_ballons)
cv2.imwrite('output/5.png', result_5)