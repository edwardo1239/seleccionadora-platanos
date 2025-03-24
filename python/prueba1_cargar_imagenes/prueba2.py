from PIL import Image
import numpy as np

img = Image.open("platano_reducido_2.jpg")
imagenbn = img.convert("L")
imagenbn.show()
imga = imagenbn.array
