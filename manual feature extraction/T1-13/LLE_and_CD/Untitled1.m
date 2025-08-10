clc,clear all,close all;
t=0:0.001:1;
x1= sin(90*pi*t);
x2 = rand(1000,1);  % generate random time series
tau = 1;  % time delay
dim = 5;  % embedding dimension
MLE1 = lyapunov(x1, tau, dim)
MLE2 = lyapunov(x2, tau, dim)
plot(x1)
hold on;
plot(x2)


[D,lnMr] = gp_dim(x1,5,tau)

