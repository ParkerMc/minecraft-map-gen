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
import os
import ui
import wx
import wx.xrc
import core
import subprocess
import wx.richtext

def main():
    app = wx.App(False)
    MySplash = ui.Splach()
    MySplash.Show()
    frame = ui.Start(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
