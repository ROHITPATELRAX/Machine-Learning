import numpy as np
import cv2

height=512
width=512

img=np.zeros((height,width,3),np.uint8)
cv2.namedWindow("Bouncy Ball")

radius=3

ballMovePointer=radius

while True:
    if ((ballMovePointer+radius)==width):
        ballMovePointer=radius
    
    cv2.circle(img,(int(height/2),ballMovePointer),radius,(0,0,255),cv2.FILLED)
    
    cv2.imshow("Bouncy Ball",img)
    ballMovePointer+=1

    inpFromKeyboard=cv2.waitKey(27) & 0xff

    if inpFromKeyboard==ord('q'):
        break

