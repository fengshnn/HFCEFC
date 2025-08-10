% �����ڹ��ʵı仯�������ԡ�������ģ�������У������ں�����BCG���ʱ����С�ǰ������MIC  �ı仯

clear all;
clc;
close all;
addpath(genpath('D:\MatlabProject\matlab\Synchronization\Mine'))
% 


% % ����Ԥ���������
% BCG_epoch0= load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\BCG_epoch0.txt'); %������BCG����epoch
% BCG_epoch1=load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\BCG_epoch1.txt'); %��˥��BCG����epoch
% RES_epoch0= load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\RES_epoch0.txt'); 
% RES_epoch1=load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\RES_epoch1.txt'); 
% [m0,epoch0_number]=size(BCG_epoch0)
% [m1,epoch1_number]=size(BCG_epoch1)

% ����������������ȡ
% BCG_epoch0=load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\20s_10s\BCG_epoch_3class.txt'); %����+��˥
% RES_epoch0=load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\20s_10s\RES_epoch_3class.txt');%����+��˥

BCG_epoch0=load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\10s_5s\BCG_epoch_3class.txt'); %
RES_epoch0=load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\10s_5s\RES_epoch_3class.txt'); %

[m0,epoch0_number]=size(BCG_epoch0)


fs=1000;
N =10; %�źų���30��
T=1/fs; 
t=[0:N*fs-1]*T;
move=1*1000;window =2*1000;  %10��һ�����ڣ�����Ӧ�ô���һ���������ڡ�
m=2;r=0.15;
CodeIsHere =1;CodeIsHere2 =1;


%�����������
for i=1:epoch0_number
    BCGsignal0 = BCG_epoch0(:,i);BCGsignal0 =BCGsignal0';
    RESsignal0 =RES_epoch0(:,i);RESsignal0=RESsignal0';
    
        % ��һ�� ���߱�׼����    
%     [Y,PS] = mapminmax(signal,-1,1);  %������Ҫ������������һ��BCG����
%     signal =Y';
    BCGsignal0  = standardization( BCGsignal0 );% ��׼��BCG���ݡ�
    RESsignal0 =standardization( RESsignal0 );% ��׼���������ݡ�
    
    [MovingWindowSignal_BCG,k0_BCG] = MovingWindow(BCGsignal0',window,move); 
    [MovingWindowSignal_breath,k0_breath] = MovingWindow(RESsignal0',window,move); 
    for j=1:k0_BCG
        Signal_move_BCG=MovingWindowSignal_BCG(j,:);  %������,BCG�ź�
        Signal_move_Breath =MovingWindowSignal_breath(j,:); %�������������ź�
        

        BCG_Signal_move_FE(i,j) = mohu(resample(Signal_move_BCG,200,1000),m,r,2,1);   %%���㻬��������BCG ��ģ���ء��õ�ģ��������
        Breath_Signal_move_FE(i,j) = mohu(resample(Signal_move_Breath,200,1000),m,r,2,1);  %����ģ����
        BCG_Signal_move_Power(i,j) =rms(Signal_move_BCG).^2; %���㻬��������BCG �� ���ʡ��õ��������С�
%         
        BCGandRES_Signal_move_PowerRate(i,j)=(rms(Signal_move_Breath).^2)/(rms(Signal_move_BCG).^2);%���㻬�������ں�����BCG �� ���ʱȡ��õ����ʱ�����

        
    end
    CodeIsHere =CodeIsHere+1
    
    
    % ����BCGǰ�����е�MIC
     for j=1:k0_BCG-1
        signal1 = MovingWindowSignal_BCG(j,:);  %������
        signal2 = MovingWindowSignal_BCG(j+1,:);  %������
        signal1=resample(signal1,200,1000); %
        signal2=resample(signal2,200,1000); %
        [Mic(i,j), mmm] = mine(signal1, signal2);   %Mine ������������
        
    end
    
end



% BCG_FE_SC=[BCG_Signal_move_FE;BCG_Signal_move_FE1];
% RES_FE_SC=[Breath_Signal_move_FE;Breath_Signal_move_FE1];
% BCG_POWER_SC =[BCG_Signal_move_Power;BCG_Signal_move_Power1];
% BCG_MIC_SC=[Mic;Mic1];

% BCG_POWERRATE_SC=[BCGandRES_Signal_move_PowerRate;BCGandRES_Signal_move_PowerRate1];


