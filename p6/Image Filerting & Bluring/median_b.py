import cv2
image=cv2.imread("p6\Image Filerting & Bluring\kks.jpg")
resize=cv2.resize(image,(300,300))

blurred=cv2.medianBlur( resize,3)

cv2.imshow("original image", resize)
cv2.imshow("clean image",blurred)
cv2.waitKey(0)
cv2.destroyALLWindows()