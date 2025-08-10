function [ signal_standard ] = standardization( signal )
%UNTITLED3 此处显示有关此函数的摘要
%   此处显示详细说明
%标准化 ：yi=(xi-mean)/std



mean_value = mean(signal);
std_value =std(signal);

signal_standard =(signal-mean_value)/std_value;

end

