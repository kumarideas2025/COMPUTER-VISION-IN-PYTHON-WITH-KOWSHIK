import cv2
image=cv2.imread("p6\Image Filerting & Bluring\kks.jpg")

resize=cv2.resize(image,(300,300))

blurred=cv2.GaussianBlur(resize,(9,9),0)

cv2.imshow("original Image",resize)
cv2.imshow("Blur image",blurred)
cv2.waitKey(0)
cv2.destroyALLWindows()

# kernel will blur the center pixel with the average some of all other pixel in a image frame
# your color is 67 ..and your pixel average color is 80. then 67 will be replace with 50.