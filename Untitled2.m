% �������嶯��epoch�ֶ�ɾ��
clear all;
clc;
close all;


% %           �����˲����BCG�ź�
BCG= load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\10s_5s\BCG1.txt'); 
RES=load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\10s_5s\BREATH1.txt'); 
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
        if BCG(j,i) >100      %�޸���ֵ���ҳ��嶯Ƭ�Σ��ֶ�ɾ�������±��档
            c=i
%             continue
            break
        end
        
    end
   
end

figure(3)
plot(BCG(:,2));

