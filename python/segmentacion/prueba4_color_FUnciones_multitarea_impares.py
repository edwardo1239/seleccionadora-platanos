from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Pool
from skimage.color import rgb2grey
from skimage.morphology import disk
from skimage.filters.rank import minimum
from skimage.util import img_as_ubyte
from skimage.filters.rank import maximum
from time import time

def leer_imagen():
    imgc=io.imread("platano_reducido_2.jpg")
    #imgc=io.imread("170.jpg")
   
    return imgc

def leer_fondo(): 
    fondo=io.imread("fondo_REDUCIDO.jpg")
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
    n=s.shape
    for x in range(10 , n[0]-10):
        for y in range(10, n[1]-10):
            if s[x][y] == 255:
                vecr = np.append(vecr, imgc[x][y][0])
              
    return vecr
def aplicar_filtro_verde(s):
    vecg=np.zeros(1)
    n=s.shape
    for x in range(10 , n[0]-10):
        for y in range(10, n[1]-10):
            if s[x][y] == 255:
            
                vecg = np.append(vecg, imgc[x][y][1])
                
    return vecg
def aplicar_filtro_azul(s):
    vecb=np.zeros(1)
    n=s.shape
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


tiempo_i=time()
imgc=leer_imagen()

if __name__ == '__main__':

    
    fondo=leer_fondo()

    img =  rgb2grey(imgc)
    fondo =  rgb2grey(fondo)

    s=segmentar(img, fondo)

    n=img.shape
    s=img_as_ubyte(s)
    s = minimum(s,disk(2))
    s = maximum(s,disk(7))

    p = Pool(processes=3)
    vecr=p.map(aplicar_filtro_rojo, [s])
    vecg=p.map(aplicar_filtro_verde, [s])
    vecb=p.map(aplicar_filtro_azul, [s])
    p.close()

    p = Pool(processes=3)
    sumr=p.map(Suma_rojo, [vecr])
    sumg=p.map(Suma_verde, [vecg])
    sumb=p.map(Suma_azul, [vecb])
   
    p.close()
    print(sumr)
    print(sumg)
    print(sumb)
#sumr= threading.Thread(target=Suma_rojo(vecr))
#sumr= threading.Thread(target=Suma_rojo, args=(vecr))
#sumg=Suma_verde(vecg)
#sumg= threading.Thread(target=Suma_verde, args=(vecg))
#sumb=Suma_azul(vecb)

    
    #io.imshow(s)
    #io.show()
tiempo_f=time()
tiempo=tiempo_f- tiempo_i
print ('El tiempo de ejecucion fue:',tiempo)
