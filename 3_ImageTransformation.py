import cv2 as cv
import numpy as np

img = cv.imread('Path')

# Translate - Shift an image about an axis
def Translate(img, x, y): #image, pixles to shift by (x and y)
    newImage = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, newImage, dimension)

newImage = Translate(img, 100, 100) # x and y represent the axes

# Rotate - Image can be rotated around any point
def Rotate(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]
    if rotationPoint == None:
        rotationPoint = (width//2, height//2)
    rotatedMatrix = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotatedMatrix, dimension)

newImage2 = Rotate(img, 45, (100, 100))

# Flip
newImage3 = cv.flip(img, 0) # 0 or 1 to flip horizontal or vertical
