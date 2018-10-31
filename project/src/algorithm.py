import cv2
import numpy as np
from matplotlib import pyplot as plt

def algorithm(image):

    image = cv2.GaussianBlur(image, (5, 5), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image = cv2.GaussianBlur(image, (5, 5), 0)

    kernel = np.ones((3, 3), np.uint8)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    image = cv2.inRange(image, lower_skin, upper_skin)

    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    plt.plot(histogram, color='b')
    #plt.xlim([0, 256])

    cv2.imshow("post processing image", image)
    plt.show()
    
    cv2.waitKey(5000)