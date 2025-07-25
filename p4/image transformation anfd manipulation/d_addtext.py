import cv2
image=cv2.imread("p4\image transformation anfd manipulation\kumar.jpg")
if image is None:
    print("not working")
else:
    print("image loaded succesfull ")
    resize=cv2.resize(image,(300,300))
    cv2. putText(resize, "hello kowshik",(30,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv2.imshow(" adding text",resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # FONT_HERSHEY_COMPLEX is one of several font types available in OpenCV.
    # It is a proportional font that has a more complex appearance compared to simpler 
    # fonts like FONT_HERSHEY_SIMPLEX. The complex font includes additional features such as slant 
    # and varying thickness, making it suitable for more stylized text rendering.