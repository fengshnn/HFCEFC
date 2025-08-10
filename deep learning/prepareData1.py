import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from scipy.io import loadmat # 用于加载mat文件

             # 1. 读入数据文件
#  -----  加载滤波后的原始信号数据----

#      -----     健康+心衰------------
Load_data1 =loadmat('10s_data/Sign_epoch_200hz.mat') #通道1的输入序列：BCG_epoch 加载BCG号序列;Sign_epoch_200hz  Sign_epoch_origin
data_load1 = Load_data1["Sign_epoch_H"]#我需要的是这个，BCG_epoch_H;Sign_epoch_H  Sign_epoch_origin_H,数据是以行保存的，最后一位是标签
BCG_data =pd.DataFrame(data_load1) #转换成pandas数据。
print(BCG_data)
#-------- 加载数据----
Load_data2 =loadmat('10s_data/RES_epoch.mat') #通道2的输入序列：加载RES信号序列
data_load2 = Load_data2["RES_epoch_H"]#我需要的是这个，
RES_data =pd.DataFrame(data_load2) #转换成pandas数据。

# -----对于EF2分级重新制作了标签
labEF3_epoch=loadmat('10s_data/labEF3_epoch.mat')  #健康，心衰（LVEF《40，》40）3分类
EF2_lab =labEF3_epoch["EFlab"]

Feature_data =pd.read_csv('10s_data/Data_1.csv', header = None) #手工特征，Data_1是33个特征
N_length_1= len(BCG_data.columns)-1 # 数据的列数，-1是减去标签列  #修改这里：序列的长度。

print('BCG_data:',BCG_data.iloc[0:5,:])
#
X_1 = BCG_data.iloc[:,0:N_length_1].values.astype(float)  #  数据，BCG序列#健康VS心衰3分类,10s片段
X_2 = RES_data.iloc[:,0:N_length_1].values.astype(float)  #  数据，RES序列#健康VS心衰3分类,10s片段

feature = Feature_data.iloc[:,0:33].values.astype(float)#健康VS心衰3分类,10s片段
# feature = Feature_data.iloc[2617:7830,0:33].values.astype(float)#心衰2分类,10s片段

# 标签y取值于第四列
# 将第6001列取出来，作为int型,标签
# y_1 = EF2_lab[:,0].astype(int)  #心衰患者2分级
y_1 = EF2_lab[:,0].astype(int)  #健康，心衰患者3分级

# 分割数据为训练集和测试集
from sklearn.model_selection import StratifiedKFold
# k=5折验证
skf = StratifiedKFold(n_splits=5,shuffle=True,random_state=20)# Standard 5-Fold
# skf = StratifiedKFold(n_splits=5,shuffle=False)#Group 5-Fold
skf.get_n_splits(X_1, y_1)  # 给出K折的折数，输出为5
print(skf)
# 输出为：StratifiedKFold(n_splits=2,random_state=None, shuffle=False)
i=1
for train_index, test_index in skf.split(X_1, y_1):
    print("第%d次训练:"%(i))

    print("TRAIN:", train_index, "TEST:", test_index)
    Xtrain1, Xtest1 = X_1[train_index], X_1[test_index] #BCG序列
    Ytrain1, Ytest1 = y_1[train_index], y_1[test_index] #标签
    Xtrain2, Xtest2 = X_2[train_index], X_2[test_index]  #呼吸序列

    Xtrain_feature, Xtest_feature = feature[train_index], feature[test_index]  #手工特征


    if i ==1:  # i=1,2,3,4,5修改这里，选择训练的样本集
        train_x_1   =  Xtrain1
        test_x_1    =  Xtest1
        train_y_1   =  Ytrain1
        test_y_1    =  Ytest1
        train_x_2 = Xtrain2
        test_x_2 = Xtest2

        train_XGBT  =  Xtrain_feature#手工特征
        test_XGBT   =  Xtest_feature
    i = i+1

print("--------------预处理---------------------------")

from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

# 实例化StandardScaler
scaler = StandardScaler()

# 特征数据标准化，转换为均值0，标准差为1的分布
train_x_1 = preprocessing.scale(train_x_1)  #标准化
test_x_1= preprocessing.scale(test_x_1)
train_x_2 = preprocessing.scale(train_x_2)  #标准化
test_x_2= preprocessing.scale(test_x_2)
train_XGBT = preprocessing.scale(train_XGBT)  #标准化
test_XGBT= preprocessing.scale(test_XGBT)


# 类别标签独热编码,2:2分类
train_y_ohe = to_categorical(train_y_1,3)
test_y_ohe = to_categorical(test_y_1, 3)

# print('BCG_data测试数据标签值:',test_y_1)
# print('RES_data测试数据标签值:',test_y_2)
# print('Sign_data测试数据标签值:',test_y_3)
# print('前五条测试数据标签的独热码：\n',test_y_ohe[0:50])
print("--------------END---------------------------")