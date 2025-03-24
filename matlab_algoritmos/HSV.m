 img=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\python\HSV\2.jpg');
 fondo=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\python\HSV\2.jpg');
 
 hsv_img = rgb2hsv(img);
 hsv_fondo = rgb2hsv(fondo);
 
 platano = hsv_img - hsv_fondo;
 figure
 imshow(platano)