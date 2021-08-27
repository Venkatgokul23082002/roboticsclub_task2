
####################### IMPORT MODULES #######################
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
##############################################################


# Global variable for details of shapes found in image and will be put in this dictionary, returned from scan_image function
shapes = {}


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################


##############################################################


def scan_image(img_file_path):
    """
    Purpose:
    ---
    this function takes file path of an image as an argument and returns dictionary
    containing details of colored (non-white) shapes in that image

    Input Arguments:
    ---
    `img_file_path` :		[ str ]
        file path of image

    Returns:
    ---
    `shapes` :              [ dictionary ]
        details of colored (non-white) shapes present in image at img_file_path
        { 'Shape' : ['color', Area, cX, cY] }

    Example call:
    ---
    shapes = scan_image(img_file_path)
    """

    global shapes

    ##############	ADD YOUR CODE HERE	##############
import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow
shapes={}
img = cv2.imread('./Sample2.png')
image = cv2.resize(img, (700, 600))
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
glower = np.array([50, 100, 100])
gupper = np.array([70, 255, 255])
rlower = np.array([0, 50, 50])
rupper = np.array([10, 255, 255])
blower = np.array([110, 50, 50])
bupper = np.array([130, 255, 255])
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
blue_mask=cv2.inRange(hsv, blower, bupper)
red_mask=cv2.inRange(hsv, rlower, rupper)
green_mask=cv2.inRange(hsv, glower, gupper)
contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

colour="red"
_,threshold = cv2.threshold(red_mask, 0, 255, cv2.THRESH_BINARY)
contours,_=cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
i=0
for cnt in contours:
    
   cv2.drawContours(img,[cnt],0,(0),5)
   approx=cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
   if(len(approx)==3):
     shape="triangle"
   elif(len(approx)==4):
     shape="quadrilateral"
   elif(len(approx)==5):
     shape="pentagon"
   elif(len(approx)==6):
     shape="hexagon"
   else:
     shape="circle"
   M = cv2.moments(cnt)
   cX = int(M['m10'] / M['m00'])
   cY = int(M['m01'] / M['m00'])
   area = cv2.contourArea(cnt)
   shapes[shape]=[colour,area,cX,cY]
contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

colour="green"
_,threshold = cv2.threshold(green_mask, 0, 255, cv2.THRESH_BINARY)
contours,_=cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
i=0
for cnt in contours:
  
   cv2.drawContours(img,[cnt],0,(0),5)
   approx=cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
   if(len(approx)==3):
     shape="triangle"
   elif(len(approx)==4):
     shape="quadrilateral"
   elif(len(approx)==5):
     shape="pentagon"
   elif(len(approx)==6):
     shape="hexagon"
   else:
     shape="circle"
   M = cv2.moments(cnt)
   cX = int(M['m10'] / M['m00'])
   cY = int(M['m01'] / M['m00'])
   area = cv2.contourArea(cnt)
   shapes[shape]=[colour,area,cX,cY]
contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

colour="blue"
_,threshold = cv2.threshold(blue_mask, 0, 255, cv2.THRESH_BINARY)
contours,_=cv2.findContours(threshold, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
i=0
for cnt in contours:
   
   cv2.drawContours(img,[cnt],0,(0),5)
   approx=cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
   if(len(approx)==3):
     shape="triangle"
   elif(len(approx)==4):
     shape="quadrilateral"
   elif(len(approx)==5):
     shape="pentagon"
   elif(len(approx)==6):
     shape="hexagon"
   else:
     shape="circle"
   M = cv2.moments(cnt)
   cX = int(M['m10'] / M['m00'])
   cY = int(M['m01'] / M['m00'])
   area = cv2.contourArea(cnt)
   shapes[shape]=[colour,area,cX,cY]
print(sorted(shapes.items(),key=lambda x:x[1][2], reverse=True))
    ##################################################

    return shapes


##################################################
if __name__ == '__main__':

    curr_dir_path = os.getcwd()
    print('Currently working in ' + curr_dir_path)

    # path directory of images in 'Samples' folder
    img_dir_path = curr_dir_path + '/Samples/'

    # path to 'Sample1.png' image file
    # change the path when running with a new image
    img_file_path = img_dir_path + 'Sample1' + '.png'
    print('============================================')
    shapes = scan_image(img_file_path)
    if type(shapes) is dict:
        print(shapes)
        print('\nOutput generated. Please verify.')
    else:
        print('\n[ERROR] scan_image function returned a ' +
              str(type(shapes)) + ' instead of a dictionary.\n')
        exit()
