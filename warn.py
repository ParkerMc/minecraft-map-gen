#-------------------------------------------------------------------------------
# Name:        warn
# Purpose:     Show the Warning Dialog
#
# Author:      ParkerMc
#
# Created:     29/06/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     MIT
#-------------------------------------------------------------------------------
from PyQt4 import QtGui, uic

warn_class = uic.loadUiType("ui/warn.ui")[0]

class warn(QtGui.QDialog, warn_class):
    def __init__(self, warningmsg, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.label.setText(warningmsg)