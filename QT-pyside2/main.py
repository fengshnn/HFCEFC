from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QStylePainter, QWidget, QTabWidget, QTableWidget, \
    QTableWidgetItem
from PySide2 import QtWidgets, QtUiTools
from PySide2.QtUiTools import QUiLoader
from lib.share import SI
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import functions as fn
from scipy import signal, fftpack
# from scipy.signal import butter, lfilter, filtfilt
import pandas as pd
import os
import copy
import datetime
import matplotlib.pyplot as plt


class Win_Enter:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # self.ui = QUiLoader().load('enter.ui')
        self.ui = loader.load(os.path.join(CURRENT_DIR, "enter.ui"))
        self.ui.pushButton.clicked.connect(self.onSignIn)
        self.ui.pushButton_2.clicked.connect(self.onSignOut)

    def onSignIn(self):
        SI.mainWin = Win_Main()
        SI.mainWin.ui.show()
        # self.ui = QUiLoader().load('home.ui')
        # self.ui.show()
        self.ui.close()

    def onSignOut(self):
        self.ui.close()


m1 = 0
m2 = 10000


class Win_Main:

    def __init__(self):

        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'd')
        pg.setConfigOptions(antialias=True)  # 启用抗锯齿
        # label = pg.LabelItem(color='r', justify='center')
        region = pg.LinearRegionItem()
        region.setZValue(10)
        # label.setText('biaoqian')
        loader = QUiLoader()
        loader.registerCustomWidget(pg.PlotWidget)
        self.ui = loader.load('home.ui')
        self.ui.dataPlot.addItem(region, ignoreBounds=True)

        self.ui.actionexit.triggered.connect(fn.Exit)
        self.ui.actionopen.triggered.connect(self.Opentxt)
        self.ui.lineEdit.setText(str((m2 - m1) / fs))
        self.ui.pushButton_2.clicked.connect(self.setNumN)
        self.ui.pushButton_3.clicked.connect(self.Plot2)
        self.ui.pushButton.clicked.connect(self.setNumL)
        self.ui.actiondataview.triggered.connect(self.Plot)
        self.ui.Butterworth.triggered.connect(self.butterworth)
        self.ui.Morphological.triggered.connect(self.toMorphological)
        self.ui.actionMovement.triggered.connect(self.toMovement)
        self.ui.actionMovement2.triggered.connect(self.toMovement2)
        self.ui.actionTemplate.triggered.connect(self.toTemplateMatching)
        self.ui.MD_TemplateMatching.triggered.connect(self.toMD_TemplateMatching)

    def Opentxt(self):
        fname = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')

        if fname[0]:
            f = open(fname[0], 'r', encoding='UTF-8')

            with f:
                global data

                # data1 = f.read()
                data = np.loadtxt(f)
                for data[0] in data:
                    data1 = str(data[0])
                    self.ui.textBrowser.append(data1)

            # data = pd.read_csv(f[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)

    def butterworth(self):
        SI.filterWin = Win_Filter()
        SI.filterWin.ui.show()

    def setNumN(self):
        global m1, m2
        m1, m2 = fn.nextPage(m1, m2, fs)
        self.ui.dataPlot.setXRange(min=m1, max=m2)

    def setNumL(self):
        global m1, m2
        m1, m2 = fn.lastPage(m1, m2, fs)
        self.ui.dataPlot.setXRange(min=m1, max=m2)

    def Plot2(self):
        self.ui.dataPlot.clear()
        global m1, m2
        m1 = 0
        m22 = float(self.ui.lineEdit.text()) * fs
        m2 = int(m22)
        self.ui.dataPlot.setXRange(min=m1, max=m2)
        x = fn.xSet(data, fs)
        self.ui.dataPlot.plot(x, data, pen=pg.mkPen(color='b', width=1))

    def Plot(self):
        self.ui.dataPlot.clear()
        fname = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')

        if fname[0]:
            f = open(fname[0], 'r', encoding='UTF-8')

            with f:
                global data

                # data1 = f.read()
                data = np.loadtxt(f)
        self.ui.dataPlot.clear()
        self.ui.dataPlot.setXRange(min=m1, max=m2)
        self.ui.dataPlot.setTitle("原始信号", color='008080', size='10pt')
        self.ui.dataPlot.addLegend()
        # self.ui.dataPlot.setLabel('left', text='X轴', size='16pt')
        self.ui.dataPlot.plot(data, pen=pg.mkPen(color='b', width=1), name='BCG')

    def toMorphological(self):
        SI.MorphologicalWin = Morphological()
        SI.MorphologicalWin.ui.show()

    def toMovement(self):
        SI.MovementWin = Movement()
        SI.MovementWin.ui.show()

    def toMovement2(self):
        SI.MovementWin2 = Movement2()
        SI.MovementWin2.ui.show()

    def toTemplateMatching(self):
        SI.TemplateMatchingWin = TemplateMatching()
        SI.TemplateMatchingWin.ui.show()

    def toMD_TemplateMatching(self):
        SI.MD_TemplateMatchingWin = MD_TemplateMatching()
        SI.MD_TemplateMatchingWin.ui.show()


data = []
dataIn = []
dataOut = []


# newdataOut = []


class Win_Filter:

    def __init__(self):
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'd')
        self.ui = QUiLoader().load('Filter.ui')
        self.ui.returnMainWin.clicked.connect(fn.returnMain)
        self.ui.progressBar.setValue(0)
        self.ui.pushButton_2.clicked.connect(self.getfile)
        self.ui.pushButton_3.clicked.connect(self.Plot)
        self.ui.pushButton_4.clicked.connect(self.Preprocessing)
        self.ui.pushButton_5.clicked.connect(SI.butterMsg.getname)
        self.ui.lineEdit.setText('0')
        self.ui.lineEdit_2.setText('0')
        self.ui.lineEdit_3.setText('2')
        self.ui.lineEdit_5.setText('1000')

    def getfile(self):
        self.ui.progressBar.setValue(10)
        file = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')
        f = open(file[0], encoding='UTF-8').name
        self.ui.textEdit.setPlainText(f)
        global data, dataIn
        dataIn = pd.read_csv(file[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)
        self.ui.progressBar.setValue(20)

    def Plot(self):  # 画出原始数据data波形
        XdataIn = fn.xSet(dataIn, fs)
        self.ui.dataPlot.clear()
        self.ui.dataPlot.plot(XdataIn, dataIn, pen=pg.mkPen(color='b', width=1))

    def Preprocessing(self):
        """
        对输入信号进行预处理:
               1.低通滤波
               2.移除基线
        :param dataIn:        输入信号数据
        :return:            预处理后的信号数据
        """

        self.ui.progressBar.setValue(60)
        f_low1 = self.ui.lineEdit.text()
        f_high1 = self.ui.lineEdit_2.text()
        f_low = float(f_low1)
        f_high = float(f_high1)
        order1 = self.ui.lineEdit_3.text()
        order2 = int(order1)

        filterType = self.ui.comboBox.currentText()
        # fs1 = SI.filterWin.ui.lineEdit_5.text()
        fs1 = self.ui.lineEdit_5.text()
        fs = float(fs1)
        returndata = fn.Butterworth(np.array(dataIn), fs, type=filterType, lowcut=f_low, highcut=f_high,
                                    order=order2)
        # baseline = signal.medfilt(returndata, 351)
        # returndata = returndata - baseline
        # returndata = Win_Filter.Butterworth(np.array(returndata), type="bandpass", lowcut=2.5, highcut=f_high, order=order2)
        # baseline = Win_Filter.Butterworth(np.array(baseline), type="bandpass", lowcut=0.01, highcut=0.6, order=2)
        # return returndata, baseline
        # self.ui.dataPlot.plot(data)
        Xreturndata = fn.xSet(returndata, fs)
        self.ui.dataPlot_2.clear()
        self.ui.dataPlot_2.plot(Xreturndata, returndata, pen=pg.mkPen(color='b', width=1))
        self.ui.dataPlot_2.setXLink(self.ui.dataPlot)
        # self.ui.dataPlot_2.plot(baseline, pen=pg.mkPen(color='r', width=1))
        self.ui.progressBar.setValue(100)
        global dataOut
        dataOut = returndata

    def write(self):
        baseName = SI.butterMsg.ui.lineEdit.text()
        txtPath = QFileDialog.getExistingDirectory(self.ui, '请选择一个文件夹', '/')
        txtName = txtPath + '/' + baseName + '.txt'
        if len(dataOut) == 0:
            pass
        else:
            with open(txtName, 'w', encoding='utf8') as f:
                for i in dataOut:
                    f.write(str(i) + '\n')
                f.close()


class Morphological:
    def __init__(self):
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'd')
        self.ui = QUiLoader().load('Morphological.ui')
        self.ui.returnMainWin.clicked.connect(fn.returnMain2)
        self.ui.pushButton_2.clicked.connect(self.getfile)
        self.ui.pushButton_3.clicked.connect(self.Plot)
        self.ui.pushButton_4.clicked.connect(self.Preprocessing)
        self.ui.pushButton_5.clicked.connect(SI.butterMsg.getname)
        self.ui.lineEdit.setText('200')

    def Preprocessing(self):
        """
        对输入信号进行预处理:
               1.低通滤波
               2.移除基线(形态滤波)
        :param data:        输入信号数据
        :return:            预处理后的信号数据
        """
        # data = Butterworth(np.array(data), type="lowpass", lowcut=20, order=4)
        # 结构元宽度M，论文选择为采样频率的18%

        M1 = self.ui.lineEdit.text()  # 获取输入数值
        M = int(M1)

        # M = 200
        g = np.ones(M)
        Data_pre = np.insert(dataIn, 0, np.zeros(M))
        Data_pre = np.insert(Data_pre, -1, np.zeros(M))
        # 开运算:腐蚀+膨胀
        out1 = fn.Eorde(Data_pre, len(Data_pre), g, M)  # 腐蚀
        out2 = fn.Dilate(out1, len(out1), g, M)  # 膨胀
        out2 = np.insert(out2, 0, np.zeros(M - 2))
        # 闭运算:膨胀+腐蚀+腐蚀+膨胀
        out5 = fn.Dilate(Data_pre, len(Data_pre), g, M)  # 膨胀
        out6 = fn.Eorde(out5, len(out5), g, M)  # 腐蚀
        out6 = np.insert(out6, 0, np.zeros(M - 2))

        baseline = (out2 + out6) / 2

        # -------------------------保留剩余价值------------------------
        returndata = Data_pre[:len(baseline)] - baseline
        returndata = np.delete(returndata, range(0, M), axis=0)
        returndata = returndata[:len(dataIn)]
        baseline = baseline[M:]
        returndata[-1] = returndata[-2] = returndata[-3]
        baseline[-1] = baseline[-2] = baseline[-3]
        # -----------------------------------------------------------

        # baseline = fn.Butterworth(baseline, fs, type="bandpass", lowcut=0.01, highcut=0.7, order=2)
        #
        # returndata = fn.Butterworth(np.array(returndata), fs, type="bandpass", lowcut=2, highcut=8.5, order=4)

        self.ui.dataPlot_2.clear()
        self.ui.dataPlot_2.setXLink(self.ui.dataPlot)
        self.ui.dataPlot_2.plot(returndata, pen=pg.mkPen(color='b', width=1))
        # self.ui.dataPlot_2.plot(out2, pen=pg.mkPen(color='r', width=1))
        # self.ui.dataPlot_2.plot(out6, pen=pg.mkPen(color='m', width=1))
        self.ui.dataPlot.plot(baseline, pen=pg.mkPen(color='r', width=1))
        self.ui.progressBar.setValue(100)
        global dataOut
        dataOut = returndata

    def getfile(self):
        self.ui.progressBar.setValue(10)
        file = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')
        f = open(file[0], encoding='UTF-8').name
        self.ui.textEdit.setPlainText(f)
        global dataIn
        dataIn = pd.read_csv(file[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)
        # dataIn = dataIn[0:10000]
        self.ui.progressBar.setValue(20)

    def Plot(self):  # 画出原始数据data波形
        self.ui.dataPlot.clear()
        self.ui.dataPlot.plot(dataIn, pen=pg.mkPen(color='b', width=1))


class MsgButer:
    def __init__(self):
        self.ui = QUiLoader().load('msgFilter.ui')
        self.ui.pushButton.clicked.connect(fn.OK)
        self.ui.pushButton_2.clicked.connect(fn.shutMsg)

    def getname(self):
        if len(dataOut) == 0:
            pass
        else:
            self.ui.show()
            self.ui.lineEdit.clear()


class Movement:
    def __init__(self):
        self.ui = QUiLoader().load('Movement.ui')
        self.ui.lineEdit_5.setText('1000')
        self.ui.lineEdit.setText('10')
        self.ui.lineEdit_2.setText('1')
        self.ui.lineEdit_3.setText('0.1')
        self.ui.pushButton_2.clicked.connect(self.getfile)
        self.ui.pushButton_3.clicked.connect(self.Plot)
        self.ui.pushButton_4.clicked.connect(self.Statedetect)
        self.ui.pushButton_5.clicked.connect(SI.butterMsg.getname)
        self.ui.returnMainWin.clicked.connect(fn.returnMain3)
        self.ui.lineEdit_4.setText('1.5')
        self.ui.lineEdit_6.setText('50')

    def getfile(self):
        self.ui.progressBar.setValue(10)
        file = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')
        f = open(file[0], encoding='UTF-8').name
        self.ui.textEdit.setPlainText(f)
        global dataIn
        dataIn = pd.read_csv(file[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)
        self.ui.progressBar.setValue(20)

    def Plot(self):  # 画出原始数据data波形
        self.ui.dataPlot.clear()
        x = fn.xSet(dataIn, fs)
        self.ui.dataPlot.plot(x, dataIn, pen=pg.mkPen(color='b', width=1))

    def Statedetect(self):
        """
        函数说明：
        将输入生理信号进行处理，移除大体动以及空床状态，只保留正常睡眠
        :param dataIn:                输入信号数据
        :param threshold:           设置空床门槛
        :return:                    返还剩余的正常睡眠信号
        """
        fs1 = self.ui.lineEdit_5.text()
        fs = float(fs1)
        t = self.ui.lineEdit.text()
        num = fs * float(t)
        num = int(num)
        th = self.ui.lineEdit_3.text()
        threshold = float(th)
        cro1 = self.ui.lineEdit_2.text()
        cro2 = float(cro1) * fs
        cro = int(cro2)
        win = fn.windows(dataIn, num, cro)
        win = np.array(win, dtype=object)
        SD = np.zeros(win.shape[0])
        Mean = np.zeros(win.shape[0])
        SD_times = float(self.ui.lineEdit_4.text())
        Mean_plus = float(self.ui.lineEdit_6.text())
        state = []
        for i in range(win.shape[0]):
            SD[i] = np.std(np.array(win[i]), ddof=1)  # 计算标准差
            Mean[i] = np.mean(np.array(abs(win[i])))  # 计算平均值
            print('i:', i)
        Median_SD = np.median(SD)  # 计算中位数
        Median_Mean = np.median(Mean)

        for i in range(len(SD)):
            if SD[i] > (Median_SD * SD_times) or Mean[i] > (Median_Mean) + Mean_plus or Mean[i] < (
                    Median_Mean - Mean_plus):
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
        Cutdata, MovementData, mark = fn.CutData(dataIn, state, num)
        # MovementData = fn.Butterworth(np.array(MovementData), fs, type="高通", highcut=0.1, order=2)
        print('MovementData:', MovementData)
        # NewdataOut = np.full(len(dataOut), np.nan)  # 创建与orgBCG降采样后一样长度的空数组
        # newdata = []
        # for i in range(len(Cutdata)):
        #     newdata.append(Cutdata[i].tolist())
        # global dataOut
        # dataOut = [x for y in newdata for x in y]
        self.ui.dataPlot_2.clear()
        x = fn.xSet(Cutdata, fs)
        self.ui.dataPlot_2.setXLink(self.ui.dataPlot)
        self.ui.dataPlot_2.plot(x, Cutdata, pen=pg.mkPen(color='b', width=1))
        self.ui.dataPlot_2.plot(x, MovementData, pen=pg.mkPen(color='r', width=1))
        self.ui.progressBar.setValue(100)


class Movement2:
    def __init__(self):
        self.ui = QUiLoader().load('Movement2.ui')
        self.ui.lineEdit_5.setText('1000')
        self.ui.lineEdit.setText('2')
        # self.ui.lineEdit_2.setText('1')
        # self.ui.lineEdit_3.setText('0.1')
        self.ui.lineEdit_4.setText('30')
        self.ui.lineEdit_7.setText('60')
        self.ui.lineEdit_8.setText('120')
        self.ui.lineEdit_9.setText('300')
        self.ui.lineEdit_6.setText('1.5')
        self.ui.lineEdit_10.setText('1.8')
        self.ui.lineEdit_11.setText('1.8')
        self.ui.lineEdit_12.setText('1.8')
        self.ui.lineEdit_13.setText('2')
        self.ui.lineEdit_14.setText('2')
        self.ui.lineEdit_15.setText('2')
        self.ui.lineEdit_16.setText('2')
        self.ui.pushButton_2.clicked.connect(self.getfile)
        # self.ui.pushButton_3.clicked.connect(self.Plot)
        self.ui.pushButton_4.clicked.connect(self.Statedetect)
        self.ui.pushButton_5.clicked.connect(SI.butterMsg.getname)
        self.ui.returnMainWin.clicked.connect(fn.returnMain3R)

    def getfile(self):
        self.ui.progressBar.setValue(10)
        file = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')
        f = open(file[0], encoding='UTF-8').name
        self.ui.textEdit.setPlainText(f)
        global dataIn
        dataIn = pd.read_csv(file[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)
        dataIn = fn.Butterworth(dataIn, fs, type='高通', highcut=1, order=4)
        self.ui.dataPlot.clear()
        x = fn.xSet(dataIn, fs)
        self.ui.dataPlot.plot(x, dataIn, pen=pg.mkPen(color='b', width=1))
        self.ui.progressBar.setValue(20)

    def Plot(self):  # 画出原始数据data波形
        self.ui.dataPlot.clear()
        x = fn.xSet(dataIn, fs)
        self.ui.dataPlot.plot(x, dataIn, pen=pg.mkPen(color='b', width=1))

    def Statedetect(self):
        """
        函数说明：
        将输入生理信号进行处理，移除大体动以及空床状态，只保留正常睡眠
        :param dataIn:                输入信号数据
        :param threshold:           设置空床门槛
        :return:                    返还剩余的正常睡眠信号
        """
        fs1 = self.ui.lineEdit_5.text()
        fs = float(fs1)
        t = self.ui.lineEdit.text()
        num = fs * float(t)
        num = int(num)
        # th = self.ui.lineEdit_3.text()
        # threshold = float(th)
        # cro1 = self.ui.lineEdit_2.text()
        # cro2 = float(cro1) * fs
        # cro = int(cro2)
        t1 = self.ui.lineEdit_4.text()
        t1 = float(t1)
        t2 = self.ui.lineEdit_7.text()
        t2 = float(t2)
        t3 = self.ui.lineEdit_8.text()
        t3 = float(t3)
        t4 = self.ui.lineEdit_9.text()
        t4 = float(t4)
        q1 = float(self.ui.lineEdit_6.text())
        q2 = float(self.ui.lineEdit_10.text())
        q3 = float(self.ui.lineEdit_11.text())
        q4 = float(self.ui.lineEdit_12.text())
        d1 = float(self.ui.lineEdit_13.text())
        d2 = float(self.ui.lineEdit_14.text())
        d3 = float(self.ui.lineEdit_15.text())
        d4 = float(self.ui.lineEdit_16.text())
        All_state = fn.Artifacts_win(dataIn, num, fs, t1, t2, t3, t4, q1, q2, q3, q4, d1, d2, d3, d4)  # 前向体动检测
        print('allstate:', All_state)
        reversed_All_state = fn.Artifacts_win(dataIn[::-1], num, fs, t1, t2, t3, t4, q1, q2, q3, q4, d1, d2, d3,
                                              d4)  # 后向体动检测
        print('reversed:', reversed_All_state)
        reversed_All_state = reversed_All_state[::-1]  # 后向体动检测倒置
        # print('Allstate:', All_state)
        # print('reversed_All_state:', reversed_All_state)
        final_state = []
        for i in range(len(All_state)):
            if All_state[i] == "Movement" or reversed_All_state[i] == "Movement":
                final_state.append("Movement")
            else:
                final_state.append("Sleep")
            print('state:', final_state)

        state = np.array(final_state)
        Cutdata, MovementData, mark = fn.CutData(dataIn, state, num)
        # print('state_index:', state_index)
        newdata = []
        for i in range(len(Cutdata)):
            newdata.append(Cutdata[i])
        global dataOut
        dataOut = newdata
        # dataOut = [x for y in newdata for x in y]
        # print('dataOut', dataOut)
        self.ui.dataPlot_2.clear()
        x = fn.xSet(Cutdata, fs)
        self.ui.dataPlot_2.setXLink(self.ui.dataPlot)
        self.ui.dataPlot_2.plot(x, Cutdata, pen=pg.mkPen(color='b', width=1))
        self.ui.dataPlot_2.plot(x, MovementData, pen=pg.mkPen(color='r', width=1))
        self.ui.progressBar.setValue(100)


dataInECG = []
dataInBCG = []
BCG_OUT = []
BCG_Out = []
Resp_OUT = []
ECGInitpos_OUT = []
Initpos_OUT = []
Initpos_OUT = []
BCGRegion = []
corr = []
seqP = []
RMSSeq = []
fs = 1000

JJI = []
Max = 1
Min = 0
ModelList = []


class TemplateMatching:

    def __init__(self):
        self.ui = QUiLoader().load('TemplateMatching.ui')
        self.ui.lineEdit_5.setText('1000')
        self.ui.lineEdit.setText('0.7')
        self.ui.lineEdit_2.setText('10')
        self.ui.lineEdit_3.setText('1')
        self.ui.lineEdit_4.setText('1')
        self.ui.progressBar.setValue(0)
        self.ui.lineEdit_6.setText('0.1')
        self.ui.lineEdit_7.setText('0.7')
        self.ui.lineEdit_8.setText('500')
        self.ui.lineEdit_9.setText('1300')
        self.ui.lineEdit_10.setText('2')
        self.ui.lineEdit_12.setText('8.5')
        self.ui.lineEdit_11.setText('4')
        self.ui.lineEdit_13.setText('60')
        self.ui.lineEdit_14.setText('60')
        self.ui.lineEdit_15.setText('30')
        self.ui.lineEdit_16.setText('1')
        self.ui.lineEdit_17.setText('0')
        self.ui.spinBox.setValue(0)
        self.ui.spinBox.setRange(0, 600000)
        # self.ui.spinBox.setMaximum(600000)
        # self.ui.spinBox.setMinimum(0)
        self.ui.spinBox.setSingleStep(50)
        self.ui.spinBox_2.setValue(50)
        self.ui.spinBox_2.setMaximum(600000)
        self.ui.spinBox_2.setMinimum(0)
        self.ui.spinBox_2.setSingleStep(50)
        self.ui.pushButton.clicked.connect(self.Acreage)
        self.ui.pushButton_2.clicked.connect(self.getBCG)
        self.ui.pushButton_6.clicked.connect(self.getECG)
        self.ui.returnMainWin.clicked.connect(fn.returnMain4)
        self.ui.pushButton_4.clicked.connect(self.Model)
        self.ui.pushButton_5.clicked.connect(SI.butterMsg.getname)
        self.ui.pushButton_7.clicked.connect(self.saveResp)
        self.ui.pushButton_8.clicked.connect(fn.toHRWin)
        self.ui.pushButton_9.clicked.connect(self.clear)
        self.ui.pushButton_10.clicked.connect(self.clear2)
        self.ui.pushButton_11.clicked.connect(self.setModel)
        self.ui.pushButton_12.clicked.connect(self.saveModel)
        self.ui.pushButton_13.clicked.connect(self.LocalM4)
        self.ui.pushButton_14.clicked.connect(self.LocalM5)
        self.ui.pushButton_15.clicked.connect(self.LocalM6)
        self.ui.pushButton_16.clicked.connect(self.LocalM7)
        self.ui.pushButton_17.clicked.connect(self.LocalM8)
        self.ui.pushButton_18.clicked.connect(self.LocalM9)
        self.ui.pushButton_19.clicked.connect(self.LocalM10)
        self.ui.pushButton_20.clicked.connect(self.ModelDis)
        self.ui.pushButton_21.clicked.connect(self.Kurtosis)
        self.ui.pushButton_22.clicked.connect(self.Skewness)
        self.ui.pushButton_23.clicked.connect(self.Power)
        self.ui.pushButton_24.clicked.connect(self.Energy)
        self.ui.pushButton_25.clicked.connect(self.RMS)
        self.ui.pushButton_26.clicked.connect(self.saveBCGRegion)
        self.ui.pushButton_27.clicked.connect(self.saveRespRegion)
        self.ui.pushButton_28.clicked.connect(self.waveConsistency)
        self.ui.pushButton_29.clicked.connect(self.waveConsistency_Am)
        self.ui.pushButton_30.clicked.connect(self.saveORGRegion)
        self.ui.pushButton_31.clicked.connect(self.beat_to_beat_Consistency)
        self.ui.pushButton_32.clicked.connect(self.saveCorr)
        self.ui.pushButton_33.clicked.connect(self.beat_to_model_Consistency)
        self.ui.pushButton_34.clicked.connect(self.seq_to_seq_Consistency)
        self.ui.pushButton_35.clicked.connect(self.saveSeq_P)
        self.ui.pushButton_36.clicked.connect(self.saveECGRegion)
        self.ui.pushButton_37.clicked.connect(self.saveBCGPeakIndex)
        self.ui.pushButton_56.clicked.connect(self.saveRMSSeq)

        global fs
        fs = float(self.ui.lineEdit_5.text())

    # def Morphology_simlarity_distance(self):

    def seq_to_seq_Consistency(self):

        beatNum = int(self.ui.lineEdit_16.text())
        seqNum = int(self.ui.lineEdit_17.text())
        fs = float(self.ui.lineEdit_5.text())
        Modellength = int(float(self.ui.lineEdit.text()) * fs)
        BCGRegion = copy.deepcopy(BCG_OUT[r1:r2])
        InitposRegion = copy.deepcopy(Initpos_OUT[r1:r2])
        index = []
        for i in range(len(InitposRegion)):
            if InitposRegion[i] >= 0:
                index.append(i)
        # BCG = []
        # for i in range(len(InitposRegion)):       # 以模板长度取beats
        #     if InitposRegion[i] >= 0 and (len(InitposRegion) - 0.6 * Modellength) >= i >= 0.4 * Modellength:
        #         BCG.append(BCGRegion[int(i - 0.4 * Modellength):int(i + 0.6 * Modellength)])
        #     else:
        #         pass
        Initpos_Seq = []
        for i in range(len(InitposRegion)):  # 以beat数连续取值提取beats
            if InitposRegion[i] >= 0:
                Initpos_Seq.append(i)
        BCGSeq = []
        for i in range(seqNum):
            BCGSeq.append(BCGRegion[Initpos_Seq[i]:Initpos_Seq[i + beatNum]])
        print('lenBCGSeq:', len(BCGSeq))
        print('lenBCGSeq[0]:', len(BCGSeq[0]))
        print('lenBCGSeq[1]:', len(BCGSeq[1]))
        # InitposRegion = np.array(InitposRegion).astype(int)
        # for i in range(len(BCG)):
        #     MAX = max(BCG[i])
        #     MIN = min(BCG[i])
        #     for j in range(len(BCG[i])):
        #         BCG[i][j] = ((BCG[i][j] - MIN) / (MAX - MIN))
        w1 = self.ui.graphicsView
        w1.clear()
        # BCGSeq = []
        # for i in range(seqNum):
        #     Seq = []
        #     Seq.append(BCG[i:i + beatNum])
        #     # print('lenSeq:', len(Seq))
        #     seq = []
        #     for j in range(len(Seq[0])):
        #         for k in range(len(Seq[0][j])):
        #             seq.append(Seq[0][j][k])
        #     BCGSeq.append(seq)
        # print('lenBCGseq:', len(BCGSeq))

        listP = []
        for i in range(len(BCGSeq)):
            PBCG = 0
            for j in BCGSeq[i]:
                PBCG = (PBCG + j ** 2) / (len(BCGSeq[i]) / fs)
            P = round(abs(PBCG), 3)
            listP.append(P)
        print('listP:', listP)
        global seqP
        seqP = listP

        # RMS = []
        # for i in range(len(BCGSeq)):
        #     p = 0
        #     for j in BCGSeq[i]:
        #         p = p + j ** 2
        #     RMS.append((p / (len(BCGSeq) * Modellength) ** 0.5))
        RMS = []
        for i in range(len(BCGSeq)):
            p = 0
            for j in BCGSeq[i]:
                p = p + j ** 2
            RMS.append((p / (len(BCGSeq[i]))) ** 0.5)
        global RMSSeq
        RMSSeq = RMS
        print('RMSSeq:', RMSSeq)

        # corrL = []
        # for i in range(len(BCGSeq) - 1):
        #     CORR = []
        #     CORR.append(np.array(BCGSeq[i]))
        #     CORR.append(np.array(BCGSeq[i + 1]))
        #     corrL.append((np.corrcoef(CORR))[0][1])
        # global corr
        # corr = corrL
        # print('lencorr:', len(corr))
        # print('corr:', corr)
        aveRMS = round(np.sum(RMSSeq) / len(RMSSeq), 3)
        avePD = round(np.sum(listP) / len(listP), 3)
        # aveCorr = round(np.sum(corr) / len(corr), 3)
        # corBCG = round(fn.Cor(BCGRegion), 3)
        # snrBCG = round(fn.SNR2(BCGRegion, index, Modellength), 3)
        # self.ui.textEdit_18.setPlainText(str(snrBCG))
        # self.ui.textEdit_21.setPlainText(str(corBCG))
        # self.ui.textEdit_28.setPlainText(str(aveCorr))
        self.ui.textEdit_31.setPlainText(str(avePD))
        self.ui.textEdit_61.setPlainText(str(aveRMS))
        w1 = self.ui.graphicsView
        w1.clear()
        for i in range(int((len(BCGSeq) + 1) / 2)):
            p1 = w1.addPlot()
            p1.plot(BCGSeq[i], pen=pg.mkPen(color='r', width=1))

        w1.nextRow()
        for i in range(int((len(BCGSeq) + 1) / 2), len(BCGSeq)):
            p1 = w1.addPlot()
            p1.plot(BCGSeq[i], pen=pg.mkPen(color='r', width=1))

    def beat_to_beat_Consistency(self):

        beatNum = int(self.ui.lineEdit_16.text())

        fs = float(self.ui.lineEdit_5.text())
        Modellength = int(float(self.ui.lineEdit.text()) * fs)
        BCGRegion = copy.deepcopy(BCG_OUT[r1:r2])
        InitposRegion = copy.deepcopy(Initpos_OUT[r1:r2])
        index = []
        print('BCGRegion:', BCGRegion)
        for i in range(len(InitposRegion)):
            if InitposRegion[i] >= 0:
                index.append(i)
        print('InitposRegion:', InitposRegion)
        print('index:', index)
        BCG = []
        for i in range(len(InitposRegion)):
            if InitposRegion[i] >= 0 and (len(InitposRegion) - 0.6 * Modellength) >= i >= 0.4 * Modellength:
                BCG.append(BCGRegion[int(i - 0.4 * Modellength):int(i + 0.6 * Modellength)])
            else:
                pass
        if int(self.ui.lineEdit_17.text()) == 0:
            seqNum = len(BCG)
        else:
            seqNum = int(self.ui.lineEdit_17.text())
        print('seqNum:', seqNum)
        # InitposRegion = np.array(InitposRegion).astype(int)
        # for i in range(len(BCG)):
        #     MAX = max(BCG[i])
        #     MIN = min(BCG[i])
        #     for j in range(len(BCG[i])):
        #         BCG[i][j] = ((BCG[i][j] - MIN) / (MAX - MIN))
        data = []
        for i in range(len(BCG)):
            for j in BCG[i]:
                data.append(j)
        # print('data:', data)
        BCGSeq = []
        for i in range(seqNum):
            BCGSeq.append(data[beatNum * Modellength * i:beatNum * Modellength * (i + 1)])
        # print('lenBCGSeq:', len(BCGSeq))
        # print('BCGSeq:', BCGSeq)
        corrL = []
        for i in range(len(BCGSeq) - 1):
            CORR = []
            CORR.append(np.array(BCGSeq[i]))
            CORR.append(np.array(BCGSeq[i + 1]))
            corrL.append((np.corrcoef(CORR))[0][1])
        global corr
        corr = corrL
        print('lencorr:', len(corr))
        print('corr:', corr)
        aveCorr = round(np.sum(corr) / len(corr), 3)
        corBCG = round(fn.Cor(BCG), 3)
        snrBCG = round(fn.SNR2(BCG, index, Modellength), 3)
        self.ui.textEdit_18.setPlainText(str(snrBCG))
        self.ui.textEdit_21.setPlainText(str(corBCG))
        self.ui.textEdit_28.setPlainText(str(aveCorr))
        w1 = self.ui.graphicsView
        w1.clear()
        for i in range(int((len(BCGSeq) + 1) / 2)):
            p1 = w1.addPlot()
            p1.plot(BCGSeq[i], pen=pg.mkPen(color='r', width=1))

        w1.nextRow()
        for i in range(int((len(BCGSeq) + 1) / 2), len(BCGSeq)):
            p1 = w1.addPlot()
            p1.plot(BCGSeq[i], pen=pg.mkPen(color='r', width=1))

    def beat_to_model_Consistency(self):
        model = []
        MAX = max(Model)
        MIN = min(Model)
        for j in range(len(Model)):
            a = ((Model[j] - MIN) / (MAX - MIN))
            model.append(a)
        fs = float(self.ui.lineEdit_5.text())
        Modellength = int(float(self.ui.lineEdit.text()) * fs)
        BCGRegion = copy.deepcopy(BCG_OUT)
        InitposRegion = copy.deepcopy(Initpos_OUT)
        index = []
        for i in range(len(InitposRegion)):  # 获取J峰索引
            if InitposRegion[i] >= 0:
                index.append(i)
        BCG = []
        for i in range(len(InitposRegion)):  # 以峰值点为中心取一个完整BCG
            if InitposRegion[i] >= 0 and (len(InitposRegion) - 0.6 * Modellength) >= i >= 0.4 * Modellength:
                BCG.append(BCGRegion[int(i - 0.4 * Modellength):int(i + 0.6 * Modellength)])
            else:
                pass
        # BCG = BCG[1:11]
        # InitposRegion = np.array(InitposRegion).astype(int)
        for i in range(len(BCG)):  # 逐个对所取BCG以最大幅值差为1进行归一化
            MAX = max(BCG[i])
            MIN = min(BCG[i])
            for j in range(len(BCG[i])):
                BCG[i][j] = ((BCG[i][j] - MIN) / (MAX - MIN))
        data = []
        for i in range(len(BCG)):
            for j in BCG[i]:
                data.append(j)
        corrL = []
        for i in range(len(BCG)):
            CORR = []
            CORR.append(copy.deepcopy(np.array(model)))
            CORR.append(BCG[i])
            # for j in BCG[i]:
            #     CORR.append(j)
            print('CORR:', CORR)
            CORR = np.array(CORR).reshape(2, Modellength)
            corrL.append((np.corrcoef(CORR))[0][1])
            print('np.corrcoef(CORR):', np.corrcoef(CORR))
        global corr
        # corr = []
        corr = corrL
        print('corr:', corr)
        aveCorr = round(np.sum(corr) / len(corr), 3)
        corBCG = round(fn.Cor(BCG), 3)
        snrBCG = round(fn.SNR2(BCG, index, Modellength), 3)
        self.ui.textEdit_18.setPlainText(str(snrBCG))
        self.ui.textEdit_21.setPlainText(str(corBCG))
        self.ui.textEdit_28.setPlainText(str(aveCorr))
        w1 = self.ui.graphicsView
        w1.clear()
        p1 = w1.addPlot()
        for i in range(int(len(BCG) / 2 - 1)):
            p1.plot(BCG[i], pen=pg.mkPen(color='r', width=1))
            p1 = w1.addPlot()
        w1.nextRow()
        for i in range(int(len(BCG) / 2), len(BCG)):
            p1.plot(BCG[i], pen=pg.mkPen(color='r', width=1))
            p1 = w1.addPlot()

    def waveConsistency(self):
        l1 = int(self.ui.lineEdit_8.text())
        l2 = int(self.ui.lineEdit_9.text())
        fs = float(self.ui.lineEdit_5.text())
        Modellength = int(float(self.ui.lineEdit.text()) * fs)
        BCGRegion = BCG_OUT[r1: r2]
        InitposRegion = Initpos_OUT[r1:r2]
        RespRegion = Resp_OUT[r1:r2]
        t = float(self.ui.lineEdit_2.text())
        num = int(t * fs)  # 每个信号窗的数据量
        cro = float(self.ui.lineEdit_3.text())
        croDot = int(cro * fs)
        orgInitpos_win = fn.windows(InitposRegion, num, croDot)
        orgInitpos_win = orgInitpos_win[0]
        Resp_win = fn.windows(RespRegion, 10000, croDot)
        print('lenRESPwin:', len(Resp_win))
        RespPeak = []
        Resp = []
        Resppos_OUT = []
        for win in range(len(Resp_win)):
            RespPeak.extend(win * 10000 + fn.RespBeatDetect(Resp_win[win], 3000, 5500))
            print('lenrespwin[win]:', len(Resp_win[win]))
            print('lenRespPeak', len(RespPeak))
            print('RespPeak:', RespPeak)
            Resppos = np.full(len(Resp_win[win]), np.nan)
            for n in range(len(RespPeak)):
                print('n:', n)
                Resppos[n] = Resp_win[win][n]
            if win == 0:
                Resp = np.append(Resp, Resp_win[win][:-croDot])
                Resppos_OUT = np.append(Resppos_OUT, Resppos[:-croDot])
            elif win != len(Resp_win) - 1:
                Resp = np.append(Resp, Resp_win[win][croDot:-croDot])
                Resppos_OUT = np.append(Resppos_OUT, Resppos[croDot:-croDot])
            else:
                Resp = np.append(Resp, Resp_win[win][croDot:])
                Resppos_OUT = np.append(Resppos_OUT, Resppos[croDot:])
        print('Resppos:', len(Resppos))
        print('Resppos_OUT:', len(Resppos_OUT))
        InitPeak = []
        for i in range(len(orgInitpos_win)):
            if orgInitpos_win[i] > 0:
                InitPeak.append(i)
        SNR = fn.SNR(BCGRegion, InitPeak, Modellength)
        self.ui.textEdit_18.setText(str(round(SNR, 3)))

        w1 = self.ui.graphicsView
        w1.clear()
        p1 = w1.addPlot()
        xResp = fn.xSet(RespRegion, fs)
        p1.plot(xResp, Resp, pen=pg.mkPen(color='b', width=1))
        p1.plot(xResp, Resppos_OUT, name='Resp-peak', pen=None, symbolBrush=(255, 0, 0), symbol='o')
        # p3.plot(xBCG_OUT, Initpos_OUT, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')
        p1.setLabel('bottom', 'Time(s)')

    def waveConsistency_Am(self):
        fs = float(self.ui.lineEdit_5.text())
        Modellength = int(float(self.ui.lineEdit.text()) * fs)
        BCGRegion = copy.deepcopy(BCG_OUT[r1:r2])
        InitposRegion = copy.deepcopy(Initpos_OUT[r1:r2])
        index = []
        for i in range(len(InitposRegion)):
            if InitposRegion[i] >= 0:
                index.append(i)
        BCG = []
        for i in range(len(InitposRegion)):
            if InitposRegion[i] >= 0 and (len(InitposRegion) - 0.6 * Modellength) >= i >= 0.4 * Modellength:
                BCG.append(BCGRegion[int(i - 0.4 * Modellength):int(i + 0.6 * Modellength)])
            else:
                pass
        BCG = BCG[1:11]
        # InitposRegion = np.array(InitposRegion).astype(int)
        for i in range(len(BCG)):
            MAX = max(BCG[i])
            MIN = min(BCG[i])
            for j in range(len(BCG[i])):
                BCG[i][j] = ((BCG[i][j] - MIN) / (MAX - MIN))
            # print('BCG[', i, ']:', max(BCG[i]))
        data = []
        for i in range(len(BCG)):
            for j in BCG[i]:
                data.append(j)
        corBCG = round(fn.Cor(BCG), 3)
        snrBCG = round(fn.SNR2(BCG, index, Modellength), 3)
        # tsqiBCG = round(fn.tSQI(BCGRegion, index, Modellength), 3)
        print('corBCG:', corBCG)
        print('tsqibcg:', snrBCG)
        self.ui.textEdit_18.setPlainText(str(snrBCG))
        self.ui.textEdit_21.setPlainText(str(corBCG))

        w1 = self.ui.graphicsView
        w1.clear()
        p1 = w1.addPlot()
        for i in range(int(len(BCG) / 2 - 1)):
            p1.plot(BCG[i], pen=pg.mkPen(color='r', width=1))
            p1 = w1.addPlot()
        w1.nextRow()
        for i in range(int(len(BCG) / 2), len(BCG)):
            p1.plot(BCG[i], pen=pg.mkPen(color='r', width=1))
            p1 = w1.addPlot()

    def saveBCGPeakIndex(self):
        global dataOut
        dataOut = Initpos_OUT
        SI.butterMsg.getname()

    def saveModel(self):
        global dataOut
        dataOut = Model
        SI.butterMsg.getname()

    def saveRMSSeq(self):
        global dataOut
        dataOut = RMSSeq
        SI.butterMsg.getname()

    def saveCorr(self):
        global dataOut
        dataOut = corr
        SI.butterMsg.getname()

    def saveSeq_P(self):
        global dataOut
        dataOut = seqP
        SI.butterMsg.getname()

    def saveResp(self):
        global dataOut
        dataOut = Resp_OUT
        SI.butterMsg.getname()

    def saveRespRegion(self):
        global dataOut
        dataOut = Resp_OUT[r1:r2]
        SI.butterMsg.getname()

    def saveORGRegion(self):
        global dataOut
        dataOut = dataIn[r1:r2]
        SI.butterMsg.getname()

    def saveBCGRegion(self):
        global dataOut
        dataOut = BCG_OUT[r1:r2]
        SI.butterMsg.getname()

    def saveECGRegion(self):
        global dataOut
        dataOut = dataInECG[r1:r2]
        SI.butterMsg.getname()

    def getBCG(self):
        file = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')
        f = open(file[0], encoding='UTF-8').name
        self.ui.textEdit.setPlainText(f)
        global dataInBCG
        dataInBCG = pd.read_csv(file[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)
        # dataIn = dataIn[0:100000]
        X = []
        for i in range(len(dataInBCG)):
            j = i / fs
            X.append(j)
        w1 = self.ui.graphicsView_2
        w1.clear()
        p1 = w1.addPlot()
        p1.plot(X, dataInBCG, pen=pg.mkPen(color='b', width=1))
        p1.setLabel('bottom', 'Time(s)')
        p1.setLabel('left', 'Amplitude(mV)')
        lr = pg.LinearRegionItem([0, 0.3])
        lr.setZValue(1)
        p1.addItem(lr)
        # r1, r2 = lr.getRegion()
        w1.nextRow()
        p4 = w1.addPlot(title="Zoom on selected region")
        p4.plot(X, dataInBCG, name='BCG', pen=pg.mkPen(color='b', width=1))
        global Max, Min
        if len(dataInBCG) > 1500:
            pass
        else:
            Max = max(dataInBCG)
            Min = min(dataInBCG)

        def updatePlot():
            p4.setXRange(*lr.getRegion(), padding=0)
            global r1, r2, r11
            r11, r22 = lr.getRegion()
            r1 = int(r11 * fs)
            r2 = int(r22 * fs)

        def updateRegion():
            lr.setRegion(p4.getViewBox().viewRange()[0])

        lr.sigRegionChanged.connect(updatePlot)
        p4.sigXRangeChanged.connect(updateRegion)
        updatePlot()

    def LocalM4(self):
        mP = np.max(dataIn[r1:r2])
        index = np.argmax(dataIn[r1:r2]) + r1
        num = round((mP - Min) / (Max - Min), 3)
        # num = round(mP, 3)
        self.ui.textEdit_4.setPlainText(str(num))
        self.ui.textEdit_11.setPlainText(str(index))

    def LocalM5(self):
        mV = np.min(dataIn[r1:r2])
        index = np.argmin(dataIn[r1:r2]) + r1
        num = round((mV - Min) / (Max - Min), 3)
        # num = round(mV, 3)
        self.ui.textEdit_5.setPlainText(str(num))
        self.ui.textEdit_12.setPlainText(str(index))

    def LocalM6(self):
        mP = np.max(dataIn[r1:r2])
        index = np.argmax(dataIn[r1:r2]) + r1
        num = round((mP - Min) / (Max - Min), 3)
        # num = round(mP, 3)
        self.ui.textEdit_6.setPlainText(str(num))
        self.ui.textEdit_13.setPlainText(str(index))

    def LocalM7(self):
        m = np.min(dataIn[r1:r2])
        index = np.argmin(dataIn[r1:r2]) + r1
        num = round((m - Min) / (Max - Min), 3)
        # num = round(m, 3)
        self.ui.textEdit_7.setPlainText(str(num))
        self.ui.textEdit_14.setPlainText(str(index))

    def LocalM8(self):
        mP = np.max(dataIn[r1:r2])
        index = np.argmax(dataIn[r1:r2]) + r1
        num = round((mP - Min) / (Max - Min), 3)
        # num = round(mP, 3)
        self.ui.textEdit_8.setPlainText(str(num))
        self.ui.textEdit_15.setPlainText(str(index))

    def LocalM9(self):
        mP = np.min(dataIn[r1:r2])
        index = np.argmin(dataIn[r1:r2]) + r1
        num = round((mP - Min) / (Max - Min), 3)
        # num = round(mP, 3)
        self.ui.textEdit_9.setPlainText(str(num))
        self.ui.textEdit_16.setPlainText(str(index))

    def LocalM10(self):
        m = np.max(dataIn[r1:r2])
        index = np.argmax(dataIn[r1:r2]) + r1
        num = round((m - Min) / (Max - Min), 3)
        # num = round(m, 3)
        self.ui.textEdit_10.setPlainText(str(num))
        self.ui.textEdit_17.setPlainText(str(index))

    def Acreage(self):
        Aall = Aregion = 0
        for i in dataIn:
            i = (i - Min) / (Max - Min)
            Aall = Aall + i
        if r1 >= 20:
            if dataIn[r1 - 9] - dataIn[r1 - 10] < 0:
                r11 = np.argmin(dataIn[(r1 - 20):(r1 + 20)]) + (r1 - 20)
            else:
                r11 = np.argmax(dataIn[(r1 - 20):(r1 + 20)]) + (r1 - 20)
        else:
            if dataIn[0] - dataIn[1] > 0:
                r11 = np.argmin(dataIn[0:40])
            else:
                r11 = np.argmax(dataIn[0:40])
        if r2 <= len(dataIn) - 20:
            if dataIn[r2 + 19] - dataIn[r2 + 20] < 0:
                r22 = np.argmin(dataIn[(r2 - 20):(r2 + 20)]) + (r2 - 20)
            else:
                r22 = np.argmax(dataIn[(r2 - 20):(r2 + 20)]) + (r2 - 20)
        else:
            if dataIn[-1] - dataIn[-2] < 0:
                r22 = np.argmin(dataIn[-40:]) + len(dataIn) - 40
            else:
                r22 = np.argmax(dataIn[-40:]) + len(dataIn) - 40
        print(r1, r2)
        print(r11, r22)
        for j in dataIn[r11:r22]:
            j = (j - Min) / (Max - Min)
            Aregion = Aregion + j
        print('Aregion / Aall:', Aregion / Aall)
        perc = round(Aregion / Aall, 3)
        self.ui.textEdit_20.setText(str(perc))

    def Kurtosis(self):
        dataRegion = []
        for i in dataIn:
            i = (i - Min) / (Max - Min)
            dataRegion.append(i)
        if r1 >= 20:
            r11 = np.argmin(dataRegion[(r1 - 20):(r1 + 20)]) + (r1 - 20)
        else:
            r11 = np.argmin(dataRegion[0:40])
        if r2 + 20 <= len(dataRegion):
            r22 = np.argmin(dataRegion[(r2 - 20):(r2 + 20)]) + (r2 - 20)
        else:
            r22 = np.argmin(dataRegion[-40:]) + len(dataRegion - 40)
        print(r1, r2)
        print(r11, r22)
        k = pd.Series(dataRegion[r11:r22])
        print('k:', k)
        kur = k.kurt()
        print(kur)
        self.ui.textEdit_23.setText(str(round(kur, 3)))

    def Skewness(self):
        Aall = Aregion = 0
        for i in dataIn:
            i = (i - Min) / (Max - Min)
            Aall = Aall + i
        if r1 >= 20:
            r11 = np.argmin(dataIn[(r1 - 20):(r1 + 20)]) + (r1 - 20)
        else:
            r11 = np.argmin(dataIn[0:40])
        if r2 + 20 <= len(dataIn):
            r22 = np.argmin(dataIn[(r2 - 20):(r2 + 20)]) + (r2 - 20)
        else:
            r22 = np.argmin(dataIn[-40:]) + len(dataIn) - 40
        print(r1, r2)
        print(r11, r22)
        s = pd.Series(dataIn[r11:r22])
        print('s:', s)
        ske = s.skew()
        print(ske)
        self.ui.textEdit_24.setText(str(round(ske, 3)))

    def Power(self):
        dataNor = []
        for i in dataIn:
            i = (i - Min) / (Max - Min)
            dataNor.append(i)
        if r1 >= 20:
            if dataNor[r1 - 9] - dataNor[r1 - 10] < 0:
                r11 = np.argmin(dataNor[(r1 - 20):(r1 + 20)]) + (r1 - 20)
            else:
                r11 = np.argmax(dataNor[(r1 - 20):(r1 + 20)]) + (r1 - 20)
        else:
            if dataNor[0] - dataNor[1] > 0:
                r11 = np.argmin(dataNor[0:40])
            else:
                r11 = np.argmax(dataNor[0:40])
        if r2 <= len(dataNor) - 20:
            if dataNor[r2 + 9] - dataNor[r2 + 10] < 0:
                r22 = np.argmin(dataNor[(r2 - 20):(r2 + 20)]) + (r2 - 20)
            else:
                r22 = np.argmax(dataNor[(r2 - 20):(r2 + 20)]) + (r2 - 20)
        else:
            if dataNor[-1] - dataNor[-2] < 0:
                r22 = np.argmin(dataNor[-40:]) + len(dataNor) - 40
            else:
                r22 = np.argmax(dataNor[-40:]) + len(dataNor) - 40
        print(r1, r2)
        print(r11, r22)
        p = 0
        for i in dataNor[r11:r22]:
            p = p + i ** 2
        P = p / (r22 - r11)
        self.ui.textEdit_25.setText(str(round(P, 3)))

    def Energy(self):
        dataNor = []
        for i in dataIn:
            i = (i - Min) / (Max - Min)
            dataNor.append(i)
        if r1 >= 20:
            if dataNor[r1 - 9] - dataNor[r1 - 10] < 0:
                r11 = np.argmin(dataNor[(r1 - 20):(r1 + 20)]) + (r1 - 20)
            else:
                r11 = np.argmax(dataNor[(r1 - 20):(r1 + 20)]) + (r1 - 20)
        else:
            if dataNor[0] - dataNor[1] > 0:
                r11 = np.argmin(dataNor[0:40])
            else:
                r11 = np.argmax(dataNor[0:40])
        if r2 <= len(dataNor) - 20:
            if dataNor[r2 + 9] - dataNor[r2 + 10] < 0:
                r22 = np.argmin(dataNor[(r2 - 20):(r2 + 20)]) + (r2 - 20)
            else:
                r22 = np.argmax(dataNor[(r2 - 20):(r2 + 20)]) + (r2 - 20)
        else:
            if dataNor[-1] - dataNor[-2] < 0:
                r22 = np.argmin(dataNor[-40:]) + len(dataNor) - 40
            else:
                r22 = np.argmax(dataNor[-40:]) + len(dataNor) - 40
        print(r1, r2)
        print(r11, r22)
        p = 0
        for i in dataNor[r11:r22]:
            p = p + i ** 2
        self.ui.textEdit_26.setText(str(round(p, 3)))

    def RMS(self):
        dataNor = []
        for i in dataIn:
            i = (i - Min) / (Max - Min)
            dataNor.append(i)
        if r1 >= 20:
            if dataNor[r1 - 9] - dataNor[r1 - 10] < 0:
                r11 = np.argmin(dataNor[(r1 - 20):(r1 + 20)]) + (r1 - 20)
            else:
                r11 = np.argmax(dataNor[(r1 - 20):(r1 + 20)]) + (r1 - 20)
        else:
            if dataNor[0] - dataNor[1] > 0:
                r11 = np.argmin(dataNor[0:40])
            else:
                r11 = np.argmax(dataNor[0:40])
        if r2 <= len(dataNor) - 20:
            if dataNor[r2 + 9] - dataNor[r2 + 10] < 0:
                r22 = np.argmin(dataNor[(r2 - 20):(r2 + 20)]) + (r2 - 20)
            else:
                r22 = np.argmax(dataNor[(r2 - 20):(r2 + 20)]) + (r2 - 20)
        else:
            if dataNor[-1] - dataNor[-2] < 0:
                r22 = np.argmin(dataNor[-40:]) + len(dataNor) - 40
            else:
                r22 = np.argmax(dataNor[-40:]) + len(dataNor) - 40
        print(r1, r2)
        print(r11, r22)
        p = 0
        for i in dataNor[r11:r22]:
            p = p + i ** 2
        rms = (p / (r22 - r11)) ** 0.5
        self.ui.textEdit_27.setText(str(round(rms, 3)))

    def getECG(self):
        file = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')
        f = open(file[0], encoding='UTF-8').name
        self.ui.textEdit_2.setPlainText(f)
        global dataInECG
        dataInECG = pd.read_csv(file[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)[:480000]
        dataInECG = fn.Butterworth(-dataInECG, fs, '带通', lowcut=1, highcut=20, order=4)
        print('lendatainECG:', len(dataInECG))

    def Model(self):
        t = float(self.ui.lineEdit_2.text())
        num = int(t * fs)  # 每个信号窗的数据量
        cro1 = self.ui.lineEdit_3.text()
        cro = float(cro1)
        croDot = int(cro * fs)
        w = float(self.ui.lineEdit_4.text())
        wins = int(w * fs)
        l1 = int(self.ui.lineEdit_8.text())
        l2 = int(self.ui.lineEdit_9.text())
        Rlowcut = float(self.ui.lineEdit_6.text())
        Rhighcut = float(self.ui.lineEdit_7.text())
        fb1 = float(self.ui.lineEdit_10.text())
        fb2 = float(self.ui.lineEdit_12.text())
        orderBCG = int(self.ui.lineEdit_11.text())
        Modellength = int(float(self.ui.lineEdit.text()) * fs)
        per = float(self.ui.lineEdit_13.text())
        RegionLength = float(self.ui.lineEdit_15.text())
        El = self.ui.spinBox.value()
        Er = self.ui.spinBox_2.value()

        global Resp_OUT, BCG_OUT, BCG_Out, ECGInitpos_OUT, Initpos_OUT, Initpos_OUT, ModelList, JJI
        global dataIn
        if len(dataInECG) == len(dataInBCG):
            dataIn = dataInECG
            orgBCG_win = fn.windows(dataInECG, num, croDot)
            BCG = [[] for x in range(len(orgBCG_win))]
            Resp = [[] for x in range(len(orgBCG_win))]

            ModelList = []
            Resp_OUT = np.array([])
            BCG_OUT = np.array([])
            ECGInitpos_OUT = []
            Initpos_OUT = []
            for win in range(len(orgBCG_win)):
                self.ui.progressBar.setValue((win / len(orgBCG_win)) * 100)
                # if win < 17 :continue
                # ------------------------------------------------------------------------------
                # -----------------------------------1.信号预处理---------------------------------
                # BCG[win], Resp[win] = fn.Preprocessing2(orgBCG_win[win], fs, Rlowcut, Rhighcut, fb1, fb2, orderBCG)
                BCG[win] = orgBCG_win[win]
                # Resp[win] = np.diff(Resp[win]) * 1000
                state = fn.Statedetect(BCG[win], 0.1, wins)
                # ------------------------------------2.状态检测-----------------------------------
                BCGcut, Cutmark = fn.Movement_Remove(BCG[win], state, wins)  # 按体动分开34efrdsa
                # --------------------------------3.Model Formation------------------------------
                InitPeak = []
                for n in range(len(BCGcut)):
                    InitPeak.extend(Cutmark[n] + fn.InitBeatDetect(BCGcut[n], l1, l2))
                print('Initpeak:', InitPeak)
                Model = fn.ReModel(BCG[win], Modellength, InitPeak, per)

                # print("cor start:" + str(datetime.datetime.now()))
                BCGcor = np.correlate(np.array(BCG[win]), np.array(Model), "same")  # same模式返回与最短向量相同的结果
                print('BCGcor', BCGcor)
                # print("cor end:" + str(datetime.datetime.now()))
                # print("dit start:" + str(datetime.datetime.now()))
                BCGdit = []
                for j in range(len(BCG[win]) - len(Model)):
                    # para = 2-ASD(xindata[win][j:j + len(ModelBCG[win])], ModelBCG[win])/SAD(xindata[win][j:j + len(ModelBCG[win])], ModelBCG[win])
                    para = 1
                    BCGdit.append(fn.distEuclidean(BCG[win][j:j + len(Model)], Model) * para)
                BCGdit = np.array(BCGdit)
                BCGdit = np.insert(BCGdit, 0, np.full(int(Modellength / 2), BCGdit[0]))
                BCGdit = np.append(BCGdit, np.full(int(Modellength / 2), BCGdit[-1]))
                print('BCGdit:', BCGdit)
                # print("dit end:" + str(datetime.datetime.now()))

                # ------------------------------------5.定位心跳-----------------------------------

                BCGcor_cut, cormark = fn.Movement_Remove(BCGcor, state, wins)
                BCGcor_cut = np.array(BCGcor_cut)
                BCGdit_cut, ditmark = fn.Movement_Remove(BCGdit, state, wins)

                # ------------------------------相关
                beatcor_forward = np.array([])
                beatcor_backward = np.array([])
                # print('BCGcor_cut', BCGcor_cut)
                for num in range(len(BCGcor_cut)):
                    # print('len(BCGcor_cut):', num)
                    # 求包络线
                    hx = fftpack.hilbert(BCGcor_cut[num])
                    hy = np.sqrt(BCGcor_cut[num] ** 2 + hx ** 2)
                    hy = fn.Butterworth(hy, fs, type="低通", lowcut=1, order=4)
                    # 检测位置
                    cor_forward = fn.BeatDetection(BCGcor_cut[num], hy, 900, up=1.6, down=0.1, style="peak")
                    cor_backward = fn.BeatDetection(BCGcor_cut[num][::-1], hy[::-1], 900, up=1.6, down=0.1,
                                                    style="peak")
                    cor_backward = len(BCGcor_cut[num]) - np.array(cor_backward)
                    cor_backward = np.sort(cor_backward)
                    # 组合
                    beatcor_forward = np.append(beatcor_forward, Cutmark[num] + np.array(cor_forward)).astype(int)
                    beatcor_backward = np.append(beatcor_backward, Cutmark[num] + cor_backward).astype(int)
                    # print('前向自相关检测：', cor_forward)
                    # print('前向自相关检测点',len(cor_forward))
                    # print('后向自相关检测：', cor_backward)
                    # print('后向自相关检测点', len(cor_backward))
                    # 删除错判峰
                    # meanBCG = np.mean(np.array(BCGcor[beatcor_forward]))
                    # if BCGcor[beatcor_forward[-1]] < meanBCG * 0.5:
                    #     beatcor_forward = np.delete(beatcor_forward, -1)
                    # # 删除错判峰
                    # meanBCG = np.mean(np.array(BCGcor[beatcor_backward]))
                    # if BCGcor[beatcor_backward[-1]] < meanBCG * 0.5:
                    #     beatcor_backward = np.delete(beatcor_backward, -1)

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
                    hy = fn.Butterworth(hy, fs, type="低通", lowcut=1, order=4)
                    # 检测位置
                    dit_forward = fn.BeatDetection(BCGdit_cut[num], hy, 900, up=1.6, down=0.625, style="peak")
                    # print('前向形态距检测：', dit_forward)
                    dit_backward = fn.BeatDetection(BCGdit_cut[num][::-1], hy[::-1], 900, up=1.6, down=0.625,
                                                    style="peak")
                    dit_backward = len(BCGdit_cut[num]) - np.array(dit_backward)
                    dit_backward = np.sort(dit_backward)
                    # 组合
                    beatdit_forward = np.append(beatdit_forward, Cutmark[num] + np.array(dit_forward)).astype(int)
                    beatdit_backward = np.append(beatdit_backward, Cutmark[num] + dit_backward).astype(int)
                    Corpos = np.full(len(BCG[win]), np.nan)
                    for num in beatdit_backward.astype(int):
                        Corpos[num] = BCGdit[num]

                # -----------------------------------联合统一前向后向---------------------------------------

                BeatPosition = fn.BeatChoose(beatcor_forward, beatcor_backward, beatdit_forward, beatdit_backward,
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
            # BCG_out, Resp_OUT = fn.Preprocessing2(dataInBCG, fs, Rlowcut, Rhighcut, fb1, fb2, orderBCG)
            Resp_OUT = fn.Butterworth(dataInBCG, fs, type="带通", lowcut=Rlowcut, highcut=Rhighcut, order=2)
            BCG_Out = fn.Butterworth(dataInBCG, fs, type="带通", lowcut=fb1, highcut=fb2, order=orderBCG)
            index = []
            for i in range(len(Initpos_OUT)):
                if Initpos_OUT[i] >= 0:
                    index.append(i)
            Initpos_OUT = np.full(len(BCG_Out), np.nan)
            print('lenInitpos_BCG:', len(Initpos_OUT))
            index_BCGpeak = []
            for i in index:
                if i < Er:
                    index_BCGpeak.append(np.argmax(BCG_Out[i + El:i + Er]) + i + El)
                elif Er <= i <= len(BCG_Out) - Er:
                    index_BCGpeak.append(np.argmax(BCG_Out[i + El:i + Er]) + i + El)
                elif len(BCG_Out) - Er <= i <= len(BCG_Out) - El:
                    index_BCGpeak.append(np.argmax(BCG_Out[i + El:]) + i + El)
                else:
                    pass

            for i in index_BCGpeak:
                Initpos_OUT[i] = BCG_Out[i]

            RJ_Interval = []
            for i in range(len(index_BCGpeak)):
                RJ_Interval.append(index_BCGpeak[i] - index[i])
            RJ_mean = round(np.mean(RJ_Interval), 3)
            RJ_std = round(np.std(RJ_Interval), 3)
            self.ui.textEdit_32.setText(str(RJ_mean))
            self.ui.textEdit_33.setText(str(RJ_std))

            xBCG_Out = fn.xSet(BCG_Out, fs)
            xBCG_OUT = fn.xSet(BCG_OUT, fs)
            xResp_OUT = fn.xSet(Resp_OUT, fs)
            dataIn0 = fn.Butterworth(np.array(dataIn), fs, type="高通", highcut=0.1, order=2)
            w1 = self.ui.graphicsView_2
            w1.clear()
            p1 = w1.addPlot()
            xdataIn = fn.xSet(dataIn0, fs)
            p1.plot(xdataIn, dataIn0, pen=pg.mkPen(color='b', width=1))
            p1.setLabel('bottom', 'Time(s)')
            p1.setLabel('left', 'Amplitude(mV)')
            w1.nextRow()
            p2 = w1.addPlot()
            p2.plot(xBCG_OUT, BCG_OUT, pen=pg.mkPen(color='r', width=1))
            p2.plot(xBCG_OUT, Initpos_OUT, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')
            p2.setLabel('bottom', 'Time(s)')
            p2.setLabel('left', 'Amplitude(mV)')
            p2.setXLink(p1)
            # win.addLegend(offset=(1, 1))
            w1.nextRow()
            p3 = w1.addPlot()
            p3.setXLink(p1)
            p3.plot(xBCG_Out, BCG_Out, name='BCG', pen=pg.mkPen(color='b', width=1))
            # p3.plot(xResp_OUT, Resp_OUT, name='Resp', pen=pg.mkPen(color='r', width=1))
            p3.plot(xBCG_Out, Initpos_OUT, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')
            p3.setLabel('bottom', 'Time(s)')
            p3.setLabel('left', 'Amplitude(mV)')
            lr = pg.LinearRegionItem([0, RegionLength])
            lr.setZValue(1)
            p3.addItem(lr)
            r1, r2 = lr.getRegion()
            w1.nextRow()
            p4 = w1.addPlot(title="Zoom on selected region")
            p4.plot(xBCG_Out, BCG_Out, name='BCG', pen=pg.mkPen(color='b', width=1))
            p4.plot(xBCG_Out, Initpos_OUT, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')

            JJI = np.full(len(BCG_Out), np.nan)
            for i in range(len(index_BCGpeak) - 1):
                if 500 < (index_BCGpeak[i + 1] - index_BCGpeak[i]) < 2001:
                    JJI[index_BCGpeak[i]:index_BCGpeak[i + 1]] = np.full(index_BCGpeak[i + 1] - index_BCGpeak[i],
                                                                         index_BCGpeak[i + 1] - index_BCGpeak[i])
                else:
                    pass
            self.ui.dataPlot_2.clear()
            self.ui.dataPlot_2.plot(xBCG_OUT, JJI, pen=pg.mkPen(color='m', width=1), name='JJI')

        else:
            dataIn = dataInBCG
            orgBCG_win = fn.windows(dataIn, num, croDot)
            BCG = [[] for x in range(len(orgBCG_win))]
            Resp = [[] for x in range(len(orgBCG_win))]
            # global Resp_OUT, BCG_OUT, Initpos_OUT, ModelList
            ModelList = []
            Resp_OUT = np.array([])
            BCG_OUT = np.array([])
            Initpos_OUT = []
            # AllBCGcor = np.array([])
            # AllBCGdit = np.array([])
            # AllBeat = np.array([])
            # AllJJI = np.array([])
            for win in range(len(orgBCG_win)):
                self.ui.progressBar.setValue((win / len(orgBCG_win)) * 100)
                # if win < 17 :continue
                # ------------------------------------------------------------------------------
                # -----------------------------------1.信号预处理---------------------------------
                BCG[win], Resp[win] = fn.Preprocessing2(orgBCG_win[win], fs, Rlowcut, Rhighcut, fb1, fb2, orderBCG)
                Resp[win] = np.diff(Resp[win]) * 1000
                state = fn.Statedetect(BCG[win], 0.1, wins)

                # ------------------------------------2.状态检测-----------------------------------
                BCGcut, Cutmark = fn.Movement_Remove(BCG[win], state, wins)  # 按体动分开34efrdsa
                # --------------------------------3.Model Formation------------------------------
                InitPeak = []
                for n in range(len(BCGcut)):
                    InitPeak.extend(Cutmark[n] + fn.InitBeatDetect(BCGcut[n], l1, l2))
                print('Initpeak:', InitPeak)
                Model = fn.ReModel(BCG[win], Modellength, InitPeak, per)

                # print("cor start:" + str(datetime.datetime.now()))
                BCGcor = np.correlate(np.array(BCG[win]), np.array(Model), "same")  # same模式返回与最短向量相同的结果
                print('BCGcor', BCGcor)
                # print("cor end:" + str(datetime.datetime.now()))
                # print("dit start:" + str(datetime.datetime.now()))
                BCGdit = []
                for j in range(len(BCG[win]) - len(Model)):
                    # para = 2-ASD(xindata[win][j:j + len(ModelBCG[win])], ModelBCG[win])/SAD(xindata[win][j:j + len(ModelBCG[win])], ModelBCG[win])
                    para = 1
                    BCGdit.append(fn.distEuclidean(BCG[win][j:j + len(Model)], Model) * para)
                BCGdit = np.array(BCGdit)
                BCGdit = np.insert(BCGdit, 0, np.full(int(Modellength / 2), BCGdit[0]))
                BCGdit = np.append(BCGdit, np.full(int(Modellength / 2), BCGdit[-1]))
                print('BCGdit:', BCGdit)
                # print("dit end:" + str(datetime.datetime.now()))

                # ------------------------------------5.定位心跳-----------------------------------

                BCGcor_cut, cormark = fn.Movement_Remove(BCGcor, state, wins)
                BCGcor_cut = np.array(BCGcor_cut)
                BCGdit_cut, ditmark = fn.Movement_Remove(BCGdit, state, wins)

                # ------------------------------相关
                beatcor_forward = np.array([])
                beatcor_backward = np.array([])
                # print('BCGcor_cut', BCGcor_cut)
                for num in range(len(BCGcor_cut)):
                    # print('len(BCGcor_cut):', num)
                    # 求包络线
                    hx = fftpack.hilbert(BCGcor_cut[num])
                    hy = np.sqrt(BCGcor_cut[num] ** 2 + hx ** 2)
                    hy = fn.Butterworth(hy, fs, type="低通", lowcut=1, order=4)
                    # 检测位置
                    cor_forward = fn.BeatDetection(BCGcor_cut[num], hy, 900, up=1.6, down=0.1, style="peak")
                    cor_backward = fn.BeatDetection(BCGcor_cut[num][::-1], hy[::-1], 900, up=1.6, down=0.1,
                                                    style="peak")
                    cor_backward = len(BCGcor_cut[num]) - np.array(cor_backward)
                    cor_backward = np.sort(cor_backward)
                    # 组合
                    beatcor_forward = np.append(beatcor_forward, Cutmark[num] + np.array(cor_forward)).astype(int)
                    beatcor_backward = np.append(beatcor_backward, Cutmark[num] + cor_backward).astype(int)
                    # print('前向自相关检测：', cor_forward)
                    # print('前向自相关检测点',len(cor_forward))
                    # print('后向自相关检测：', cor_backward)
                    # print('后向自相关检测点', len(cor_backward))
                    # 删除错判峰
                    # meanBCG = np.mean(np.array(BCGcor[beatcor_forward]))
                    # if BCGcor[beatcor_forward[-1]] < meanBCG * 0.5:
                    #     beatcor_forward = np.delete(beatcor_forward, -1)
                    # # 删除错判峰
                    # meanBCG = np.mean(np.array(BCGcor[beatcor_backward]))
                    # if BCGcor[beatcor_backward[-1]] < meanBCG * 0.5:
                    #     beatcor_backward = np.delete(beatcor_backward, -1)

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
                    hy = fn.Butterworth(hy, fs, type="低通", lowcut=1, order=4)
                    # 检测位置
                    dit_forward = fn.BeatDetection(BCGdit_cut[num], hy, 900, up=1.6, down=0.625, style="peak")
                    # print('前向形态距检测：', dit_forward)
                    dit_backward = fn.BeatDetection(BCGdit_cut[num][::-1], hy[::-1], 900, up=1.6, down=0.625,
                                                    style="peak")
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

                    # # 删除错判峰
                    # meanBCG = np.mean(np.array(BCGdit[beatdit_forward]))
                    # if BCGdit[beatdit_forward[-1]] < meanBCG * 0.5:
                    #    beatdit_forward = np.delete(beatdit_forward, -1)
                    # # 删除错判峰
                    # meanBCG = np.mean(np.array(BCGdit[beatdit_backward]))
                    # if BCGdit[beatdit_backward[-1]] < meanBCG * 0.5:
                    #    beatdit_backward = np.delete(beatdit_backward, -1)

                # -----------------------------------联合统一前向后向---------------------------------------

                BeatPosition = fn.BeatChoose(beatcor_forward, beatcor_backward, beatdit_forward, beatdit_backward,
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

                print(win, '/', len(orgBCG_win))

                # BeatPosition = fn.fineTun(BCG[win], BeatPosition, 200)

                # -----------------------------------------------总体合成区
                # if win == 0:
                #     BeatPosition = [x for x in BeatPosition if x < wins * fs]
                # elif win == 1:
                #     BeatPosition = [x for x in BeatPosition if croDot < x < len(BCG[win]) + croDot]
                #     BeatPosition = np.array(BeatPosition) + win * len(BCG[win]) - croDot
                # else:
                #     BeatPosition = [x for x in BeatPosition if croDot < x < len(BCG[win]) + croDot]
                #     BeatPosition = np.array(BeatPosition) + win * len(BCG[win]) - croDot
                # # ------------
                # print('beatposition:', BeatPosition)
                # if win == 0:
                #     AllBCG = np.append(AllBCG, BCG[win][: -croDot])
                #     AllResp = np.append(AllResp, Resp[win][: -croDot])
                #     AllBCGcor = np.append(AllBCGcor, BCGcor[: 30000])
                #     AllBCGdit = np.append(AllBCGdit, BCGdit[: 30000])
                # AllBeat = np.append(AllBeat, BeatPosition)
                #
                # else:
                #     AllBCG = np.append(AllBCG, BCG[win][croDot:-croDot])
                #     AllResp = np.append(AllResp, Resp[win][croDot: -croDot])
                #     AllBCGcor = np.append(AllBCGcor, BCGcor[5000: 35000])
                #     AllBCGdit = np.append(AllBCGdit, BCGdit[5000: 35000])
                # AllBeat = np.append(AllBeat, BeatPosition)
            print('lenBCGOUT:', len(BCG_OUT))
            xBCG_OUT = fn.xSet(BCG_OUT, fs)
            xResp_OUT = fn.xSet(Resp_OUT, fs)
            dataIn0 = fn.Butterworth(np.array(dataIn), fs, type="高通", highcut=0.1, order=2)
            w1 = self.ui.graphicsView_2
            w1.clear()
            p1 = w1.addPlot()
            xdataIn = fn.xSet(dataIn0, fs)
            p1.plot(xdataIn, dataIn0, pen=pg.mkPen(color='b', width=1))
            p1.plot(xResp_OUT, Resp_OUT, name='Resp', pen=pg.mkPen(color='r', width=1))
            p1.setLabel('bottom', 'Time(s)')
            p1.setLabel('left', 'Amplitude(mV)')
            # win.addLegend(offset=(1, 1))
            w1.nextRow()
            p3 = w1.addPlot()
            p3.setXLink(p1)
            p3.plot(xBCG_OUT, BCG_OUT, name='BCG', pen=pg.mkPen(color='b', width=1))
            p3.plot(xBCG_OUT, Initpos_OUT, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')
            p3.setLabel('bottom', 'Time(s)')
            p3.setLabel('left', 'Amplitude(mV)')
            lr = pg.LinearRegionItem([0, RegionLength])
            lr.setZValue(1)
            p3.addItem(lr)
            r1, r2 = lr.getRegion()
            w1.nextRow()
            p4 = w1.addPlot(title="Zoom on selected region")
            p4.plot(xBCG_OUT, BCG_OUT, name='BCG', pen=pg.mkPen(color='b', width=1))
            p4.plot(xBCG_OUT, Initpos_OUT, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')

            def updatePlot():
                p4.setXRange(*lr.getRegion(), padding=0)
                global r1, r2
                r11, r22 = lr.getRegion()
                # r22 = r11 + RegionLength
                if r11 < 0:
                    r11 = 0
                if r22 > len(BCG_OUT):
                    r22 = len(BCG_OUT)
                r1 = int(r11 * fs)
                r2 = int(r22 * fs)
                print('r1, r2:', r1, r2)

            def updateRegion():
                lr.setRegion(p4.getViewBox().viewRange()[0])

            lr.sigRegionChanged.connect(updatePlot)
            p4.sigXRangeChanged.connect(updateRegion)
            updatePlot()

            # global dataInECG
            if len(dataInECG) == 0:
                pass
            else:
                xdataInECG = fn.xSet(dataInECG, fs)
                w1.nextRow()
                p2 = w1.addPlot()
                p2.plot(xdataInECG, dataInECG, pen=pg.mkPen(color='r', width=1))
                p2.setLabel('bottom', 'Time(s)')
                p2.setLabel('left', 'Amplitude(mV)')
                p2.setXLink(p1)
            # self.ui.dataPlot_2.plot(k * dataInECG + b, pen=pg.mkPen(color='r', width=1), name='ECG')
            # dataInECG = []

            p3.plot(xBCG_OUT, Initpos_OUT, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')
            # self.ui.dataPlot_2.setXLink(self.ui.dataPlot)
            self.ui.dataPlot_2.setXLink(p1)
            # self.ui.dataPlot_2.plot(Initpos_OUT, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')
            self.ui.progressBar.setValue(100)
            index_out = []
            for i in range(len(Initpos_OUT)):
                if Initpos_OUT[i] >= 0:
                    index_out.append(i)
            global dataOut
            dataOut = index_out

            JJI = np.full(len(BCG_OUT), np.nan)
            for i in range(len(index_out) - 1):
                if 500 < (index_out[i + 1] - index_out[i]) < 2001:
                    JJI[index_out[i]:index_out[i + 1]] = np.full(index_out[i + 1] - index_out[i],
                                                                 index_out[i + 1] - index_out[i])
                else:
                    pass
            self.ui.dataPlot_2.clear()
            self.ui.dataPlot_2.plot(xBCG_OUT, JJI, pen=pg.mkPen(color='m', width=1), name='JJI')

    def ModelDis(self):
        BCGRegion = BCG_Out[r1: r2]
        InitposRegion = Initpos_OUT[r1:r2]
        PBCG = 0
        PResp = 0
        for i in range(r1, r2 - 3):
            PBCG = PBCG + (BCG_Out[i]) ** 2
            PResp = PResp + (Resp_OUT[i]) ** 2
        P = round(PResp / PBCG, 3)
        global fs
        fs = float(self.ui.lineEdit_5.text())
        t = float(self.ui.lineEdit_2.text())
        num = int(t * fs)  # 每个信号窗的数据量
        cro = float(self.ui.lineEdit_3.text())
        croDot = int(cro * fs)
        w = float(self.ui.lineEdit_4.text())
        Modellength = int(float(self.ui.lineEdit.text()) * fs)
        self.ui.textEdit_3.setPlainText(str(P))
        per = float(self.ui.lineEdit_13.text())  # 模板提取分位数
        per2 = float(self.ui.lineEdit_14.text())
        RegionLength = float(self.ui.lineEdit_15.text())
        orgInitpos_win = fn.windows(InitposRegion, num, croDot)
        orgInitpos_win = orgInitpos_win[0]
        InitPeak = []
        for i in range(len(orgInitpos_win)):
            if orgInitpos_win[i] > 0:
                InitPeak.append(i)
        global Model
        Model = fn.ReModel(BCGRegion, Modellength, InitPeak, per)
        ModelList.append(Model)
        # print('ModelList:', ModelList)
        PeakList = []
        for i in range(len(ModelList)):
            j = 0.4 * Modellength + i * Modellength
            PeakList.append(int(j))

        cor = fn.Cor(ModelList)
        self.ui.textEdit_22.setText(str(round(cor, 3)))
        Max = max(Model)
        Min = min(Model)
        xModel = fn.xSet(Model, fs)
        w2 = self.ui.graphicsView
        pw1 = w2.addPlot()
        pw1.setLabel('bottom', 'Time(s)')
        pw1.plot(xModel, (Model - Min) / (Max - Min), pen=pg.mkPen(color='r', width=2))
        Initpos = []
        for i in range(len(Initpos_OUT)):
            if Initpos_OUT[i] > 0:
                Initpos.append(i)
        SNR = fn.SNR(BCGRegion, InitPeak, Modellength)
        self.ui.textEdit_18.setPlainText(str(round(SNR, 3)))
        tSQI = fn.tSQI(BCGRegion, InitPeak, Modellength)
        self.ui.textEdit_21.setPlainText(str(round(tSQI, 3)))
        index_out = []
        for i in range(len(InitposRegion)):
            if InitposRegion[i] >= 0:
                index_out.append(i)
        Mean_HR = round(60 / ((index_out[-1] - index_out[0]) / ((len(index_out) - 1) * fs)), 1)
        self.ui.textEdit_19.setPlainText(str(Mean_HR))

    def clear(self):
        win = self.ui.graphicsView
        win.clear()

    def clear2(self):
        win = self.ui.graphicsView_2
        win.clear()

    def setModel(self):
        BCGRegion = BCG_Out[r1: r2]
        InitposRegion = Initpos_OUT[r1:r2]
        RespRegion = Resp_OUT[r1:r2]
        JJIRegion = JJI[r1:r2]
        PBCG = 0
        PResp = 0
        for i in range(r1, r2 - 3):
            PBCG = PBCG + (BCG_OUT[i]) ** 2
            PResp = PResp + (Resp_OUT[i]) ** 2
        P = round(PResp / PBCG, 3)
        global fs
        fs = float(self.ui.lineEdit_5.text())
        t = float(self.ui.lineEdit_2.text())
        num = int(t * fs)  # 每个信号窗的数据量
        cro = float(self.ui.lineEdit_3.text())
        croDot = int(cro * fs)
        w = float(self.ui.lineEdit_4.text())
        wins = int(w * fs)
        Rlowcut = float(self.ui.lineEdit_6.text())
        Rhighcut = float(self.ui.lineEdit_7.text())
        l1 = int(self.ui.lineEdit_8.text())
        l2 = int(self.ui.lineEdit_9.text())
        Modellength = int(float(self.ui.lineEdit.text()) * fs)
        self.ui.textEdit_3.setPlainText(str(P))
        per = float(self.ui.lineEdit_13.text())  # 模板提取分位数
        per2 = float(self.ui.lineEdit_14.text())

        orgBCG_win = fn.windows(BCGRegion, num, croDot)
        orgInitpos_win = fn.windows(InitposRegion, num, croDot)
        BCG = [[] for x in range(len(orgBCG_win))]
        # Resp = [[] for x in range(len(orgBCG_win))]
        # AllBCG = np.array([])
        # global Resp_OUT, BCG_OUT
        Resp_OUT2 = np.array([])
        BCG_OUT2 = np.array([])
        meanModel = np.zeros(Modellength)
        ModelSum = []
        global Model
        print('lenRegion:', len(BCGRegion))
        for win in range(len(orgBCG_win)):
            self.ui.progressBar.setValue((win / len(orgBCG_win)) * 100)  # 设置进度条
            # if win < 17 :continue
            # ------------------------------------------------------------------------------
            # -----------------------------------1.信号预处理---------------------------------
            # BCG[win], Resp[win] = fn.Preprocessing2(orgBCG_win[win], fs, Rlowcut, Rhighcut)
            BCG[win] = orgBCG_win[win]

            # Resp[win] = np.diff(Resp[win]) * 1000
            # state = fn.Statedetect(BCG[win], 0.1, wins)

            # ------------------------------------2.状态检测-----------------------------------
            # BCGcut, Cutmark = fn.CutData(BCG[win], state, wins)  # 按体动分开34efrdsa

            # --------------------------------3.Model Formation------------------------------
            InitPeak = []
            for i in range(len(orgInitpos_win[win])):
                if orgInitpos_win[win][i] > 0:
                    InitPeak.append(i)

            Model = fn.ReModel(BCG[win], Modellength, InitPeak, per)
            ModelSum.append(np.array(Model))
            Max = max(Model)
            Min = min(Model)
            xModel = fn.xSet(Model, fs)
            for i in range(len(Model)):
                if Model[i] > 0:
                    Model[i] = Model[i] / Max
                else:
                    Model[i] = Model[i] / (-Min)
            w2 = self.ui.graphicsView
            pw1 = w2.addPlot()
            pw1.setLabel('left', 'Normalized Amplitude')
            pw1.setLabel('bottom', 'Time(s)')
            # pw1.plot(xModel, (Model - Min) / (Max - Min), pen=pg.mkPen(color='b', width=2))
            pw1.plot(xModel, Model, pen=pg.mkPen(color='b', width=2))

            # print("cor start:" + str(datetime.datetime.now()))
            BCGcor = np.correlate(np.array(BCG[win]), np.array(Model), "same")

            # print("cor end:" + str(datetime.datetime.now()))
            # print("dit start:" + str(datetime.datetime.now()))
            BCGdit = []
            for j in range(len(BCG[win]) - len(Model)):
                # para = 2-ASD(xindata[win][j:j + len(ModelBCG[win])], ModelBCG[win])/SAD(xindata[win][j:j + len(ModelBCG[win])], ModelBCG[win])
                para = 1
                BCGdit.append(fn.distEuclidean(BCG[win][j:j + len(Model)], Model) * para)
            BCGdit = np.array(BCGdit)
            BCGdit = np.insert(BCGdit, 0, np.full(int(Modellength / 2), BCGdit[0]))
            BCGdit = np.append(BCGdit, np.full(int(Modellength / 2), BCGdit[-1]))
            # print("dit end:" + str(datetime.datetime.now()))

            # ------------------------------------5.定位心跳-----------------------------------

            # BCGcor_cut, cormark = fn.CutData(BCGcor, state, wins)
            # BCGcor_cut = np.array(BCGcor_cut)
            # BCGdit_cut, ditmark = fn.CutData(BCGdit, state, wins)
            # ------------------------------相关
            beatcor_forward = np.array([])
            beatcor_backward = np.array([])
            # ---------------------------------形态距
            beatdit_forward = np.array([])
            beatdit_backward = np.array([])

            # -----------------------------------联合统一前向后向---------------------------------------

            BeatPosition = fn.BeatChoose(beatcor_forward, beatcor_backward, beatdit_forward, beatdit_backward,
                                         900).astype(int)
            # print('最终点坐标', BeatPosition)
            # print('最终点个数', len(BeatPosition))
            # ---------------------------------------END---------------------------------------------
            BCGcor = BCGcor / 40000
            BCGdit = BCGdit / 20
            # -----------------------------------------------标记展示区

            # InitPeak = np.array(InitPeak).astype(int)
            # Initpos = np.full(len(BCG[win]), np.nan)
            # for num in InitPeak:
            #     Initpos[num] = BCG[win][num]

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

            if win == 0:
                BCG_OUT2 = np.append(BCG_OUT2, BCG[win][:-croDot])
                # Resp_OUT2 = np.append(Resp_OUT2, Resp[win][:-croDot])
                # Initpos_OUT = np.append(Initpos_OUT, Initpos[:-croDot])
            elif win != len(orgBCG_win) - 1:
                BCG_OUT2 = np.append(BCG_OUT2, BCG[win][croDot:-croDot])
                # Resp_OUT2 = np.append(Resp_OUT2, Resp[win][croDot:-croDot])
                # Initpos_OUT = np.append(Initpos_OUT, Initpos[croDot:-croDot])
            else:
                BCG_OUT2 = np.append(BCG_OUT2, BCG[win][croDot:])
                # Resp_OUT2 = np.append(Resp_OUT2, Resp[win][croDot:])
                # Initpos_OUT = np.append(Initpos_OUT, Initpos[croDot:])

            print(win, '/', len(orgBCG_win))
        Initpos = []
        for i in range(len(InitposRegion)):
            if InitposRegion[i] > 0:
                Initpos.append(i)
        SNR = fn.SNR(BCGRegion, Initpos, Modellength)
        self.ui.textEdit_18.setPlainText(str(round(SNR, 3)))
        tSQI = fn.tSQI(BCGRegion, Initpos, Modellength)
        self.ui.textEdit_21.setPlainText(str(round(tSQI, 3)))
        for i in range(len(ModelSum)):
            meanModel += ModelSum[i]
        meanModel = meanModel / len(ModelSum)
        # Model = fn.ReModel2(BCGRegion, meanModel, Modellength, Initpos, per2)
        Max = max(meanModel)
        Min = min(meanModel)
        xModel = fn.xSet(meanModel, fs)
        w2 = self.ui.graphicsView
        pw1 = w2.addPlot()
        pw1.setLabel('bottom', 'Time(s)')
        pw1.plot(xModel, (meanModel - Min) / (Max - Min), pen=pg.mkPen(color='r', width=2))

        dataIn0 = fn.Butterworth(np.array(dataIn), fs, type="高通", highcut=0.1, order=2)
        xBCG_OUT = fn.xSet(BCGRegion, fs)
        xRespRegion = fn.xSet(RespRegion, fs)
        w1 = self.ui.graphicsView_2
        w1.clear()
        p1 = w1.addPlot()
        xdataIn = fn.xSet(dataIn0[r1:r2], fs)
        p1.plot(xdataIn, dataIn0[r1:r2], pen=pg.mkPen(color='b', width=1))
        p1.plot(xRespRegion, RespRegion, name='Resp', pen=pg.mkPen(color='r', width=1))
        p1.setLabel('bottom', 'Time(s)')
        w1.nextRow()
        p3 = w1.addPlot()
        p3.setXLink(p1)
        p3.plot(xBCG_OUT, BCGRegion, name='BCG', pen=pg.mkPen(color='b', width=1))
        # p3.plot(xRespRegion, RespRegion, name='Resp', pen=pg.mkPen(color='r', width=1))
        p3.plot(xBCG_OUT, InitposRegion, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')
        p3.setLabel('bottom', 'Time(s)')
        p3.setLabel('left', 'Amplitude(mV)')
        # p3.setLabel('right', 'Low SNR')
        lr = pg.LinearRegionItem([5, 15])
        lr.setZValue(1)
        p3.addItem(lr)
        w1.nextRow()
        p4 = w1.addPlot(title="Zoom on selected region")
        p4.plot(xBCG_OUT, BCGRegion, name='BCG', pen=pg.mkPen(color='b', width=1))
        p4.plot(xBCG_OUT, InitposRegion, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')

        def updatePlot():
            p4.setXRange(*lr.getRegion(), padding=0)
            global r1, r2
            r11, r22 = lr.getRegion()
            r1 = int(r11 * fs)
            r2 = int(r22 * fs)
            print(r1, r2)

        def updateRegion():
            lr.setRegion(p4.getViewBox().viewRange()[0])

        lr.sigRegionChanged.connect(updatePlot)
        p4.sigXRangeChanged.connect(updateRegion)
        updatePlot()

        global dataInECG
        if len(dataInECG) == 0:
            pass
        else:
            xdataInECG = fn.xSet(dataInECG, fs)
            w1.nextRow()
            p2 = w1.addPlot()
            p2.plot(xdataInECG, dataInECG, pen=pg.mkPen(color='r', width=1))
            p2.setLabel('bottom', 'Time(s)')
            p2.setLabel('left', 'Amplitude(mV)')
            p2.setXLink(p1)
            dataInECG = []

        self.ui.dataPlot_2.setXLink(p1)
        self.ui.progressBar.setValue(100)
        index_out = []
        for i in range(len(InitposRegion)):
            if InitposRegion[i] >= 0:
                index_out.append(i)
        Mean_HR = round(60 / ((index_out[-1] - index_out[0]) / ((len(index_out) - 1) * fs)), 1)
        self.ui.textEdit_19.setPlainText(str(Mean_HR))
        global dataOut
        dataOut = index_out
        self.ui.dataPlot_2.clear()
        self.ui.dataPlot_2.plot(xBCG_OUT, JJIRegion, pen=pg.mkPen(color='m', width=1), name='JJI')

    def clear(self):
        win = self.ui.graphicsView
        win.clear()

    def clear2(self):
        win = self.ui.graphicsView_2
        win.clear()


class MD_TemplateMatching:

    def __init__(self):
        self.ui = QUiLoader().load('MD_TemplateMatching.ui')
        self.ui.lineEdit_5.setText('1000')
        self.ui.lineEdit.setText('0.7')
        self.ui.lineEdit_2.setText('10')
        self.ui.lineEdit_3.setText('1')
        self.ui.lineEdit_4.setText('1')
        self.ui.doubleSpinBox.setValue(1)
        self.ui.doubleSpinBox.setRange(0.00001, 10000)
        self.ui.doubleSpinBox_2.setValue(-300)
        self.ui.doubleSpinBox_2.setRange(-10000, 10000)
        self.ui.doubleSpinBox_2.setSingleStep(100)
        self.ui.progressBar.setValue(0)
        self.ui.lineEdit_6.setText('0.01')
        self.ui.lineEdit_7.setText('0.7')
        self.ui.pushButton_2.clicked.connect(self.getBCG)
        self.ui.pushButton_6.clicked.connect(self.getECG)
        self.ui.returnMainWin.clicked.connect(fn.returnMain4)
        self.ui.pushButton_4.clicked.connect(self.Model)
        self.ui.pushButton_5.clicked.connect(SI.butterMsg.getname)
        self.ui.pushButton_7.clicked.connect(self.saveResp)
        self.ui.pushButton_8.clicked.connect(fn.toHRWin)
        # self.ui.pushButton.clicked.connect(self.operateECG)
        # self.ui.pushButton_7.cliked.connect(self.respPlot)

    def saveResp(self):
        global dataOut
        dataOut = Resp_OUT
        SI.butterMsg.getname()

    def getBCG(self):
        file = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')
        f = open(file[0], encoding='UTF-8').name
        self.ui.textEdit.setPlainText(f)
        global dataIn
        dataIn = pd.read_csv(file[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)
        self.ui.dataPlot.clear()
        self.ui.dataPlot.plot(dataIn, pen=pg.mkPen(color='b', width=1))

    def getECG(self):
        file = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')
        f = open(file[0], encoding='UTF-8').name
        self.ui.textEdit_2.setPlainText(f)
        global dataInECG
        dataInECG = pd.read_csv(file[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)
        self.ui.dataPlot.plot(dataInECG, pen=pg.mkPen(color='r', width=1))

    def Model(self):
        global fs
        fs = float(self.ui.lineEdit_5.text())
        t = float(self.ui.lineEdit_2.text())
        num = int(t * fs)  # 每个信号窗的数据量
        cro1 = self.ui.lineEdit_3.text()
        cro = float(cro1)
        croDot = int(cro * fs)
        w = float(self.ui.lineEdit_4.text())
        wins = int(w * fs)
        k = float(self.ui.doubleSpinBox.value())
        b = int(self.ui.doubleSpinBox_2.value())
        Rlowcut = float(self.ui.lineEdit_6.text())
        Rhighcut = float(self.ui.lineEdit_7.text())
        Modellength = int(float(self.ui.lineEdit.text()) * fs)
        orgBCG_win = fn.windows(dataIn, num, croDot)
        # print('orgdata:', orgBCG_win)
        BCG = [[] for x in range(len(orgBCG_win))]
        Resp = [[] for x in range(len(orgBCG_win))]

        # AllBCG = np.array([])
        global Resp_OUT, BCG_OUT, Initpos_OUT
        Resp_OUT = np.array([])
        BCG_OUT = np.array([])
        Initpos_OUT = []
        # AllBCGcor = np.array([])
        # AllBCGdit = np.array([])
        # AllBeat = np.array([])
        # AllJJI = np.array([])
        print('len(orgBCG_win):', len(orgBCG_win))
        for win in range(len(orgBCG_win)):
            self.ui.progressBar.setValue((win / len(orgBCG_win)) * 100)
            # if win < 17 :continue
            # ------------------------------------------------------------------------------
            # -----------------------------------1.信号预处理---------------------------------
            BCG[win], Resp[win] = fn.Preprocessing2(orgBCG_win[win], fs, Rlowcut, Rhighcut)
            Resp[win] = np.diff(Resp[win]) * 1000
            state = fn.Statedetect(BCG[win], 0.1, wins)

            # ------------------------------------2.状态检测-----------------------------------
            BCGcut, Cutmark = fn.CutData(BCG[win], state, wins)  # 按体动分开34efrdsa

            # --------------------------------3.Model Formation------------------------------
            InitPeak = []
            for n in range(len(BCGcut)):
                # print('BCGcut[n]:', BCGcut[n])
                InitPeak.extend(Cutmark[n] + fn.InitBeatDetect(BCGcut[n]))
            Model = fn.Modeldetect(BCG[win], Modellength, InitPeak)
            # print("cor start:" + str(datetime.datetime.now()))
            BCGcor = np.correlate(np.array(BCG[win]), np.array(Model), "same")
            # print("cor end:" + str(datetime.datetime.now()))
            # print("dit start:" + str(datetime.datetime.now()))
            BCGdit = []
            for j in range(len(BCG[win]) - len(Model)):
                # para = 2-ASD(xindata[win][j:j + len(ModelBCG[win])], ModelBCG[win])/SAD(xindata[win][j:j + len(ModelBCG[win])], ModelBCG[win])
                para = 1
                BCGdit.append(fn.distEuclidean(BCG[win][j:j + len(Model)], Model) * para)
            BCGdit = np.array(BCGdit)
            BCGdit = np.insert(BCGdit, 0, np.full(int(Modellength / 2), BCGdit[0]))
            BCGdit = np.append(BCGdit, np.full(int(Modellength / 2), BCGdit[-1]))
            # print("dit end:" + str(datetime.datetime.now()))

            # ------------------------------------5.定位心跳-----------------------------------

            BCGcor_cut, cormark = fn.CutData(BCGcor, state, wins)
            BCGcor_cut = np.array(BCGcor_cut)
            BCGdit_cut, ditmark = fn.CutData(BCGdit, state, wins)
            # ------------------------------相关
            beatcor_forward = np.array([])
            beatcor_backward = np.array([])
            # print('BCGcor_cut', BCGcor_cut)
            for num in range(len(BCGcor_cut)):
                # print('len(BCGcor_cut):', num)
                # 求包络线
                hx = fftpack.hilbert(BCGcor_cut[num])
                hy = np.sqrt(BCGcor_cut[num] ** 2 + hx ** 2)
                hy = fn.Butterworth(hy, fs, type="低通", lowcut=1, order=4)
                # 检测位置
                cor_forward = fn.BeatDetection(BCGcor_cut[num], hy, 900, up=1.6, down=0.1, style="peak")
                cor_backward = fn.BeatDetection(BCGcor_cut[num][::-1], hy[::-1], 900, up=1.6, down=0.1, style="peak")
                cor_backward = len(BCGcor_cut[num]) - np.array(cor_backward)
                cor_backward = np.sort(cor_backward)
                # 组合
                beatcor_forward = np.append(beatcor_forward, Cutmark[num] + np.array(cor_forward)).astype(int)
                beatcor_backward = np.append(beatcor_backward, Cutmark[num] + cor_backward).astype(int)
                # print('前向自相关检测：', cor_forward)
                # print('前向自相关检测点',len(cor_forward))
                # print('后向自相关检测：', cor_backward)
                # print('后向自相关检测点', len(cor_backward))
                # 删除错判峰
                # meanBCG = np.mean(np.array(BCGcor[beatcor_forward]))
                # if BCGcor[beatcor_forward[-1]] < meanBCG * 0.5:
                #     beatcor_forward = np.delete(beatcor_forward, -1)
                # # 删除错判峰
                # meanBCG = np.mean(np.array(BCGcor[beatcor_backward]))
                # if BCGcor[beatcor_backward[-1]] < meanBCG * 0.5:
                #     beatcor_backward = np.delete(beatcor_backward, -1)

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
                hy = fn.Butterworth(hy, fs, type="低通", lowcut=1, order=4)
                # 检测位置
                dit_forward = fn.BeatDetection(BCGdit_cut[num], hy, 900, up=1.6, down=0.625, style="peak")
                # print('前向形态距检测：', dit_forward)
                dit_backward = fn.BeatDetection(BCGdit_cut[num][::-1], hy[::-1], 900, up=1.6, down=0.625, style="peak")
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

                # # 删除错判峰
                # meanBCG = np.mean(np.array(BCGdit[beatdit_forward]))
                # if BCGdit[beatdit_forward[-1]] < meanBCG * 0.5:
                #    beatdit_forward = np.delete(beatdit_forward, -1)
                # # 删除错判峰
                # meanBCG = np.mean(np.array(BCGdit[beatdit_backward]))
                # if BCGdit[beatdit_backward[-1]] < meanBCG * 0.5:
                #    beatdit_backward = np.delete(beatdit_backward, -1)

            # -----------------------------------联合统一前向后向---------------------------------------

            BeatPosition = fn.BeatChoose(beatcor_forward, beatcor_backward, beatdit_forward, beatdit_backward,
                                         900).astype(int)
            # print('最终点坐标', BeatPosition)
            # print('最终点个数', len(BeatPosition))
            # ---------------------------------------END---------------------------------------------
            BCGcor = BCGcor / 40000
            BCGdit = BCGdit / 20
            # -----------------------------------------------标记展示区

            InitPeak = np.array(InitPeak).astype(int)
            Initpos = np.full(len(BCG[win]), np.nan)
            for num in InitPeak:
                Initpos[num] = BCG[win][num]

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
            print(win, '/', len(orgBCG_win))

            # BeatPosition = fn.fineTun(BCG[win], BeatPosition, 200)

            # -----------------------------------------------总体合成区
            # if win == 0:
            #     BeatPosition = [x for x in BeatPosition if x < wins * fs]
            # elif win == 1:
            #     BeatPosition = [x for x in BeatPosition if croDot < x < len(BCG[win]) + croDot]
            #     BeatPosition = np.array(BeatPosition) + win * len(BCG[win]) - croDot
            # else:
            #     BeatPosition = [x for x in BeatPosition if croDot < x < len(BCG[win]) + croDot]
            #     BeatPosition = np.array(BeatPosition) + win * len(BCG[win]) - croDot
            # # ------------
            # print('beatposition:', BeatPosition)
            # if win == 0:
            #     AllBCG = np.append(AllBCG, BCG[win][: -croDot])
            #     AllResp = np.append(AllResp, Resp[win][: -croDot])
            #     AllBCGcor = np.append(AllBCGcor, BCGcor[: 30000])
            #     AllBCGdit = np.append(AllBCGdit, BCGdit[: 30000])
            # AllBeat = np.append(AllBeat, BeatPosition)
            #
            # else:
            #     AllBCG = np.append(AllBCG, BCG[win][croDot:-croDot])
            #     AllResp = np.append(AllResp, Resp[win][croDot: -croDot])
            #     AllBCGcor = np.append(AllBCGcor, BCGcor[5000: 35000])
            #     AllBCGdit = np.append(AllBCGdit, BCGdit[5000: 35000])
            # AllBeat = np.append(AllBeat, BeatPosition)

        self.ui.dataPlot_2.clear()
        self.ui.dataPlot_2.addLegend(offset=(1, 1))
        # self.ui.dataPlot_2.plot(AllBCG, name='BCG', pen=pg.mkPen(color='b', width=1))
        self.ui.dataPlot_2.plot(BCG_OUT, name='BCG', pen=pg.mkPen(color='b', width=1))
        self.ui.dataPlot_2.plot(Resp_OUT, name='Resp', pen=pg.mkPen(color='r', width=1))
        global dataInECG
        if len(dataInECG) == 0:
            pass
        else:
            self.ui.dataPlot_2.plot(k * dataInECG + b, pen=pg.mkPen(color='r', width=1), name='ECG')
            dataInECG = []
        self.ui.dataPlot_2.setXLink(self.ui.dataPlot)
        self.ui.dataPlot_2.plot(Initpos_OUT, name='Init_Jpeak', pen=None, symbolBrush=(255, 0, 0), symbol='o')
        self.ui.progressBar.setValue(100)
        index_out = []
        for i in range(len(Initpos_OUT)):
            if Initpos_OUT[i] >= 0:
                index_out.append(i)
        global dataOut
        dataOut = index_out
        global JJI
        JJI = np.full(len(BCG_OUT), np.nan)
        for i in range(len(index_out) - 1):
            if 500 < (index_out[i + 1] - index_out[i]) < 2001:
                JJI[index_out[i]:index_out[i + 1]] = np.full(index_out[i + 1] - index_out[i],
                                                             index_out[i + 1] - index_out[i])
            else:
                pass

        self.ui.dataPlot_2.plot(range(len(BCG_OUT)), JJI, pen=pg.mkPen(color='m', width=1), name='JJI')


class HeartRate:
    def __init__(self):
        loader = QUiLoader()
        loader.registerCustomWidget(pg.PlotWidget)
        loader.registerCustomWidget(pg.GraphicsLayoutWidget)
        self.ui = loader.load('HeartRate.ui')
        self.ui.lineEdit.setText('40')
        newItem = QTableWidgetItem('Mean JJ')
        newItem_3 = QTableWidgetItem('ms')
        newItem1 = QTableWidgetItem('STD JJ')
        newItem1_3 = QTableWidgetItem('ms')
        newItem2 = QTableWidgetItem('Mean HR')
        newItem2_3 = QTableWidgetItem('beats/min')
        newItem3 = QTableWidgetItem('STD HR')
        newItem3_3 = QTableWidgetItem('beats/min')
        newItem4 = QTableWidgetItem('RMSSD')
        newItem4_3 = QTableWidgetItem('ms')
        newItem5 = QTableWidgetItem('NN50')
        newItem5_3 = QTableWidgetItem('count')
        newItem6 = QTableWidgetItem('pNN50')
        newItem6_3 = QTableWidgetItem('%')
        # newItem6 = QTableWidgetItem('pNN50')
        # newItem6_3 = QTableWidgetItem('%')

        self.ui.lineEdit_2.setText('120')
        self.ui.lineEdit_3.setText('1000')
        self.ui.tableWidget.setItem(0, 0, newItem)
        self.ui.tableWidget.setItem(0, 2, newItem_3)
        self.ui.tableWidget.setItem(1, 0, newItem1)
        self.ui.tableWidget.setItem(1, 2, newItem1_3)
        self.ui.tableWidget.setItem(2, 0, newItem2)
        self.ui.tableWidget.setItem(2, 2, newItem2_3)
        self.ui.tableWidget.setItem(3, 0, newItem3)
        self.ui.tableWidget.setItem(3, 2, newItem3_3)
        self.ui.tableWidget.setItem(4, 0, newItem4)
        self.ui.tableWidget.setItem(4, 2, newItem4_3)
        self.ui.tableWidget.setItem(5, 0, newItem5)
        self.ui.tableWidget.setItem(5, 2, newItem5_3)
        self.ui.tableWidget.setItem(6, 0, newItem6)
        self.ui.tableWidget.setItem(6, 2, newItem6_3)
        nonlinearItem = QTableWidgetItem('SD1')
        nonlinearItem_3 = QTableWidgetItem('ms')
        nonlinearItem2 = QTableWidgetItem('SD2')
        nonlinearItem2_3 = QTableWidgetItem('ms')
        self.ui.tableWidget_2.setItem(0, 0, nonlinearItem)
        self.ui.tableWidget_2.setItem(0, 2, nonlinearItem_3)
        self.ui.tableWidget_2.setItem(1, 0, nonlinearItem2)
        self.ui.tableWidget_2.setItem(1, 2, nonlinearItem2_3)
        self.ui.pushButton.clicked.connect(self.HRplot)
        self.ui.pushButton_2.clicked.connect(self.PoincarePlot)
        self.ui.pushButton_3.clicked.connect(self.clear)
        # self.ui.pushButton_4.clicked.connect(self.clearOne)
        self.ui.pushButton_5.clicked.connect(self.getBCG)
        self.ui.pushButton_6.clicked.connect(self.getJpeaks)

    def getBCG(self):
        file = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')
        f = open(file[0], encoding='UTF-8').name
        self.ui.textEdit.setPlainText(f)
        global BCG_OUT
        BCG_OUT = pd.read_csv(file[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)

    def getJpeaks(self):
        file = QFileDialog.getOpenFileName(self.ui, u'Open file', '/')
        f = open(file[0], encoding='UTF-8').name
        self.ui.textEdit_2.setPlainText(f)
        global dataOut
        dataOut = pd.read_csv(file[0], 'r', encoding='UTF-8', header=None).to_numpy().reshape(-1)

    def HRplot(self):
        HRfs = float(self.ui.lineEdit_3.text())
        win = self.ui.graphicsView
        Mean_JJ = round((dataOut[-1] - dataOut[0]) / (len(dataOut) - 1), 2)
        Mean_HR = round(60 / ((dataOut[-1] - dataOut[0]) / ((len(dataOut) - 1) * HRfs)), 3)
        b = c = d = 0
        for i in range(len(dataOut) - 1):
            a = ((dataOut[i + 1] - dataOut[i]) - Mean_JJ) ** 2
            b = a + b
        SDNN = round((b / (len(dataOut) - 1)) ** 0.5, 3)
        for i in range(len(dataOut) - 1):
            a = (((dataOut[i + 1] - dataOut[i]) / HRfs) * 60 - Mean_HR) ** 2
            c = a + c
        STD_HR = round((c / (len(dataOut) - 1)) ** 0.5, 3)
        for i in range(len(dataOut) - 2):
            a = ((dataOut[i + 2] - dataOut[i + 1]) - (dataOut[i + 1] - dataOut[i])) ** 2
            d = a + d
        RMSSD = round((d / (len(dataOut) - 2)) ** 0.5, 3)
        NN50 = 0
        for i in range(len(dataOut) - 2):
            if 1000 * ((dataOut[i + 2] - dataOut[i + 1]) - (dataOut[i + 1] - dataOut[i])) / HRfs > 50:
                NN50 += 1
            else:
                pass
        pNN50 = round(100 * NN50 / (len(dataOut) - 2), 3)
        newItem_2 = QTableWidgetItem(str(Mean_JJ))
        newItem1_2 = QTableWidgetItem(str(SDNN))
        newItem2_2 = QTableWidgetItem(str(Mean_HR))
        newItem3_2 = QTableWidgetItem(str(STD_HR))
        newItem4_2 = QTableWidgetItem(str(RMSSD))
        newItem5_2 = QTableWidgetItem(str(NN50))
        newItem6_2 = QTableWidgetItem(str(pNN50))
        self.ui.tableWidget.setItem(0, 1, newItem_2)
        self.ui.tableWidget.setItem(1, 1, newItem1_2)
        self.ui.tableWidget.setItem(2, 1, newItem2_2)
        self.ui.tableWidget.setItem(3, 1, newItem3_2)
        self.ui.tableWidget.setItem(4, 1, newItem4_2)
        self.ui.tableWidget.setItem(5, 1, newItem5_2)
        self.ui.tableWidget.setItem(6, 1, newItem6_2)
        p1 = win.addPlot()
        p2 = win.addPlot()
        win.nextRow()
        p3 = win.addPlot(colspan=2)
        data = np.hstack(np.array(dataOut))

        l1 = len(BCG_OUT) / HRfs
        l2 = int(len(BCG_OUT) / HRfs)
        if l1 == l2:
            BCG = BCG_OUT
        else:
            BCG = BCG_OUT[:int(l2 * HRfs)]
        y = []
        for i in range(l2 - 60):
            count = 0
            for j in data:
                if i * HRfs <= j < (i + 60) * HRfs:
                    count += 1
            y.append(count)
            # y, x = np.histogram(data, bins=np.linspace(0, len(BCG), l2 + 1))
        # y, x = np.histogram(data, bins=np.linspace(0, len(BCG), l2 + 1))
        x = range(0, len(y) + 1)
        # print('x:', x, 'lenx:', len(x))
        print('y:', y, 'leny:', len(y))
        # y, x = np.histogram(data, bins=np.linspace(0, len(BCG_OUT), 10000))
        a = int(self.ui.lineEdit.text())
        b = int(self.ui.lineEdit_2.text())
        y1, x1 = np.histogram(y, bins=np.linspace(a, b, b + 1 - a))
        print('x1:', x1, 'y1:', y1)
        print('lenx1:', len(x1), '\n', 'leny1:', len(y1))

        p1.plot(x, y, stepMode='center', pen=pg.mkPen(color='b', width=1))
        p1.setLabel('bottom', 's')
        p1.setLabel('left', 'beats/min')
        # p2.plot(x1-0.5, y1, stepMode="center", fillLevel=0, fillOutline=True, brush=(0, 0, 255, 150))
        bg1 = pg.BarGraphItem(x=range(a, b), height=y1, width=0.8, brush='b')
        p2.setLabel('bottom', 'beats/min')
        p2.addItem(bg1)
        dataHR = []
        for i in range(len(dataOut) - 1):
            hr = 60 / ((dataOut[i + 1] - dataOut[i]) / HRfs)
            dataHR.append(hr)
        p3.setLabel('bottom', '心搏（次）')
        p3.setLabel('left', 'beats/min')
        p3.plot(dataHR, pen=pg.mkPen(color='b', width=2))

    def PoincarePlot(self):
        win = self.ui.graphicsView_2
        sd1 = sd2 = []
        for i in range(len(dataOut) - 2):
            sd = ((dataOut[i + 1] - dataOut[i]) - (dataOut[i + 2] - dataOut[i + 1])) / (2 ** 0.5)
            sd1.append(sd)
        SD1 = round((np.var(sd1)) ** 0.5, 3)
        for i in range(len(dataOut) - 2):
            sdd = ((dataOut[i + 1] - dataOut[i]) + (dataOut[i + 2] - dataOut[i + 1])) / (2 ** 0.5)
            sd2.append(sdd)
        SD2 = round((np.var(sd2)) ** 0.5, 3)
        print('SD1:', SD1)
        print('SD2:', SD2)
        nonlinearItem_2 = QTableWidgetItem(str(SD1))
        nonlinearItem2_2 = QTableWidgetItem(str(SD2))
        self.ui.tableWidget_2.setItem(0, 1, nonlinearItem_2)
        self.ui.tableWidget_2.setItem(1, 1, nonlinearItem2_2)
        JJx, JJy = fn.dotCompute(dataOut)
        print('JJX:', JJx, '\n', 'JJY:', JJy)
        # win.setWindowTitle('pyqtgraph example: Scrolling Plots')
        p1 = win.addPlot()
        p1.setLabel('bottom', "RRi(ms)")
        p1.setLabel('left', "RRi+1(ms)")
        s1 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(0, 0, 255))
        s1.addPoints(JJx, JJy)
        x = np.linspace(min(JJx), max(JJx), max(JJx) + 1 - min(JJx))
        y = x
        p1.addItem(s1)
        p1.plot(x, y, pen=pg.mkPen(color='r', width=2))
        # p1.plot(JJx, JJy, brush=(0, 0, 255), symbol='o', symbolSize=8)

    def clear(self):
        win = self.ui.graphicsView
        win.clear()

    # def TDVariable(self):
    #     Mean_JJ = (dataOut[-1] - dataOut[0])/len(dataOut)
    #     newItem_2 = QTableWidgetItem(Mean_JJ)
    #     self.ui.tableWidget.setItem(0, 1, newItem_2)
    # def clearOne(self):
    #     win = self.ui.graphicsView
    #     win.removeItem(item=(1, 1))

    # def Ave_Heartrate(self):
    #     beat =
    #     Heartrate = beats / t


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class UiLoader(QtUiTools.QUiLoader):
    def createWidget(self, className, parent=None, name=""):
        if className == "PlotWidget":
            return pg.PlotWidget(parent=parent)
        elif className == "GraphicsLayoutWidget":
            return pg.GraphicsLayoutWidget(parent=parent)
        return super().createWidget(className, parent, name)


if __name__ == '__main__':
    app = QApplication([])
    loader = UiLoader()
    SI.enterWin = Win_Enter()
    SI.butterMsg = MsgButer()
    SI.filterWin = Win_Filter()
    # SI.HRWin = HeartRate.test
    SI.HRWin = HeartRate()
    SI.enterWin.ui.show()
    app.exec_()
