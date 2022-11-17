import cv2 
import time
import mediapipe as mpipe

class HandTrack():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mHands=mpipe.solutions.hands
        self.hands=self.mHands.Hands()
        self.mpDraw=mpipe.solutions.drawing_utils
    
    def processHands(self,frame,imgRGB,draw=True):
        self.results=self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for i in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(frame,i,self.mHands.HAND_CONNECTIONS)
        return frame
    
    def findPosition(self,frame,handNo=0,draw=True):
        lmList=list()
        if self.results.multi_hand_landmarks:
            hands = self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(hands.landmark):
                h,w,c=frame.shape
                cx,cy=(lm.x*w),(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    # if id==4 or id==8 :
                        cv2.circle(center=(int(cx),int(cy)),color=(0,0,225),img=frame,radius=20)
                        # cv2.circle(frame,(cx,cy),20,(0,0,225),cv2.FILLED)
        return lmList

def main():

    cap=cv2.VideoCapture(0)

    currentTime=0
    pTime=0
    fps=0

    handTracker=HandTrack()

    while(True):
        status, frame = cap.read()

        imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        frame=handTracker.processHands(frame,imgRGB)

        lmList=handTracker.findPosition(frame,draw=True)

        # print(lmList)

        currentTime=time.time()
        fps=1//(currentTime-pTime)
        pTime=currentTime

        cv2.putText(frame,str(fps),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)

        cv2.imshow('Frame',frame)

        cv2.waitKey(1)

if __name__=="__main__":
    main()