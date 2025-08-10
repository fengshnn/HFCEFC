clear all;
clc;
close all;
addpath(genpath('D:\LLE_and_CD')); %计算LLE和CD

%--------------导入数据----------------------
%所有样本 数据 ，论文的数据。导入预处理得数据，数据以列的形式存储
BCG_epoch1=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG_epoch_3class.txt'); %健康+HF的所有epoch
RES_epoch1=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\RES_epoch_3class.txt'); 

[m1,epoch1_number]=size(BCG_epoch1)  %

fs=1000;
% T=1/fs; 
% t=[0:30000-1]*T;


%%
% **************************** 计算原始信号线性 非线性特征******************

%初始化
BCG_epoch1_timeFeature= zeros(epoch1_number,11);
BCG_epoch1_timeAndfrequency=  zeros(epoch1_number,24);  %11个时域和13个频域特征。

RES_epoch1_timeFeature= zeros(epoch1_number,9);
RES_epoch1_timeAndfrequency=  zeros(epoch1_number,24);  %11个时域和13个频域特征。

BCG_RES_epoch1_Feature= zeros(epoch1_number,4);


for epoch_1=1:epoch1_number
    epoch_1
     % BCG数据标准化
    BCGsignal1 = BCG_epoch1(:,epoch_1);
    %不能归一化，归一化后 均值和方差都为一样了。
%     BCGsignal1 =BCGsignal1';BCGsignal1  = standardization( BCGsignal1 );BCGsignal1 =BCGsignal1';%列存储标准化BCG数据。
     
    [ BCGtimestruct ] = timeDomainFeatures( BCGsignal1,fs); %时间序列的统计和非线性参数。
    BCG_epoch1_timeFeature(epoch_1,1)=BCGtimestruct.RMS; 
    BCG_epoch1_timeFeature(epoch_1,2)=BCGtimestruct.power;
    BCG_epoch1_timeFeature(epoch_1,3)=BCGtimestruct.F;
    BCG_epoch1_timeFeature(epoch_1,4)=BCGtimestruct.ske;
    BCG_epoch1_timeFeature(epoch_1,5)=BCGtimestruct.kur;
    BCG_epoch1_timeFeature(epoch_1,6)=BCGtimestruct.kr;
    BCG_epoch1_timeFeature(epoch_1,7)=BCGtimestruct.FE;
    BCG_epoch1_timeFeature(epoch_1,8)=BCGtimestruct.CLZ;
    BCG_epoch1_timeFeature(epoch_1,9)=BCGtimestruct.MLZ;
    BCG_epoch1_timeFeature(epoch_1,10)=BCGtimestruct.LLE;
    BCG_epoch1_timeFeature(epoch_1,11)=BCGtimestruct.CD;

%     
%          % RES数据标准化
    RESsignal1 = RES_epoch1(:,epoch_1);
%     %不能归一化，归一化后 均值和方差都为一样了。
% %     RESsignal1 =RESsignal1';RESsignal1  = standardization( RESsignal1 );RESsignal1 =RESsignal1';%列存储标准化BCG数据。
%      
    [ REStimestruct ] = timeDomainFeatures( RESsignal1,fs); %时间序列的统计和非线性参数。
    RES_epoch1_timeFeature(epoch_1,1)=REStimestruct.RMS; 
    RES_epoch1_timeFeature(epoch_1,2)=REStimestruct.power;
    RES_epoch1_timeFeature(epoch_1,3)=REStimestruct.F;
    RES_epoch1_timeFeature(epoch_1,4)=REStimestruct.ske;
    RES_epoch1_timeFeature(epoch_1,5)=REStimestruct.kur;
    RES_epoch1_timeFeature(epoch_1,6)=REStimestruct.kr;
    RES_epoch1_timeFeature(epoch_1,7)=REStimestruct.FE;
    RES_epoch1_timeFeature(epoch_1,8)=REStimestruct.CLZ;
    RES_epoch1_timeFeature(epoch_1,9)=REStimestruct.MLZ;
 
%    
% %     %--------心肺参数------------------------
    BCG_RES_epoch1_Feature(epoch_1,1)=RES_epoch1_timeFeature(epoch_1,2)/BCG_epoch1_timeFeature(epoch_1,2); %呼吸与BCG功率比
    BCG_RES_epoch1_Feature(epoch_1,2)=RES_epoch1_timeFeature(epoch_1,3)/BCG_epoch1_timeFeature(epoch_1,3);%呼吸与BCG的峰值系数比
    BCG_RES_epoch1_Feature(epoch_1,3)=RES_epoch1_timeFeature(epoch_1,7)/BCG_epoch1_timeFeature(epoch_1,7);% 呼吸与BCG的FE之比
    BCG_RES_epoch1_Feature(epoch_1,4)=RES_epoch1_timeFeature(epoch_1,7)+BCG_epoch1_timeFeature(epoch_1,7);%呼吸与BCG的FE之和
%      

end

%%
BCG_epoch = downsample(BCG_epoch1,5); %
RES_epoch = downsample(RES_epoch1,5);


