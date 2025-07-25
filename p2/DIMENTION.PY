import cv2 
image=cv2.imread( "p2/dsogy.png/dog.jpg(1).jpg")
                 
if image is not None:
   h,w,c=image.shape
   print(f"Image Loaded:\nHeight:{h}\nWidth:{w}\nChannels:{c}")
else:
    print("could not loaded")