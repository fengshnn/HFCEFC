% ���� ��ԭʼ���зֱ�Ӵ�window����ȡ���ֶ� ʱ�����С�
% ԭʼ���� 1,2,3,4,5,6,7,8,9,0
%�Ӵ�window= 5;
% �õ������б�Ϊ��1,2,3,4,5
%                6,7,8,9,0 
% signal :�����ʱ������
% window  �ֵĵ������е����������

% junfen_signal  ������ ��k�� window �еľ��� ��
% k              �����ɵ�k��������

%   fengshenn  
%data  2020/12/27

function [junfen_signal,k] = Windows(signal,window)

if window==1,junfen_signal=signal,k=length(signal);end

n=length(signal);
k=fix(n/window);
junfen_signal=zeros(k,window);%��ʼ��һ��
for i=1:k
    junfen_signal(i,1:window)=signal(i*window-window+1:i*window);
end
end

