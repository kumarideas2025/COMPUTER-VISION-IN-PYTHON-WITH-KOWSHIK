import cv2 
image=cv2.imread("p3\image resizing and  reshaping\output_dog.png ")

if image is None:
    print("image is not found")
    # width then height and always save
else:
    print("Image loaded")
    
    
    resize=cv2.resize(image,(300,300))
    
    cv2.imshow("Original image",image)
    cv2.imshow("Resized image",resize)
    
    cv2.imwrite("resized _output.png",resize)
    cv2.waitKey(0)
    cv2.DestroyALLWindows() 
    
    
    
 