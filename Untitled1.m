% 将原始信号分解成epoch，按列存储，并将具有体动的列删除。
%%
clear all;
clc;
close all;


% % %           导入滤波后的BCG信号
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\083703_BCG.txt'); %滤波后的BCG
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\083703_BREATH.txt');  %滤波后的呼吸
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\083703_orig.txt'); %原始信号

% BCGsignal2= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\101945_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\101945_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\101945_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\101945_orig.txt'); %原始信号

% BCGsignal3= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\105600_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\105600_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\105600_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\105600_orig.txt'); %原始信号

% BCGsignal4= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\115321_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\115321_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\115321_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\115321_orig.txt'); %原始信号

% BCGsignal5= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\100123_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\100123_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\100123_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\100123_orig.txt'); %原始信号

% BCGsignal6= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170740_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170740_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170740_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170740_orig.txt'); %原始信号

% BCGsignal7= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\141257_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\141257_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\141257_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\141257_orig.txt'); %原始信号

% BCGsignal8= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\150512_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\150512_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\150512_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\150512_orig.txt'); %原始信号


% BCGsignal9= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163715_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163715_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163715_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163715_orig.txt'); %原始信号

% BCGsignal10= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\110903_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\110903_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\110903_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\110903_orig.txt'); %原始信号

% BCGsignal11= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170721_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170721_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170721_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170721_orig.txt'); %原始信号

% BCGsignal12= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\112223_BCG.txt');
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\112223_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\112223_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\112223_orig.txt'); %原始信号

% BCGsignal13= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\114700_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\114700_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\114700_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\114700_orig.txt'); %原始信号

% BCGsignal14= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\174545_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\174545_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\174545_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\174545_orig.txt'); %原始信号

% BCGsignal15= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\173730_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\173730_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\173730_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\173730_orig.txt'); %原始信号

% BCGsignal16= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\165020_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\165020_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\165020_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\165020_orig.txt'); %原始信号

% BCGsignal17= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\171306_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\171306_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\171306_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\171306_orig.txt'); %原始信号

% BCGsignal18= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\094839_BCG.txt');
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\094839_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\094839_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\094839_orig.txt'); %原始信号

% BCGsignal19= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\140503_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\140503_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\140503_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\140503_orig.txt'); %原始信号

% BCGsignal20= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\143028_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\143028_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\143028_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\143028_orig.txt'); %原始信号

% BCGsignal21= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\164543_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\164543_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\164543_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\164543_orig.txt'); %原始信号

% BCGsignal22= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163835_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163835_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163835_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163835_orig.txt'); %原始信号

% BCGsignal23= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170458_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170458_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170458_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170458_orig.txt'); %原始信号

% BCGsignal24= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\110539_BCG.txt');
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\110539_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\110539_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\110539_orig.txt'); %原始信号

% BCGsignal25= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\143742_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\143742_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\143742_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\143742_orig.txt'); %原始信号

% BCGsignal26= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\152505_BCG.txt');
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\152505_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\152505_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\152505_orig.txt'); %原始信号

% BCGsignal27= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170537_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170537_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170537_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170537_orig.txt'); %原始信号

% BCGsignal28= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\112359_BCG.txt'); 
BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\112359_BCG.txt'); 
Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\112359_BREATH.txt');
Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\112359_orig.txt'); %原始信号，健康者

% BCGsignal29= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\164314_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\164314_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\164314_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\164314_orig.txt'); %原始信号

% BCGsignal30= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\153217_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\153217_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\153217_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\153217_orig.txt'); %原始信号


% BCGsignal31= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\101456_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\101456_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\101456_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\101456_orig.txt'); %原始信号

% BCGsignal32= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\160729_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\160729_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\160729_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\160729_orig.txt'); %原始信号

% BCGsignal33= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170356_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170356_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170356_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\170356_orig.txt'); %原始信号，呼吸急促


% BCGsignal34= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\172351_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\172351_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\172351_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\172351_orig.txt'); %原始信号

% BCGsignal35= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\122157_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\122157_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\122157_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\122157_orig.txt'); %原始信号

% BCGsignal36= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\160419_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\160419_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\160419_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\160419_orig.txt'); %原始信号

% BCGsignal37= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\151931_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\151931_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\151931_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\151931_orig.txt'); %原始信号

% BCGsignal38= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\100828_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\100828_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\100828_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\100828_orig.txt'); %原始信号

% BCGsignal39= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162338_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162338_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162338_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162338_orig.txt'); %原始信号

% BCGsignal40= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\114836_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\114836_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\114836_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\114836_orig.txt'); %原始信号

% BCGsignal41= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154437_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154437_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154437_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154437_orig.txt'); %原始信号

% BCGsignal42= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\094306_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\094306_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\094306_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\094306_orig.txt'); %原始信号

% BCGsignal43= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\161859_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\161859_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\161859_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\161859_orig.txt'); %原始信号

% BCGsignal44= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\165622_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\165622_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\165622_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\165622_orig.txt'); %原始信号

% BCGsignal45= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\123456_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\123456_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\123456_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\123456_orig.txt'); %原始信号

% BCGsignal46= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154038_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154038_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154038_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154038_orig.txt'); %原始信号

% BCGsignal47= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162728_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162728_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162728_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162728_orig.txt'); %原始信号

% BCGsignal48= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162329_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162329_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162329_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\162329_orig.txt'); %原始信号

% BCGsignal49= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\111746_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\111746_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\111746_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\111746_orig.txt'); %原始信号

% BCGsignal50= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\155311_BCG.txt');
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\155311_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\155311_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\155311_orig.txt'); %原始信号

% BCGsignal51= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\161348_BCG.txt'); % 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\161348_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\161348_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\161348_orig.txt'); %原始信号

% BCGsignal52= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\104518_BCG.txt'); % 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\104518_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\104518_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\104518_orig.txt'); %原始信号

% BCGsignal53= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\145537_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\145537_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\145537_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\145537_orig.txt'); %原始信号

% BCGsignal54= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154408_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154408_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154408_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\154408_orig.txt'); %原始信号

% BCGsignal55= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\144955_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\144955_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\144955_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\144955_orig.txt'); %原始信号

% BCGsignal56= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\152931_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\152931_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\152931_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\152931_orig.txt'); %原始信号



% BCGsignal57= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\145549_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\145549_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\145549_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\145549_orig.txt'); %原始信号

% BCGsignal58= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163806_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163806_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163806_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\163806_orig.txt'); %原始信号


% BCGsignal59= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\121537_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\121537_BCG.txt'); 
% Breathsignal1=load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\121537_BREATH.txt');
% Signsignal1 = load('D:\HRV心衰\超声数据\2021BCG整理\提取滤波后数据2\121537_orig.txt'); %原始信号


% BCGsignal60= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\161858_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\161858_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\161858_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\161858_orig.txt');

% BCGsignal61= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\142934_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\142934_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\142934_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\142934_orig.txt');

% BCGsignal62= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\103326_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\103326_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\103326_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\103326_orig.txt');

% BCGsignal63= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\155528_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\155528_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\155528_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\155528_orig.txt');

% BCGsignal64= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\160640_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\160640_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\160640_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\160640_orig.txt');

% BCGsignal65= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\143837_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\143837_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\143837_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\143837_orig.txt');

% BCGsignal66= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\154209_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\154209_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\154209_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\154209_orig.txt');

% BCGsignal67= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\115041_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\115041_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\115041_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\115041_orig.txt');

% BCGsignal68= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\162050_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\162050_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\162050_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\162050_orig.txt');

% BCGsignal69= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170333_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170333_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170333_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170333_orig.txt');

% BCGsignal70= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\171957_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\171957_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\171957_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\171957_orig.txt');

% BCGsignal71= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\173101_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\173101_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\173101_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\173101_orig.txt');

%---


% BCGsignal72= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170011_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170011_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170011_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170011_orig.txt');

% BCGsignal73= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\163932_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\163932_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\163932_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\163932_orig.txt');

% BCGsignal74= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\165958_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\165958_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\165958_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\165958_orig.txt');

% BCGsignal75= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\121251_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\121251_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\121251_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\121251_orig.txt');

% BCGsignal76= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\161456_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\161456_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\161456_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\161456_orig.txt');


% BCGsignal77= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\165643_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\165643_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\165643_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\165643_orig.txt');

% BCGsignal78= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\163747_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\163747_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\163747_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\163747_orig.txt');

% BCGsignal79= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\122520_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\122520_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\122520_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\122520_orig.txt');

% BCGsignal80= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\124852_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\124852_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\124852_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\124852_orig.txt');

% % BCGsignal81= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170012_BCG.txt'); 
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170012_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170012_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\170012_orig.txt');

% % BCGsignal82
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\152248_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\152248_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\152248_orig.txt');

% % BCGsignal83
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\154835_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\154835_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\154835_orig.txt');

% % BCGsignal84
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\160811_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\160811_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\160811_orig.txt');

% BCGsignal85
% BCGsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\172133_BCG.txt'); 
% Breathsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\172133_BREATH.txt');
% Signsignal1= load('D:\HRV心衰\超声数据\2022BCG整理\提取滤波后数据2\172133_orig.txt');


% BCGsignal86     数据采集作废。
% 145307_BCG.txt;




BCGsignal1 =BCGsignal1(1:length(Breathsignal1),1);
Signsignal1=Signsignal1(1:length(Breathsignal1),1);
%------   分割成10秒重叠信号------------
figure(1)
plot(BCGsignal1);
figure(2)
window = 10*1000; move =5*1000;% 有重叠的分10s为1 epoch
[BCG_MovingWindowSignal,epoch] = MovingWindow(BCGsignal1,window,move) %BCG重叠式分段
BCG = BCG_MovingWindowSignal'; % 将所有epoch 按列存储。
[Sign_MovingWindowSignal,epoch] = MovingWindow(Signsignal1,window,move) %原始信号重叠式分段
Sign = Sign_MovingWindowSignal'; % 将所有epoch 按列存储。
[RES_MovingWindowSignal,epoch] = MovingWindow(Breathsignal1,window,move) %RES重叠式分段, 由于。。按照呼吸的长度
RES = RES_MovingWindowSignal'; % 将所有epoch 按列存储。
for i=1:epoch
  
    plot(BCG(:,i));
    hold on;
end


BCG_new =BCG;RES_new =RES;Sign_new =Sign;

%%
ii=0;
for i=1:epoch
        if max(BCG(:,i)) >80      %修改阈值，找出体动片段，删除，重新保存。ID:1-10,无,130,130，300，200，100，150，100
            ii=ii+1;
            c(ii)=i
        end   
end

%删除指定的列。
BCG_new(:,c)=[]; 
RES_new(:,c)=[];
Sign_new(:,c)=[];
%画出去掉体动数据列-BCG
[m_new,epoch_new]=size(BCG_new)
figure(3)
for i=1:epoch_new
    plot(BCG_new(:,i));
    hold on;
end

%%
save BCG85.txt -ascii BCG_new
save BREATH85.txt -ascii RES_new
save Sign85.txt -ascii Sign_new

%%





