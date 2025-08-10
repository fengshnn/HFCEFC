import matplotlib.pyplot as plt
import pandas as pd
import os
import functions as fn
import numpy as np
# D:\file\Dataset\二沙数据\2022-04-09_103050
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']
file_Path = "D:/file/Dataset/二沙数据"  # 文件夹的绝对路劲
file_Name = os.path.basename(file_Path)
NormalBcgPath = file_Path + "/2022-04-09_104818/raw_xx.txt"  # 原始数据路径
ECGPath = file_Path + "/2022-04-09_104818/raw_ecg.txt"  # 体动数据路径
NormalBCG = pd.read_csv(NormalBcgPath, header=None).to_numpy().reshape(-1)  # 原始数据读取为numpy形式
ECG = pd.read_csv(ECGPath, header=None).to_numpy().reshape(-1)  # 标签数据读取为numpy形式，并reshape为n行4列的数组

NormalBCG = fn.Butterworth(NormalBCG, 1000, '带通', lowcut=2, highcut=8.5, order=4)
X1 = fn.xSet(NormalBCG, 1000)
ECG = fn.Butterworth(ECG, 1000, '带通', lowcut=2, highcut=20, order=4)
X2 = fn.xSet(ECG, 1000)
# BCG = NormalBCG[2000:3000]
# X3 = fn.xSet(BCG, 1000)

plt.figure()
# x_label = np.arange(0, 5000, 5)
# x_label = np.array(X1) / 100  # // sunshi
# plt.subplot(311)
plt.plot(X1, NormalBCG, color='b', label="BCG")
plt.plot(X2, 1.8*ECG+240, color='r', label="ECG")
plt.xticks(fontproperties='Times New Roman', size=18)
plt.legend(loc='upper left', ncol=3)
plt.legend(prop={'size': 15})
# plt.xticks(ticks=X1, labels=x_label)
# plt.subplot(312)
# plt.plot(X1, NormalBCG, color='b', label="健康样本BCG")
# plt.legend(loc='upper left', ncol=3, prop={'size': 15})
# # plt.legend(prop={'size': 14})
# plt.xticks(fontproperties='Times New Roman', size=18)
# # plt.title('BCG', fontsize=15)
# plt.subplot(313)
# plt.plot(X2, HFBCG, color='b', label="心衰患者BCG")
# plt.xlabel('Time(s)', fontsize=24)
# plt.xticks(fontproperties='Times New Roman', size=18)
# # plt.ylabel('Y Axis ：Voltage', fontsize=8)
# plt.legend(loc='upper right', ncol=3, prop={'size': 15})  # loc为Location Code ncol = 2为一行允许放入4个参数
# # plt.legend(prop={'size': 14})
plt.show()
