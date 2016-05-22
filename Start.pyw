#-------------------------------------------------------------------------------
# Name:        Splach
# Purpose:     Show the Splach screen
#
# Author:      ParkerMc
#
# Created:     21/05/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     MIT
#-------------------------------------------------------------------------------

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import Main, sip

if __name__ == "__main__":
    import sys, time

    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap('assets/splach.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    time.sleep(3)

    mainw = Main.Main()
    mainw.show()
    splash.finish(mainw)
    app.exec_()