import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage.color import rgb2hsv
from skimage import io



img = io.imread("2.jpg")
fondo = io.imread("fondo.jpg")

hsv_img = rgb2hsv(img)
hsv_fondo = rgb2hsv(fondo)

print(hsv_img[200][200][0])
n = hsv_img.shape
s=np.zeros(n)
imgc=np.zeros((126,250))

i=0
j=0
for x in range(122, n[0]-152,1):
	j=0
	for y in range(50, n[1]-100,1):
		s[x][y]=hsv_img[x][y] / hsv_fondo[x][y]

		if (s[x][y][0] >= 0.36) :
			imgc[i][j] = 0
		else:
			imgc[i][j] = 1

		j=j+1
	i=i+1
io.imshow(imgc)
io.show()
