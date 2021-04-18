import cv2 as cv

img = cv.imread('image.jpg')
img = cv.resize(img, (img.shape[1]//4, img.shape[0]//4))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple thresholding
# Values will change depending upon the images to process
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple threshold', thresh)

# Inverse thresholding
threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse threshold', thresh_inv)

# Adaptive thresholding
# Let the computer find optimum values to threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 3)
cv.imshow('Adaptive threshold', adaptive_thresh)

cv.waitKey(0)