from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2grey
from skimage.morphology import disk
from skimage.filters.rank import minimum
from skimage.util import img_as_ubyte
from skimage.filters.rank import maximum
from time import time

def leer_imagen():
    imgc=io.imread("platano_reducido_2.jpg")
    # imgc=io.imread("170.jpg")
   
    return imgc
def leer_fondo(): 
    fondo=io.imread("fondo_REDUCIDO.jpg")
    return fondo
def segmentar(img, fondo):
    n=img.shape
    s=np.zeros(n)
    vecr=np.zeros(1)
    vecg=np.zeros(1)
    i=0
    for x in range(200 , n[0]-200, 2):
        for y in range(50, n[1]-50):
            s[x][y]=img[x][y]- fondo[y][x]
            if s[x][y] <= 0.117:
                pass
            else:
                vecr = np.append(vecr, imgc[x][y][0])
                vecg = np.append(vecg, imgc[x][y][1])
    return vecr, vecg

def Suma_rojo(vecr):
    sumr = np.sum(vecr)
    return sumr 
def Suma_verde(vecg):
    sumg = np.sum(vecg)
    return sumg 

def umbral(sumr, sumg):
    if sumr >= (sumg-1000):
       print('maduro')
    else:
        print('verde')
    

#tiempo_i=time()
imgc=leer_imagen()
fondo=leer_fondo()
#print(imgc.shape)
img =  rgb2grey(imgc)
fondo =  rgb2grey(fondo)

vecr, vecg=segmentar(img, fondo)



sumr=Suma_rojo(vecr)
sumg=Suma_verde(vecg)

umbral(sumr, sumg)

#tiempo_f=time()
#tiempo=tiempo_f- tiempo_i
#print ('El tiempo de ejecucion fue:',tiempo)
#print(s)

io.imshow(s)
io.show()


