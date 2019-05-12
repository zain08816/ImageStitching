import cv2
import numpy as np
from PIL import Image

imageContainer = Image.new("RGBA", (500,500), (0,0,0,0))

img = cv2.imread('broccoli_house_1.png')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

imageContainer.paste(Image.fromarray(dst), (0,0))
imageContainer.show()