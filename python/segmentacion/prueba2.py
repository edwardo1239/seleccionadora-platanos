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
            s[x][y]=1


print(s)
s=img_as_ubyte(s)
s = minimum(s,disk(1))
s = maximum(s,disk(7))
print(s)


io.imshow(s)
io.show()

