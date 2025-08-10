% 将具有体动的epoch手动删除
clear all;
clc;
close all;


% %           导入滤波后的BCG信号
BCG= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG1.txt'); 
RES=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH1.txt'); 
[m,epoch]=size(BCG)
figure(1)
for i=1:epoch
    plot(BCG(:,i));
    hold on;
end
figure(2)
for i=1:epoch
    plot(RES(:,i));
    hold on;
end

for i=1:epoch
    for j=1:10000
        if BCG(j,i) >100      %修改阈值，找出体动片段，手动删除，重新保存。
            c=i
%             continue
            break
        end
        
    end
   
end

figure(3)
plot(BCG(:,2));

