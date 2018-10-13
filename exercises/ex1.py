import cv2
import numpy as np
import argparse

image = cv2.imread("clouds.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Over the Clouds", image)
# cv2.imshow("Over the Clouds - gray", gray_image)

#----------------------------------- ex 1---------------------------

# a)


width, height, channels = image.shape

print("Image Dimensions")
print("Width: %d" % width)
print("Height: %d" % height)
print("Channels: %d" % channels)


# cv2.destroyAllWindows()

# b)

# cv2.imwrite('clouds.bmp', image)

# c)

refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False

        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        image = clone.copy()

    elif key == ord("c"):
        break

if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)

    cv2.imwrite('roi.jpg', roi)

# cv2.waitKey(5000)
cv2.destroyAllWindows()

