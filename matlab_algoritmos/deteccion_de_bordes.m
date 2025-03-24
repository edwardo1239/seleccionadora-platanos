clear all
close all
clc
tic
%A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\platano-tropical.jpg');

% A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\fotos_platanos_pi\fotos_cortadas_3\foto_21.jpg');
A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\fotos_verde_huaweip20\150(2)_reducida.jpg');
%A=imread('C:\Users\EDWAR\Pictures\671171e5-4464-4e19-9457-2daa4eaab5a6.jpg');
%A=rgb2gray(A);
figure
imshow(A);
% 
% H = fspecial('sobel');
% Htrans = H';
% 
% S_horizontal = imfilter(A, H);
% S_vertical = imfilter(A, Htrans);
% 
% S = imadd(S_horizontal, S_vertical);

S = edge(A, 'canny', 0.5);


figure

imshow(S)

[h, theta, rho] = hough(S,'RhoResolution',0.001,'ThetaResolution',0.1);
peaks = houghpeaks(h,6);
lines = houghlines(S, theta, rho, peaks);

figure, imshow(S), hold on
for k=1:length(lines)
    xy = [lines(k).point1 : lines(k).point2];
    plot(xy(:,2), xy(:,1), 'LineWidth', 2, 'Color', [1 0 0]);
end