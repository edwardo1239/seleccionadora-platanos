from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2grey
from skimage.morphology import disk
from skimage.filters.rank import minimum
from skimage.util import img_as_ubyte
from skimage.filters.rank import maximum

#img=io.imread("platano_reducido_2.jpg")
img=io.imread("170.jpg")
fondo=io.imread("fondo_REDUCIDO.jpg")

img=img_as_ubyte(img)
fondo=img_as_ubyte(fondo)

n=img.shape
s=np.zeros(n)
print(img.shape)
print(fondo.shape)
print(s.shape)

for z in range(n[2]):
    for x in range(n[0]):
        for y in range(n[1]):
            s[x][y][z]=img[x][y][z]- fondo[y][x][z]

print(s.shape)
io.imshow(s*255)
io.show()
            
