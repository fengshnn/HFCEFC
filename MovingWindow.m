function [MovingWindowSignal,k] = MovingWindow(signal,window,move)
%ע�⣺move ҪԶС�� window �źã������ϱȽ������壻
% �� move �� windowȡֵ��ͬʱ����ʵ���ǽ�ԭʼ���о��ֳ�k��
% �������ƣ�MovingAverageing
% �������ܣ�
% ���룺   x1  x2   x3  x4  x5   x6  x7  x8   x9
% ��� ��    x1  x2   x3
%           x2  x3   x4
%            x3  x4  x5
%           x4  x5   x6
%            x5  x6  x7
%           x6  x7  x8
%           x7  x8   x9
%            
       
%   ������Ǵ�windowΪ3�ģ��ƶ�����moveΪ1 �õ��ֶ�������

% �������룺����ʱ������   signal
%          �����и���       k
% ����������ƶ����õ��µķֶ�����  
% ��д���ߣ� fengshnn
% ��дʱ�䣺 2020.12.27
% ����˵�����ƶ�����move
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