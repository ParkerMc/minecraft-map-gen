import sys, wx, file
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("ui/opening.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.open.clicked.connect(self.openc)
        self.newc.clicked.connect(self.new)

    def openc(self):
        cfile = file.openf()
        self.close()
    def new(self):
        self.close()

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()
