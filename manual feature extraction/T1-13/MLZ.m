function  lzm=MLZ(data,U,m)
%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ����һά�źŵĸ��Ӷ�
% data��һάʱ������
% lzm:�źŵĸ��Ӷ�
% m: ��dataԭʼ���з�Ϊm����������
%U :�ֵ�ʱ������
%%%%%%%%%%%%%%%%%%%%%%%%%%%

[symbolic_data, pointers] =  timeseries2symbol(data, length(data),U, m);
x= symbolic_data;


c = 1;                %ģʽ��ʼֵ
S = x(1);
Q = [];
SQ = [];             %S Q SQ��ʼ��
for i=2:length(x)
   Q = strcat(Q,x(i));
   SQ = strcat(S,Q);
   SQv = SQ(1:length(SQ)-1);
   if isempty(findstr(SQv,Q))     %���Q����SQv�е��Ӵ���˵��Q���³��ֵ�ģʽ��ִ��c ��1���� 
     S = SQ;
     Q = [];
     c = c+1; 
   end
end

c=c+1;    %ѭ���õ���c���ַ����ϵ����Ŀ������Ҫ��1
b = length(x)/log2(length(x));
lzm = c/b;
end