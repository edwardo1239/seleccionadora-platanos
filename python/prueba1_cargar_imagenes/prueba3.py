from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2grey

image=io.imread("platano_reducido_2.jpg")
# imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1

#print("- Dimensiones de la imagen:")
print(image.shape)
plt.imshow(image)
#print(image)

A =  rgb2grey(image)
io.imshow(A)
io.show()
print(A[0][0])



