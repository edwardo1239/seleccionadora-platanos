import os
import numpy as np
from skimage import io
from skimage.color import rgb2grey
from PIL import Image, ImageOps

path = "C:/Users/EDWAR/Documents/u/proyecto_de_grado/fotos_platano/fotodpi2/20-07"
fondo=io.imread("C:/Users/EDWAR/Documents/u/proyecto_de_grado/fotos_platano/fotodpi2/20-07/fondo.jpg")
fondo=rgb2grey(fondo)
n = fondo.shape
s=np.zeros(n)
for i in  os.listdir(path):
	path2=("C:/Users/EDWAR/Documents/u/proyecto_de_grado/fotos_platano/fotodpi2/binarizadas/20-07/" + i)
	img=io.imread(path + "/" + i)
	print(path + "/" + i)
	img =  rgb2grey(img)
	n=img.shape
	imgc=np.zeros((126,250))
	# imgc=np.zeros((75,150))

	i=0
	j=0
	for x in range(122, n[0]-152,1):
		j=0
		for y in range(50, n[1]-100,1):
			s[x][y]=img[x][y]- fondo[x][y]

			if s[x][y] <= 0.117:
				imgc[i][j] = 0
			else:
				imgc[i][j] = 1

			j=j+1
		i=i+1

	io.imsave(path2, imgc)

io.imshow(imgc)
io.show()