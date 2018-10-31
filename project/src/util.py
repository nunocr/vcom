import cv2
import numpy as np

def videoCapture():

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("taking picture")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("taking picture", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            return frame
    cam.release()