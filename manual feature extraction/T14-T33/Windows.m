% 窗， 将原始序列分别加窗window，截取出分段 时间序列。
% 原始序列 1,2,3,4,5,6,7,8,9,0
%加窗window= 5;
% 得到的序列变为：1,2,3,4,5
%                6,7,8,9,0 
% signal :输入的时间序列
% window  分的单个序列的样本点个数

% junfen_signal  ：生成 的k行 window 列的矩阵 。
% k              ：生成的k个新序列

%   fengshenn  
%data  2020/12/27

function [junfen_signal,k] = Windows(signal,window)

if window==1,junfen_signal=signal,k=length(signal);end

n=length(signal);
k=fix(n/window);
junfen_signal=zeros(k,window);%初始化一下
for i=1:k
    junfen_signal(i,1:window)=signal(i*window-window+1:i*window);
end
end

