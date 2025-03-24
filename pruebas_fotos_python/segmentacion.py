import os
import numpy as np
from skimage import io
from skimage.color import rgb2grey
from skimage.color import rgb2hsv
from PIL import Image, ImageOps

# se cargan las imagenes
fondo=io.imread("foto_fondo.jpg")
img=io.imread("foto_1.jpg")

#se convierte al modelo hsv
# img = rgb2hsv(img)
# fondo = rgb2hsv(fondo)

#se convierte a esccala de grises
img = rgb2grey(img)
fondo = rgb2grey(fondo)

#se obtiene el tamaño de las imagenes 
n = fondo.shape
print(n)
n=img.shape
print(n)
imgc=np.zeros(n)
# imgc=np.zeros((126,250))

# i=0
# j=0
#se recorre la imagen y se segmenta de acuerdo al umbral deseado
for x in range(n[0]):
	# j=0
	for y in range(n[1]):
		if img[x][y]- fondo[x][y] <= 0.15:
		# if img[x][y][0]- fondo[x][y][0] >= 0.023:
			imgc[x][y] = 0
		else:
			imgc[x][y] = 1

	# 	j=j+1
	# i=i+1


#se muestra la imagen segmentada
io.imshow(imgc)
io.show()