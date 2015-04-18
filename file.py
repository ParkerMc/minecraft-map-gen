#open and save windows
import wx
import os

def openf():
    app = wx.PySimpleApp()
    wildcard = "Config file (*.cfg)|*.cfg| All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        file = dialog.GetPath()

    dialog.Destroy()
    return file
def savef():
    app = wx.PySimpleApp()
    wildcard = "Config file (*.cfg)|*.cfg| All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Save the file", os.getcwd(), "", wildcard, wx.SAVE)
    if dialog.ShowModal() == wx.ID_OK:
        file = dialog.GetPath()

    dialog.Destroy()
    return file