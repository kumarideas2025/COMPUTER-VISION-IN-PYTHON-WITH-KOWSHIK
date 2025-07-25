
import cv2 
image=cv2.imread( "p2/dsogy.png/dog.jpg(1).jpg")
                 
if image is None:
      print("error:image not found")
else:
      print("image loaded successfully")
