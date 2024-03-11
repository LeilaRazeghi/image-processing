import cv2 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 50)

pic = cv2.imread('input\clinton_hillaryr.jpg', -1)
pic = cv2.resize(pic, (700, 750))

while True:   
    cv2.imshow("Background", pic)   
    ret, frame = cap.read()

   
    resized_frame_region = cv2.resize(frame[150:200, 150:300], (150, 75))
    
    
    pic[325:400, 275:425] = resized_frame_region 

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
