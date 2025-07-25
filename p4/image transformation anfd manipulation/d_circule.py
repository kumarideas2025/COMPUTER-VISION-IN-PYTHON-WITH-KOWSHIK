import cv2
image=cv2.imread("p4\image transformation anfd manipulation\kumar.jpg")
if image is None:
    print("not working")
else:
    print("image loaded succesfull ")
    resize=cv2.resize(image,(300,300))
    cv2.circle(resize,(150,150),50,(265,0,0),1)
    cv2.imshow("drawing circle",resize)
    cv2.waitKey()
    cv2.destroyAllWindows()
    