function [ timestruct ] = timeDomainFeatures( src,fs)
%src:输入是列向量；
% fs是采样率。

%计算频域统计特征
%***********************对信号进行FFT变换*******************************
FS=fs;
N=length(src);

%********************************计算时域特征值**********************
% timestruct.p1=mean(src');
% timestruct.p2=sum((src'-timestruct.p1).^2)/(length(src')-1);
% timestruct.p3=   sum(sqrt(abs(src')))^2/length(src')^2;
% timestruct.p4= sqrt(sum(src'.^2)/length(src'));
% timestruct.p5=max(abs(src'));
% timestruct.p6 = sum((src'-timestruct.p1).^3)/(length(src')-1)*timestruct.p2^3;
% timestruct.p7 =sum((src'-timestruct.p1).^4)/(length(src')-1)*timestruct.p2^4;
% timestruct.p8 =timestruct.p5/timestruct.p4;
% timestruct.p9 =timestruct.p5/timestruct.p3;
% timestruct.p10 =length(src')*timestruct.p4/sum(abs(src'));
% timestruct.p11 =length(src')*timestruct.p5/sum(abs(src'));

%********************************计算*****************************
timestruct.RMS =rms(src); %RMS，有效值
timestruct.power=rms(src).^2; %功率
timestruct.F=rms(src)/(max(src)-min(src)); %峰值系数，反应BCG幅度变化。
    %计算30秒内的峰度，偏度。
timestruct.ske =skewness(src);%偏度
timestruct.kur =kurtosis(src); % 峰度（峭度）：用作衡量偏离正态分布的尺度之一
timestruct.kr = timestruct.kur/std(src);
timestruct.FE =mohu(resample(src,200,1000),2,0.15,2,1);   %模糊熵m=2,r=0.15
%     BCG_epoch1_ApEn(epoch_1,1) = ApEn(resample(BCGsignal1',10,1000),m,r); % 信号近似熵值
%     BCG_epoch1_sampen(epoch_1,1)  = sampen(resample(BCGsignal1',10,1000),m,r);   % 信号样本熵值
%     BCG_epoch1_pailie(epoch_1,1)=  pailie(resample(BCGsignal1',200,1000),m,1) ;            % 信号排列熵值
timestruct.CLZ=  CLZ(resample(src',200,1000))  ;
timestruct.MLZ=  MLZ(resample(src',200,1000),150,8);
timestruct.LLE = lyapunov(resample(src',200,1000),1,2);%t=1,m=2
timestruct.CD = gp_dim(resample(src',200,1000),2,1); %m=2,t=1




end
% ————————————————
