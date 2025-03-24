from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2grey

img=io.imread("foto_1.jpg")
fondo=io.imread("foto_fondo.jpg")

img =  rgb2grey(img)
fondo =  rgb2grey(fondo)

n=img.shape
s=np.zeros(n)
print(img.shape)
print(fondo.shape)
print(s.shape)
for x in range(n[0]):
    for y in range(n[1]):
        s[x][y]=img[x][y]- fondo[y][x]
        if s[x][y]*255 <= 30:
            s[x][y]=0
        else:
            s[x][y]=255

s=s*255
print(s)
io.imshow(s)
io.show()

