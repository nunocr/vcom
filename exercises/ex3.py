import numpy as np
import cv2
import keyboard


'''

# Capture Video from Camera

capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

'''

# Playing Video from File

capture = cv2.VideoCapture('franku.mp4')

while(capture.isOpened()):
    ret, frame = capture.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        re2, image = capture.read()
        cv2.imshow("Captured Frame", image)
        cv2.waitKey(5000)
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()