import cv2
import numpy as np


# this will be a function, called when needed
image = cv2.imread("opencv_frame.png")
imageHsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lowerRange = np.array([95,150,89])
upperRange = np.array([125,255,255])

mask = cv2.inRange(imageHsv, lowerRange, upperRange)

contours, hierchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#optionals
cv2.imshow("Image", image)
cv2.imshow("Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()