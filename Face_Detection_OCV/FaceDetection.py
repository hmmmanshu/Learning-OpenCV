# Face detection using haarcascade classifier

import cv2 as cv

img = cv.imread('Data/person.png')
img = cv.resize(img, (img.shape[1]//4, img.shape[0]//4))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Find how many faces were found
haar_cascade = cv.CascadeClassifier('haarcascade_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=3)
print("Number of faces found = ", len(faces_rect))

# Mark all the faces in the image
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow("Detected faces", img)

cv.waitKey(0)