from algorithm import algorithm
from util import videoCapture
import subprocess as sp

import cv2

print("~ Hand Symbol Recognition Program ~\n")
print("1 - take picture\n")
print("2 - upload file\n")
print("your option: ")

input = int(input())

if input == 1:
    sp.call('clear', shell=True)
    videoCapture()
    image = videoCapture()
    #cv2.imshow("captured image", image)

elif input == 2:
    sp.call('clear', shell=True)
    print("file name: ")
    input = raw_input()
    image = cv2.imread(input)
    #cv2.imshow("uploaded image", image)

else:
     print("invalid option")

cv2.imshow("image", image)
#cv2.waitKey(5000)
algorithm(image)