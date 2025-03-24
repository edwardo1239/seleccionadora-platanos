clear all
close all
clc
tic
%A=imread('C:\Users\EDWAR\Pictures\142.JPG');
 A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\platano-tropical.jpg');
 %A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\fotos_verde_huaweip20\150(2)_reducida.jpg');
A1=rgb2gray(A);
BW = edge(A1,'canny');

[H,T,R] = hough(BW,'RhoResolution',1,'ThetaResolution',1);
picos = houghpeaks(H, 10);
lineas = houghlines(BW, T, R, picos);

figure, imshow(BW'), hold on
for j=1 : length(lineas)
    
    xy = [lineas(j) .point1 ; lineas(j) .point2];
    plot(xy(:,2), xy(:,1), 'Linewidt',4,'color',[1 0 0]);
end

toc