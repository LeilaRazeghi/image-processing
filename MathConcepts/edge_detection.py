import cv2
import numpy as np

lion_image = cv2.imread("input\lion.png", cv2.IMREAD_GRAYSCALE)
spide_image = cv2.imread("input\spider.webp", cv2.IMREAD_GRAYSCALE)

def edge_detection(image):
    rows, cols = image.shape
    result = np.zeros((rows, cols), dtype= np.uint8)

    #filter = np.array([[-1, -1, -1],
    #                  [-1, 8, -1],
    #                 [-1, -1, -1]])

    filter = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]])
    
    for i in range(1, rows -1):
        for j in range(1, cols-1):
            small_neighbor = image[i-1:i+2, j-1:j+2]
            average = np.abs(np.sum(filter*small_neighbor))
            result[i, j] = average
    
    return result

lion_edge_image = edge_detection(lion_image)
spider_edge_image = edge_detection(spide_image)


#cv2.imshow('', lion_edge_image)
cv2.imshow('', spider_edge_image)
#cv2.imwrite("output/lion_edge.png", lion_edge_image)
cv2.imwrite("output/spider_edge.png", spider_edge_image)
cv2.waitKey()
