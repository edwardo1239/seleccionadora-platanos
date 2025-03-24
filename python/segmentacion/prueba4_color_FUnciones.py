from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2grey
from skimage.morphology import disk
from skimage.filters.rank import minimum
from skimage.util import img_as_ubyte
from skimage.filters.rank import maximum


def leer_imagen():
    imgc=io.imread("C:/Users/EDWAR/Documents/u/proyecto_de_grado/fotos_platano/fotos_platanos_pi/21-06/21-06-1/foto_26.jpg")
    #imgc=io.imread("170.jpg")
   
    return imgc

def leer_fondo(): 
    fondo=io.imread("C:/Users/EDWAR/Documents/u/proyecto_de_grado/fotos_platano/fotos_platanos_pi/21-06/21-06-1/foto_fondo.jpg")
    return fondo

def segmentar(img, fondo):
    n=img.shape
    s=np.zeros(n)
    i=0
    for x in range(n[0]):
        for y in range(n[1]):
            s[x][y]=img[x][y]- fondo[y][x]
            if s[x][y]*255 <=30:
                s[x][y]=0
            else:
                s[x][y]=1
    return s

def aplicar_filtro_rojo(s):
    vecr=np.zeros(1)
    for x in range(10 , n[0]-10):
        for y in range(10, n[1]-10):
            if s[x][y] == 255:
                vecr = np.append(vecr, imgc[x][y][0])
              
    return vecr
def aplicar_filtro_verde(s):
    vecg=np.zeros(1)
    for x in range(10 , n[0]-10):
        for y in range(10, n[1]-10):
            if s[x][y] == 255:
            
                vecg = np.append(vecg, imgc[x][y][1])
                
    return vecg
def aplicar_filtro_azul(s):
    vecb=np.zeros(1)
    for x in range(10 , n[0]-10):
        for y in range(10, n[1]-10):
            if s[x][y] == 255:
            
                vecb = np.append(vecb, imgc[x][y][2])
                
    return vecb

def Suma_rojo(vecr):
    sumr= 0
    for x in range(len(vecr)):
        sumr= sumr+vecr[x]
    return sumr
def Suma_verde(vecg):
    sumg= 0
    for x in range(len(vecg)):
        sumg= sumg+vecg[x]
    return sumg
def Suma_azul(vecb):
    sumb= 0
    for x in range(len(vecb)):
        sumb= sumb+vecb[x]
    return sumb



imgc=leer_imagen()
fondo=leer_fondo()

img =  rgb2grey(imgc)
fondo =  rgb2grey(fondo)

s=segmentar(img, fondo)

n=img.shape
s=img_as_ubyte(s)
s = minimum(s,disk(2))
s = maximum(s,disk(7))

vecr=aplicar_filtro_rojo(s)
vecg=aplicar_filtro_verde(s)
vecb=aplicar_filtro_azul(s)

sumr=Suma_rojo(vecr)
sumg=Suma_verde(vecg)
sumb=Suma_azul(vecb)

print(sumr)
print(sumg)
print(sumb)
io.imshow(s)
io.show()

print ('El tiempo de ejecucion fue:',tiempo)
