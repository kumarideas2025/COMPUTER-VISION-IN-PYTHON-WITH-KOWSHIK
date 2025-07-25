import cv2 
image=cv2.imread( "p2/dsogy.png/dog.jpg(1).jpg")
                 
if image is not None:
    success=cv2.imwrite("output_dog.png",image)
    if success:
        print("image saved successfully as 'output_dog.png'")
    else:
        print("failed to save image")
else:
    print("eRROR:could not load image")