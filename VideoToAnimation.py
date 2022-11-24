import cv2
import time
# import sys

# VIDEO_URL = str(sys.argv[1])

cap = cv2.VideoCapture(0)

currentTime=0
pTime=0
fps=0

while(True):
    ret, frame = cap.read()

    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    imgRGB=cv2.medianBlur(imgRGB,5)
    

    currentTime=time.time()
    fps=1//(currentTime-pTime)
    pTime=currentTime

    cv2.putText(frame,str(fps),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)

    cv2.imshow('Frame',frame)
    cv2.waitKey(1)

