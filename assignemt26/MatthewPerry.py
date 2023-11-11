import cv2

matthew_perry = cv2.imread('matthew perry.jpg')
matthew_perry_2 = cv2.cvtColor(matthew_perry, cv2.COLOR_BGR2GRAY)
pic_size=matthew_perry_2.shape
black_width=50

for i in range(100):
        if i<=100-black_width:
           matthew_perry_2[i,100-black_width-i:100-i]=0
        else:
           matthew_perry_2[i,0:100-i]=0

cv2.imshow(" ",matthew_perry_2)
cv2.waitKey()


