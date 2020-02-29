import numpy as np
import cv2

#def readImage():
import glob
path = "/Users/lfxjtu/OneDrive - Whitireia and WelTec/SSD/left_barriers/"
image_name_pre = "img_"
image_name_post = "_c0.pgm"
image_name_middle = ""

for i in range(400):
    i = i+1
    if i < 10:
        image_name_middle = "000" + str(i)
    elif i < 100:
        image_name_middle = "00" + str(i)
    else:
        image_name_middle = "0" + str(i)
    image_name = image_name_pre + image_name_middle + image_name_post

    print ("loading an image named " + image_name)
    print (image_name)
    image = cv2.imread(image_name)
    print (image.size)
    cv2.imshow('Color image', image)
    # wait for 3 second
    k = cv2.waitKey()

    # destroy the window
    cv2.destroyAllWindows()

#image = cv2.imread('img_0001_c0.pgm')
