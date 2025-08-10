function [MovingWindowSignal,k] = MovingWindow(signal,window,move)
%注意：move 要远小于 window 才好，物理上比较有意义；
% 当 move 与 window取值相同时候，其实就是将原始序列均分成k份
% 函数名称：MovingAverageing
% 函数功能：
% 输入：   x1  x2   x3  x4  x5   x6  x7  x8   x9
% 输出 ：    x1  x2   x3
%           x2  x3   x4
%            x3  x4  x5
%           x4  x5   x6
%            x5  x6  x7
%           x6  x7  x8
%           x7  x8   x9
%            
       
%   这个就是窗window为3的，移动因子move为1 得到分段新序列

% 函数输入：输入时间序列   signal
%          新序列个数       k
% 函数输出：移动窗得到新的分段序列  
% 编写作者： fengshnn
% 编写时间： 2020.12.27
% 其他说明：移动因子move
%           
if window==1,MovingWindowSignal=signal,k=length(signal);end
M=length(signal);
k=fix((M-window)/move)+1;


j=1;
for i = 1 : k
    y(i,:)=signal(j:window);
    j=j+move;
    window=window+move;
   
end
MovingWindowSignal=y;
end