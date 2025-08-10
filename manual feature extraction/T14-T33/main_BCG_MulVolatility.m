% 窗口内功率的变化，波动性。窗口内模糊熵序列，窗口内呼吸与BCG功率比序列。前后序列MIC  的变化

clear all;
clc;
close all;
addpath(genpath('D:\MatlabProject\matlab\Synchronization\Mine'))
% 


% % 导入预处理得数据
% BCG_epoch0= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\BCG_epoch0.txt'); %正常的BCG——epoch
% BCG_epoch1=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\BCG_epoch1.txt'); %心衰的BCG——epoch
% RES_epoch0= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\RES_epoch0.txt'); 
% RES_epoch1=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\RES_epoch1.txt'); 
% [m0,epoch0_number]=size(BCG_epoch0)
% [m1,epoch1_number]=size(BCG_epoch1)

% 三分类数据特征提取
% BCG_epoch0=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\20s_10s\BCG_epoch_3class.txt'); %健康+心衰
% RES_epoch0=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\20s_10s\RES_epoch_3class.txt');%健康+心衰

BCG_epoch0=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG_epoch_3class.txt'); %
RES_epoch0=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\RES_epoch_3class.txt'); %

[m0,epoch0_number]=size(BCG_epoch0)


fs=1000;
N =10; %信号长度30秒
T=1/fs; 
t=[0:N*fs-1]*T;
move=1*1000;window =2*1000;  %10秒一个窗口，窗口应该大于一个呼吸周期。
m=2;r=0.15;
CodeIsHere =1;CodeIsHere2 =1;


%健康组的特征
for i=1:epoch0_number
    BCGsignal0 = BCG_epoch0(:,i);BCGsignal0 =BCGsignal0';
    RESsignal0 =RES_epoch0(:,i);RESsignal0=RESsignal0';
    
        % 归一化 或者标准化。    
%     [Y,PS] = mapminmax(signal,-1,1);  %输入需要是行向量。归一化BCG数据
%     signal =Y';
    BCGsignal0  = standardization( BCGsignal0 );% 标准化BCG数据。
    RESsignal0 =standardization( RESsignal0 );% 标准化呼吸数据。
    
    [MovingWindowSignal_BCG,k0_BCG] = MovingWindow(BCGsignal0',window,move); 
    [MovingWindowSignal_breath,k0_breath] = MovingWindow(RESsignal0',window,move); 
    for j=1:k0_BCG
        Signal_move_BCG=MovingWindowSignal_BCG(j,:);  %行向量,BCG信号
        Signal_move_Breath =MovingWindowSignal_breath(j,:); %行向量，呼吸信号
        

        BCG_Signal_move_FE(i,j) = mohu(resample(Signal_move_BCG,200,1000),m,r,2,1);   %%计算滑动窗口内BCG 的模糊熵。得到模糊熵序列
        Breath_Signal_move_FE(i,j) = mohu(resample(Signal_move_Breath,200,1000),m,r,2,1);  %呼吸模糊熵
        BCG_Signal_move_Power(i,j) =rms(Signal_move_BCG).^2; %计算滑动窗口内BCG 的 功率。得到功率序列。
%         
        BCGandRES_Signal_move_PowerRate(i,j)=(rms(Signal_move_Breath).^2)/(rms(Signal_move_BCG).^2);%计算滑动窗口内呼吸与BCG 的 功率比。得到功率比序列

        
    end
    CodeIsHere =CodeIsHere+1
    
    
    % 计算BCG前后序列的MIC
     for j=1:k0_BCG-1
        signal1 = MovingWindowSignal_BCG(j,:);  %横向量
        signal2 = MovingWindowSignal_BCG(j+1,:);  %横向量
        signal1=resample(signal1,200,1000); %
        signal2=resample(signal2,200,1000); %
        [Mic(i,j), mmm] = mine(signal1, signal2);   %Mine ，输入行向量
        
    end
    
end



% BCG_FE_SC=[BCG_Signal_move_FE;BCG_Signal_move_FE1];
% RES_FE_SC=[Breath_Signal_move_FE;Breath_Signal_move_FE1];
% BCG_POWER_SC =[BCG_Signal_move_Power;BCG_Signal_move_Power1];
% BCG_MIC_SC=[Mic;Mic1];

% BCG_POWERRATE_SC=[BCGandRES_Signal_move_PowerRate;BCGandRES_Signal_move_PowerRate1];


