# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(724, 606)
        self.Butterworth = QAction(MainWindow)
        self.Butterworth.setObjectName(u"Butterworth")
        self.actionbanben = QAction(MainWindow)
        self.actionbanben.setObjectName(u"actionbanben")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        icon = QIcon()
        icon.addFile(u"images/exit.webp", QSize(), QIcon.Normal, QIcon.On)
        self.actionexit.setIcon(icon)
        self.actiondataview = QAction(MainWindow)
        self.actiondataview.setObjectName(u"actiondataview")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(130, 0, 581, 261))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.ViewButton = QPushButton(self.centralwidget)
        self.ViewButton.setObjectName(u"ViewButton")
        self.ViewButton.setGeometry(QRect(20, 280, 75, 41))
        self.dataPlot = PlotWidget(self.centralwidget)
        self.dataPlot.setObjectName(u"dataPlot")
        self.dataPlot.setGeometry(QRect(130, 269, 581, 241))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.dataPlot.sizePolicy().hasHeightForWidth())
        self.dataPlot.setSizePolicy(sizePolicy1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 724, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_6 = QMenu(self.menubar)
        self.menu_6.setObjectName(u"menu_6")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actiondataview)
        self.menu_2.addAction(self.Butterworth)
        self.menu_5.addAction(self.actionbanben)
        self.menu_5.addAction(self.actionexit)
        self.toolBar.addAction(self.actionexit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WISLab", None))
        self.Butterworth.setText(QCoreApplication.translate("MainWindow", u"\u5df4\u7279\u6c83\u65af\u6ee4\u6ce2", None))
        self.actionbanben.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c\u53f7", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actiondataview.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u89c6\u5316", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.ViewButton.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u89c6\u5316", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u9884\u5904\u7406", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5206\u6790", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menu_6.setTitle(QCoreApplication.translate("MainWindow", u"\u8d44\u6e90", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

