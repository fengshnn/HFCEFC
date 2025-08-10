% 健康+心衰的，将所有epoch合并
clear all;
clc;
close all;

% %           导入滤波后的BCG信号
BCG1= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG1.txt'); 
RES1=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH1.txt'); 

BCG2= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG2.txt'); 
RES2=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH2.txt'); 

BCG3= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG3.txt'); 
RES3=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH3.txt'); 

BCG4= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG4.txt'); 
RES4=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH4.txt'); 
% BCG4=BCG4(:,1:10);RES4=RES4(:,1:10);


BCG5= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG5.txt'); 
RES5=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH5.txt'); 

BCG6= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG6.txt'); 
RES6=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH6.txt'); 
% BCG6=BCG6(:,1:10);RES6=RES6(:,1:10);

BCG7= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG7.txt'); 
RES7=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH7.txt'); 

BCG8= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG8.txt'); 
RES8=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH8.txt'); 

BCG9= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG9.txt'); 
RES9=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH9.txt'); 
% BCG9=BCG9(:,1:10);RES9=RES9(:,1:10);

BCG10= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG10.txt'); 
RES10=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH10.txt'); 

BCG11= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG11.txt'); 
RES11=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH11.txt'); 
% BCG11=BCG11(:,1:10);RES11=RES11(:,1:10);

BCG12= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG12.txt'); 
RES12=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH12.txt'); 

BCG13= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG13.txt'); 
RES13=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH13.txt'); 

BCG14= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG14.txt'); 
RES14=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH14.txt'); 
% BCG14=BCG14(:,1:10);RES14=RES14(:,1:10);

BCG15= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG15.txt'); 
RES15=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH15.txt'); 
BCG16= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG16.txt'); 
RES16=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH16.txt'); 

BCG17= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG17.txt'); 
RES17=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH17.txt'); 
BCG18= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG18.txt'); 
RES18=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH18.txt'); 
% BCG18=BCG18(:,1:10);RES18=RES18(:,1:10);

BCG19= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG19.txt'); 
RES19=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH19.txt'); 

BCG20= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG20.txt'); 
RES20=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH20.txt'); 
BCG21= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG21.txt'); 
RES21=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH21.txt');
% BCG21=BCG21(:,1:10);RES21=RES21(:,1:10);
BCG22= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG22.txt'); 
RES22=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH22.txt'); 

BCG23= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG23.txt'); 
RES23=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH23.txt'); 
% BCG23=BCG23(:,1:10);RES23=RES23(:,1:10);
BCG24= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG24.txt'); 
RES24=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH24.txt'); 
% BCG24=BCG24(:,1:10);RES24=RES24(:,1:10);
BCG25= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG25.txt'); 
RES25=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH25.txt'); 


BCG26= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG26.txt'); 
RES26=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH26.txt'); 

BCG27= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG27.txt'); 
RES27=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH27.txt'); 

BCG28= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG28.txt'); 
RES28=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH28.txt'); 

BCG29= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG29.txt'); 
RES29=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH29.txt'); 

BCG30= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG30.txt'); 
RES30=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH30.txt'); 
% BCG30=BCG30(:,1:10);RES30=RES30(:,1:10);

BCG31= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG31.txt'); 
RES31=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH31.txt'); 
% BCG31=BCG31(:,1:10);RES31=RES31(:,1:10);

BCG32= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG32.txt'); 
RES32=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH32.txt'); 
% BCG32=BCG32(:,1:10);RES32=RES32(:,1:10);

BCG33= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG33.txt'); 
RES33=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH33.txt'); 
% BCG33=BCG33(:,1:10);RES33=RES33(:,1:10);

BCG34= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG34.txt'); 
RES34=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH34.txt'); 
% BCG34=BCG34(:,1:10);RES34=RES34(:,1:10);

BCG35= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG35.txt'); 
RES35=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH35.txt'); 
% BCG35=BCG35(:,1:10);RES35=RES35(:,1:10);

BCG36= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG36.txt'); 
RES36=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH36.txt'); 

BCG37= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG37.txt'); 
RES37=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH37.txt'); 

BCG38= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG38.txt'); 
RES38=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH38.txt'); 

BCG39= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG39.txt'); 
RES39=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH39.txt'); 
% BCG39=BCG39(:,1:10);RES39=RES39(:,1:10);

BCG40= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG40.txt'); 
RES40=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH40.txt'); 
% BCG40=BCG40(:,1:10);RES40=RES40(:,1:10);
BCG41= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG41.txt'); 
RES41=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH41.txt'); 
% BCG41=BCG41(:,1:10);RES41=RES41(:,1:10);

BCG42= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG42.txt'); 
RES42=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH42.txt'); 
% BCG42=BCG42(:,1:10);RES42=RES42(:,1:10);

BCG43= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG43.txt'); 
RES43=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH43.txt'); 
% BCG43=BCG43(:,1:10);RES43=RES43(:,1:10);
BCG44= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG44.txt'); 
RES44=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH44.txt'); 
% BCG44=BCG44(:,1:10);RES44=RES44(:,1:10);

BCG45= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG45.txt'); 
RES45=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH45.txt'); 
% BCG45=BCG45(:,1:10);RES45=RES45(:,1:10);
BCG46= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG46.txt'); 
RES46=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH46.txt'); 
% BCG46=BCG46(:,1:10);RES46=RES46(:,1:10);

BCG47= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG47.txt'); 
RES47=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH47.txt'); 
% BCG47=BCG47(:,1:12);RES47=RES47(:,1:12);
BCG48= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG48.txt'); 
RES48=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH48.txt'); 
% BCG48=BCG48(:,1:10);RES48=RES48(:,1:10);
BCG49= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG49.txt'); 
RES49=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH49.txt'); 

BCG50= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG50.txt'); 
RES50=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH50.txt'); 
% BCG50=BCG50(:,1:10);RES50=RES50(:,1:10);
BCG51= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG51.txt'); 
RES51=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH51.txt'); 
% BCG51=BCG51(:,1:10);RES51=RES51(:,1:10);

BCG52= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG52.txt'); 
RES52=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH52.txt'); 
BCG53= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG53.txt'); 
RES53=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH53.txt'); 
% BCG53=BCG53(:,1:10);RES53=RES53(:,1:10);

BCG54= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG54.txt'); 
RES54=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH54.txt'); 
BCG55= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG55.txt'); 
RES55=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH55.txt'); 
% BCG55=BCG55(:,1:10);RES55=RES55(:,1:10);
BCG56= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG56.txt'); 
RES56=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH56.txt'); 
% BCG56=BCG56(:,1:10);RES56=RES56(:,1:10);

BCG57= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG57.txt'); 
RES57=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH57.txt');
% BCG57=BCG57(:,1:10);RES57=RES57(:,1:10);
BCG58= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG58.txt'); 
RES58=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH58.txt'); 
% BCG58=BCG58(:,1:18);RES58=RES58(:,1:18);

BCG59= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG59.txt'); 
RES59=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH59.txt');
% BCG59=BCG59(:,1:6);RES59=RES59(:,1:6);

BCG60= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG60.txt'); 
RES60=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH60.txt'); 
BCG61= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG61.txt'); 
RES61=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH61.txt'); 
BCG62= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG62.txt'); 
RES62=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH62.txt'); 
BCG63= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG63.txt'); 
RES63=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH63.txt'); 
BCG64= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG64.txt'); 
RES64=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH64.txt'); 
BCG65= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG65.txt'); 
RES65=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH65.txt'); 
BCG66= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG66.txt'); 
RES66=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH66.txt'); 
BCG67= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG67.txt'); 
RES67=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH67.txt'); 
BCG68= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG68.txt'); 
RES68=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH68.txt'); 
BCG69= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG69.txt'); 
RES69=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH69.txt'); 
BCG70= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG70.txt'); 
RES70=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH70.txt'); 
BCG71= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG71.txt'); 
RES71=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH71.txt'); 

BCG72= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG72.txt'); 
RES72=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH72.txt'); 
BCG73= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG73.txt'); 
RES73=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH73.txt');
BCG74= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG74.txt'); 
RES74=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH74.txt');
BCG75= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG75.txt'); 
RES75=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH75.txt');
BCG76= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG76.txt'); 
RES76=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH76.txt');
BCG77= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG77.txt'); 
RES77=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH77.txt');
BCG78= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG78.txt'); 
RES78=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH78.txt');
BCG79= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG79.txt'); 
RES79=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH79.txt');
BCG80= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG80.txt'); 
RES80=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH80.txt');
BCG81= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG81.txt'); 
RES81=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH81.txt');
BCG82= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG82.txt'); 
RES82=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH82.txt');
BCG83= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG83.txt'); 
RES83=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH83.txt');
BCG84= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG84.txt'); 
RES84=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH84.txt');
BCG85= load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BCG85.txt'); 
RES85=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\BREATH85.txt');

Sign1=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign1.txt');
Sign2=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign2.txt');
Sign3=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign3.txt');
Sign4=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign4.txt');
Sign5=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign5.txt');
Sign6=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign6.txt');
Sign7=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign7.txt');
Sign8=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign8.txt');
Sign9=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign9.txt');
Sign10=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign10.txt');
Sign11=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign11.txt');
Sign12=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign12.txt');
Sign13=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign13.txt');
Sign14=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign14.txt');
Sign15=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign15.txt');
Sign16=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign16.txt');
Sign17=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign17.txt');
Sign18=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign18.txt');
Sign19=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign19.txt');
Sign20=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign20.txt');
Sign21=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign21.txt');
Sign22=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign22.txt');
Sign23=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign23.txt');
Sign24=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign24.txt');
Sign25=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign25.txt');
Sign26=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign26.txt');
Sign27=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign27.txt');
Sign28=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign28.txt');
Sign29=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign29.txt');
Sign30=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign30.txt');
Sign31=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign31.txt');
Sign32=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign32.txt');
Sign33=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign33.txt');
Sign34=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign34.txt');
Sign35=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign35.txt');
Sign36=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign36.txt');
Sign37=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign37.txt');
Sign38=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign38.txt');
Sign39=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign39.txt');
Sign40=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign40.txt');
Sign41=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign41.txt');
Sign42=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign42.txt');
Sign43=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign43.txt');
Sign44=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign44.txt');
Sign45=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign45.txt');
Sign46=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign46.txt');
Sign47=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign47.txt');
Sign48=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign48.txt');
Sign49=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign49.txt');
Sign50=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign50.txt');
Sign51=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign51.txt');
Sign52=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign52.txt');
Sign53=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign53.txt');
Sign54=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign54.txt');
Sign55=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign55.txt');
Sign56=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign56.txt');
Sign57=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign57.txt');
Sign58=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign58.txt');
Sign59=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign59.txt');
Sign60=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign60.txt');
Sign61=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign61.txt');
Sign62=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign62.txt');
Sign63=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign63.txt');
Sign64=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign64.txt');
Sign65=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign65.txt');
Sign66=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign66.txt');
Sign67=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign67.txt');
Sign68=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign68.txt');
Sign69=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign69.txt');
Sign70=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign70.txt');
Sign71=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign71.txt');
Sign72=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign72.txt');
Sign73=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign73.txt');
Sign74=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign74.txt');
Sign75=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign75.txt');
Sign76=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign76.txt');
Sign77=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign77.txt');
Sign78=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign78.txt');
Sign79=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign79.txt');
Sign80=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign80.txt');
Sign81=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign81.txt');
Sign82=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign82.txt');
Sign83=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign83.txt');
Sign84=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign84.txt');
Sign85=load('D:\MatlabProject\heartfailure\BCG大学城\预处理\10s_5s\Sign85.txt');

%论文2的数据   按照EF分级，和健康，0：健康，1：EF≥40%的心衰，2：EF<40%的心衰。
BCG_epoch0 =[BCG1 BCG2 BCG3 BCG5 BCG7 BCG8 BCG10 BCG12 BCG13 BCG15 BCG17 BCG19 BCG20 BCG22 BCG25 BCG26 BCG27 BCG28 BCG29 BCG60 BCG63 BCG65 BCG68 BCG69 BCG74 BCG79 BCG80 BCG81];  %健康
BCG_epoch1 =[BCG4 BCG9 BCG18 BCG21 BCG30 BCG31 BCG33 BCG34 BCG35 BCG36 BCG37 BCG38 BCG40 BCG41 BCG42 BCG43 BCG44 BCG45 BCG47 BCG48 BCG54 BCG56 BCG58 BCG59 BCG61 BCG64 BCG67 BCG70 BCG71 BCG75 BCG76 BCG77 BCG78 BCG82 BCG84]; %EF: 40-
BCG_epoch2 =[BCG6 BCG11 BCG14 BCG23 BCG24 BCG32 BCG39 BCG46 BCG49 BCG50 BCG51 BCG52 BCG53 BCG55 BCG57 BCG66 BCG72 BCG73 BCG83 BCG85];%EF: 40以下
BCG_epoch =[BCG_epoch0 BCG_epoch1 BCG_epoch2];
RES_epoch0 =[RES1 RES2 RES3 RES5 RES7 RES8 RES10 RES12 RES13 RES15 RES17 RES19 RES20 RES22 RES25 RES26 RES27 RES28 RES29 RES60 RES63 RES65 RES68 RES69 RES74 RES79 RES80 RES81];  %健康
RES_epoch1 =[RES4 RES9 RES18 RES21 RES30 RES31 RES33 RES34 RES35 RES36 RES37 RES38 RES40 RES41 RES42 RES43 RES44 RES45 RES47 RES48 RES54 RES56 RES58 RES59 RES61 RES64 RES67 RES70 RES71 RES75 RES76 RES77 RES78 RES82 RES84];
RES_epoch2 =[RES6 RES11 RES14 RES23 RES24 RES32 RES39 RES46 RES49 RES50 RES51 RES52 RES53 RES55 RES57 RES66 RES72 RES73 RES83 RES85];
RES_epoch =[RES_epoch0 RES_epoch1 RES_epoch2];
[m0,epoch0]=size(RES_epoch0)
[m1,epoch1]=size(RES_epoch1)
[m2,epoch2]=size(RES_epoch2)
Sign_epoch0=[Sign1 Sign2 Sign3 Sign5 Sign7 Sign8 Sign10 Sign12 Sign13 Sign15 Sign17 Sign19 Sign20 Sign22 Sign25 Sign26 Sign27 Sign28 Sign29 Sign60 Sign63 Sign65 Sign68 Sign69 Sign74 Sign79 Sign80 Sign81];  %健康
Sign_epoch1 =[Sign4 Sign9 Sign18 Sign21 Sign30 Sign31 Sign33 Sign34 Sign35 Sign36 Sign37 Sign38 Sign40 Sign41 Sign42 Sign43 Sign44 Sign45 Sign47 Sign48 Sign54 Sign56 Sign58 Sign59 Sign61 Sign64 Sign67 Sign70 Sign71 Sign75 Sign76 Sign77 Sign78 Sign82 Sign84];
Sign_epoch2 =[Sign6 Sign11 Sign14 Sign23 Sign24 Sign32 Sign39 Sign46 Sign49 Sign50 Sign51 Sign52 Sign53 Sign55 Sign57 Sign66 Sign72 Sign73 Sign83 Sign85];
Sign_epoch =[Sign_epoch0 Sign_epoch1 Sign_epoch2];

[m3,epoch3]=size(RES_epoch)
lab0=ones(1,epoch0)*0
lab1=ones(1,epoch1)*1
lab2=ones(1,epoch2)*2

lab=[lab0 lab1 lab2];
Sign_epoch_signal=zeros(m3,epoch3)
%1.保存BCG和呼吸片段样本，用于特征提取。
save BCG_epoch_3class.txt -ascii BCG_epoch
save RES_epoch_3class.txt -ascii RES_epoch

%滤除原始信号的基线漂移和工频干扰；带通滤波器，0.2-30HZ，采用频率1000，4阶。
for i=1:(epoch0 + epoch1 + epoch2)
    Sign_epoch_signal(:,i)=bandpass_butterworth(Sign_epoch(:,i),[0.2 30],1000,4); %对原始信号带通滤波，去除工频和基线漂移。
end

% % -----保存下面数据作为CNN的输入，（降采样，以行的形式保存，最右边一列为lab）

BCG_epoch = downsample(BCG_epoch,5); %
RES_epoch = downsample(RES_epoch,5);
Sign_epoch_signal_200hz= downsample(Sign_epoch_signal,5); %滤波后的信号 200hz
Sign_epoch_origin_200hz= downsample(Sign_epoch,5); %原始信号 200hz

%% 
BCG_epoch=[BCG_epoch;lab];%按列存，每列最后一个数字是lable
RES_epoch=[RES_epoch;lab];
Sign_epoch_signal_200hz=[Sign_epoch_signal_200hz;lab];
Sign_epoch_origin_200hz = [Sign_epoch_origin_200hz;lab];
% Sign_FFT_signal= [Sign_FFT_signal;lab];

BCG_epoch_H=BCG_epoch';% 转置，按行存。
RES_epoch_H=RES_epoch';
Sign_epoch_H=Sign_epoch_signal_200hz';
Sign_epoch_origin_H = Sign_epoch_origin_200hz';
% Sign_FFT_signal_H =Sign_FFT_signal';

%1.保存在mat文件
save Sign_epoch_200hz.mat Sign_epoch_H         %保存去除基线漂移和工频干扰的原始信号，200HZ
% save Sign_epoch_origin.mat Sign_epoch_origin_H   %保存原始信号，200HZ。
save BCG_epoch.mat  BCG_epoch_H
save RES_epoch.mat  RES_epoch_H




