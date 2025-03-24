clear all
close all
clc
tic
%A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\platano-tropical.jpg');
%A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\450_1000.jpg');
A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\caja_negra\270.jpg');

A=rgb2gray(A);
figure
imshow(A);

A = histeq(A);

 H = fspecial ('prewitt');
 S = imfilter (A, H);
 
figure
imshow(S);
toc