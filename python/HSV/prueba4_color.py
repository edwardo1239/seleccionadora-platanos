from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2grey
from skimage.morphology import disk
from skimage.filters.rank import minimum
from skimage.util import img_as_ubyte
from skimage.filters.rank import maximum

imgc=io.imread("platano_reducido_2.jpg")
#imgc=io.imread("170.jpg")
fondo=io.imread("fondo_REDUCIDO.jpg")

img =  rgb2grey(imgc)
fondo =  rgb2grey(fondo)

n=img.shape
s=np.zeros(n)
vecr=np.zeros(1)
vecg=np.zeros(1)
veca=np.zeros(1)
i=0
#print(img.shape)
#print(fondo.shape)
#print(s.shape)
for x in range(n[0]):
    for y in range(n[1]):
        s[x][y]=img[x][y]- fondo[y][x]
        if s[x][y]*255 <=30:
            s[x][y]=0
        else:
            s[x][y]=1
   


#print(imgc[2][229][1])
s=img_as_ubyte(s)
s = minimum(s,disk(2))
s = maximum(s,disk(7))
#print(s)
for x in range(10 , n[0]-10):
    for y in range(10, n[1]-10):
        if s[x][y] == 255:
            vecr = np.append(vecr, imgc[x][y][0])
            vecg = np.append(vecg, imgc[x][y][1])
            veca = np.append(veca, imgc[x][y][2])

sumr= 0
sumg= 0
suma= 0
print(len(vecr))
for x in range(len(vecr)):
    sumr= sumr+vecr[x]
    sumg= sumg+vecg[x]
    suma= suma+veca[x]
print(sumr)
print(sumg)
print(suma)
io.imshow(s)
io.show()

