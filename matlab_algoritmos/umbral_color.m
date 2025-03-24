clear all
close all
clc
tic
% A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\fotos_platano_negro\reducidas\210.jpg');
A=imread('C:\Users\EDWAR\Documents\u\proyecto_de_grado\fotos_platano\fotos_platanos_pi\21-06\21-06-1\foto_10.jpg');

figure
imshow(A);
A = rgb2hsv(A);
S1= A(:,:,1)<0.5 ;
S1= A(:,:,1)>130 ;
S2=A(:,:,2)<0.2;
S3=A(:,:,3)>0.2;
figure
imshow(S1);
figure
imshow(S2);
figure
imshow(S3);


% SS= bwareaopen(SS,10);

% figure
% imshow(SS);

% SS1= imfill(SS,'holes');

% figure
% imshow(SS1);

% total=sum(sum(SS1))
