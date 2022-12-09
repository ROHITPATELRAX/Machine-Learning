import numpy as np
import cv2

height=512
width=512


cv2.namedWindow("Bouncy Ball")

radius=30

speed=1
minSpeed=1
maxSpeed=20

ballMovePointer=radius
vertical=False

upDownFlag=False

while True:
    if ((ballMovePointer+speed+radius)>=width):
        upDownFlag=True
    
    elif ((ballMovePointer+speed-radius)<=0):
        upDownFlag=False
    
    img=np.zeros((height,width,3),np.uint8)

    cv2.putText(img=img,color=(230,230,0),text=f"Speed: {speed}",fontFace=cv2.FONT_HERSHEY_COMPLEX,org=(10,50),fontScale=1,thickness=3)
    # cv2.putText(frame,str(fps),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    if vertical:
        cv2.circle(img,(int(height/2),ballMovePointer),radius,(253,0,255),cv2.FILLED)
    else:
        cv2.circle(img,(ballMovePointer,int(width/2)),radius,(150,0,255),cv2.FILLED)
    
    cv2.imshow("Bouncy Ball",img)

    if upDownFlag:
        ballMovePointer-=speed
    else:
        ballMovePointer+=speed
    

    inpFromKeyboard=cv2.waitKey(27) & 0xff

    if inpFromKeyboard==ord('p'):
        speed+=1
    
    if inpFromKeyboard==ord('v'):
        vertical= not vertical

    if speed==maxSpeed:
        speed=minSpeed

    if inpFromKeyboard==ord('q'):
        break

