import os
import cv2 as cv
import numpy as np

people = []
for i in os.listdir(r'D:\Programs\Python\OpenCV\Face_Recognition\Data'):
    people.append(i)
DIR = r"D:\Programs\Python\OpenCV\Face_Recognition\Data"

features = []
labels = []

haar_cascade = cv.CascadeClassifier('haarcascade_face.xml')

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label =  people.index(person)

        for im in os.listdir(path):
            img_path = os.path.join(path, im)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Find face
            faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 1)

            # Crop to the face part only
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

#print("No. of features = ", len(features))
#print("No. of labels = ", len(labels))

face_recognizer = cv.face.LBHPFaceRecognizer_create()
face_recognizer.save("face_model.yml")

# Train the model
features = np.array(features, dtype=object)
labels = np.array(labels)
np.save('features.npy', features)
np.save('labels.npy', labels)
face_recognizer.train(features, labels)