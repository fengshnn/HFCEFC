function [ signal_standard ] = standardization( signal )
%UNTITLED3 �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
%��׼�� ��yi=(xi-mean)/std



mean_value = mean(signal);
std_value =std(signal);

signal_standard =(signal-mean_value)/std_value;

end

