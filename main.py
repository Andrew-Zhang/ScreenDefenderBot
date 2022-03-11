import cv2 as cv
import numpy as np
import webbrowser
from osax import *



# def numFaces(frame):
#     faces = haarCascade.detectMultiScale(frame)
#     return len(faces)
    
haarCascade = cv.CascadeClassifier('harrFace.xml')
sa = OSAX()
cap = cv.VideoCapture(0)
numConsecutive = 0
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    # cv.imshow('Video', frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = haarCascade.detectMultiScale(gray)
    
    if len(faces) > 1:
        numConsecutive += 1
    else:
        numConsecutive = 0
    
    if numConsecutive >= 5:
        webbrowser.open('https://docs.google.com/document/d/1K08AvgMnCHqc-3sP6vOZBYwhK3YbtQ9JwVkePi4iBHg/edit', new=2)
        sa.set_volume(0)
        numConsecutive = 0
        time.sleep(5)
    print(len(faces))
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break