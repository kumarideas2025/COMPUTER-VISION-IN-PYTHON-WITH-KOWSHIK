import cv2
#with the help of gray scale we turn color image into gray image.
img=cv2.imread("p7/edge detection and  Thresholding/flower.jpeg",cv2.IMREAD_GRAYSCALE)
#then with the help oif color image ..took canny function and turn into a canny image
edges=cv2.Canny(img,50,150)
cv2.imshow("original image",img)
cv2.imshow("canny image",edges)
cv2.waitKey()
cv2.destroyALLWindows()