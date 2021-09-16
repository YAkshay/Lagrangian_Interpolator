

from form import Ui_MainWindow
from sympy import *

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *

from PyQt5.QtCore import Qt
from matplotlib.backends.qt_compat import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


from matplotlib.figure import Figure

import sys

import matplotlib.pyplot as plt
import numpy as np


class PlotLag(QtWidgets.QMainWindow):
     def __init__(self, parent=None):
        super().__init__(parent= parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowIcon(QIcon('iitm.png'))
        self.ui.widget1 = QWidget()
        self.setCentralWidget(self.ui.widget1)       
    
        # setting up of different layouts
        page_layout = QHBoxLayout(self.ui.widget1) #creates a horizontal layout
        button_layout = QVBoxLayout(self.ui.widget1) #creates a vertical layout
        
        # adding widgets to the layout for inputs and buttons
        button_layout.addWidget(self.ui.input_label)
        button_layout.addWidget(self.ui.spinBox)
        button_layout.addWidget(self.ui.tableWidget,2)
        button_layout.addWidget(self.ui.res_label, alignment= Qt.AlignBottom)
        button_layout.addWidget(self.ui.res)
        button_layout.addWidget(self.ui.plotL, 1)
        button_layout.addWidget(self.ui.poly_label, 1)
        button_layout.addWidget(self.ui.in2, 1)
        button_layout.addWidget(self.ui.Find)
        button_layout.addWidget(self.ui.y_label, 1, alignment= Qt.AlignTop)
        
        #making a static canvas 
        self.static_canvas = FigureCanvas(Figure(figsize=(5, 5))) 
        self.addToolBar(NavigationToolbar(self.static_canvas, self))
        self._static_ax = self.static_canvas.figure.subplots()
        
        # adding plot canvas and input layout consisting of buttons and input widgets
        page_layout.addLayout(button_layout,2)
        page_layout.addWidget(self.static_canvas,5) 
        
        #connect change in events to different methods      
        self.ui.spinBox.valueChanged.connect(lambda: self.ui.tableWidget.
                                             setRowCount(self.ui.spinBox.value())) 
                                                # changes no.of rows of table widget when value in spinBox changes
        self.ui.plotL.clicked.connect(self.lag_pol) #lag_pol method gets activated on clicking plot pushButton
        self.ui.res.valueChanged.connect(self.Res) #used to to change no. of points sampled       
        self.ui.Find.clicked.connect(lambda: self.ui.y_label.
                                   setText('y(x)='+ str(self.eq.subs(self.x,self.ui.in2.text()))))
                                     #updates y(x) label on clicking find button   
                
        
         
     def lag_pol(self): #this function finds the lagrangian polynomial from the user given points
         self.x=symbols('x')
         self.post=self.ui.res.value()    
         rc= self.ui.tableWidget.rowCount()
         cc=self.ui.tableWidget.columnCount()
         l=[]
         for i in range(rc): #this loop is used to extract data from table widget           
             t=[]
             for j in range(cc):
                 t.append(float(self.ui.tableWidget.item(i,j).text()))
             l.append(t)
         
         self.x_given=np.array([l[y][0] for y in range(len(l))], dtype='float')
         self.y_given=np.array([l[y][1] for y in range(len(l))], dtype='float')
         self.x_pl= np.linspace(min(self.x_given), max(self.x_given), self.post)        
        
         pi=np.array([]) #array to store coeff of yi's in lagrange polynomial formula
         for xi,yi in zip(self.x_given, self.y_given):
             p=1
             for xj in self.x_given:
                 if xi != xj:
                     p*= (self.x-xj)/(xi-xj)
             pi= np.append(pi,p)
         self.eq=simplify(np.sum(pi*self.y_given))
         self.y_pl=np.array([self.eq.subs(self.x,x_val) for x_val in self.x_pl], dtype='float')
         
         self.PlotCurve()
         
     def Res(self): #this function changes no. of samples in the curve
         self.post= self.ui.res.value()
         self.ui.res_label.setText('number of points:'+ str(self.post))
         self.lag_pol()

         
     def PlotCurve(self):  #this function is used to plot the curve on canvas             
        self._static_ax.axes.cla()
        self._static_ax.plot(self.x_pl,self.y_pl,'b-o', self.x_given, self.y_given,'ro')
        self._static_ax.axes.set_ylabel('y(x)', fontsize=20)
        self._static_ax.axes.set_xlabel('x', fontsize=20)
        self._static_ax.axes.set_title('Plot of interpolating polynomial', fontsize=20)
        self.static_canvas.draw_idle()
        
        self.ui.poly_label.setText('lagrange polynimial:\n'+str(self.eq))
    
    
if __name__ == '__main__':
    
    
    app = QtWidgets.QApplication([])
    win = PlotLag()
    win.show()
    win.activateWindow()
    win.raise_()
    sys.exit(app.exec_())
