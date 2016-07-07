#-------------------------------------------------------------------------------
# Name:        close
# Purpose:     Show the save on close Dialog
#
# Author:      ParkerMc
#
# Created:     29/06/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     MIT
#-------------------------------------------------------------------------------
import error, sys
sys.excepthook = error.excepthook
from PyQt4 import QtGui, uic

close_class = uic.loadUiType("ui/close.ui")[0]

class close(QtGui.QDialog, close_class):
    def __init__(self, se, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.se = se
        self.setupUi(self)
        self.can.clicked.connect(self.canf)
        self.no.clicked.connect(self.nof)
        self.yes.clicked.connect(self.yesf)

    def canf(self):
        self.close()

    def nof(self):
        self.se.forceClose = True

    def yesf(self):
        self.se.save()
        self.se.forceClose = True