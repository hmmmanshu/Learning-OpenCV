import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haarcascade_faces.xml')

people = ["Dr_Strange", "Elon_Musk", "Kim_Jong_Un", "Roger_Federer"]
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBHPFaceRecognizer_create()
face_recognizer.read('face_model.yml')

img = cv.imread(input("Enter image path"))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect face
faces_rect = haar_cascade.detectMultiScale(img, 1.1, 2)
for (x,y,w,h) in faces_rect:
    faces_roi = img[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'{people[label]} label with a confidence of {confidence}')