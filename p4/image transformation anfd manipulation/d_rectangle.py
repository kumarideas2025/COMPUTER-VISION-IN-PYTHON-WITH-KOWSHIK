import cv2
image=cv2.imread("p4\image transformation anfd manipulation\kumar.jpg")
if image is None:
    print("not working")
else:
    print("image loaded succesfull ")
    resize=cv2.resize(image,(300,300))
    pt1=(100,100)
    pt2=(200,200)
    color=(0,0,255)
    thickness=6
    cv2.rectangle(resize,pt1,pt2,color,thickness)
    
    cv2.imshow("image focusing rectangle",resize)
    cv2.waitKey()
    cv2.destroyAllWindows()