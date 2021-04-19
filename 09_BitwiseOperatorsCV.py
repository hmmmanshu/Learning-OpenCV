import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
rect = cv.rectangle(blank.copy(), (30,30), (370,370), (200,200,200), -1)
circle = cv.circle(blank.copy(), (200,200), 200, (200,200,200), -1)

# bitwise AND
# perform bitwise AND for ON and OFF pixels
bitwise_and = cv.bitwise_and(rect, circle) 
cv.imshow("AND", bitwise_and)

# bitwise OR
# perform bitwise OR for ON and OFF pixels
bitwise_or = cv.bitwise_or(rect, circle)
cv.imshow("OR", bitwise_or)

# bitwise XOR
# perform bitwise OR for ON and OFF pixels
bitwise_xor = cv.bitwise_xor(rect, circle)
cv.imshow("XOR", bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(rect)
cv.imshow("NOT", bitwise_not)


cv.waitKey(0)