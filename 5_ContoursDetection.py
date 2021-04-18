import cv2 as cv
import numpy as np

img = cv.imread('image.jpg')
img = cv.resize(img, (img.shape[1]//4, img.shape[0]//4))

# Convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Add some blur
gray_blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)

# Find the edges
canny = cv.Canny(gray_blur, 125, 175)
cv.imshow('Edges', canny)

# Find the contours
contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

# ========================================================
# Instead of canny edge detector, we could use threshold
# ========================================================

ret, thresh = cv.threshold(gray, 100, 205, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

# Visulaize the contours
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.drawContours(blank, contours, -1, (255, 255, 255), thickness=2) #-1 means draw all the contours
cv.imshow("Contours", blank)
cv.waitKey(0)