

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.showMaximized()        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #creates a slider for number of samples
        self.res = QtWidgets.QSlider(self.centralwidget)
        self.res.setGeometry(QtCore.QRect(30, 260, 201, 31))
        self.res.setProperty("value", 50)
        self.res.setOrientation(QtCore.Qt.Horizontal)
        self.res.setObjectName("res")
        self.res.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        
        #creates a push button
        self.plotL = QtWidgets.QPushButton(self.centralwidget)
        self.plotL.setGeometry(QtCore.QRect(60, 300, 93, 28))
        self.plotL.setObjectName("plotL")
        self.plotL.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.plotL.setStyleSheet(
            "border: 2px solid black;"
            "border-radius: 10px;"
            "background-color: white")
        
        #crates a label for text "input"
        self.input_label = QtWidgets.QLabel(self.centralwidget)
        self.input_label.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.input_label.setObjectName("input_label")
        
        #creates a spin box for number of inputs
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(150, 30, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        
        #creates a table for typing in the points we have
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 256, 151))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        
        #creates a label showing number of samples used in creating the curve
        self.res_label = QtWidgets.QLabel(self.centralwidget)
        self.res_label.setGeometry(QtCore.QRect(100, 240, 100, 16))
        self.res_label.setObjectName("res_label")
        
        #creates a line edit widget to input the value of x where we want to find the value
        self.in2 = QtWidgets.QLineEdit(self.centralwidget)
        self.in2.setGeometry(QtCore.QRect(30, 400, 113, 22))
        self.in2.setObjectName("in2")
        
        #prints the value of polynomial at user given value of x
        self.y_label = QtWidgets.QLabel(self.centralwidget)
        self.y_label.setGeometry(QtCore.QRect(40, 440, 55, 16))
        self.y_label.setObjectName("y_label")
        
        #prints the lagrangian polynomial for the given set of points
        self.poly_label = QtWidgets.QLabel(self.centralwidget)
        self.poly_label.setGeometry(QtCore.QRect(30, 350, 131, 16))
        self.poly_label.setObjectName("poly_label")
        self.poly_label.setWordWrap(True)
        
        #creates a push button
        self.Find = QtWidgets.QPushButton(self.centralwidget)
        self.Find.setGeometry(QtCore.QRect(60, 470, 93, 28))
        self.Find.setObjectName("Find")
        self.Find.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.Find.setStyleSheet(
            "border: 2px solid black;"
            "border-radius: 10px;"
            "background-color: white")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ED3010 Project-Lagrangian Interpolation"))
        self.plotL.setText(_translate("MainWindow", "Plot"))
        self.input_label.setText(_translate("MainWindow", "number of inputs"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x points"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y points"))
        self.res_label.setText(_translate("MainWindow", "number of points:"))
        self.in2.setPlaceholderText(_translate("MainWindow", "value @ x"))
        self.y_label.setText(_translate("MainWindow", "y(x)="))
        self.poly_label.setText(_translate("MainWindow", "lagrangian polynomial"))
        self.Find.setText(_translate("MainWindow", "Find"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
