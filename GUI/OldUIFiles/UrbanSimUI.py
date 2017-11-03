#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows an icon
in the titlebar of the window.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
import os
import glob

# Required to prevent error from importing qgis.core
import sip
sip.setapi('QDate', 2)
sip.setapi('QDateTime', 2)
sip.setapi('QString', 2)
sip.setapi('QTextStream', 2)
sip.setapi('QTime', 2)
sip.setapi('QUrl', 2)
sip.setapi('QVariant', 2)

from qtpy.QtGui import *
from qtpy.QtCore import *

#QGIS_PATH1="C:\\GoogleDrive\\COE_UrbanSim\\edmonton_urbansim\\GUI\\QGIS\\apps\\qgis\\bin"
#QGIS_PATH2="C:\\GoogleDrive\\COE_UrbanSim\\edmonton_urbansim\\GUI\\QGIS\\bin"
#QGIS_PYTHONHOME="C:\\GoogleDrive\\COE_UrbanSim\\edmonton_urbansim\\GUI\\QGIS\\apps\\Python27"
#QGIS_PYTHONPATH="C:\\GoogleDrive\\COE_UrbanSim\\edmonton_urbansim\\GUI\\QGIS\\apps\\qgis\\python"
#rerun1 = True
#rerun2 = True
#rerun3 = True
#rerun4 = True
#
#if not QGIS_PATH1 in os.environ.get('PATH'):
#    os.environ['PATH'] += ";" + QGIS_PATH1
#else:
#    rerun1 = False
#
#if not QGIS_PATH2 in os.environ.get('PATH'):
#    os.environ['PATH'] += ";" + QGIS_PATH2
#else:
#    rerun2 = False
#    
#if not 'PYTHONHOME' in os.environ:
#    os.environ['PYTHONHOME'] = QGIS_PYTHONHOME
#elif not QGIS_PYTHONHOME in os.environ.get('PYTHONHOME'):
#    os.environ['PYTHONHOME'] += ";" + QGIS_PYTHONHOME
#else:
#    rerun3 = False
#    
#if not 'PYTHONPATH' in os.environ:
#    os.environ['PYTHONPATH'] = QGIS_PYTHONPATH
#elif not QGIS_PYTHONPATH in os.environ.get('PYTHONPATH'):
#    os.environ['PYTHONPATH'] += ";" + QGIS_PYTHONPATH
#else:
#    rerun4 = False
#    
#if rerun1 or rerun2 or rerun3 or rerun4:
#    print os.path.realpath(__file__)
#    print ""
#    print sys.argv
#    print ""
#    print os.environ
#    print ""
#    os.execve("C:\\GoogleDrive\\COE_UrbanSim\\edmonton_urbansim\\GUI\\QGIS\\bin\\python.exe", ["C:\\GoogleDrive\\COE_UrbanSim\\edmonton_urbansim\\GUI\\QGIS\\bin\\python.exe", os.path.realpath(__file__)], os.environ)
##    os.execve(sys.executable, [sys.executable, "-c", "import os; open('C:\\GoogleDrive\\COE_UrbanSim\\edmonton_urbansim\\GUI\\onefile', 'w').write(os.environ['ddd'])"], {'ddd':'xxx'})
##    os.execve(sys.executable, [sys.executable]+sys.argv, os.environ)
##    os.execve("C:\Users\dershu\AppData\Local\Continuum\Anaconda2\python.exe", sys.argv, os.environ)
##    os.execve(os.path.realpath(__file__), sys.argv, os.environ)
##    os.execve(os.path.realpath(__file__), [sys.argv[0], "blah"], os.environ)
#    
#    #Should never happen
#    print "Problem with beginning of execution of UI"
#    sys.exit() 

#sys.path.append('C:/GoogleDrive/COE_UrbanSim/edmonton_urbansim/GUI/QGIS/apps/qgis/python')
#sys.path.append('C:/GoogleDrive/COE_UrbanSim/edmonton_urbansim/GUI/QGIS/apps/Python27')
#sys.path.append('C:/GoogleDrive/COE_UrbanSim/edmonton_urbansim/GUI/QGIS/apps/Python27/Lib')
#sys.path.append('C:/GoogleDrive/COE_UrbanSim/edmonton_urbansim/GUI/QGIS/apps/Python27/Lib/site-packages')
#sys.path.append('C:/GoogleDrive/COE_UrbanSim/edmonton_urbansim/GUI/QGIS/bin')
#sys.path.append('C:/GoogleDrive/COE_UrbanSim/edmonton_urbansim/GUI/QGIS/include')
#sys.path.append('C:/GoogleDrive/COE_UrbanSim/edmonton_urbansim/GUI/QGIS/apps/qgis/bin')
#print os.environ["PATH"]
#print "\n\n\n\n\n"
#os.environ["PATH"] = "C:\\PROGRA~1\\QGIS2~1.18\\bin;C:\\PROGRA~1\\QGIS2~1.18\\apps\\qgis\\bin;" + os.environ["PATH"]
#print "\n\n\n\n\n"
#print os.environ["PATH"]
#print "\n\n\n\n\n"
#os.environ["PYTHONHOME"] = "C:\\PROGRA~1\\QGIS2~1.18\\apps\\Python27"
#os.environ["PYTHONPATH"] = "C:\\PROGRA~1\\QGIS2~1.18\\apps\\qgis\\python"
#os.system('echo %PYTHONPATH%')
#os.system('set PATH=C:/PROGRA~1/QGIS2~1.18/apps/qgis;%PATH%')
#os.system('echo %PATH%')

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

# supply path to qgis install location
QgsApplication.setPrefixPath("C:\\Google Drive\\COE_UrbanSim\\edmonton_urbansim\\GUI\\QGIS\\apps\\qgis", True)

# create a reference to the QgsApplication
# setting the second argument to True enables the GUI, which we need to do
# since this is a custom application
qgs = QgsApplication([], True)

# load providers
qgs.initQgis()
urbansim_env = os.environ.copy()
del urbansim_env['QGIS']
del urbansim_env['QGISNAME']
del urbansim_env['QGIS_PREFIX_PATH']
del urbansim_env['PYTHONPATH']
del urbansim_env['PYTHONHOME']
del urbansim_env['OSGEO4W_ROOT']
urbansim_env['PATH'] = 'C:\\Users\\dershu\\AppData\\Local\\Continuum\\Anaconda2\\Library\\bin;C:\\Program Files (x86)\\Common Files\\Intergraph\\GeoMedia\\Program;\\\\CEPFILE2\\apps\\ORACLE\\Ora11203x86\\BIN;C:\\Program Files (x86)\\Geomedia Objects\\Program;c:\\PROGRA~2\\FileNet\\IDM;C:\\windows\\system32;C:\\windows;C:\\windows\\System32\\Wbem;C:\\windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\QuickTime\\QTSystem\\;C:\\Program Files (x86)\\Lenovo\\Access Connections\\;T:\\ORACLE\\Ora11203\\BIN;ReallySuppress;C:\Program Files (x86)\\SLIM\\Commands\\bin;C:\\Program Files (x86)\\SLIM\\Commands\\dependencies;\\\\CEPFILE2\\apps\\ORACLE\\Ora1220x86\\BIN;C:\\Program Files (x86)\\SLIM;C:\\Users\\dershu\\AppData\\Local\\Continuum\\Anaconda2;C:\\Users\\dershu\\AppData\\Local\\Continuum\\Anaconda2\\Scripts;C:\\Users\\dershu\\AppData\\Local\\Continuum\\Anaconda2\\Library\\bin'
#urbansim_env[""] = ""
            
            

class MyWnd(QMainWindow):
    def __init__(self, layer=None):
        QMainWindow.__init__(self)
        
        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(Qt.white)
        self.canvas.setExtent(layer.extent())
        self.canvas.setLayerSet([QgsMapCanvasLayer(layer)])
        
        self.setCentralWidget(self.canvas)
        
        actionZoomIn = QAction(QString("Zoom in"), self)
        actionZoomOut = QAction(QString("Zoom out"), self)
        actionPan = QAction(QString("Pan"), self)
        
        actionZoomIn.setCheckable(True)
        actionZoomOut.setCheckable(True)
        actionPan.setCheckable(True)
        
        self.connect(actionZoomIn, SIGNAL("triggered()"), self.zoomIn)
        self.connect(actionZoomOut, SIGNAL("triggered()"), self.zoomOut)
        self.connect(actionPan, SIGNAL("triggered()"), self.pan)
        
        self.toolbar = self.addToolBar("Canvas actions")
        self.toolbar.addAction(actionZoomIn)
        self.toolbar.addAction(actionZoomOut)
        self.toolbar.addAction(actionPan)
        
        # create the map tools
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
        self.toolZoomIn.setAction(actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
        self.toolZoomOut.setAction(actionZoomOut)
        
        self.pan()
        
    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)
        
    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)
    
    def pan(self):
        self.canvas.setMapTool(self.toolPan)


## supply path to qgis install location
#QgsApplication.setPrefixPath("C:/GoogleDrive/COE_UrbanSim/edmonton_urbansim/GUI/QGIS", True)
#
## create a reference to the QgsApplication
## setting the second argument to True enables the GUI, which we need to do
## since this is a custom application
#qgs = QgsApplication([], True)
#
## load providers
#qgs.initQgis()
#urbansim_env = os.environ.copy()
#del urbansim_env['QGIS']
#del urbansim_env['QGISNAME']
#del urbansim_env['QGIS_PREFIX_PATH']
#del urbansim_env['PYTHONPATH']
#del urbansim_env['PYTHONHOME']
#del urbansim_env['OSGEO4W_ROOT']
#urbansim_env['PATH'] = 'C:\\Users\\dershu\\AppData\\Local\\Continuum\\Anaconda2\\Library\\bin;C:\\Program Files (x86)\\Common Files\\Intergraph\\GeoMedia\\Program;\\\\CEPFILE2\\apps\\ORACLE\\Ora11203x86\\BIN;C:\\Program Files (x86)\\Geomedia Objects\\Program;c:\\PROGRA~2\\FileNet\\IDM;C:\\windows\\system32;C:\\windows;C:\\windows\\System32\\Wbem;C:\\windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\QuickTime\\QTSystem\\;C:\\Program Files (x86)\\Lenovo\\Access Connections\\;T:\\ORACLE\\Ora11203\\BIN;ReallySuppress;C:\Program Files (x86)\\SLIM\\Commands\\bin;C:\\Program Files (x86)\\SLIM\\Commands\\dependencies;\\\\CEPFILE2\\apps\\ORACLE\\Ora1220x86\\BIN;C:\\Program Files (x86)\\SLIM;C:\\Users\\dershu\\AppData\\Local\\Continuum\\Anaconda2;C:\\Users\\dershu\\AppData\\Local\\Continuum\\Anaconda2\\Scripts;C:\\Users\\dershu\\AppData\\Local\\Continuum\\Anaconda2\\Library\\bin'
##urbansim_env[""] = ""
#            
#            
#class Example(QMainWindow):
#    
#    def __init__(self):
#        
#        super(Example, self).__init__()
#        
#        self.initUI()
#        
#        
#    def initUI(self):
#        
#        preprocessBtn = QPushButton('Preprocess', self)
#        preprocessBtn.resize(preprocessBtn.sizeHint())
#        preprocessBtn.clicked.connect(self.preprocess)
#        preprocessBtn.move(10, 15)
#        
#        simulationBtn = QPushButton('Simulate', self)
#        simulationBtn.resize(simulationBtn.sizeHint())
#        simulationBtn.clicked.connect(self.simulate)
#        simulationBtn.move(10, 40)
#        
#        self.resize(300, 300)
#        self.center()
#        self.setWindowTitle('Edmonton UrbanSim')
#        self.setWindowIcon(QIcon('Geodesign.png'))        
#    
#        self.show()
#        
#        
#    def closeEvent(self, event):
#        
##        reply = QMessageBox.question(self, 'Message',
##            "Are you sure to quit?", QMessageBox.Yes | 
##            QMessageBox.No, QMessageBox.No)
##
##        if reply == QMessageBox.Yes:
##            event.accept()
##        else:
##            event.ignore() 
#        # When your script is complete, call exitQgis() to remove the provider and
#        # layer registries from memory
#        qgs.exitQgis()
#        event.accept()
#            
#    def center(self):
#        
#        qr = self.frameGeometry()
#        cp = QDesktopWidget().availableGeometry().center()
#        qr.moveCenter(cp)
#        self.move(qr.topLeft())
#        
#        
#    @pyqtSlot()
#    def preprocess(self):
#        self.statusBar().showMessage('Running preprocessing')
#        task = subprocess.Popen('C:\Users\dershu\AppData\Local\Continuum\Anaconda2\python.exe baus.py -c --mode preprocessing', env=urbansim_env, cwd="..")
#        task.wait()
#        if task.returncode != 0:
#            self.statusBar().showMessage('Error in preprocessing')
#        else:
#            self.statusBar().showMessage('Done preprocessing.')
#
#
#    @pyqtSlot()
#    def simulate(self):
#        self.statusBar().showMessage('Running simulation')
##        os.system('python ../baus.py -c --mode simulation')
#        self.statusBar().showMessage('Done simulation.')

        
        
if __name__ == '__main__':
#    app = QApplication(sys.argv)
#
#    w = QWidget()
#    w.resize(250, 150)
#    w.move(300, 300)
#    w.setWindowTitle('Simple')
#    w.show()
#    
#    sys.exit(app.exec_())
#    app = QApplication(sys.argv)
#    ex = Example()
    w = MyWnd()
    w.show()
    sys.exit(app.exec_()) 
