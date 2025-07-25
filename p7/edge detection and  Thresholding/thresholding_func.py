import cv2
img=cv2.imread("p7\edge detection and  Thresholding\kowshik.jpg ",cv2.IMREAD_GRAYSCALE)
resize=cv2.resize(img,(300,300))
ret,thresh_img=cv2.threshold(resize,120,255,cv2.THRESH_BINARY)
cv2.imshow("original image",resize)
cv2.imshow(" THRESHOLD image",thresh_img)
cv2.waitKey()
cv2.destroyALLWindows()

# 90-0=> black, 130-255=> white,180-255=>white,50-0=>black