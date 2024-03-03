import cv2
import numpy as np

board_noise = cv2.imread("input/board_noisy.png", cv2.IMREAD_GRAYSCALE)
xray_noise = cv2.imread("input/xray_noisy.png", cv2.IMREAD_GRAYSCALE)
circle_noise = cv2.imread("input/image_noisy.png", cv2.IMREAD_GRAYSCALE)

def noise_reduction(image):
    rows, cols = image.shape
    results = np.zeros((rows, cols), dtype=np.uint8)

    filter = np.ones((3,3))/ 9

    for i in range (1 , rows-1):
        for j in range( 1, cols-1):
            small_neighbor = image[i-1:i+2, j-1:j+2]
            average = np.abs(np.sum( filter * small_neighbor))
            results[i,j] = average

    return results

reduced_board_noise = noise_reduction(board_noise)
cv2.imwrite('output/board_noise_reduction.png', reduced_board_noise)
#reduced_xray_noise = noise_reduction(xray_noise)
#cv2.imwrite('output/xray_noise_reduction.png', reduced_xray_noise)
#reduced_circle_noise = noise_reduction(circle_noise)
#cv2.imwrite('output/circle_noise_reduction.png', reduced_circle_noise)