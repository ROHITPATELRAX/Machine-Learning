import time
import math
import cv2
import HandTrackingModule as htm

# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# devices = AudioUtilities.GetSpeakers()


# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# interface=devices
# volume.GetMute()
# volume.GetMasterVolumeLevel()
# volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(-20.0, None)

obj=htm.HandTrack(detectionCon=0.8)

VideoSource=cv2.VideoCapture(0)
pTime=0

while True:
    status,frame = VideoSource.read()
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame=obj.processHands(frame,imgRGB)

    lmList=obj.findPosition(frame=frame,draw=False)

    
    if len(lmList)!=0:
        x1,y1=int(lmList[4][1]),int(lmList[4][2])
        x2,y2=int(lmList[8][1]),int(lmList[8][2])
        cx,cy=(x2+x1)//2,(y2+y1)//2
        frame=cv2.circle(center=(int(x1),int(y1)),color=(255,0,25),img=frame,radius=8,thickness=cv2.FILLED)
        frame=cv2.circle(center=(int(x2),int(y2)),color=(255,0,25),img=frame,radius=8,thickness=cv2.FILLED)
        frame=cv2.line(color=(255,0,25),img=frame,pt1=(x1,y1),pt2=(x2,y2),thickness=3)
        frame=cv2.circle(center=(int(cx),int(cy)),color=(255,0,25),img=frame,radius=8,thickness=cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        print(length)

        if length<50:
            frame=cv2.circle(center=(int(cx),int(cy)),color=(0,255,0),img=frame,radius=8,thickness=cv2.FILLED)
        elif length>250:
            frame=cv2.circle(center=(int(cx),int(cy)),color=(0,0,0),img=frame,radius=8,thickness=cv2.FILLED)
        else:
            pass


    currentTime=time.time()
    fps=1//(currentTime-pTime)
    pTime=currentTime

    cv2.putText(frame,str(fps),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    cv2.imshow("Volumn Cotrol Panel: ",frame)
    cv2.waitKey(1)