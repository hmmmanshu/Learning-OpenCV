import cv2 as cv
import numpy as np
# img = cv.imread('Filename.jpg')
# cv.imshow('Windowname', img)

#or draw on a blank image as shown below
blank = np.zeros((500, 500, 3), dtype='uint8') #uint8 is the data type for an graphics ranging 0-255

# Change color of array [BGR works for OpenCV rather than traditional RGB]
blank[:] = 255,0,0
blank[200:300, 200:300] = 0,255,0 

# Draw a rectangle
cv.rectangle(blank, (0, 0), (100, 100), (0,200,200), thickness=2)
cv.rectangle(blank, (100, 100), (200, 200), (0,200,200), thickness=cv.FILLED)

# Draw a circle
cv.circle(blank, (250,250), 30, (0, 100, 100), thickness=-1)

#Put some text
cv.putText(blank, "Hii", (300, 300), cv.FONT_HERSHEY_PLAIN, 10, (0,150, 150), thickness=2)

cv.waitKey(0)