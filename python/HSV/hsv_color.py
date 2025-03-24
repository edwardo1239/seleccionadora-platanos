import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage.color import rgb2hsv
from skimage import io



img = io.imread("2.jpg")

hsv_img = rgb2hsv(img)
hsv_verde = hsv_img
print(hsv_img[200][200][0])
n = hsv_img.shape
imgc=np.zeros(n)

#segmentacion usando solamente el matiz

for x in range(n[0]):
	for y in range(n[0]):
		if hsv_img[x][y][0] <= 0.369:
			imgc[x][y]= 1
		else:
			imgc[x][y]= 0
			
	
io.imshow(imgc)
io.show()
