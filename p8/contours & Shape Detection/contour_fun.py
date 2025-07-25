import cv2
img = cv2.imread("p8/contours & Shape Detection/triangle.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# _ MEANS A PLACE HOLDER . WHERE IT IS NOT NEEDED FOR NOW BUT WE KNEW THAT IN FUTURE THAT WILL BE WORKABLE.
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    corners = len(approx)
    if corners == 3:
        shape_name = "triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentangle"
    elif corners > 5:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"
        
# with drawContours we simple-fly the output image with green outline . 2 picture img and approx(with green outline ) . 0 means we have to work with 1st picture.
cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)

# revel()   is a part of numpy. we use it for (multi dimension array to 1d array)
#example:
# [[100,200],
#  [150,250],
#  [120,270]]
#      to
# [100,200,150,250,120,270]

x = approx.ravel()[0]
y = approx.ravel()[1]-10
cv2.putText(img, shape_name, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,265) ,2)

cv2.imshow("contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
