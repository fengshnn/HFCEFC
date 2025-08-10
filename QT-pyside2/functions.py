# from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
# from PySide2.QtUiTools import QUiLoader
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from lib.share import SI
from scipy import signal
# from scipy.signal import butter, lfilter, filtfilt
import pandas as pd
import copy
import math


# from libtiff import TIFFfile

# from main import Win_Filter

# def toMovement(self):
#     SI.MorphologicalWin = main.Movement()
#     SI.MovementWin.ui.show()

def returnMain(self):
    SI.filterWin.ui.hide()
    SI.mainWin.ui.show()


def returnMain2(self):
    SI.MorphologicalWin.ui.hide()
    SI.mainWin.ui.show()


def returnMain3(self):
    SI.MovementWin.ui.hide()
    SI.mainWin.ui.show()


def returnMain3R(self):
    SI.MovementWin2.ui.hide()
    SI.mainWin.ui.show()


def returnMain4(self):
    SI.TemplateMatchingWin.ui.hide()
    SI.mainWin.ui.show()


def returnMain5(self):
    self.ui.hide()
    SI.mainWin.ui.show()


def OK(self):
    SI.butterMsg.ui.close()
    SI.filterWin.write()


def shutMsg(self):
    SI.butterMsg.ui.close()


def toHRWin(self):
    SI.HRWin.ui.show()


def xSet(data, fs):
    X = []
    for i in range(len(data)):
        j = i / fs
        X.append(j)
    return X


def nextPage(num1, num2, fs):
    x1 = SI.mainWin.ui.lineEdit.text()
    x = int(x1) * fs
    num1 += x
    num2 += x
    return num1, num2


def lastPage(num1, num2, fs):
    x1 = SI.mainWin.ui.lineEdit.text()
    x = int(x1) * fs
    num1 -= x
    num2 -= x
    return num1, num2


def Exit(self):
    SI.mainWin.ui.hide()
    SI.enterWin.ui.show()


def distEuclidean(veca, vecb):
    """
    计算欧几里得距离
    """
    return np.sqrt(np.sum(np.square(veca - vecb)))


def windows(data, num, croDot):
    """
    函数说明：
    对输入信号data分窗
    :param data:                  输入数据组
    :param num:                   输入规定每个窗的数据量
    :param croDot:                输入每个窗前后交叠长度
    :return:                      返还分窗后的二维数组 return[i][j]，i为第i个窗,j为第i个窗的第j个点
    """

    row = int(len(data) / num)
    returndata = []
    for i in range(row):
        if i == 0:
            returndata.append(data[0: num + croDot])
        else:
            returndata.append(data[num * i - croDot:num * (i + 1) + croDot])
    if row * num < len(data):
        returndata.append(data[row * num - croDot:])
    return returndata


def windows_r(data, num):
    """
    函数说明：
    对输入信号data分窗
    :param data:                  输入数据组
    :param num:                   输入规定每个窗的数据量
    :return:                      返还分窗后的二维数组 return[i][j]，i为第i个窗,j为第i个窗的第j个点
    """
    # list = num  # 每个窗num个点
    row = math.ceil(len(data) / num)
    returndata = []
    for i in range(row):
        if i == row:
            returndata.append(data[num * i: -1])
        else:
            returndata.append(data[num * i:num * (i + 1)])
    return returndata


def Artifacts_win(data, num, fs, t1, t2, t3, t4, q1, q2, q3, q4, d1, d2, d3, d4):
    [T1, T2, T3, T4] = sorted([t1, t2, t3, t4])
    # print('T1, T2, T3, T4:', T1, T2, T3, T4)
    m1 = int(fs * T1 / num)
    m2 = int(fs * T2 / num)
    m3 = int(fs * T3 / num)
    m4 = int(fs * T4 / num)
    # print('m1, m2, m3, m4:', m1, m2, m3, m4)
    Max_value_set = []
    state = []
    win = windows_r(data, num)
    for i in range(len(win)):
        Max_value = np.max(win[i])
        Max_value_set.append(Max_value)
    # len_30s = int(len(data) / 30000)
    # len_60s = int(len(data) / 60000)
    # len_120s = int(len(data) / 120000)
    # len_300s = int(len(data) / 300000)
    # print('m1, m2, m3, m4:', m1, m2, m3, m4)
    # print('max_value_set:', len(Max_value_set))
    i = 0
    while True:
        i_Count = 0
        if i + m4 <= len(Max_value_set):
            Max_value_30s = Max_value_set[i:i + m1]  # 提取30s内的最大值（15个2s的最大值）
            Max_value_60s = Max_value_set[i:i + m2]  # 提取60s内的最大值（30个2s的最大值）
            Max_value_120s = Max_value_set[i:i + m3]  # 提取120s内的最大值（60个2s的最大值）
            Max_value_300s = Max_value_set[i:i + m4]  # 提取300s内的最大值（150个2s的最大值）

        elif i + m4 > len(Max_value_set) and i + m3 <= len(Max_value_set):
            Max_value_30s = Max_value_set[i:i + m1]  # 提取30s内的最大值（15个2s的最大值）
            Max_value_60s = Max_value_set[i:i + m2]  # 提取60s内的最大值（30个2s的最大值）
            Max_value_120s = Max_value_set[i:i + m3]  # 提取120s内的最大值（60个2s的最大值）
            Max_value_300s = Max_value_set[i:-1]  # 提取300s内的最大值（150个2s的最大值）
        elif i + m3 > len(Max_value_set) and i + m2 <= len(Max_value_set):
            Max_value_30s = Max_value_set[i:i + m1]  # 提取30s内的最大值（15个2s的最大值）
            Max_value_60s = Max_value_set[i:i + m2]  # 提取60s内的最大值（30个2s的最大值）
            Max_value_120s = Max_value_set[i:-1]  # 提取120s内的最大值（60个2s的最大值）
            Max_value_300s = Max_value_set[i:-1]  # 提取300s内的最大值（150个2s的最大值）
        elif i + m2 > len(Max_value_set) and i + m1 <= len(Max_value_set):
            Max_value_30s = Max_value_set[i:i + m1]  # 提取30s内的最大值（15个2s的最大值）
            Max_value_60s = Max_value_set[i:-1]  # 提取60s内的最大值（30个2s的最大值）
            Max_value_120s = Max_value_set[i:-1]  # 提取120s内的最大值（60个2s的最大值）
            Max_value_300s = Max_value_set[i:-1]  # 提取300s内的最大值（150个2s的最大值）
        else:
            Max_value_30s = Max_value_set[i:-1]  # 提取30s内的最大值（15个2s的最大值）
            Max_value_60s = Max_value_set[i:-1]  # 提取60s内的最大值（30个2s的最大值）
            Max_value_120s = Max_value_set[i:-1]  # 提取120s内的最大值（60个2s的最大值）
            Max_value_300s = Max_value_set[i:-1]  # 提取300s内的最大值（150个2s的最大值）

        Quartile_30s = np.percentile(Max_value_30s, 25)
        Quartile_60s = np.percentile(Max_value_60s, 25)
        Quartile_120s = np.percentile(Max_value_120s, 25)
        Quartile_300s = np.percentile(Max_value_300s, 25)

        Q1_30s = Quartile_30s * q1  # 提取30s内最大值的四分位数的1.5倍作为上基线
        Q1_60s = Quartile_60s * q2  # 提取60s内最大值的四分位数的1.5倍作为上基线
        Q1_120s = Quartile_120s * q3  # 提取120s内最大值的四分位数的1.5倍作为上基线
        Q1_300s = Quartile_300s * q4  # 提取300s内最大值的四分位数的1.5倍作为上基线
        down_Q1_30s = Quartile_30s / d1  # 提取30s内最大值的四分位数的1.5倍作为下基线
        down_Q1_60s = Quartile_60s / d2  # 提取60s内最大值的四分位数的1.5倍作为下基线
        down_Q1_120s = Quartile_120s / d3  # 提取120s内最大值的四分位数的1.5倍作为下基线
        down_Q1_300s = Quartile_300s / d4  # 提取300s内最大值的四分位数的1.5倍作为下基线
        # print('Q1_30s', Q1_30s)
        # print('Q1_60s', Q1_60s)
        # print('Q1_120s', Q1_120s)
        # print('Q1_300s', Q1_300s)
        if Max_value_set[i] > Q1_30s or Max_value_set[i] < down_Q1_30s:
            i_Count = i_Count + 1
        if Max_value_set[i] > Q1_60s or Max_value_set[i] < down_Q1_60s:
            i_Count = i_Count + 1
        if Max_value_set[i] > Q1_120s or Max_value_set[i] < down_Q1_120s:
            i_Count = i_Count + 1
        if Max_value_set[i] > Q1_300s or Max_value_set[i] < down_Q1_300s:
            i_Count = i_Count + 1

        if i_Count > 1:
            state.append("Movement")
        else:
            state.append("Sleep")

        i = i + 1

        if i > len(Max_value_set) - 2:
            break

    new_state = copy.deepcopy(state)
    for i in range(len(state) - 1):  # 将体动前后2s的窗口都设置为体动
        if state[i] == "Movement":
            if i == 1:  # 如果第一个窗口就是体动，则只将后一个2s置为体动
                new_state[i + 1] = "Movement"
            else:
                new_state[i - 1] = "Movement"
                new_state[i + 1] = "Movement"
        else:
            pass
    # print('new_state:', new_state)
    Count_index = 0
    count = 0
    i = 0
    start_matrix = []
    end_matrix = []
    count_matrix = []
    while True:
        # print('i:', i)
        if i > len(new_state) - 1:
            break
        if new_state[i] == "Sleep" and Count_index == 0 and count == 0:
            i = i + 1
            pass
        elif new_state[i] == "Movement" and Count_index == 0 and count == 0:
            Count_index = 1
            start_index = i
            i = i + 1
        elif new_state[i] == "Movement" and Count_index == 1 and count == 0:
            Count_index = 1
            start_index = i
            # print('start_index:', start_index)
            i = i + 1
        elif new_state[i] == "Sleep" and Count_index == 1:
            count = count + 1
            i = i + 1
        elif new_state[i] == "Movement" and Count_index == 1 and count != 0:
            Count_index = 0
            end_index = i
            # print('end_index', end_index)
            start_matrix.append(start_index)
            end_matrix.append(end_index)
            count_matrix.append(count)
            # print('count_matrix:', count_matrix)
            count = 0
            i = i + 1
    for i in range(len(start_matrix)):
        if 0 < count_matrix[i] <= 5:
            list = ["Movement" for x in range(end_matrix[i] - start_matrix[i])]
            new_state[start_matrix[i]:end_matrix[i]] = list

        #     print('start:', start_matrix[i])
        #     print('end_matrix', end_matrix[i])
        # print('newstate:', new_state)
    return np.array(new_state)


def CutData(data, state, wins):
    """
    函数说明：根据数组state的不同状态，对数据进行划分
    :param wins:                        每个窗口数据点数
    :param data:                        输入信号数组
    :param state:                       输入状态数组
    :return:                            返还切割后信号数组
    """
    Movestate = np.argwhere(state == "Movement").flatten().astype(int)
    cutdata = np.full(len(data), np.nan)
    MovementData = np.full(len(data), np.nan)
    mark = []
    count = 0
    if len(Movestate) == 0:
        mark.append(0)
        cutdata = data
        return cutdata, MovementData, mark
    for num in Movestate:
        if count != num * wins:
            cutdata[count:num * wins] = data[count:num * wins]
            # cutdata.append(data[count:num * wins])
            mark.append(count)
        else:
            pass
        count = (num + 1) * wins
    if Movestate[-1] == int(len(data) / wins - 1):
        pass
    else:
        cutdata[(Movestate[-1] + 1) * wins:] = (data[(Movestate[-1] + 1) * wins:])
        # cutdata.append(data[(Movestate[-1] + 1) * wins:])
        mark.append((Movestate[-1] + 1) * wins)
    for i in range(len(data)):
        if cutdata[i] != data[i]:
            MovementData[i] = data[i]
        else:
            pass

    return cutdata, MovementData, mark


def Movement_Remove(data, state, wins):
    """
    函数说明：根据数组state的不同状态，对数据进行划分
    :param wins:                        每个窗口数据点数
    :param data:                        输入信号数组
    :param state:                       输入状态数组
    :return:                            返还切割后信号数组
    """
    Movestate = np.argwhere(state == "Movement").flatten().astype(int)
    cutdata = []
    mark = []
    count = 0
    if len(Movestate) == 0:
        mark.append(0)
        cutdata.append(data)
        return cutdata, mark
    for num in Movestate:
        if count != num * wins:
            cutdata.append(data[count:num * wins])
            mark.append(count)
        else:
            pass
        count = (num + 1) * wins
    if Movestate[-1] == int(len(data) / wins - 1):
        pass
    else:
        cutdata.append(data[(Movestate[-1] + 1) * wins:])
        mark.append((Movestate[-1] + 1) * wins)
    return cutdata, mark


def Butterworth(dataIn, fs, type, lowcut=0, highcut=0, order=4):
    """
    函数说明：
    将输入信号dataIn，经过一Butterworth滤波器后，输出信号
    :param dataIn:                        输入处理信号
    :param type:                     滤波类型(lowpass,highpass,bandpass)
    :param lowcut:                   低频带截止频率
    :param highcut:                  高频带截止频率
    :param order:                    滤波器阶数
    :return:                         返还处理后的信号
        """
    # print('fs:', fs)
    if type == "低通":  # 低通滤波处理
        b, a = signal.butter(order, lowcut / (fs * 0.5), btype='lowpass')
        return signal.filtfilt(b, a, np.array(dataIn))
    elif type == "带通":  # 带通滤波处理
        low = lowcut / (fs * 0.5)
        high = highcut / (fs * 0.5)
        b, a = signal.butter(order, [low, high], btype='bandpass')
        return signal.filtfilt(b, a, np.array(dataIn))
    elif type == "高通":  # 高通滤波处理
        b, a = signal.butter(order, highcut / (fs * 0.5), btype='highpass')
        return signal.filtfilt(b, a, np.array(dataIn))
    else:  # 警告,滤波器类型必须有
        print("Please choose a type of fliter")


def Dilate(x, N, g, M):
    """
    函数说明：
    对输入信号进行膨胀运算
    :param x:                     信号数据
    :param N:                     信号长度N
    :param g:                     结构信号
    :param M:                     结构信号长度M
    :return:
    """
    returndata = np.array([])
    for num in range(N - M + 1):
        returndata = np.append(returndata, np.min(np.array(x[num:num + M]) - np.array(g)))
    return returndata


def Eorde(x, N, g, M):
    """
    函数说明：
    对输入信号进行腐蚀运算
    :param x:                     信号数据
    :param N:                     信号长度N
    :param g:                     结构信号
    :param M:                     结构信号长度M
    :return:
    """
    returndata = np.array([])
    for num in range(N - M + 1):
        returndata = np.append(returndata, np.max(np.array(x[num:num + M]) - np.array(g)))
    return returndata


def Preprocessing2(data, fs, Rlowcut, Rhighcut, fb1=2, fb2=8.5, orderBCG=4):
    """
    对输入信号进行预处理:
           1.低通滤波
           2.移除基线(形态滤波)
    :param data:        输入信号数据
    :return:            预处理后的信号数据
    """
    data = Butterworth(np.array(data), fs, type="低通", lowcut=20, order=4)
    # 结构元宽度M，选择为采样频率的18%
    M = int(fs * 0.2)
    g = np.ones(M)
    Data_pre = np.insert(data, 0, np.zeros(M))
    Data_pre = np.insert(Data_pre, -1, np.zeros(M))
    # 开运算:腐蚀+膨胀
    out1 = Eorde(Data_pre, len(Data_pre), g, M)  # 腐蚀
    out2 = Dilate(out1, len(out1), g, M)  # 膨胀
    out2 = np.insert(out2, 0, np.zeros(M - 2))
    # 闭运算:膨胀+腐蚀+腐蚀+膨胀
    out5 = Dilate(Data_pre, len(Data_pre), g, M)  # 膨胀
    out6 = Eorde(out5, len(out5), g, M)  # 腐蚀
    out6 = np.insert(out6, 0, np.zeros(M - 2))

    baseline = (out2 + out6) / 2

    # -------------------------保留剩余价值------------------------
    returndata = Data_pre[:len(baseline)] - baseline
    returndata = np.delete(returndata, range(0, 200), axis=0)
    returndata = returndata[:len(data)]
    baseline = baseline[200:]
    returndata[-1] = returndata[-2] = returndata[-3]
    baseline[-1] = baseline[-2] = baseline[-3]
    # -----------------------------------------------------------

    Resp = Butterworth(baseline, fs, type="带通", lowcut=Rlowcut, highcut=Rhighcut, order=2)

    returndata = Butterworth(np.array(returndata), fs, type="带通", lowcut=fb1, highcut=fb2, order=orderBCG)

    return returndata, Resp


def Modeldetect(data, ModelLength, Jpeak, ECG=[]):
    """
    函数说明：对信号data进行模板检测。检通过选取每段之间的最大值为疑似J峰，然后相加平均形成模板
    :param data:                     输入待检测模板信号
    :param ModelLength:              输入模板长度
    :param Jpeak:                    输入预设J峰值
    :return:                         返还模板信号
    """
    test = []
    np.seterr(divide='ignore', invalid='ignore')
    for peak in Jpeak:
        if peak < ModelLength / 2 or (peak + ModelLength) > len(data):
            continue
        else:
            test.append(data[int(peak - (0.4 * ModelLength)):int(peak + (0.6 * ModelLength))])
    meanBCG = np.zeros(ModelLength)  # ----------------------对初始预判J峰的信号段相加平均
    for num in range(len(test)):
        meanBCG += test[num]
    meanBCG = meanBCG / len(test)
    dit = np.array([])  # ----------------------计算初始预判信号与平均信号的相似性
    for num in range(len(test)):
        # para = 2 - ASD(test[num], meanBCG) / SAD(test[num], meanBCG)
        dit = np.append(dit, distEuclidean(test[num], meanBCG) * 1)

    indexmin = np.array([])  # -----------------------选择与平均信号最相似的3个原始信号
    for num in range(1):
        if len(dit) > 1:
            indexmin = np.append(indexmin, np.argmin(dit))  # -----------取形态距最小值的索引
            dit[np.argmin(dit)] = float("inf")  # ----------将所取索引位置数值置为正无穷
        else:
            pass
    indexmin = indexmin.astype(int)

    Model = np.zeros(ModelLength)
    for num in indexmin:
        Model += test[num]
    Model = Model / 1

    # --------------------------------------
    chooseJ = np.full(len(data), np.nan)
    for num in np.array(Jpeak).astype(int):
        chooseJ[num] = data[num]

    chooseModel = []
    for num in indexmin:
        chooseModel.append(test[num])

    ChooseBCG = np.full(len(data), np.nan)
    for num in indexmin:
        ChooseBCG[int(Jpeak[num]) - int(0.2 * ModelLength):int(Jpeak[num]) + int(0.8 * ModelLength)] = data[int(
            Jpeak[num]) - int(0.2 * ModelLength):int(Jpeak[num]) + int(0.8 * ModelLength)]
    return Model


def ReModel(data, ModelLength, Jpeak, per, ECG=[]):
    """
    函数说明：对信号data进行模板检构建。检通过选取每段之间的最大值为疑似J峰，然后相加平均形成模板
    :param data:                     输入待检测模板信号
    :param ModelLength:              输入模板长度
    :param Jpeak:                    输入预设J峰值
    :return:                         返还模板信号
    """
    test = []
    np.seterr(divide='ignore', invalid='ignore')
    for peak in Jpeak:
        if peak < ModelLength / 2 or (peak + ModelLength) > len(data):
            continue
        else:
            test.append(data[int(peak - (0.4 * ModelLength)):int(peak + (0.6 * ModelLength))])
    meanBCG = np.zeros(ModelLength)  # ----------------------对初始预判J峰的信号段相加平均
    for num in range(len(test)):
        meanBCG += test[num]
    meanBCG = meanBCG / len(test)
    dit = np.array([])  # ----------------------计算初始预判信号与平均信号的相似性
    for num in range(len(test)):
        # para = 2 - ASD(test[num], meanBCG) / SAD(test[num], meanBCG)
        dit = np.append(dit, distEuclidean(test[num], meanBCG) * 1)
    n = int(np.percentile(dit, per))  # 计算分位数值
    l = 0
    for i in dit:
        if i < n:
            l += 1

    indexmin = np.array([])  # -----------------------选择与平均信号最相似的3个原始信号
    for num in range(l):
        if len(dit) > l:
            indexmin = np.append(indexmin, np.argmin(dit))  # -----------取形态距最小值的索引
            dit[np.argmin(dit)] = float("inf")  # ----------将所取索引位置数值置为正无穷
        else:
            pass
    indexmin = indexmin.astype(int)

    Model = np.zeros(ModelLength)
    for num in indexmin:
        Model += test[num]
    return Model


def ReModel2(data, meanModel, ModelLength, Jpeak, per, ECG=[]):
    """
    函数说明：对信号data进行模板检构建。检通过选取每段之间的最大值为疑似J峰，然后相加平均形成模板
    :param data:                     输入待检测模板信号
    :param ModelLength:              输入模板长度
    :param Jpeak:                    输入预设J峰值
    :return:                         返还模板信号
    """
    test = []
    np.seterr(divide='ignore', invalid='ignore')
    for peak in Jpeak:
        if peak < ModelLength / 2 or (peak + ModelLength) > len(data):
            continue
        else:
            test.append(data[int(peak - (0.4 * ModelLength)):int(peak + (0.6 * ModelLength))])
    dit = np.array([])  # ----------------------计算初始预判信号与平均信号的相似性
    for num in range(len(test)):
        # para = 2 - ASD(test[num], meanBCG) / SAD(test[num], meanBCG)
        dit = np.append(dit, distEuclidean(test[num], meanModel) * 1)
    n = int(np.percentile(dit, per))  # 计算分位数值
    l = 0
    for i in dit:
        if i < n:
            l += 1
    indexmin = np.array([])  # -----------------------选择与平均模板最相似的l个原始信号
    for num in range(l):
        if len(dit) > l:
            indexmin = np.append(indexmin, np.argmin(dit))  # -----------取形态距最小值的索引
            dit[np.argmin(dit)] = float("inf")  # ----------将所取索引位置数值置为正无穷
        else:
            pass
    indexmin = indexmin.astype(int)
    Model = np.zeros(ModelLength)
    for num in indexmin:
        Model += test[num]
    # print('model1:', Model)
    Model = Model / len(indexmin)
    return Model


def InitBeatDetect(data, l1, l2, style="peak"):
    """
    函数说明：
    查找合理心跳点
    :param data:                  输入数据信号
    :param maxi_index:            输入数据峰值坐标
    :return:                      处理后的峰值坐标
    """
    length = len(data)
    # 创建新的索引和返回信号
    index = []
    # 创建当前峰和识别窗
    win_min = 0
    win_max = 900
    while (True):
        vally = int(np.argmin(data[win_min:win_max]) + win_min)
        if style == "peak":
            if vally > win_min:
                beat = int(np.argmax(data[win_min:vally]) + win_min)
            else:
                beat = int(np.argmax(data[win_min:win_max]) + win_min)
        else:
            beat = int(np.argmin(data[win_min:win_max]) + win_min)
        index.append(beat)
        win_min = max(0, beat + l1)
        win_max = min(length, beat + l2)
        if (win_min >= length):
            break
    return np.array(index)


def RespBeatDetect(data, l1, l2, style="peak"):
    """
    函数说明：
    查找合理心跳点
    :param data:                  输入数据信号
    :param maxi_index:            输入数据峰值坐标
    :return:                      处理后的峰值坐标
    """
    length = len(data)
    # 创建新的索引和返回信号
    index = []
    # 创建当前峰和识别窗
    win_min = 100
    win_max = 5000
    while (True):
        vally = int(np.argmin(data[win_min:win_max]) + win_min)
        if style == "peak":
            if vally > win_min:
                beat = int(np.argmax(data[win_min:vally]) + win_min)
            else:
                beat = int(np.argmax(data[win_min:win_max]) + win_min)
        else:
            beat = int(np.argmin(data[win_min:win_max]) + win_min)
        index.append(beat)
        win_min = max(0, beat + l1)
        win_max = min(length, beat + l2)
        if (win_min >= length):
            break
    return np.array(index)


def windows_2(data, num):
    """
    函数说明：
    对输入信号data分窗
    :param data:                  输入数据组
    :param num:                   输入规定每个窗的数据量
    :return:                      返还分窗后的二维数组 return[i][j]，i为第i个窗,j为第i个窗的第j个点
    """
    list = num  # 每个窗num个点
    row = int(len(data) / list)
    returndata = np.zeros((row, list))
    for i in range(row):
        for j in range(list):
            returndata[i][j] = data[i * num + j]
    return returndata


def Statedetect(data, threshold, wins):
    """
    函数说明：
    将输入生理信号进行处理，移除大体动以及空床状态，只保留正常睡眠
    :param data:                输入信号数据
    :param wins:                输入规定每个窗的数据量
    :param threshold:           设置空床门槛
    :return:                    返还剩余的正常睡眠信号
    """
    win = windows(data, wins, 1000)
    win = np.array(win, dtype=object)
    # win = windows_2(data, wins)
    SD = np.zeros(win.shape[0])
    Mean = np.zeros(win.shape[0])
    state = []
    for i in range(win.shape[0]):
        SD[i] = np.std(np.array(win[i]), ddof=1)
        Mean[i] = np.mean(np.array(abs(win[i])))
    Median_SD = np.median(SD)
    Median_Mean = np.median(Mean)
    for i in range(len(SD)):
        # print('i:', i)
        if SD[i] > (Median_SD * 1.5) or Mean[i] > (Median_Mean) + 50 or Mean[i] < (Median_Mean - 50):
            state.append("Movement")
        elif SD[i] < threshold:
            state.append("Movement")
        else:
            state.append("Sleep")

    new_state = copy.deepcopy(state)
    for i in range(len(state) - 1):  # 将体动前后2s的窗口都设置为体动
        if state[i] == "Movement":
            if i == 0:  # 如果第一个窗口就是体动，则只将后一个2s置为体动
                new_state[i + 1] = "Movement"
            else:
                new_state[i - 1] = "Movement"
                new_state[i + 1] = "Movement"
        else:
            pass
    state = np.array(new_state)
    print('state:', state)
    return np.array(state)


def findpeak(data):
    """
    :param data:                  输入序列信号
    :return:                      返还峰峰值对应的坐标数组( 峰峰值相隔>1s )
    """
    # 建立峰峰值数组和其对应的坐标
    maxi = np.zeros(len(data) - 2)
    maxi_index = []
    # 获取峰峰值点对应的x坐标
    for i in range(1, len(data) - 2):
        maxi[i] = np.where([(data[i] - data[i - 1] > 0) & (data[i] - data[i + 1] > 0)], data[i], np.nan)
        if np.isnan(maxi[i]):
            continue
        maxi_index.append(i)
    return np.array(maxi_index)


def findtrough(data):
    """
    函数说明：
    查找出输入信号的峰值点
    :param data:                  输入序列信号
    :return:                      返还峰值信号，非峰值点的信号段为np.nan
    """
    # 建立峰峰值数组和其对应的坐标
    mini = np.zeros(len(data) - 2)
    a = []
    mini_index = np.array(a)
    # 获取峰峰值点对应的x坐标
    for i in range(1, len(data) - 2):
        mini[i] = np.where([(data[i] - data[i - 1] < 0) & (data[i] - data[i + 1] < 0)], data[i], np.nan)
        if np.isnan(mini[i]):
            continue
        mini_index = np.append(mini_index, i)
    return np.array(mini_index)


def BeatDetection(data, envelop, MeanRR, up=1.86, down=0.53, style="peak"):
    """
    前向检测,根据Style选择合适的心跳位置
    :param data:                   输入数据信息
    :param up:                     上限倍数 Default = 1.86
    :param down:                   下限倍数 Default = 0.53
    :param style:                  根据峰或谷
    :return:                       心跳位置
    """
    length = len(data)
    envelop = np.array(envelop)
    data = np.array(data)

    # 心跳位置的索引
    index = []
    # 设置初始窗口
    win_min = 0
    win_max = 150
    if style == "peak":
        while (True):
            peak = findpeak(data[win_min:win_max]) + win_min

            peak = peak.astype(int)
            # print('peak:', peak)
            if len(peak) == 0:
                break
            peakmax = np.argmax(data[peak])
            beat = peak[peakmax]
            # print('beat:', beat)
            if len(index) == 0:  # 首个检测
                if (beat > MeanRR * 1.2) and len(peak) > 1:  # 间隔过大，查询包络是否有峰值
                    EnvelopPeak = findpeak(envelop[win_min:win_min + 100]) + win_min
                    if len(EnvelopPeak) == 0:
                        index.append(beat)
                    else:
                        peak = findpeak(data[win_min:win_min + 100]) + win_min
                        peak = peak.astype(int)
                        peakmax = np.argmax(data[peak])
                        beat = peak[peakmax]
                        index.append(beat)
                else:
                    index.append(beat)
            else:
                dit = beat - index[-1]
                if len(index) == 1:
                    std = MeanRR
                else:
                    std = np.mean(np.append(np.diff(index), MeanRR))
                    # std = MeanRR
                while ((dit > (std * 1.4)) or (dit < (std / 1.4))) and (len(peak) > 1):
                    if (dit > (std * 1.4)):
                        EnvelopPeak = findpeak(envelop[win_min:win_min + 50]) + win_min
                        if len(EnvelopPeak) == 0:
                            peak = np.delete(peak, peakmax)
                            peakmax = np.argmax(data[peak])
                            Senbeat = peak[peakmax]
                            if data[Senbeat] > data[beat] * 0.9:
                                beat = Senbeat
                            else:
                                break
                            dit = beat - index[-1]
                        else:
                            peak = findpeak(data[win_min:win_min + 50]) + win_min
                            peak = peak.astype(int)
                            if (len(peak) == 0):
                                break
                            peakmax = np.argmax(data[peak])
                            Senbeat = peak[peakmax]
                            beat = Senbeat
                            dit = beat - index[-1]
                    elif dit < (std / 1.4):
                        peak = np.delete(peak, peakmax)
                        peakmax = np.argmax(data[peak])
                        Senbeat = peak[peakmax]
                        if data[Senbeat] > data[beat] * 0.9:
                            beat = Senbeat
                        else:
                            break
                        dit = beat - index[-1]
                    elif dit > up * std or dit < down * std:
                        peak = np.delete(peak, peakmax)
                        peakmax = np.argmax(data[peak])
                        beat = peak[peakmax]
                        dit = beat - index[-1]
                    else:
                        break

                index.append(beat)
            win_min = max(0, index[-1] + 50)
            win_max = min(length, index[-1] + 150)
            if (win_min > length - 3):
                break
    else:
        print("Vally is not exist!")
        while (True):
            peak = findtrough(data[win_min:win_max])
            peak = peak + win_min
            peak = peak.astype(int)
            if len(peak) == 0:
                break
            peakmax = np.argmax(data[peak])
            beat = peak[peakmax]
            if len(index) < 2:  # 首个检测
                if (beat > MeanRR * 1.2) and len(peak) > 1:  # 间隔过大，查询包络是否有峰值
                    EnvelopPeak = findpeak(envelop[win_min:beat])
                    if len(EnvelopPeak) == 0:
                        index.append(beat)
                    else:
                        peak = np.where(peak < (EnvelopPeak[0] + 300))
                        peakmax = np.argmax(data[peak])
                        beat = peak[peakmax]
                        index.append(beat)
                else:
                    index.append(beat)
            else:
                dit = beat - index[-1]
                std = np.mean(np.diff(index))
                std = (std + MeanRR) / 2
                while (dit > std * up) or (dit < std * down) and len(peak) > 1:
                    EnvelopPeak = findpeak(envelop[win_min:beat])
                    if len(EnvelopPeak) == 0:
                        peak = np.delete(peak, peakmax)
                        peakmax = np.argmax(data[peak])
                        beat = peak[peakmax]
                        dit = beat - index[-1]
                    else:

                        peak = np.where(peak < (EnvelopPeak[0] + 300))
                        peakmax = np.argmax(data[peak])
                        Senbeat = peak[peakmax]
                        if data[Senbeat] > data[beat] * 0.4:
                            beat = Senbeat
                        else:
                            beat = beat
                        dit = beat - index[-1]

                index.append(beat)
            win_min = max(0, index[-1] + 500)
            win_max = min(length, index[-1] + 1500)
            if (win_min > length - 3):
                break
    # print('index:', index)
    return index


def BeatChoose(cor_f, cor_b, dit_f, dit_b, initInterval):
    """
    函数解释:根据Cor和Dit曲线检测的心跳位置，来定位最终心跳位置
    :param cor_f:               相关前向检测心跳位置
    :param cor_b:               相关后向检测心跳位置
    :param dit_f:               距离前向检测心跳位置
    :param dit_b:               距离后向检测心跳位置
    :param BCGCor:              BCG相关曲线
    :return:                    最终确定的心跳位置
    """
    print('cor_f', len(cor_f))
    BeatPosition = np.array([])
    num0, num1, num2, num3 = 0, 0, 0, 0
    while (True):
        if num0 >= len(cor_f) or num1 >= len(cor_b) or num2 >= len(dit_f) or num3 >= len(dit_b):
            break
        else:
            beat = np.array([
                cor_f[num0], cor_b[num1],
                dit_f[num2], dit_b[num3]
            ])

            # 移除间隔小于500的点
            beat_detect = np.array([0, 1, 2, 3])
            if len(BeatPosition) > 0:
                beat_detect = np.where((beat - BeatPosition[-1]) < 500)[0]
                if len(beat_detect) == 0:
                    pass
                else:
                    if 0 in beat_detect:
                        num0 = num0 + 1
                    if 1 in beat_detect:
                        num1 = num1 + 1
                    if 2 in beat_detect:
                        num2 = num2 + 1
                    if 3 in beat_detect:
                        num3 = num3 + 1
                    continue
            else:
                pass

            # 找出最小位置
            if len(BeatPosition) > 2:
                initInterval = (initInterval + np.mean(np.diff(BeatPosition))) // 2

            Minibeat = np.min(beat)
            beat_choose = np.where((beat - Minibeat) <= (initInterval // 2))[0]

            case1 = False  # cor b=f
            case2 = False  # dit b=f

            if 1 and 0 in beat_choose:
                if abs(beat[0] - beat[1]) < 30:
                    case1 = True
                else:
                    case1 = False
            else:
                case1 = False

            if 2 and 3 in beat_choose:
                if abs(beat[2] - beat[3]) < 30:
                    case2 = True
                else:
                    case2 = False
            else:
                case2 = False

            beat = np.array(beat[beat_choose])

            if len(beat) > 0:

                if case2 and case1:
                    pos = np.mean(beat)
                elif case1:
                    pos = beat[0]
                elif case2:
                    pos = beat[-1]
                else:
                    beat = beat.astype(int)
                    if len(beat) == 1:  # 长度为1时，取该点BCGCor和前3个心跳的BCGCor相比较,再和前面的RR间期相比较
                        pos = beat[0]
                    else:
                        pos = np.mean(beat)  # 取平均作预估心跳点
                # ----------判断间期是否接受
                if pos == 0:
                    pass
                elif len(BeatPosition) == 1:
                    if 500 < pos - BeatPosition[-1] < 2000:
                        BeatPosition = np.append(BeatPosition, pos)
                    else:
                        pass
                elif len(BeatPosition) > 1:
                    Interval = BeatPosition[-1] - BeatPosition[-2]
                    if 500 < pos - BeatPosition[-1] < 2000:
                        BeatPosition = np.append(BeatPosition, pos)
                    elif (pos - BeatPosition[-1] > 2001):
                        BeatPosition = np.append(BeatPosition, pos)
                    else:
                        pass
                # 首个不用判断
                else:
                    BeatPosition = np.append(BeatPosition, pos)
            else:
                pass
            # ----------num+1
            if 0 in beat_choose or 0 in beat_detect:
                num0 = num0 + 1
            if 1 in beat_choose or 1 in beat_detect:
                num1 = num1 + 1
            if 2 in beat_choose or 2 in beat_detect:
                num2 = num2 + 1
            if 3 in beat_choose or 3 in beat_detect:
                num3 = num3 + 1

    return BeatPosition


def fineTun(data, peaks, th=200):
    return_peak = []
    for peak in peaks:
        if peak > len(data): continue
        min_win, max_win = max(0, int(peak - th)), min(len(data), int(peak + th))
        new_peakindex = findpeak(data[min_win: max_win]) + min_win
        new_index = np.argmax(data[min_win: max_win]) + min_win
        if new_index in new_peakindex:
            return_peak.append(new_index)
    return return_peak


def dotCompute(data):
    datax = []
    datay = []
    for i in range(len(data) - 2):
        x = data[i + 1] - data[i]
        y = data[i + 2] - data[i + 1]
        datax.append(x)
        datay.append(y)
    return datax, datay


def SNR(data, beat, Modellength):
    """
    :param data:            输入信号数据
    :param beat:            输入定位的心搏
    :return:                输入信噪比
    """
    BCG = [[] for i in range(5)]
    BCG_all = []
    for b in beat:
        if b < 0.4 * Modellength or b > len(data) - 0.6 * Modellength:
            continue
        BCG_all.append(data[b - int(0.4 * Modellength): b + int(0.6 * Modellength)])
    BCG_mean = np.mean(BCG_all, axis=0)
    BCG_noise = [BCG - BCG_mean for BCG in BCG_all]
    BCG_noise = np.var(BCG_noise, axis=0)
    SNR = math.log((np.sum(BCG_mean ** 2) / (np.mean(BCG_noise) * Modellength)), 10) * 10
    return SNR


def SNR2(data, beat, Modellength):
    """
    :param data:            输入信号数据
    :param beat:            输入定位的心搏
    :return:                输入信噪比
    """
    BCG = [[] for i in range(5)]
    BCG_mean = np.mean(data, axis=0)
    BCG_noise = [BCG - BCG_mean for BCG in data]
    BCG_noise = np.var(BCG_noise, axis=0)
    SNR = math.log((np.sum(BCG_mean ** 2) / (np.mean(BCG_noise) * Modellength)), 10) * 10
    return SNR


def tSQI(data, beat, Modellength):
    """
    函数说明：计算信号段内两两心跳的相关系数来评估信号质量
    :param data:            输入信号段
    :param beat:            输入心搏位置
    :return:                tSQI ( tSQI = \sum{ c_ij } i,j 属于 [0,M) )
    """
    print('beat:', beat)
    print('Modellength:', Modellength)
    # print('data', data)
    beat_segment = []
    for index in beat:
        if index < 0.4 * Modellength or index > len(data) - 0.6 * Modellength:
            continue
        beat_segment.append(data[index - int(0.4 * Modellength): index + int(0.6 * Modellength)])
    if len(beat_segment) <= 1:  # 若检测到的心搏数少于2个，直接返回0
        return 0
    else:
        corrcoef = np.corrcoef(beat_segment)  # 计算两两心搏的相关系数
        return np.sum(corrcoef) / (corrcoef.shape[0] ** 2)


def Cor(data):
    """
    函数说明：计算信号段内两两心跳的相关系数来评估信号质量
    :param data:            输入信号段
    :param beat:            输入心搏位置
    :return:                tSQI ( tSQI = \sum{ c_ij } i,j 属于 [0,M) )
    """
    beat_segment = []
    if len(data) <= 1:  # 若检测到的心搏数少于2个，直接返回0
        return 0
    else:
        corrcoef = np.corrcoef(data)  # 计算两两心搏的相关系数
        # print('corrcoef:', corrcoef)
        # print('corrcoef.shape[0]', corrcoef.shape[0])
        return np.sum(corrcoef) / (corrcoef.shape[0] ** 2)


def SampEn(U, m, r):
    """
    用于量化时间序列的可预测性
    :param U: 时间序列
    :param m: 模板向量维数
    :param r: 距离容忍度，一般取0.1~0.25倍的时间序列标准差，也可以理解为相似度的度量阈值
    :return: 返回一个-np.log(A/B)，该值越小预测难度越小
    """

    def _maxdist(x_i, x_j):
        """
         Chebyshev distance
        :param x_i:
        :param x_j:
        :return:
        """
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):
        x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
        C = [len([1 for j in range(len(x)) if i != j and _maxdist(x[i], x[j]) <= r]) for i in range(len(x))]
        return sum(C)

    N = len(U)
    return -np.log(_phi(m + 1) / _phi(m))


if __name__ == '__main__':
    _U = [0.2, 0.6, 0.7, 1.2, 55, 66]
    rand_small = np.random.randint(0, 100, size=120)
    rand_big = np.random.randint(0, 100, size=136)
    m = 2
    print(SampEn(_U, m, r=0.2 * np.std(_U)))
    print(SampEn(rand_small, m, r=0.2 * np.std(rand_small)))
    print(SampEn(rand_big, m, r=0.2 * np.std(rand_big)))


def peaklocate(orgBCG_win, BCG, Resp, fs, Rlowcut, Rhighcut, fb1, fb2, orderBCG, wins, l1, l2, Modellength):
    for win in range(len(orgBCG_win)):
        # if win < 17 :continue
        # ------------------------------------------------------------------------------
        # -----------------------------------1.信号预处理---------------------------------
        BCG[win], Resp[win] = Preprocessing2(orgBCG_win[win], fs, Rlowcut, Rhighcut, fb1, fb2, orderBCG)
        Resp[win] = np.diff(Resp[win]) * 1000
        state = Statedetect(BCG[win], 0.1, wins)

        # ------------------------------------2.状态检测-----------------------------------
        BCGcut, Cutmark = Movement_Remove(BCG[win], state, wins)  # 按体动分开34efrdsa
        # --------------------------------3.Model Formation------------------------------
        InitPeak = []
        for n in range(len(BCGcut)):
            InitPeak.extend(Cutmark[n] + InitBeatDetect(BCGcut[n], l1, l2))
        print('Initpeak:', InitPeak)
        Model = ReModel(BCG[win], Modellength, InitPeak, 60)

        # print("cor start:" + str(datetime.datetime.now()))
        BCGcor = np.correlate(np.array(BCG[win]), np.array(Model), "same")  # same模式返回与最短向量相同的结果
        print('BCGcor', BCGcor)
        # print("cor end:" + str(datetime.datetime.now()))
        # print("dit start:" + str(datetime.datetime.now()))
        BCGdit = []
        for j in range(len(BCG[win]) - len(Model)):
            # para = 2-ASD(xindata[win][j:j + len(ModelBCG[win])], ModelBCG[win])/SAD(xindata[win][j:j + len(ModelBCG[win])], ModelBCG[win])
            para = 1
            BCGdit.append(distEuclidean(BCG[win][j:j + len(Model)], Model) * para)
        BCGdit = np.array(BCGdit)
        BCGdit = np.insert(BCGdit, 0, np.full(int(Modellength / 2), BCGdit[0]))
        BCGdit = np.append(BCGdit, np.full(int(Modellength / 2), BCGdit[-1]))
        print('BCGdit:', BCGdit)
        # print("dit end:" + str(datetime.datetime.now()))

        # ------------------------------------5.定位心跳-----------------------------------

        BCGcor_cut, cormark = Movement_Remove(BCGcor, state, wins)
        BCGcor_cut = np.array(BCGcor_cut)
        BCGdit_cut, ditmark = Movement_Remove(BCGdit, state, wins)

        # ------------------------------相关
        beatcor_forward = np.array([])
        beatcor_backward = np.array([])
        # print('BCGcor_cut', BCGcor_cut)
        for num in range(len(BCGcor_cut)):
            # print('len(BCGcor_cut):', num)
            # 求包络线
            hx = fftpack.hilbert(BCGcor_cut[num])
            hy = np.sqrt(BCGcor_cut[num] ** 2 + hx ** 2)
            hy = Butterworth(hy, fs, type="低通", lowcut=1, order=4)
            # 检测位置
            cor_forward = BeatDetection(BCGcor_cut[num], hy, 900, up=1.6, down=0.1, style="peak")
            cor_backward = BeatDetection(BCGcor_cut[num][::-1], hy[::-1], 900, up=1.6, down=0.1, style="peak")
            cor_backward = len(BCGcor_cut[num]) - np.array(cor_backward)
            cor_backward = np.sort(cor_backward)
            # 组合
            beatcor_forward = np.append(beatcor_forward, Cutmark[num] + np.array(cor_forward)).astype(int)
            beatcor_backward = np.append(beatcor_backward, Cutmark[num] + cor_backward).astype(int)

        # ---------------------------------形态距
        beatdit_forward = np.array([])
        beatdit_backward = np.array([])
        # 移除基线
        for num in range(len(BCGdit_cut)):
            BCGdit_cut[num] = np.max(BCGdit) - BCGdit_cut[num]

        for num in range(len(BCGdit_cut)):
            # 求包络线
            hx = fftpack.hilbert(BCGcor_cut[num])
            hy = np.sqrt(BCGcor_cut[num] ** 2 + hx ** 2)
            hy = Butterworth(hy, fs, type="低通", lowcut=1, order=4)
            # 检测位置
            dit_forward = BeatDetection(BCGdit_cut[num], hy, 900, up=1.6, down=0.625, style="peak")
            # print('前向形态距检测：', dit_forward)
            dit_backward = BeatDetection(BCGdit_cut[num][::-1], hy[::-1], 900, up=1.6, down=0.625, style="peak")
            dit_backward = len(BCGdit_cut[num]) - np.array(dit_backward)
            dit_backward = np.sort(dit_backward)
            # 组合
            beatdit_forward = np.append(beatdit_forward, Cutmark[num] + np.array(dit_forward)).astype(int)
            beatdit_backward = np.append(beatdit_backward, Cutmark[num] + dit_backward).astype(int)
            # print('前向形态距检测：', dit_forward)
            # print('前向形态距检测点', len(dit_forward))
            # print('后向形态距检测：', dit_backward)
            # print('后向形态距检测点', len(dit_backward))
            Corpos = np.full(len(BCG[win]), np.nan)
            for num in beatdit_backward.astype(int):
                Corpos[num] = BCGdit[num]

        # -----------------------------------联合统一前向后向---------------------------------------

        BeatPosition = BeatChoose(beatcor_forward, beatcor_backward, beatdit_forward, beatdit_backward,
                                  900).astype(int)
        # print('最终点坐标', BeatPosition)
        # print('最终点个数', len(BeatPosition))
        # ---------------------------------------END---------------------------------------------
        BCGcor = BCGcor / 40000
        BCGdit = BCGdit / 20
        # -----------------------------------------------标记展示区

        # InitPeak = np.array(InitPeak).astype(int)
        print('Initpeak2:', InitPeak)
        print('leninitpeak:', len(InitPeak))
        Initpos = np.full(len(BCG[win]), np.nan)
        for num in InitPeak:
            Initpos[num] = BCG[win][num]
        print('Initpos', Initpos)
        Corpos_for = np.full(len(BCG[win]), np.nan)
        for num in beatcor_forward.astype(int):
            Corpos_for[num] = BCGcor[num]

        Corpos_back = np.full(len(BCG[win]), np.nan)
        for num in beatcor_backward.astype(int):
            Corpos_back[num] = BCGcor[num]

        Ditpos_for = np.full(len(BCG[win]), np.nan)
        for num in beatdit_forward.astype(int):
            Ditpos_for[num] = BCGdit[num]

        Ditpos_back = np.full(len(BCG[win]), np.nan)
        for num in beatdit_backward.astype(int):
            Ditpos_back[num] = BCGdit[num]

        # DecisionBeat = np.full(len(BCG[win]), np.nan)
        # for num in BeatPosition.astype(int):
        #     DecisionBeat[num] = 0

        # print('cordot:', croDot)
        # print('bcgwin:', len(BCG[win]))

        if win == 0:
            BCG_OUT = np.append(BCG_OUT, BCG[win][:-croDot])
            Resp_OUT = np.append(Resp_OUT, Resp[win][:-croDot])
            Initpos_OUT = np.append(Initpos_OUT, Initpos[:-croDot])
        elif win != len(orgBCG_win) - 1:
            BCG_OUT = np.append(BCG_OUT, BCG[win][croDot:-croDot])
            Resp_OUT = np.append(Resp_OUT, Resp[win][croDot:-croDot])
            Initpos_OUT = np.append(Initpos_OUT, Initpos[croDot:-croDot])
        else:
            BCG_OUT = np.append(BCG_OUT, BCG[win][croDot:])
            Resp_OUT = np.append(Resp_OUT, Resp[win][croDot:])
            Initpos_OUT = np.append(Initpos_OUT, Initpos[croDot:])
