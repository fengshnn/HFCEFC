function  lzc=CLZ(data)
%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ����һά�źŵĸ��Ӷ�
% data��һάʱ������
% lzc:�źŵĸ��Ӷ�
%%%%%%%%%%%%%%%%%%%%%%%%%%%

MeanData = mean(data);   % ���ݻ��ھ�ֵ�Ķ�ֵ������
b=(data> MeanData);
x(1:length(b))='0';            
x(b)='1';           %��ֵ����õ�01�����ַ�����
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
lzc = c/b;
end