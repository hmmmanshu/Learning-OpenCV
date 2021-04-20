import cv2 as cv

vid = cv.VideoCapture('Data/a.mp4')
haar_cascade = cv.CascadeClassifier('haarcascade_face.xml')

while(1):
    isTrue, frame = vid.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor = 1.2, minNeighbors=3)
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
vid.release()
cv.destroyAllWindows()
