import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image.jpg')

# Grayscale histogram
# Set range to anything below 255 as nothing goes >255 in RGB
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray], [0], None, [300], [0,300])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Intensity")
plt.ylabel("Pixels")
plt.plot(gray_hist)
plt.show()

# Coloured histogram
colors = ('b', 'g', 'r') # To get respective coloured line in the plot
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [255], [0,255])
    plt.plot(hist, color=col)

plt.title("RGB histogram")
plt.show()