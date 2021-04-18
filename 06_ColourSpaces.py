import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image.jpg')
img = cv.resize(img, (img.shape[1]//4, img.shape[0]//4))

# use the cvtColor to convert one color space to another
cv.imshow("BnW", cv.cvtColor(img, cv.COLOR_BGR2GRAY))
cv.imshow("HSV", cv.cvtColor(img, cv.COLOR_BGR2HSV))
cv.imshow("LAB", cv.cvtColor(img, cv.COLOR_BGR2LAB))

# =======================================================
# BGR and RGB conflict
# Only openCV uses the BGR format while outside openCV, we need to use to RGB format
# See below how matplotlib percieves both the images
# =======================================================
plt.imshow(img) #BGR format
plt.title("BGR")
plt.show()

RGB_image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(RGB_image, ) #RGB format
plt.title("RGB")
plt.show()

# All the color spaces can be converted back int similar way

cv.waitKey(0)
