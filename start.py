#-------------------------------------------------------------------------------
# Name:        Start
# Purpose:     The stater of the Program
#
# Author:      ParkerMc
#
# Created:     03/05/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     MIT
#-------------------------------------------------------------------------------
import wx, ui

def main():
    app = wx.App(False)
    MySplash = ui.Splach()
    MySplash.Show()
    frame = ui.Start(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
