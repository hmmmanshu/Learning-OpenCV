import cv2 as cv

img = cv.imread('image.jpg')

# Convert an image to grayscale
newImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

# Blur the image
newImage2 = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)

# Edge cascade
# Edge cascading means to make a sort of a sketch of the given image
# Only the edges of the objects in the image will be shown
newImage3 = cv.Canny(img, 125, 175)

# Resize a video
import cv2 as cv
def rescaleFrame(frame, scale = .75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

capture = cv.videoCapture('path')

while(1):
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame_resized)

# Crop
# Since images are arrays, use array slicing
newImage5 = img[50:200, 200: 300]
