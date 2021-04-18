# Split or merge color channels of a color space
import cv2 as cv
import numpy as np

img = cv.imread('image.jpg')
img = cv.resize(img, (img.shape[1]//4, img.shape[0]//4))

b,g,r = cv.split(img)

# We can see the intensity distribution og the colors as shown below
cv.imshow("B",b)
cv.imshow("G",g)
cv.imshow("R",r)

# To print the actual color channel, merge the channel with a blank image
blank = np.zeros(img.shape[:2], dtype='uint8')
Green = cv.merge([blank, g, blank])
cv.imshow("Green Channel", Green)

cv.waitKey(0)
