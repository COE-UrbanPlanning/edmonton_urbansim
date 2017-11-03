# -*- coding: utf-8 -*-

import sip
sip.setapi('QDate', 2)
sip.setapi('QDateTime', 2)
sip.setapi('QString', 2)
sip.setapi('QTextStream', 2)
sip.setapi('QTime', 2)
sip.setapi('QUrl', 2)
sip.setapi('QVariant', 2)

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import sys
import os
import numpy 
from SelectTool import SelectMapTool
# Import our GUI
from shapeviewer_gui_3 import Ui_MainWindow

# Environment variable QGISHOME must be set to the install directory
# before running the application
qgis_prefix = os.getenv("QGIS")
xCord=numpy.zeros((100,100))
yCord=numpy.zeros((100,100))
elev=numpy.zeros((100,100))



try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class ShapeViewer(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.layer = None
        self.layers = []
        
        # Required by Qt4 to initialize the UI
        self.setupUi(self)

        QObject.connect(self.mBtnZoomIn,  SIGNAL("clicked()"),  self.zoomIn)
        QObject.connect(self.mBtnZoomOut,  SIGNAL("clicked()"),  self.zoomOut)
        QObject.connect(self.mBtnAddVector,  SIGNAL("clicked()"),  self.loadVectorLayer)
        QObject.connect(self.mBtnAddRaster,  SIGNAL("clicked()"),  self.loadRasterLayer)
        QObject.connect(self.mBtnSelection,  SIGNAL("clicked()"),  self.setSelectionTool)
        self.mFieldComboBox.fieldChanged.connect(self.onFieldChanged)

        # Set the title for the app
        self.setWindowTitle("ShapeViewer")

        # Create the map canvas
        self.canvas = QgsMapCanvas()
        self.canvas.useImageToRender(False)
        self.canvas.setCanvasColor(Qt.white)
        self.canvas.enableAntiAliasing(True)
        self.canvas.show()
        
        # from https://gis.stackexchange.com/questions/141516/adding-legend-to-canvas-in-standalone-pyqgis-application
        self.root = QgsProject.instance().layerTreeRoot()
        self.bridge = QgsLayerTreeMapCanvasBridge(self.root, self.canvas)
        self.model = QgsLayerTreeModel(self.root)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeReorder)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeRename)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility)
        self.model.setFlag(QgsLayerTreeModel.ShowLegend)
        self.view = QgsLayerTreeView()
        self.view.setModel(self.model)
        self.field = ""
        
        self.legendQDockWidget.setWidget( self.view )
        self.legendQDockWidget.setFloating(False)
        self.legendQDockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.legendQDockWidget.setTitleBarWidget(QWidget())

        # Lay our widgets out in the main window using a
        # vertical box layout
        self.layout = QVBoxLayout(self.canvasFrame)
        self.layout.addWidget(self.canvas)
        
        # Add map tools
        self.selectTool = SelectMapTool(self.canvas)
    
        self.demLayer = None
        
        #number of divisions for the legend
        self.classes = 6
        
        self.modes = { "Equal Interval"         : QgsGraduatedSymbolRendererV2.EqualInterval,
                      "Quantile"                : QgsGraduatedSymbolRendererV2.Quantile,
                      "Natural Breaks (Jenks)"  : QgsGraduatedSymbolRendererV2.Jenks,
                      "Standard Deviation"      : QgsGraduatedSymbolRendererV2.StdDev,
                      "Pretty Breaks"           : QgsGraduatedSymbolRendererV2.Pretty
                      }
        
        for mode in self.modes.keys():
            self.modeComboBox.addItem(mode)
            
        self.mode = self.modeComboBox.currentText()
            
        self.modeComboBox.currentIndexChanged.connect(self.onModeChanged)

    def zoomIn(self):
        qDebug("Zoom In Activated")
        self.canvas.zoomIn();
	  
    def zoomOut(self):
        qDebug("Zoom Out Activated")
        self.canvas.zoomOut();

    def loadVectorLayer(self):
        qDebug("Loading Vector Layer")
        
        # layout is set - open a layer
        # Add an OGR layer to the map
        file = QFileDialog.getOpenFileName(self, "Open Shapefile", ".", "Shapefiles (*.shp)")
        fileInfo = QFileInfo(file)
	        
        # Add the layer
        layer = QgsVectorLayer(fileInfo.absoluteFilePath(), fileInfo.fileName()[:-4], "ogr")
        	
        if not layer.isValid():
            print "Layer is invalid"
            return
        
        # Remove previous layers from the registry
#        QgsMapLayerRegistry.instance().removeAllMapLayers()
        
        # Add layer to the registry
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        
        # Set extent to the extent of our layer
        self.canvas.setExtent(layer.extent())
        
#        # Change the color of the layer to gray
#        #symbols = layer.renderer().symbols()
#        #ymbol = symbols[0]
#        #ymbol.setFillColor(QColor.fromRgb(192,192,192))
        
        # Set up the map canvas layer set
        cl = QgsMapCanvasLayer(layer)
        layers = [cl]
        self.canvas.setLayerSet(layers)
        
        self.layer = layer
        self.layers.append(layer)
        self.canvas.refresh()

        self.mFieldComboBox.setLayer(self.layer)
                    
        qDebug("layer loaded successfully!!" )
	
    def loadRasterLayer(self):
        qDebug("Loading Vector Layer")
        # layout is set - open a layer
        # Add an OGR layer to the map
        file = QFileDialog.getOpenFileName(self, "Open Raster", ".", "Rasters (*.*)")
        fileInfo = QFileInfo(file)
	
        # Add the layer
        #layer = QgsVectorLayer(file, fileInfo.fileName(), "ogr")
        layer = QgsRasterLayer(file, fileInfo.fileName())
	
        if not layer.isValid():
            print "Layer is invalid"
            return
	
        self.demLayer = layer

        # Add layer to the registry
        # Set extent to the extent of our layer
        self.canvas.setExtent(layer.extent())
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        layers = self.canvas.mapSettings().layerSet()
        layers.append(layer.id())
        self.canvas.mapSettings().setLayerSet(layers)
        qDebug("layer loaded successfully!!" )
        self.canvas.refresh()
	
    def getElevation(self, point):
        #point is QgsPoint
        print point.x()
        print point.y()
        choosenBand = 0
        attr = 0
        if QGis.QGIS_VERSION_INT >= 10900: # for QGIS >= 1.9
            # this code adapted from valuetool plugin
            ident = self.demLayer.dataProvider().identify(point, QgsRasterDataProvider.IdentifyFormatValue)
            if ident is not None and ident.has_key(choosenBand+1):
                attr = ident[choosenBand+1].toDouble()[0]
                if self.demLayer.dataProvider().isNoDataValue ( choosenBand+1, attr ): 
                    attr = 0
        else:
            ident = self.demLayer.identify(point)
            try:
                attr = float(ident[1].values()[choosenBand])
			
            except:
                pass
        return attr
					
    def getPointAtDistance(self,distance,geometry):
        shapelyLineGeom = loads(str(geometry.exportToWkt()))
        shapelyPoint =  shapelyLineGeom.interpolate(distance)
        qgsPointGeom = QgsGeometry.fromWkt(shapelyPoint.wkt)
        return qgsPointGeom
	  
    def getSegmentedPoints(self, geometry, ratio):
        #return list of QgsPoint
        pointList = []
        geomLength = geometry.length()
        perc = ratio * geomLength
        length = -perc
        while(length < geomLength):
            length = length + perc
            point = self.getPointAtDistance(length, geometry)
            pointList.append(point)
        return pointList
	  
    def getElevationTest(self):
        g1 = QgsGeometry.fromWkt('LINESTRING(490351.96514423 4548291.73076923, 494542.01322115 4541976.58653846)')
        spoints = self.getSegmentedPoints(g1,0.1)
        for item in spoints:
            print "print points....."
            print item.exportToWkt()		
	   
    def showBuffer(self):
        width, ok = QtGui.QInputDialog.getDouble(iface.mapCanvas(), 'Input Dialog', 'Enter Width:')
        qDebug("Loading Vector Layer")
        # layout is set - open a layer
        # Add an OGR layer to the map
        file = QFileDialog.getOpenFileName(self, "Open Raster", ".", "Rasters (*.*)")
        fileInfo = QFileInfo(file)

    def setSelectionTool(self):
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.setCurrentLayer(self.layer)
	  
    def getVerticesList(self):
        i=0
        verticesList = []
        lyrSelection = self.layer.selectedFeatures()
        for feature in lyrSelection:
            geom = feature.geometry()
            vrtcs = self.getSegmentedPoints(geom,0.1)
            for v in vrtcs:
                print "-----------------------------------------------------------------"
                qDebug (str(v.asPoint().x()) + "," + str(v.asPoint().y()))	
                print "-----------------------------------------------------------------"
                x=v.asPoint().x()
                y=v.asPoint().y()
                y1=y-5
                for j in range(5):
                    xCord[i][j]= x
                    yCord[i][j]= y 
                    elev[i][j]=self.getElevation(QgsPoint(x,y))
                    y=y+5
                for j in range(5):
                    xCord[i][j]= x
                    yCord[i][j]= y1 
                    elev[i][j]=self.getElevation(QgsPoint(x,y))
                    y=y-5
                i = i + 1 # i++ does not exist in python..
        calc(xCord,yCord,elev) ##calling the calc function in the calculation.py
        
    def validatedDefaultSymbol(self, geometryType):
        symbol = QgsSymbolV2.defaultSymbol( geometryType )
        if symbol is None:
            if geometryType == QGis.Point:
                symbol = QgsMarkerSymbolV2()
            elif geometryType == QGis.Line:
                symbol =  QgsLineSymbolV2 ()
            elif geometryType == QGis.Polygon:
                symbol = QgsFillSymbolV2 ()
        return symbol
    
    def applyGraduatedSymbologyStandardMode(self, layer, field, classes, mode):
        symbol = self.validatedDefaultSymbol( layer.geometryType() )
        colorRamp = QgsVectorGradientColorRampV2.create({'color1':'255,0,0,255', 'color2':'0,0,255,255','stops':'0.25;255,255,0,255:0.50;0,255,0,255:0.75;0,255,255,255'})
        renderer = QgsGraduatedSymbolRendererV2.createRenderer( layer, field, classes, mode, symbol, colorRamp )
        #renderer.setSizeScaleField("LABELRANK")
        layer.setRendererV2( renderer )
        
    def onFieldChanged(self, fieldName):
        self.field = fieldName
        for layer in self.layers:
            self.applyGraduatedSymbologyStandardMode(layer, self.field, self.classes, self.modes[self.mode])
        self.layer.setDisplayField(self.field)
        self.createMapTips()
        self.canvas.refresh()

        
    def onModeChanged(self, modeIndex):
        self.mode = self.modeComboBox.currentText()
        for layer in self.layers:
            self.applyGraduatedSymbologyStandardMode(layer, self.field, self.classes, self.modes[self.mode])
        self.canvas.refresh()
        
    def createMapTips( self ):
        """ Create MapTips on the map """
        self.timerMapTips = QTimer( self.canvas )
        self.mapTip = QgsMapTip()
        self.connect( self.canvas, SIGNAL( "xyCoordinates(const QgsPoint&)" ),
            self.mapTipXYChanged )
        self.connect( self.timerMapTips, SIGNAL( "timeout()" ),
            self.showMapTip )

    def mapTipXYChanged( self, p ):
        """ SLOT. Initialize the Timer to show MapTips on the map """
        if self.canvas.underMouse(): # Only if mouse is over the map
            # Here you could check if your custom MapTips button is active or sth
            self.lastMapPosition = QgsPoint( p.x(), p.y() )
            self.mapTip.clear( self.canvas )
            self.timerMapTips.start( 750 ) # time in milliseconds

    def showMapTip( self ):
        """ SLOT. Show  MapTips on the map """
        self.timerMapTips.stop()
    
        if self.canvas.underMouse(): 
            # Here you could check if your custom MapTips button is active or sth
            pointQgs = self.lastMapPosition
            pointQt = self.canvas.mouseLastXY()
            self.mapTip.showMapTip( self.layer, pointQgs, pointQt,
                self.canvas )


def main(argv):
    # create Qt application
    app = QApplication(argv)

    print "prefix: "
    print qgis_prefix

    # Initialize qgis libraries
    QgsApplication.setPrefixPath(qgis_prefix, True)
    QgsApplication.initQgis()

    print "settings:"
    print QgsApplication.showSettings()
    
    # create main window
    wnd = ShapeViewer()
    # Move the app window to upper left
    wnd.move(100,100)
    wnd.show()

    # run!
    retval = app.exec_()

    # exit
    QgsApplication.exitQgis()
    sys.exit(retval)


if __name__ == "__main__":
    main(sys.argv)
