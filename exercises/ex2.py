import cv2
import numpy as np
import random


# ex 2

image = cv2.imread("clouds.jpg")

# a) fuck this

height, width = 100, 200
blank_image = np.zeros((height, width, 3), np.uint8)
# cv2.imshow("Blank", blank_image)

# b) fuck this

# c) fuck this

# d) also fuck this

im_width, im_height, im_channels = image.shape
im_size = im_width * im_height
noise_perc = im_size * 0.1

while noise_perc > 0:
    for col in range(im_width):
        for row in range(im_height):
            if random.randint(0, 2) == 1:                            # fill with noise
                if random.randint(0, 2) == 0: 
                    image[row:col, row:col] = (0, 0, 0)              # black
                else:               
                    image[row:col, row:col] = (255, 255, 255)        # white
                noise_perc -= 1

cv2.imshow("Salt n Peppa", image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Clouds", gray_image)

# f)

# cv2.imshow("RGB Clouds", image)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow("HSV Clouds", hsv_image)

h, s, v = cv2.split(hsv_image)

# cv2.imshow("H channel", h)
# cv2.imshow("S channel", s)
# cv2.imshow("V channel", v)

s.fill(42)

hsv_image2 = cv2.merge([h, s, v])

# cv2.imshow("New HSV Image", hsv_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()