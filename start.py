#-------------------------------------------------------------------------------
# Name:        Start
# Purpose:
#
# Author:      ParkerMc
#
# Created:     03/05/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     GNU
#-------------------------------------------------------------------------------
import wx, ui

def main():
    app = wx.App(False)
    frame = ui.Start(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()

