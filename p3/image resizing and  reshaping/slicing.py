import cv2 
image=cv2.imread("p3\image resizing and  reshaping\kowshik.jpg   ")

if image is not None:
    resize=cv2.resize(image,(300,300))
    cv2.imshow("Resized image",resize)
    
    
    cropped=image[100:200,50:150]
    cv2.imshow("original image",image)
    cv2.imshow("Cropped",cropped)
    cv2.waitKey(0)
    cv2.destroyALLWindows()