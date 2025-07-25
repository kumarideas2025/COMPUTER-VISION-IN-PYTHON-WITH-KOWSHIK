import cv2
camera=cv2.VideoCapture(0)
# we use get to find the width and height of it
frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# codec that will be used for video encoding when writing video files.
#The FourCC is a 32-bit identifier used to indicate the format of the video stream.
# The asterisk (*) before the string 'XVID' is used to unpack the string into individual characters. 
# In this case, it converts the string 'XVID' into four separate characters: 'X', 'V', 'I', and 'D'. 
# This is necessary because the VideoWriter_fourcc function expects four separate characters as its arguments.

codeC=cv2.VideoWriter_fourcc(*'XVID')


recorder=cv2.VideoWriter("my_video avi",codeC,20,(frame_width,frame_height))

while True:
    success,image=camera.read()
    
    if not success:
        break
    
    recorder.write(image)
    cv2.imshow("Recoding Live",image)
    
    if cv2.waitKey(1) & 0xFF==ord('k'):
        print("quitting....")
        break
camera.release()
recorder.release()
cv2.destroyALLWindows()


# after output we get a video with file name
