import cv2
image=cv2.imread("p4\image transformation anfd manipulation\kumar.jpg")
if image is None:
    print("not working")
else:
    print("image loaded succesfull ")
    resize=cv2.resize(image,(300,300))
    pt1=(250,40)
    pt2=(20,40)
    color=(255,0,2)
    thickness=6
    cv2.line(resize,pt1,pt2,color,thickness)
    cv2.imshow("original image",resize)
    cv2.waitKey()
    cv2.destroyAllWindows()s
    