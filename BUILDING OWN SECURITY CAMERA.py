"""
Modules: cv2
Frame 1 and Frame 2
If there is difference,then it is moved,otherwise there is no any movement.
cvtColor: to convert the color to gray.
Threshold for noise cancellation{Sharper & Brighter Image}
_: we don't want that thing
Contours: for Boxes
"""

import cv2
import winsound
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1=cam.read()
    ret, frame2=cam.read()
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    #Threshold type is Binary
    _, thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    #make neccessary things to be bigger.
    dilated=cv2.dilate(thresh,None,iterations=3)
    #RETR_TREE is type of Mode
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # -1: INDEX AND (0,255,0): GREEN COLOR , 2: THICKNESS
    #To check only for bigger movements

    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x,y,w,h=cv2.boundingRect(c)
        #(0,255,0): Green and 2:Thickness.
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        #500: Frequency/Louder 200:Longer/time
        #Deteching and Sounding will happen synchronously.
        winsound.PlaySound('alert.wav',winsound.SND_ASYNC)
    if cv2.waitKey(10)==ord('q'):
        break
    cv2.imshow('Granny Cam',frame1)