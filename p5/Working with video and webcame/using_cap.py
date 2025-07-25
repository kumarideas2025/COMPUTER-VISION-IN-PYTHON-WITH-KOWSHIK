import cv2
# that will start our webcam
cap=cv2.VideoCapture(0)

while True:
    # cap.read means read one image from camera
    ret,frame=cap.read()   #ret means return. ret=True/False ..frame=image
    
    if not ret:
        print("could not read frame")
        break
    cv2.imshow("webcam feed",frame)
    # wait 1 mm second to check use has press any key.if  press k then that loop has to be break
    if cv2.waitKey(1) & 0xFF==ord('k'):
       print("quitting....")
       break
# this will stop camera
cap.release()

cv2.destroyALLWindows()