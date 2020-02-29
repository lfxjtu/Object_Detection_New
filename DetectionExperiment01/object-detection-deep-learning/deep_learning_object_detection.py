# USAGE
# python deep_learning_object_detection.py --image images/example_01.jpg \
#	--prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

# import the necessary packages
import numpy as np
import argparse
import cv2

path = "/Users/lfxjtu/OneDrive - Whitireia and WelTec/SSD/left_barriers/"
defaultOutputPath = "/Users/lfxjtu/OneDrive - Whitireia and WelTec/SSD/left_barriers/defaultDetections/"
image_name_pre = "img_"
image_name_post = "_c0.pgm"
image_name_post_output = "_c0.png"
image_name_middle = ""
test_confidence = 0.5

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#                help="path to input image")
# ap.add_argument("-p", "--prototxt", required=True,
#                help="path to Caffe 'deploy' prototxt file")
# ap.add_argument("-m", "--model", required=True,
#                help="path to Caffe pre-trained model")
# ap.add_argument("-c", "--confidence", type=float, default=0.2,
#                help="minimum probability to filter weak detections")

# args = vars(ap.parse_args())

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
#net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")

for j in range(1, 401):
    image_name_middle = str(j).zfill(4)
    image_name = image_name_pre + image_name_middle + image_name_post
    image_name_output = image_name_pre + image_name_middle + image_name_post_output
    print ("loading an image named " + image_name)
    image = cv2.imread(path + image_name)
    # load the input image and construct an input blob for the image
    # by resizing to a fixed 300x300 pixels and then normalizing it
    # (note: normalization is done via the authors of the MobileNet SSD
    # implementation)
    #image_path = "images/example_03.jpg"
    #image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

    # pass the blob through the network and obtain the detections and
    # predictions
    print("[INFO] computing object detections...")
    net.setInput(blob)
    detections = net.forward()


    # loop over the detections
    for i in np.arange(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence

        if confidence > test_confidence:
            # extract the index of the class label from the `detections`,
            # then compute the (x, y)-coordinates of the bounding box for
            # the object
            idx = int(detections[0, 0, i, 1])
            # identify when detection is a car and wait for key then
            if idx == 7:
                cv2.waitKey(0)
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # display the prediction
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            print("[INFO] {}".format(label))
            cv2.rectangle(image, (startX, startY), (endX, endY),
                          COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

    # show the output image
    cv2.imshow("Output", image)
    print("Writing to: " + defaultOutputPath + image_name_output)
    cv2.imwrite(defaultOutputPath + image_name_output, image)
    cv2.waitKey(20)
