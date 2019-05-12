from transformationMatrixFromPoints import transformationMatrixFromPoints
from PIL import Image
import cv2
from cv2 import warpAffine
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
'''
points1_img1 = [[344,117],[379,169],[467,90]]
points1_img2 = [[148,2],[157,52],[249,22]]
img1 = Image.open('robot_1.png')
img2 = Image.open('robot_2.png')

points2_img1 = [[362,283],[338,307],[397,284]]
points2_img3 = [[53,55],[15,115],[118,39]]
img3 = Image.open('robot_3.png')
'''
#imageContainer = Image.new("RGBA", (1000,1000), (0,0,0,255))
def stitchImages(image1, image2, points1, points2, origin, imageContainer):
	

	# imagepaste1 = Image.open(image1)
	# imagepaste2 = Image.open(image2)
	# img2 = cv2.imread(image2)
	rows2, cols2 = image2.size

	pts1 = np.float32(points1)
	pts2 = np.float32(points2)

	M = cv2.getAffineTransform(pts2, pts1)

	transformed = cv2.warpAffine(np.asarray(image2),M,(rows2*10, cols2*10))

	imgTransformed = Image.fromarray(transformed)

# transforming image 2 to make image 1, will compare and stitch both together 
	imageContainer.paste(image1, origin) 
	imageContainer.paste(imgTransformed, (0,0), mask=imgTransformed)
	# imageContainer.show()
	return imageContainer
	# Change directory 
	# imageContainer.save("stitched1.bmp")
	# imageContainer.save("C://Users/conni/Desktop/stitched1.bmp")

# TODO: Create function to stitch multiple images together at once

# def stitchMultipleImages(baseImage, imagesToStitch, points, origin=[0,0]):
# 	for image in imagesToStitch:

# 	stitchingContainer = stitchImages(baseImage)

'''
stitch1 = stitchImages(img1, img2, points1_img1, points1_img2, [124,48])
stitch2 = stitchImages(stitch1, img3, points2_img1, points2_img3)
stitch2.show()
'''


	