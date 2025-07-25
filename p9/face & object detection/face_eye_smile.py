import cv2
face_cascade=cv2.CascadeClassifier("p9/face & object detection/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("p9/face & object detection/haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier("p9/face & object detection/haarcascade_smile.xml")

cap=cv2.VideoCapture(0)
while  True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray, 1.1 ,5)
    
    for(x , y , w , h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,265),3)
        
    #region of face:---this will cut  face  from  full  image (called roi means region of interest)..then it will be easy to  find  eye  and smile
    #(x=100,y=150)[w=80 X h=80] ..(100,150)w=80>>>>180 and h=80>>>230
    
    
    #gray[150:150+80  , 100 :100+80]..will part this amount of part from  image for gray scale.
        roi_gray=gray[y:y +h, x:x +w]
    #color[150:150+80  , 100 :100+80]..will part this amount of part from  image for color scale.
        roi_color=frame[y:y +h, x:x +w]
    
        eyes=eye_cascade.detectMultiScale(roi_gray,1.1,10)
        if len(eyes)>0:
           cv2.putText(frame,"Eyes Detected",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,265,0),3)
    # use y-30 to adjust eye site.
    
    
        smiles=smile_cascade.detectMultiScale(roi_gray,1.7,20)
        if len(smiles)>0:
           cv2.putText(frame,"smiling",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.6,(265,0,0),3)
    cv2.imshow("webcam face detection",frame)
    if cv2.waitKey(1)&0xFF==ord('k'):
        break
cap.release()
cv2.destroyALLWindows()
