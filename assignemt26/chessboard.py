import cv2
import numpy as np

width, height = 8, 8
square_size = 50

chess_board= np.zeros((height * square_size, width * square_size, 3), dtype=np.uint8)

for row in range(height):
    for col in range(width):
        if (row + col) % 2 == 0:
            square_color = (255, 255, 255)
        else:
            square_color = (0, 0, 0)
        
        x1, y1 = col * square_size, row * square_size
        x2, y2 = (col +1) *square_size, (row + 1) * square_size

        cv2.rectangle(chess_board, (x1, y1), (x2, y2), square_color, -1)

cv2.imshow("chessboard", chess_board)
cv2.waitKey(0)
cv2.destroyAllWindows()
