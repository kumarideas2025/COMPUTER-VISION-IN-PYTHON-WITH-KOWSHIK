import cv2
import numpy as np
#image size should be same in two image.
img1=np.zeros((300,300),dtype="uint8")
img2=np.zeros((300,300),dtype="uint8")



s
# A filled circle is drawn on img1 with a center at (150, 150) and a radius of 100 pixels. 
# The color value is set to 265 
# (which may not be visible since it exceeds the maximum value for a single channel in an 8-bit image, which is 255).
cv2.circle(img1,(150,150),100,255,-1)






# A filled rectangle is drawn on img2 with the top-left corner at (100, 100) 
# and the bottom-right corner at (250, 250). The color value is also set to 265.
cv2.rectangle(img2,(100,100),(250,250),255,-1)




bitwise_and=cv2.bitwise_and(img1,img2)s
bitwise_or=cv2.bitwise_or(img1,img2)
bitwise_not=cv2.bitwise_not(img1)




cv2.imshow("Circle",img1)
cv2.imshow("rectangle",img2)
cv2.imshow("AND",bitwise_and)
cv2.imshow("OR",bitwise_or)
cv2.imshow("NOT",bitwise_not)
cv2.waitKey(0)
cv2.destroyALLWindows()


# np.zeros(...):
# This function from the NumPy library creates an array filled with zeros.
# The shape of the array is specified by the first argument.

# (300, 300):
# This tuple specifies the dimensions of the array.
# In this case, it creates a 2D array (or matrix) with 300 rows and 300 columns.
# Each element in this array will represent a pixel in the image.


# dtype="uint8":
# This argument specifies the data type of the array elements.
# uint8 stands for "unsigned 8-bit integer," which means each pixel can hold a value from 0 to 255. 
# This range is typical for grayscale images, where 0 represents black, 255 represents