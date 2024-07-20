import cv2

image = cv2.imread("...Path...")
cv2.imshow("f 0", image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("f 1",gray_image)
cv2.waitKey(0)
inverted_image = 255 - gray_image
cv2.imshow("f 2", inverted_image)
cv2.waitKey(0)
blurred = cv2.GaussianBlur(inverted_image, (21 , 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("f 3",pencil_sketch)
cv2.waitKey(0)
cv2.imshow("Org Img", image)
cv2.imshow("Pen Img", pencil_sketch)
cv2.waitKey(0)
