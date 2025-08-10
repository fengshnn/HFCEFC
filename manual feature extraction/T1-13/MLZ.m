function  lzm=MLZ(data,U,m)
%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 计算一维信号的复杂度
% data：一维时间序列
% lzm:信号的复杂度
% m: 将data原始序列分为m个符号序列
%U :分的时间区域
%%%%%%%%%%%%%%%%%%%%%%%%%%%

[symbolic_data, pointers] =  timeseries2symbol(data, length(data),U, m);
x= symbolic_data;


c = 1;                %模式初始值
S = x(1);
Q = [];
SQ = [];             %S Q SQ初始化
for i=2:length(x)
   Q = strcat(Q,x(i));
   SQ = strcat(S,Q);
   SQv = SQ(1:length(SQ)-1);
   if isempty(findstr(SQv,Q))     %如果Q不是SQv中的子串，说明Q是新出现的模式，执行c 加1操作 
     S = SQ;
     Q = [];
     c = c+1; 
   end
end

c=c+1;    %循环得到的c是字符串断点的数目，所以要加1
b = length(x)/log2(length(x));
lzm = c/b;
end