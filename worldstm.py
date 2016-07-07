#-------------------------------------------------------------------------------
# Name:        worldstm
# Purpose:     To manage the worlds table
#
# Author:      ParkerMc
#
# Created:     29/06/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     MIT
#-------------------------------------------------------------------------------
from PyQt4 import QtGui, QtCore, uic
def onchangeworld(self,a,b):
    if a > 0:
        try:
            if b==0 and self.Worlds.item(a,0).text() in self.worldnames:
                self.warncell(a,0,"w0")
                item = QtGui.QTableWidgetItem()
                item.setText(self.backw[0][a-1])
                self.Words.setItem(a,0,item)
        except: None

    self.worlds = []
    self.worldnames = []
    self.worldpaths = []
    for i in range(1,self.Worlds.rowCount()):
        try:
            if str(self.Worlds.item(i,0).text()).replace(" ","")!="" and str(self.Worlds.item(i,1).text()).replace(" ","")!="":
                self.worlds.append((str(self.Worlds.item(i,0).text()),str(self.Worlds.item(i,1).text())))
                self.worldnames.append(str(self.Worlds.item(i,0).text()))
                self.worldpaths.append(str(self.Worlds.item(i,1).text()))
        except: None
    try:
        if self.Worlds.item(self.Worlds.rowCount()-1,0).text().replace(" ","") != "":
            self.Worlds.setRowCount(self.Worlds.rowCount()+1)
            item = QtGui.QTableWidgetItem()
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
            item.setText("")
            self.Maps.setItem(self.Worlds.rowCount()-1,1,item)
    except: None
    try:
        if self.Worlds.item(self.Worlds.rowCount()-1,1).text().replace(" ","") != "":
            self.Worlds.setRowCount(self.Worlds.rowCount()+1)
            item = QtGui.QTableWidgetItem()
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
            item.setText("")
            self.Maps.setItem(self.Worlds.rowCount()-1,1,item)
    except: None
    for i in range(1,self.Worlds.rowCount()-2):
        removeroww = True
        try:
            if self.Worlds.item(i,0).text().replace(" ","") != "": removeroww = False
        except: None
        try:
            if self.Worlds.item(i,1).text().replace(" ","") != "": removeroww = False
        except: None
        if removeroww == True:
            self.Worlds.removeRow(i)

    self.dump()

def path(self,a,b):
    if a > 0 and b == 1:
        item = QtGui.QTableWidgetItem()
        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
        dire = ""
        try:
            dire = self.Worlds.item(a,b)
        except: None
        if dire == "":
            item.setText(str(QtGui.QFileDialog.getOpenFileName(directory=dire.text(),filter="Minecraft World (level.dat)"))+"")
        elif dire != "":
            item.setText(str(QtGui.QFileDialog.getOpenFileName(filter="Minecraft World (level.dat)")))
        self.Worlds.setItem(a,b,item)