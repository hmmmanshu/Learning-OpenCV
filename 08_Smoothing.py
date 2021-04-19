# Different image blurring and smoothing techniques
import cv2 as cv
img = cv.imread('image.jpg')
img = cv.resize(img, (img.shape[1]//4, img.shape[0]//4))

# Averaging
average = cv.blur(img, (3,3))

# Gaussian blur
gauss = cv.GaussianBlur(img, (5,5), 0)

#  Median blur
# Same asaverage blur but median is calculated instead of average of surrounding pixels
median = cv.medianBlur(img, 3)

# Bilateral blurring
# It might be the best blur as it blurs the image but retains the edges
bilateral = cv.bilateralFilter(img, 5, 15, 15)

cv.waitKey(0)