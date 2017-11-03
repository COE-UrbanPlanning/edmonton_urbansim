# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shapeviewer_gui.ui'
#
# Created: Mon Mar 25 22:00:05 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 781, 101))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.mBtnZoomIn = QtGui.QPushButton(self.groupBox)
        self.mBtnZoomIn.setGeometry(QtCore.QRect(20, 20, 70, 70))
        self.mBtnZoomIn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/zoomIn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnZoomIn.setIcon(icon)
        self.mBtnZoomIn.setIconSize(QtCore.QSize(50, 50))
        self.mBtnZoomIn.setObjectName(_fromUtf8("mBtnZoomIn"))
        self.mBtnZoomOut = QtGui.QPushButton(self.groupBox)
        self.mBtnZoomOut.setGeometry(QtCore.QRect(130, 20, 70, 70))
        self.mBtnZoomOut.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/zomOut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnZoomOut.setIcon(icon1)
        self.mBtnZoomOut.setIconSize(QtCore.QSize(50, 50))
        self.mBtnZoomOut.setObjectName(_fromUtf8("mBtnZoomOut"))
        self.mBtnAddRaster = QtGui.QPushButton(self.groupBox)
        self.mBtnAddRaster.setGeometry(QtCore.QRect(240, 20, 70, 70))
        self.mBtnAddRaster.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/addRaster.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnAddRaster.setIcon(icon2)
        self.mBtnAddRaster.setIconSize(QtCore.QSize(50, 50))
        self.mBtnAddRaster.setObjectName(_fromUtf8("mBtnAddRaster"))
        self.mBtnAddVector = QtGui.QPushButton(self.groupBox)
        self.mBtnAddVector.setGeometry(QtCore.QRect(350, 20, 70, 70))
        self.mBtnAddVector.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/addLayer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnAddVector.setIcon(icon3)
        self.mBtnAddVector.setIconSize(QtCore.QSize(50, 50))
        self.mBtnAddVector.setObjectName(_fromUtf8("mBtnAddVector"))
        self.mBtnElevation = QtGui.QPushButton(self.groupBox)
        self.mBtnElevation.setGeometry(QtCore.QRect(570, 20, 91, 71))
        self.mBtnElevation.setObjectName(_fromUtf8("mBtnElevation"))
        self.mBtnSelection = QtGui.QPushButton(self.groupBox)
        self.mBtnSelection.setGeometry(QtCore.QRect(450, 20, 91, 71))
        self.mBtnSelection.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/images/select.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnSelection.setIcon(icon4)
        self.mBtnSelection.setIconSize(QtCore.QSize(50, 50))
        self.mBtnSelection.setObjectName(_fromUtf8("mBtnSelection"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 109, 781, 441))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.frame = QtGui.QFrame(self.groupBox_2)
        self.frame.setGeometry(QtCore.QRect(9, 19, 761, 441))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Gis Viewer Application", None, QtGui.QApplication.UnicodeUTF8))
        self.mBtnZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.mBtnZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.mBtnAddRaster.setText(QtGui.QApplication.translate("MainWindow", "Add Raster", None, QtGui.QApplication.UnicodeUTF8))
        self.mBtnAddVector.setText(QtGui.QApplication.translate("MainWindow", "Add Vector", None, QtGui.QApplication.UnicodeUTF8))
        self.mBtnElevation.setText(QtGui.QApplication.translate("MainWindow", "Elevation", None, QtGui.QApplication.UnicodeUTF8))
        self.mBtnSelection.setText(QtGui.QApplication.translate("MainWindow", "Selection", None, QtGui.QApplication.UnicodeUTF8))

