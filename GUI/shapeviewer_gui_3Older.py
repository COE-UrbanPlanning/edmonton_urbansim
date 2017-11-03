# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shapeviewer_gui_3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(748, 479)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.titleGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleGroupBox.sizePolicy().hasHeightForWidth())
        self.titleGroupBox.setSizePolicy(sizePolicy)
        self.titleGroupBox.setMinimumSize(QtCore.QSize(360, 140))
        self.titleGroupBox.setTitle(_fromUtf8(""))
        self.titleGroupBox.setObjectName(_fromUtf8("titleGroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.titleGroupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.titleLabel = QtGui.QLabel(self.titleGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.titleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.titleLabel.setIndent(6)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.verticalLayout_5.addWidget(self.titleLabel)
        self.horizontalLayout.addWidget(self.titleGroupBox)
        self.buttonGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonGroupBox.sizePolicy().hasHeightForWidth())
        self.buttonGroupBox.setSizePolicy(sizePolicy)
        self.buttonGroupBox.setMinimumSize(QtCore.QSize(360, 140))
        self.buttonGroupBox.setTitle(_fromUtf8(""))
        self.buttonGroupBox.setObjectName(_fromUtf8("buttonGroupBox"))
        self.mBtnZoomIn = QtGui.QPushButton(self.buttonGroupBox)
        self.mBtnZoomIn.setGeometry(QtCore.QRect(10, 40, 61, 61))
        self.mBtnZoomIn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./images/zoomIn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnZoomIn.setIcon(icon)
        self.mBtnZoomIn.setIconSize(QtCore.QSize(50, 50))
        self.mBtnZoomIn.setObjectName(_fromUtf8("mBtnZoomIn"))
        self.mBtnZoomOut = QtGui.QPushButton(self.buttonGroupBox)
        self.mBtnZoomOut.setGeometry(QtCore.QRect(80, 40, 61, 61))
        self.mBtnZoomOut.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./images/zomOut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnZoomOut.setIcon(icon1)
        self.mBtnZoomOut.setIconSize(QtCore.QSize(50, 50))
        self.mBtnZoomOut.setObjectName(_fromUtf8("mBtnZoomOut"))
        self.mBtnAddRaster = QtGui.QPushButton(self.buttonGroupBox)
        self.mBtnAddRaster.setGeometry(QtCore.QRect(150, 40, 61, 61))
        self.mBtnAddRaster.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./images/addRaster.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnAddRaster.setIcon(icon2)
        self.mBtnAddRaster.setIconSize(QtCore.QSize(50, 50))
        self.mBtnAddRaster.setObjectName(_fromUtf8("mBtnAddRaster"))
        self.mBtnAddVector = QtGui.QPushButton(self.buttonGroupBox)
        self.mBtnAddVector.setGeometry(QtCore.QRect(220, 40, 61, 61))
        self.mBtnAddVector.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./images/addLayer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnAddVector.setIcon(icon3)
        self.mBtnAddVector.setIconSize(QtCore.QSize(50, 50))
        self.mBtnAddVector.setObjectName(_fromUtf8("mBtnAddVector"))
        self.mBtnSelection = QtGui.QPushButton(self.buttonGroupBox)
        self.mBtnSelection.setGeometry(QtCore.QRect(290, 40, 61, 61))
        self.mBtnSelection.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("./images/select.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mBtnSelection.setIcon(icon4)
        self.mBtnSelection.setIconSize(QtCore.QSize(50, 50))
        self.mBtnSelection.setObjectName(_fromUtf8("mBtnSelection"))
        self.mBtnZoomIn.raise_()
        self.mBtnZoomOut.raise_()
        self.mBtnAddRaster.raise_()
        self.mBtnAddVector.raise_()
        self.mBtnSelection.raise_()
        self.titleGroupBox.raise_()
        self.horizontalLayout.addWidget(self.buttonGroupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.canvasGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvasGroupBox.sizePolicy().hasHeightForWidth())
        self.canvasGroupBox.setSizePolicy(sizePolicy)
        self.canvasGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.canvasGroupBox.setTitle(_fromUtf8(""))
        self.canvasGroupBox.setObjectName(_fromUtf8("canvasGroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.canvasGroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.canvasFrame = QtGui.QFrame(self.canvasGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvasFrame.sizePolicy().hasHeightForWidth())
        self.canvasFrame.setSizePolicy(sizePolicy)
        self.canvasFrame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.canvasFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.canvasFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.canvasFrame.setObjectName(_fromUtf8("canvasFrame"))
        self.verticalLayout_4.addWidget(self.canvasFrame)
        self.horizontalLayout_2.addWidget(self.canvasGroupBox)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.dropDownGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dropDownGroupBox.sizePolicy().hasHeightForWidth())
        self.dropDownGroupBox.setSizePolicy(sizePolicy)
        self.dropDownGroupBox.setMinimumSize(QtCore.QSize(160, 60))
        self.dropDownGroupBox.setObjectName(_fromUtf8("dropDownGroupBox"))
        self.mFieldComboBox = QgsFieldComboBox(self.dropDownGroupBox)
        self.mFieldComboBox.setGeometry(QtCore.QRect(10, 20, 141, 27))
        self.mFieldComboBox.setObjectName(_fromUtf8("mFieldComboBox"))
        self.mFieldComboBox.raise_()
        self.verticalLayout_2.addWidget(self.dropDownGroupBox)
        self.legendGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.legendGroupBox.sizePolicy().hasHeightForWidth())
        self.legendGroupBox.setSizePolicy(sizePolicy)
        self.legendGroupBox.setMinimumSize(QtCore.QSize(160, 200))
        self.legendGroupBox.setAutoFillBackground(False)
        self.legendGroupBox.setFlat(False)
        self.legendGroupBox.setCheckable(False)
        self.legendGroupBox.setObjectName(_fromUtf8("legendGroupBox"))
        self.colorBox_2 = QtGui.QWidget(self.legendGroupBox)
        self.colorBox_2.setGeometry(QtCore.QRect(10, 50, 21, 21))
        self.colorBox_2.setAutoFillBackground(False)
        self.colorBox_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 95, 0);"))
        self.colorBox_2.setObjectName(_fromUtf8("colorBox_2"))
        self.colorBox_1 = QtGui.QWidget(self.legendGroupBox)
        self.colorBox_1.setGeometry(QtCore.QRect(10, 20, 21, 21))
        self.colorBox_1.setAutoFillBackground(False)
        self.colorBox_1.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.colorBox_1.setObjectName(_fromUtf8("colorBox_1"))
        self.colorBox_6 = QtGui.QWidget(self.legendGroupBox)
        self.colorBox_6.setGeometry(QtCore.QRect(10, 170, 21, 21))
        self.colorBox_6.setAutoFillBackground(False)
        self.colorBox_6.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0);"))
        self.colorBox_6.setObjectName(_fromUtf8("colorBox_6"))
        self.colorBox_5 = QtGui.QWidget(self.legendGroupBox)
        self.colorBox_5.setGeometry(QtCore.QRect(10, 140, 21, 21))
        self.colorBox_5.setAutoFillBackground(False)
        self.colorBox_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 215, 0);"))
        self.colorBox_5.setObjectName(_fromUtf8("colorBox_5"))
        self.colorBox_4 = QtGui.QWidget(self.legendGroupBox)
        self.colorBox_4.setGeometry(QtCore.QRect(10, 110, 21, 21))
        self.colorBox_4.setAutoFillBackground(False)
        self.colorBox_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 175, 0);"))
        self.colorBox_4.setObjectName(_fromUtf8("colorBox_4"))
        self.colorBox_3 = QtGui.QWidget(self.legendGroupBox)
        self.colorBox_3.setGeometry(QtCore.QRect(10, 80, 21, 21))
        self.colorBox_3.setAutoFillBackground(False)
        self.colorBox_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 135, 0);"))
        self.colorBox_3.setObjectName(_fromUtf8("colorBox_3"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.legendGroupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(40, 80, 111, 21))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.legendHorizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.legendHorizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.legendHorizontalLayout_4.setContentsMargins(8, -1, -1, -1)
        self.legendHorizontalLayout_4.setSpacing(6)
        self.legendHorizontalLayout_4.setObjectName(_fromUtf8("legendHorizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.legendHorizontalLayout_4.addWidget(self.label_7)
        self.dashLabel_4 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashLabel_4.sizePolicy().hasHeightForWidth())
        self.dashLabel_4.setSizePolicy(sizePolicy)
        self.dashLabel_4.setObjectName(_fromUtf8("dashLabel_4"))
        self.legendHorizontalLayout_4.addWidget(self.dashLabel_4)
        self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.legendHorizontalLayout_4.addWidget(self.label_8)
        self.horizontalLayoutWidget_5 = QtGui.QWidget(self.legendGroupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(40, 50, 111, 21))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.legendHorizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.legendHorizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.legendHorizontalLayout_5.setContentsMargins(8, -1, -1, -1)
        self.legendHorizontalLayout_5.setSpacing(6)
        self.legendHorizontalLayout_5.setObjectName(_fromUtf8("legendHorizontalLayout_5"))
        self.label_10 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.legendHorizontalLayout_5.addWidget(self.label_10)
        self.dashLabel_5 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashLabel_5.sizePolicy().hasHeightForWidth())
        self.dashLabel_5.setSizePolicy(sizePolicy)
        self.dashLabel_5.setObjectName(_fromUtf8("dashLabel_5"))
        self.legendHorizontalLayout_5.addWidget(self.dashLabel_5)
        self.label_12 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.legendHorizontalLayout_5.addWidget(self.label_12)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.legendGroupBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(40, 20, 111, 21))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.legendHorizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.legendHorizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.legendHorizontalLayout_6.setContentsMargins(8, -1, 0, -1)
        self.legendHorizontalLayout_6.setSpacing(6)
        self.legendHorizontalLayout_6.setObjectName(_fromUtf8("legendHorizontalLayout_6"))
        self.label_11 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.legendHorizontalLayout_6.addWidget(self.label_11)
        self.dashLabel_6 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashLabel_6.sizePolicy().hasHeightForWidth())
        self.dashLabel_6.setSizePolicy(sizePolicy)
        self.dashLabel_6.setObjectName(_fromUtf8("dashLabel_6"))
        self.legendHorizontalLayout_6.addWidget(self.dashLabel_6)
        self.label_13 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.legendHorizontalLayout_6.addWidget(self.label_13)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.legendGroupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 110, 111, 21))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.legendHorizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.legendHorizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.legendHorizontalLayout_3.setContentsMargins(8, -1, -1, -1)
        self.legendHorizontalLayout_3.setSpacing(6)
        self.legendHorizontalLayout_3.setObjectName(_fromUtf8("legendHorizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.legendHorizontalLayout_3.addWidget(self.label_5)
        self.dashLabel_3 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashLabel_3.sizePolicy().hasHeightForWidth())
        self.dashLabel_3.setSizePolicy(sizePolicy)
        self.dashLabel_3.setObjectName(_fromUtf8("dashLabel_3"))
        self.legendHorizontalLayout_3.addWidget(self.dashLabel_3)
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.legendHorizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.legendGroupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 140, 111, 21))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.legendHorizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.legendHorizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.legendHorizontalLayout_2.setContentsMargins(8, -1, -1, -1)
        self.legendHorizontalLayout_2.setSpacing(6)
        self.legendHorizontalLayout_2.setObjectName(_fromUtf8("legendHorizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.legendHorizontalLayout_2.addWidget(self.label_3)
        self.dashLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashLabel_2.sizePolicy().hasHeightForWidth())
        self.dashLabel_2.setSizePolicy(sizePolicy)
        self.dashLabel_2.setObjectName(_fromUtf8("dashLabel_2"))
        self.legendHorizontalLayout_2.addWidget(self.dashLabel_2)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.legendHorizontalLayout_2.addWidget(self.label_4)
        self.horizontalLayoutWidget = QtGui.QWidget(self.legendGroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 170, 111, 21))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.legendHorizontalLayout_1 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.legendHorizontalLayout_1.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.legendHorizontalLayout_1.setContentsMargins(8, -1, -1, -1)
        self.legendHorizontalLayout_1.setSpacing(6)
        self.legendHorizontalLayout_1.setObjectName(_fromUtf8("legendHorizontalLayout_1"))
        self.label_1 = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.legendHorizontalLayout_1.addWidget(self.label_1)
        self.dashLabel_1 = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashLabel_1.sizePolicy().hasHeightForWidth())
        self.dashLabel_1.setSizePolicy(sizePolicy)
        self.dashLabel_1.setObjectName(_fromUtf8("dashLabel_1"))
        self.legendHorizontalLayout_1.addWidget(self.dashLabel_1)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.legendHorizontalLayout_1.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.legendGroupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuMap_View = QtGui.QMenu(self.menubar)
        self.menuMap_View.setObjectName(_fromUtf8("menuMap_View"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMap_View.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Gis Viewer Application", None))
        self.titleLabel.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#0055ff;\">Land Development Model</span></p></body></html>", None))
        self.dropDownGroupBox.setTitle(_translate("MainWindow", "Model Results", None))
        self.legendGroupBox.setTitle(_translate("MainWindow", "Legend", None))
        self.label_7.setText(_translate("MainWindow", "0", None))
        self.dashLabel_4.setText(_translate("MainWindow", "-", None))
        self.label_8.setText(_translate("MainWindow", "0", None))
        self.label_10.setText(_translate("MainWindow", "0", None))
        self.dashLabel_5.setText(_translate("MainWindow", "-", None))
        self.label_12.setText(_translate("MainWindow", "0", None))
        self.label_11.setText(_translate("MainWindow", "0", None))
        self.dashLabel_6.setText(_translate("MainWindow", "-", None))
        self.label_13.setText(_translate("MainWindow", "0", None))
        self.label_5.setText(_translate("MainWindow", "0", None))
        self.dashLabel_3.setText(_translate("MainWindow", "-", None))
        self.label_6.setText(_translate("MainWindow", "0", None))
        self.label_3.setText(_translate("MainWindow", "0", None))
        self.dashLabel_2.setText(_translate("MainWindow", "-", None))
        self.label_4.setText(_translate("MainWindow", "0", None))
        self.label_1.setText(_translate("MainWindow", "0", None))
        self.dashLabel_1.setText(_translate("MainWindow", "-", None))
        self.label_2.setText(_translate("MainWindow", "0", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuMap_View.setTitle(_translate("MainWindow", "Map View", None))

from qgis.gui import QgsFieldComboBox
#import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

