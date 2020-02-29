import numpy as np
import cv2

#def readImage():
import glob
path = "/Users/lfxjtu/OneDrive - Whitireia and WelTec/SSD/left_barriers/"
image_name_pre = "img_"
image_name_post = "_c0.pgm"
image_name_middle = ""

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
str1 = []
path_name = 'cars.txt'
#clone = null


def write_to_file(x_top, y_top, x_bottom, y_bottom):
    # Writes the mouse coordinates to a text file
    # open the mouse coordinates
    with open(path_name, 'a') as file:
        # create a string ready to write to the file
        coordinates = str(x_top) + ',' + str(y_top) + ',' + str(x_bottom) + ',' + str(y_bottom) + ':'

        # write to file
        file.write(coordinates) # append at the end of the file (not over write)




def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping, bottomPoint, drawing

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
       # if drawing is False:
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            bottomPoint = [(x, y)]
            tempImage = clone.copy()
            cv2.imshow("image", tempImage)
            cv2.rectangle(tempImage, refPt[0], bottomPoint[0], (0, 255, 0), 2)
            cv2.imshow("image", tempImage)
            #cv2.waitKey()

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False

        # draw a rectangle around the region of interest
        tempImage = clone.copy()
        cv2.rectangle(tempImage, refPt[0], refPt[1], (0, 255, 0), 2)
        print(refPt[0][0], refPt[0][1], refPt[1][0], refPt[1][1])
        # str1.append(refPt)
        cv2.imshow("image", tempImage)
        write_to_file(refPt[0][0], refPt[0][1], refPt[1][0], refPt[1][1])#top left and bottom right x, y
        print ("coordinate saved to file")

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
drawing = False
for i in range(400):
    i = i+1
    print (str(i))
    if i < 10:
        image_name_middle = "000" + str(i)
    elif i < 100:
        image_name_middle = "00" + str(i)
    else:
        image_name_middle = "0" + str(i)
    image_name = image_name_pre + image_name_middle + image_name_post

    print ("loading an image named " + image_name)
    print (image_name)
    input_image = cv2.imread(image_name)

    print ("Computing histogram equalization.")
    #Histogram equalizaiton using gray scale image. The image loaded is in RGB
    img_to_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    img_to_gray = cv2.equalizeHist(img_to_gray)
    clone = cv2.cvtColor(img_to_gray, cv2.COLOR_GRAY2BGR)
    #image = clone.copy() #copy function allocates the content of clone to a new memory location and assigns it to image
    cv2.imshow("image", clone)
    key = cv2.waitKey() & 0xFF
    print (str(key))

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        current_image = clone.copy()

    # if the 'n' key is pressed, load the next image
    elif key == ord("n"):
        with open(path_name, 'a') as f:
            f.write('\n')
        continue


#image = cv2.imread('img_0001_c0.pgm')
