import sys, wx, file
from PyQt4 import QtCore, QtGui, uic

if sys.platform == "win32":
    global ops
    ops = "32"
elif sys.platform == "win64"
    global ops
    ops = "64"
elif sys.platform != "win64" and sys.platform != "win32":
    global ops
    ops = "outher"

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
