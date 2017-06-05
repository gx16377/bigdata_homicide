%% �ļ�����
f_1=5*12*28;
f_2=25*12*28;
f_3=5*12*28;
f_n='NNdata/Relationship.csv';
y_range=1;%����ǵڼ���
x_range=5:14;%ʹ�õ�feature
pca_n=0;
map=0;
%% ��ѵ��������
data_file=f_n;
data=csvread(data_file,f_1,0,[f_1,0,f_1+f_2-1,13]);
x=data(:,x_range)';
y=data(:,y_range)';
if map
    [x,inputps]=mapminmax(x,0,1);
    [y,outputps]=mapminmax(y,0,1);
end
if pca_n>0
	coef = princomp(x');
	x=(x'*coef(:,1:pca_n))';
end
%% �������������
hidden=[3];%������
net=newff(x,y,hidden);
net.trainFcn='trainlm';
if strcmp(net.trainFcn,'trainlm')
    %��ͨ��ѵ������
    net.trainParam.epochs=45;%����������
    net.trainParam.lr=1e-9;%ѧϰ��
    net.trainParam.goal=10;%Ŀ����
%     net.trainParam.max_fail=1;%�����֤���������ε����½���ֹͣ��Ĭ��6
    net.divideFcn='divideblock';
    net.divideParam.trainRatio=0.85;
    net.divideParam.valRatio=0.15;
    net.divideParam.testRatio=0;
elseif strcmp(net.trainFcn,'trainbr')
    net.trainParam.epochs=25;
%     net.trainParam.goal=0.00155;
%     net.trainParam.max_fail=2;
elseif strcmp(net.trainFcn,'trainrp')
     net.trainParam.epochs=2000;
     net.trainParam.max_fail=100;
elseif strcmp(net.trainFcn,'trainscg')
     net.trainParam.epochs=500;
     net.trainParam.max_fail=1000;
end
%% ѵ��
net=train(net,x,y);
%% �����Լ�����
data_file=f_n;
data_test=csvread(data_file,f_1+f_2,0,[f_1+f_2,0,f_1+f_2+f_3-1,13]);
x_test=data_test(:,x_range)';
y_test=data_test(:,y_range)';

if map
    x_test=mapminmax('apply',x_test,inputps);
end
if pca_n>0
	x_test=(x_test'*coef(:,1:pca_n))';
end
%% ����
output_test=sim(net,x_test);
if map
    output_test=mapminmax('reverse',output_test,outputps);
end
%% ��ʾ���
ground=mean(y_test)
error_avg=mean(abs(mean(data_test(:,5:9),2)-y_test'))
error_nn=mean(abs(y_test-output_test))

res=[data_test(:,2:4),data_test(:,1),output_test'];
NETIW=net.IW;
csvwrite('res/relationship_res.csv',res);