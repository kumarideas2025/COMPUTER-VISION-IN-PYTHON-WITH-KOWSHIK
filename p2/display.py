
import cv2 
image=cv2.imread( "p2/dsogy.png/dog.jpg(1).jpg")
                 
if image is not None:
        #open the windows 
    cv2.imshow("image showing",image)
    #  wait for key
    cv2. waitKey()
    #  close the window

    cv2.destroyALLWindows()
else:
      print("image loaded successfully")





