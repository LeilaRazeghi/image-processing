import cv2
import numpy as np

tv_image= cv2.imread("TV.jpg")
tv_image= cv2.cvtColor(tv_image, cv2.COLOR_BGR2GRAY)
rows, cols= tv_image.shape

writer=cv2.VideoWriter("tv_noise.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (cols, rows))

while True:
      tv_image= cv2.imread('TV.jpg')
      tv_image= cv2.cvtColor(tv_image, cv2.COLOR_BGR2GRAY)
      tv_noise= np.random.random((328, 577))* 255
      tv_noise= np.array(tv_noise, dtype=np.uint8)
      tv_image[30:358, 27:604]= tv_noise
      tv_image= cv2.cvtColor(tv_image, cv2.COLOR_GRAY2BGR)
      writer.write(tv_image)
      cv2.imshow('', tv_image)
      if cv2.waitKey(25) & 0xFF==("q"):
            break
writer.release()

cv2.rectangle(tv_image, (27,30 ), (604, 358), 200)
    