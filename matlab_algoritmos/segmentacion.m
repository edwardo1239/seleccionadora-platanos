clear all
close all
clc
tic
 %A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\platano-tropical.jpg');
%A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\450_1000.jpg');
A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\caja_negra\270.jpg');

m1=[1 0 ; 0 -1]
m2=[-1 0 1 ;  -1 0 1; -1 0 1]
m3=[-1 -1 -1 ; -1 9 -1 ; -1 -1 -1]
A=rgb2gray(A);
figure
imshow(A);
A = histeq(A);
figure
imshow(A);
% histogram(A)

A=double(A);

% S1=aplicar_mascara(A,m3);
% S1=S1/10;
% S1=uint8(S1);
% figure
% imshow(S1)

% S1=double(S1);
S1=aplicar_mascara(A,m3);
S1=S1/9;
S1=uint8(S1);
figure
imshow(S1)
u= 40;
S2= binarizacion(S1,u);
 
% x=size(A);
% A(:,:,1)=0;
% A(:,:,3)=0;
% for i=1:1:x(1)
%     for j=1:1:x(2)
%         if (A(i,j,2)<=200)
%             A(i,j,2)=0;
%             
%             
%             
%         end
%          
%     end
% end
figure
imshow(S2)
%imshow(S2)
toc