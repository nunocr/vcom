import cv2
import numpy as np
import random

image = cv2.imread("clouds.jpg")

saltnpeppa = zeros(len(image[0]), len(image[1]), dtype=numpy.uint8)
# saltnpeppa = [[0 for x in range(len(image[0]))] for y in range(len(image[1]))]

cv2.randu(saltnpeppa, 0, 255)

for col in range(len(saltnpeppa[0])):
    for row in range(len(saltnpeppa[1])):
        if saltnpeppa[col][row] < 29:
            image[col][row] = 0
        elif saltnpeppa[col][row] > 226:
            image[col][row] = 255
        
cv2.imshow("Salt n Peppa", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

