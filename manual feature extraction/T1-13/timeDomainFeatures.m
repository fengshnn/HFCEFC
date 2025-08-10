function [ timestruct ] = timeDomainFeatures( src,fs)
%src:��������������
% fs�ǲ����ʡ�

%����Ƶ��ͳ������
%***********************���źŽ���FFT�任*******************************
FS=fs;
N=length(src);

%********************************����ʱ������ֵ**********************
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

%********************************����*****************************
timestruct.RMS =rms(src); %RMS����Чֵ
timestruct.power=rms(src).^2; %����
timestruct.F=rms(src)/(max(src)-min(src)); %��ֵϵ������ӦBCG���ȱ仯��
    %����30���ڵķ�ȣ�ƫ�ȡ�
timestruct.ske =skewness(src);%ƫ��
timestruct.kur =kurtosis(src); % ��ȣ��Ͷȣ�����������ƫ����̬�ֲ��ĳ߶�֮һ
timestruct.kr = timestruct.kur/std(src);
timestruct.FE =mohu(resample(src,200,1000),2,0.15,2,1);   %ģ����m=2,r=0.15
%     BCG_epoch1_ApEn(epoch_1,1) = ApEn(resample(BCGsignal1',10,1000),m,r); % �źŽ�����ֵ
%     BCG_epoch1_sampen(epoch_1,1)  = sampen(resample(BCGsignal1',10,1000),m,r);   % �ź�������ֵ
%     BCG_epoch1_pailie(epoch_1,1)=  pailie(resample(BCGsignal1',200,1000),m,1) ;            % �ź�������ֵ
timestruct.CLZ=  CLZ(resample(src',200,1000))  ;
timestruct.MLZ=  MLZ(resample(src',200,1000),150,8);
timestruct.LLE = lyapunov(resample(src',200,1000),1,2);%t=1,m=2
timestruct.CD = gp_dim(resample(src',200,1000),2,1); %m=2,t=1




end
% ��������������������������������
