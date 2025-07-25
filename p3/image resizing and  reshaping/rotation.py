import cv2 
image=cv2.imread("p3\image resizing and  reshaping\kowshik.jpg   ")

if image is  None:
    print("could not load image")
else:
    # :2 means we need two values slicing
    (h,w)=image.shape[:2]
    
    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,-90,0.5)
    rotated=cv2.warpAffine(image,M,(w,h))
    
    cv2.imshow("original ",image)
    cv2.imshow("rotate 90 degree",rotated)
    cv2.waitKey()
    cv2.destroyALLWindows()
    