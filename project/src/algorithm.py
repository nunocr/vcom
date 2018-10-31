import cv2
import numpy as np

def algorithm(image):

    # convert to grayscale

    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # convert to hsv

    # image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    '''
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        kernel = np.ones((5,5), np.uint8)

        # erode the shit out of it

        erosion = cv2.erode(image, kernel, iterations = 1)
        cv2.imshow("eroded", erosion)
        cv2.waitKey(5000)

        # dilate the shit out of it

        dilation = cv2.dilate(image, kernel, iterations = 1)
        cv2.imshow("dilated", image)
        cv2.waitKey(5000)
    '''

    # image = cv2.pyrDown(image)
    image = cv2.GaussianBlur(image, (5, 5), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow("pyrDown", image)
    cv2.waitKey(5000)