from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QStylePainter
from PySide2.QtUiTools import QUiLoader
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

# app = pg.mkQApp("Plotting Example")
# mw = QtGui.QMainWindow()
# mw.resize(800,800)

n = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
# win.resize(1000, 600)
# win.setWindowTitle('pyqtgraph example: Plotting')
#
# # Enable antialiasing for prettier plots
# pg.setConfigOptions(antialias=True)

p1 = n.addPlot(title="Basic array plotting", y=np.random.normal(size=100))
# p2 = win.addPlot(title="Multiple curves")
# p2.plot(np.random.normal(size=100), pen=(255,0,0), name="Red curve")
# p2.plot(np.random.normal(size=110)+5, pen=(0,255,0), name="Green curve")
# p2.plot(np.random.normal(size=120)+10, pen=(0,0,255), name="Blue curve")
#
# p3 = win.addPlot(title="Drawing with points")
# p3.plot(np.random.normal(size=100), pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')
# win.nextRow()
#
# p4 = win.addPlot(title="Parametric, grid enabled")
# x = np.cos(np.linspace(0, 2*np.pi, 1000))
# y = np.sin(np.linspace(0, 4*np.pi, 1000))
# p4.plot(x, y)
# p4.showGrid(x=True, y=True)
QtGui.QApplication.instance().exec_()
# pg.exec()
