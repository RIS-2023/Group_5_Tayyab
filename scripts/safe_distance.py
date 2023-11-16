#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from imutils import paths
import numpy as np
import imutils
import cv2

#Calibration step
FOCAL_LENGTH = 190


def find_marker(image):
	# convert the image to grayscale, blur it, and detect edges
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv2.contourArea)
	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)

# function to get distance from object to camera
def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth

def manipulate(data):
    np_arr = np.fromstring(data.data, np.uint8)
    # converting image to a numpy array
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    # getting (x, y)-coordinates and width and height of the duckiebot (in pixels)
    marker = find_marker(image_np)
    # computing actual distance using precomputed focal length
    actual_distance = distance_to_camera(14, FOCAL_LENGTH, marker[1][0])

    if actual_distance < 5:
        print("Safe distance boundary exceeded by:" + 5-actual_distance)
    else:
        rospy.loginfo(rospy.get_caller_id() + "Current Distance to object: %s", actual_distance)




def callback(data):
    manipulate(data)

def listener():
    # run simultaneously.
    rospy.init_node('security', anonymous=True)

    rospy.Subscriber("/duckduckgopls/camera_node/image/compressed", CompressedImage, callback)

    # spin() keeps in a loop to avoid quiting
    rospy.spin()

if __name__ == '__main__':
    listener()



