from stitchImages import stitchImages
from PIL import Image
import cv2
from cv2 import warpAffine
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

baseImage = 'robot_1.png'
imagesToStitch = ['robot_2.png']

points1_img1 = [[344,117],[379,169],[467,90]]
points1_img2 = [[148,2],[157,52],[249,22]]
points2_img1 = [[362,283],[338,307],[397,284]]
points2_img3 = [[53,55],[15,115],[118,39]]

origin = [0,0]

# [ points1_img1, points1_img2;
#   points2_img1, points2_img3]
# 2 column array

points = [[points1_img1, points1_img2], [points2_img1, points2_img3]]

#Not done
def stitchMultipleImages(baseImage, imagesToStitch, points, origin):
        baseImage = Image.open(baseImage)
        stitchingContainer = Image.new("RGBA", (1000,1000), (0,0,0,255))
        for i in imagesToStitch:
               stitchImages(baseImage, Image.open(imagesToStitch(i)), points[i][0], points[i][1], origin, stitchingContainer)
                
        stitchingContainer.show()

        