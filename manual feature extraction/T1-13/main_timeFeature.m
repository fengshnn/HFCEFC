clear all;
clc;
close all;
addpath(genpath('D:\LLE_and_CD')); %����LLE��CD

%--------------��������----------------------
%�������� ���� �����ĵ����ݡ�����Ԥ��������ݣ��������е���ʽ�洢
BCG_epoch1=load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\10s_5s\BCG_epoch_3class.txt'); %����+HF������epoch
RES_epoch1=load('D:\MatlabProject\heartfailure\BCG��ѧ��\Ԥ����\10s_5s\RES_epoch_3class.txt'); 

[m1,epoch1_number]=size(BCG_epoch1)  %

fs=1000;
% T=1/fs; 
% t=[0:30000-1]*T;


%%
% **************************** ����ԭʼ�ź����� ����������******************

%��ʼ��
BCG_epoch1_timeFeature= zeros(epoch1_number,11);
BCG_epoch1_timeAndfrequency=  zeros(epoch1_number,24);  %11��ʱ���13��Ƶ��������

RES_epoch1_timeFeature= zeros(epoch1_number,9);
RES_epoch1_timeAndfrequency=  zeros(epoch1_number,24);  %11��ʱ���13��Ƶ��������

BCG_RES_epoch1_Feature= zeros(epoch1_number,4);


for epoch_1=1:epoch1_number
    epoch_1
     % BCG���ݱ�׼��
    BCGsignal1 = BCG_epoch1(:,epoch_1);
    %���ܹ�һ������һ���� ��ֵ�ͷ��Ϊһ���ˡ�
%     BCGsignal1 =BCGsignal1';BCGsignal1  = standardization( BCGsignal1 );BCGsignal1 =BCGsignal1';%�д洢��׼��BCG���ݡ�
     
    [ BCGtimestruct ] = timeDomainFeatures( BCGsignal1,fs); %ʱ�����е�ͳ�ƺͷ����Բ�����
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
%          % RES���ݱ�׼��
    RESsignal1 = RES_epoch1(:,epoch_1);
%     %���ܹ�һ������һ���� ��ֵ�ͷ��Ϊһ���ˡ�
% %     RESsignal1 =RESsignal1';RESsignal1  = standardization( RESsignal1 );RESsignal1 =RESsignal1';%�д洢��׼��BCG���ݡ�
%      
    [ REStimestruct ] = timeDomainFeatures( RESsignal1,fs); %ʱ�����е�ͳ�ƺͷ����Բ�����
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
% %     %--------�ķβ���------------------------
    BCG_RES_epoch1_Feature(epoch_1,1)=RES_epoch1_timeFeature(epoch_1,2)/BCG_epoch1_timeFeature(epoch_1,2); %������BCG���ʱ�
    BCG_RES_epoch1_Feature(epoch_1,2)=RES_epoch1_timeFeature(epoch_1,3)/BCG_epoch1_timeFeature(epoch_1,3);%������BCG�ķ�ֵϵ����
    BCG_RES_epoch1_Feature(epoch_1,3)=RES_epoch1_timeFeature(epoch_1,7)/BCG_epoch1_timeFeature(epoch_1,7);% ������BCG��FE֮��
    BCG_RES_epoch1_Feature(epoch_1,4)=RES_epoch1_timeFeature(epoch_1,7)+BCG_epoch1_timeFeature(epoch_1,7);%������BCG��FE֮��
%      

end

%%
BCG_epoch = downsample(BCG_epoch1,5); %
RES_epoch = downsample(RES_epoch1,5);


