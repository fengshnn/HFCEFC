clear all;
clc;
close all;

% %%% ---  健康者---- EF=71%
% BCGsignal1= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG79.txt'); %滤波后的BCG
% Breathsignal1=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH79.txt');  %滤波后的呼吸
% Signsignal1 = load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign79.txt'); %原始信号
% figure(1)
% plot(BCGsignal1(:,2))


% %%% --- 心衰者----  EF=46%
BCGsignal1= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG33.txt'); %滤波后的BCG
% Breathsignal1=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH33.txt');  %滤波后的呼吸
% Signsignal1 = load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign33.txt'); %原始信号
% 
% figure(1)
% plot(Signsignal1(:,2))
figure(2)
plot(BCGsignal1(:,9))
% figure(3)
% plot(Breathsignal1(:,2))



% %%% --- 心衰者----  EF=30%
% BCGsignal1= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG11.txt'); %滤波后的BCG
% Breathsignal1=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH11.txt');  %滤波后的呼吸
% Signsignal1 = load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign11.txt'); %原始信号

% figure(1)
% plot(Signsignal1(:,9))
% figure(2)
% plot(BCGsignal1(:,9))
% figure(3)
% plot(Breathsignal1(:,9))
