import cv2 
image=cv2.imread( "p2/dsogy.png/dog.jpg(1).jpg")
                 
if image is not None:
   gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
   cv2.imshow("Grayscale image",gray)
   cv2. waitKey()
   cv2.DestroyAllWindows()
else:
    print("could not create")
    
    