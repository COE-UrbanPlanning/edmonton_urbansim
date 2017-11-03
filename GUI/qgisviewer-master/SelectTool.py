# PyQt4 includes for python bindings to QT
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# QGIS bindings for mapping functions
from qgis.core import *
from qgis.gui import *

class SelectMapTool(QgsMapTool):   
    def __init__(self, canvas):
        QgsMapTool.__init__(self,canvas)
        self.dragging=False
        self.rubberBand = 0
        self.layer = None
        self.canvas=canvas
        self.selectRect = None
        self.ll = None
        self.ur = None
        self.o = QObject()
        self.cursor = QCursor(QPixmap(["13 13 3 1",
                                       "# c None","a c #222222",". c #dddddd",
                                       "#####...#####",
                                       "#####.a.#####",
                                       "#####.a.#####",
                                       "#####.a.#####",
                                       "#####.a.#####",
                                       "......a......",
                                       ".aaaaaaaaaaa.",
                                       "......a......",
                                       "#####.a.#####",
                                       "#####.a.#####",
                                       "#####.a.#####",
                                       "#####.a.#####",
                                       "#####...#####"]))
        
    def canvasPressEvent(self,event):
        #self.selectRect.setRect(event.pos().x(),event.pos().y(),0,0)
        capture_string = QString("Starting Rectangle")
        print capture_string

    def setCurrentLayer(self,vlayer):
        self.layer = vlayer

    def canvasMoveEvent(self,event):
        if not event.buttons() == Qt.LeftButton:
            return
        if not self.dragging:
            self.dragging=True
            self.rubberBand = QRubberBand(QRubberBand.Rectangle,self.canvas)
        #self.selectRect.setBottomRight(event.pos())
        #self.rubberBand.setGeometry(self.selectRect.normalized())
        #self.rubberBand.show()

    def canvasReleaseEvent(self,e):
        #if not self.dragging:
        #    return
        x = e.pos().x()
        y = e.pos().y()
        point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        searchRadius = (QgsTolerance.toleranceInMapUnits( 5, self.layer, 
               self.canvas.mapRenderer(), QgsTolerance.Pixels))
        rect = QgsRectangle()
        rect.setXMinimum( point.x() - searchRadius );
        rect.setXMaximum( point.x() + searchRadius );
        rect.setYMinimum( point.y() - searchRadius );
        rect.setYMaximum( point.y() + searchRadius );

        #self.band.reset()
        self.layer.select( self.layer.pendingAllAttributesList(), rect, True, True)    
        ids = []
        for feature in self.layer:
			print feature.id()
			ids.append(feature.id())			        
        if e.modifiers() & Qt.ControlModifier:
			ids = list(set(self.layer.selectedFeaturesIds()).union(ids))
        elif e.modifiers() & Qt.ShiftModifier:
			ids = list(set(self.layer.selectedFeaturesIds()).difference(ids))
        
        self.layer.setSelectedFeatures(ids)
        self.canvas.refresh()
             # do something with the feature
        self.o.emit(SIGNAL("finished()"))
        capture_string = QString("releasing event completed")
        print capture_string
        
    def activate(self):
        #print "Start Rectangle Tool"
        capture_string = QString("Starting Rectangle")
        self.canvas.setCursor(self.cursor)
        capture_string = QString("Draw rectangle on canvas " +
                                 "to capture coordinates...")
        print capture_string

    def deactivate(self):
        capture_string = QString("End Rectangle Tool")
        print capture_string


    def isZoomTool(self):
        return False
