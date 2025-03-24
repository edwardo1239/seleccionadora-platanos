import os
import numpy as np
from skimage import io
from skimage.color import rgb2grey

def segmentar(img, fondo):
	n=img.shape
	s = img - fondo
	vecr=np.zeros(1)
	vecg=np.zeros(1)
	for x in range(200, n[0]-150, 2):
		for y in range(100, n[1]-100,2):
			if s[x][y] <= 0.117:
				pass
			else:
				vecr = np.append(vecr, imgc[x][y][0])
				vecg = np.append(vecg, imgc[x][y][1])

	return vecr, vecg

def Suma(vec):
	sumrg = np.sum(vec)
	return sumrg 


def umbral(sumr, sumg):
    if sumr >= (sumg-1000):
       x = "maduro"
    else:
        x = "verde"
    return x

path = "21-06/21-06-5"
fondo = io.imread("foto_fondo.jpg")
f = open("datos_21-06-5.txt",'w')

for i in  os.listdir(path):
	imgc=io.imread(path + "/" + i)
	print(path + "/" + i)

	img =  rgb2grey(imgc)
	fondo =  rgb2grey(fondo)

	vecr, vecg = segmentar(img, fondo)

	sumr= Suma(vecr)
	sumg = Suma(vecg)

	
	r = umbral(sumr, sumg)

	
	f.write("{}   rojo:{}  verde:{} resultado: {}".format(i, sumr, sumg, r))
	f.write("\n")

f.close()

	

	
