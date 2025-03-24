clear all
close all
clc
tic
% A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\platano-tropical.jpg');
% A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\450_1000.jpg');
%A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\fotos_verde_huaweip20\150(2)_reducida.jpg');
%A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\platano_fondoblanco\450_reducido.jpg');
%  A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\fotos_platanos_pi\fotos_cortadas_3\foto_27.jpg');
A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\fotos_platanos_pi\21-06\21-06-3\foto_1.jpg');

 %A=rgb2gray(A);


%A = histeq(A);
figure
imshow(A);

S1= A>180 ;
% S2=A(:,:,3)>100;
% S3=A(:,:,2)<120;
% S11= S1 | S3;
% S=imadd(S1,S2);
%S=imadd(S,S3);
figure
imshow(S1);


% [h, theta, rho] = hough(S1,'RhoResolution',1,'ThetaResolution',0.1);
% peaks = houghpeaks(h,6);
% lines = houghlines(S1, theta, rho, peaks);
% 
% figure, imshow(S1'), hold on
% for k=1:length(lines)
%     xy = [lines(k).point1 : lines(k).point2];
%     plot(xy(:,2), xy(:,1), 'LineWidth', 4, 'Color', [1 0 0]);
% end


% u = graythresh(A);
% S= im2bw(A,u);
% figure
% imshow(S)
toc