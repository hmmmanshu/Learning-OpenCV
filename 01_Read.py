import cv2 as cv

# Reading image
img = cv.imread('image.jpg')
cv.imshow('Paris',img)
cv.waitKey(0)

# Reading video
vid = cv.VideoCapture('Face_Detection/a.mp4')
while(1):
    isTrue, frame = vid.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
vid.release()
cv.destroyAllWindows()
