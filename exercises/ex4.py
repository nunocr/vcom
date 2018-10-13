import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("pic2.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("image", image)
cv2.imshow("hsv", hsv)

# a)

# cv2 histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.plot(hist, color='b')
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# b)

