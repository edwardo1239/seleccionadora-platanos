clear all
close all
clc
tic
A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\python\prueba1_cargar_imagenes\platano_reducido_2.jpg');
F=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fondo_REDUCIDO.jpg');

A=rgb2gray(A);
F=rgb2gray(F);

n=size(A);

for x=1:n(1)
    for y=1:n(2)
        C(x,y)=A(x,y)-F(x,y);
    end
end
    
for x=1:n(1)
    for y=1:n(2)
        C(x,y)=C(x,y)- 10;
    end
end
    

C=C*255;
figure
imshow(C);