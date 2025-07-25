import cv2
face_cascade=cv2.CascadeClassifier("p9/face & object detection/haarcascade_frontalface_default.xml ")
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray, 1.1 ,5)
#detectMultiScale()-->scan and detect object(face)
#1.1==> scale factor....(1.1 = how much zoom level have to do when scan )...1.1 means 10% smaller every time to find the exect face[not to slow nor blind]
# 5=minNeighbors...means how much clues we to conclude that ..this is the face we want.
# 5 also means here 5 steps of test have to past  before say it.
# if we pass 3 ..that call loose checking,5-safe check,6->strict checkingKHKK
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w ,y+h),(0,255,0),2)
# example what we done in for loop->
#(x+w,y+h):
#face1(x=100,y=150)[w=80 X h=80]  , so top-left=(100,150) and Bottom-right=(180,230)

#x- how far from left
#y-how far from top
#w-width of face
#h-height of face
#x,y-top left corner
    cv2.imshow("webcam face detection",frame)
    if cv2.waitKey(1)&0xFF==ord('k'):
        break
cap.release()
cv2.destroyALLWindows()