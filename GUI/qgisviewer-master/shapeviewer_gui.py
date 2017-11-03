# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shapeviewer_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 742)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(610, 10, 361, 111))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.mBtnZoomIn = QtWidgets.QPushButton(self.groupBox)
        self.mBtnZoomIn.setGeometry(QtCore.QRect(10, 40, 61, 61))
        self.mBtnZoomIn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/zoomIn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnZoomIn.setIcon(icon)
        self.mBtnZoomIn.setIconSize(QtCore.QSize(50, 50))
        self.mBtnZoomIn.setObjectName("mBtnZoomIn")
        self.mBtnZoomOut = QtWidgets.QPushButton(self.groupBox)
        self.mBtnZoomOut.setGeometry(QtCore.QRect(80, 40, 61, 61))
        self.mBtnZoomOut.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/zomOut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnZoomOut.setIcon(icon1)
        self.mBtnZoomOut.setIconSize(QtCore.QSize(50, 50))
        self.mBtnZoomOut.setObjectName("mBtnZoomOut")
        self.mBtnAddRaster = QtWidgets.QPushButton(self.groupBox)
        self.mBtnAddRaster.setGeometry(QtCore.QRect(150, 40, 61, 61))
        self.mBtnAddRaster.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/addRaster.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnAddRaster.setIcon(icon2)
        self.mBtnAddRaster.setIconSize(QtCore.QSize(50, 50))
        self.mBtnAddRaster.setObjectName("mBtnAddRaster")
        self.mBtnAddVector = QtWidgets.QPushButton(self.groupBox)
        self.mBtnAddVector.setGeometry(QtCore.QRect(220, 40, 61, 61))
        self.mBtnAddVector.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/addLayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnAddVector.setIcon(icon3)
        self.mBtnAddVector.setIconSize(QtCore.QSize(50, 50))
        self.mBtnAddVector.setObjectName("mBtnAddVector")
        self.mBtnSelection = QtWidgets.QPushButton(self.groupBox)
        self.mBtnSelection.setGeometry(QtCore.QRect(290, 40, 61, 61))
        self.mBtnSelection.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnSelection.setIcon(icon4)
        self.mBtnSelection.setIconSize(QtCore.QSize(50, 50))
        self.mBtnSelection.setObjectName("mBtnSelection")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 801, 561))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.frame = QtWidgets.QFrame(self.groupBox_2)
        self.frame.setGeometry(QtCore.QRect(9, 19, 781, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(810, 120, 161, 571))
        self.groupBox_3.setObjectName("groupBox_3")
        self.mFieldComboBox = QgsFieldComboBox(self.groupBox_3)
        self.mFieldComboBox.setGeometry(QtCore.QRect(10, 20, 141, 27))
        self.mFieldComboBox.setObjectName("mFieldComboBox")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 601, 111))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 10, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMap_View = QtWidgets.QMenu(self.menubar)
        self.menuMap_View.setObjectName("menuMap_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMap_View.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gis Viewer Application"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Model Results"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#0055ff;\">Land Development Model</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMap_View.setTitle(_translate("MainWindow", "Map View"))

from qgsfieldcombobox import QgsFieldComboBox
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

