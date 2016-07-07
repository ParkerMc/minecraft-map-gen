#-------------------------------------------------------------------------------
# Name:        error
# Purpose:     To handle the errors
#
# Author:      ParkerMc
#
# Created:     29/06/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     MIT
#-------------------------------------------------------------------------------
import urllib, time, cStringIO, traceback, platform
from PyQt4 import QtGui, uic
def excepthook(excType, excValue, tracebackobj):
    separator = '-' * 80
    logFile = "Error.log"
    versionInfo="0.0.1"
    timeString = time.strftime("%m/%d/%Y, %H:%M:%S")
    
    
    tbinfofile = cStringIO.StringIO()
    traceback.print_tb(tracebackobj, None, tbinfofile)
    tbinfofile.seek(0)
    tbinfo = tbinfofile.read()
    errmsg = '%s: \n%s' % (str(excType), str(excValue))
    sections = [separator, timeString, separator, errmsg, separator,tbinfo,separator,"Version: "+ versionInfo,"Os: "+platform.system(), "Architecture: "+platform.architecture()[0], separator]
    msg = '\n'.join(sections)
    try:
        f = open(logFile, "w")
        f.write(msg)
        f.close()
    except IOError:
        pass
    edialog = error(msg)
    edialog.exec_()

error_class = uic.loadUiType("ui/error.ui")[0]

class error(QtGui.QDialog, error_class):
    def __init__(self, msg, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.msg = msg
        self.emsg.setText(msg)
        self.send.clicked.connect(self.sende)

    def sende(self):
        try:
            urllib.urlretrieve("""https://script.google.com/macros/s/AKfycbw0nerGGY1Q0KePlvRGMceROW948Gi1dQtr9G81lpSHueK2ofs/exec?email=%s&de=%s&msg=%s"""%(self.email.text(),self.de.toPlainText(),self.msg),"temp.html")
            errorbox = QtGui.QMessageBox(self)
            errorbox.setWindowTitle("Error")
            errorbox.setText("Email sent thank you :)")
            errorbox.exec_()
        except:
            errorbox = QtGui.QMessageBox(self)
            errorbox.setWindowTitle("Error")
            errorbox.setText("Can not send email.")
            errorbox.exec_()

