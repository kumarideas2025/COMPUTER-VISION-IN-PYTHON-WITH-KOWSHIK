import cv2 
image=cv2.imread("p3\image resizing and  reshaping\kowshik.jpg   ")

if image is  None:
    print("could not load image")
else:
    resize=cv2.resize(image,(300,300))
    flipped_horizontal=cv2.flip(resize,1)
    flipped_vertical=cv2.flip(resize,0)
    flipped_both=cv2.flip(resize,-1)
    
    cv2.imshow("origianl",resize)
    cv2.imshow("flipped Horizontal",flipped_horizontal)
    cv2.imshow("flipped vertical",flipped_vertical)
    cv2.imshow("flipped both",flipped_both)
    cv2.waitKey()
    cv2.destroyALLWindows()


    