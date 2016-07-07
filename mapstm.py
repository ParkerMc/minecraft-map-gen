#-------------------------------------------------------------------------------
# Name:        mapstm
# Purpose:     To manage the maps table
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

def imgforc(self,a):
    item = QtGui.QTableWidgetItem()
    item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
    item.setText(self.imgfor.itemText(a))
    self.Maps.setItem(self.lmr,5,item)
    self.Maps.removeCellWidget(self.lmr,5)
    self.imgfor = QtGui.QComboBox()
    self.mapsgen()
    self.dump()

def nDirc(self,a):
    item = QtGui.QTableWidgetItem()
    item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
    item.setText(self.nDir.itemText(a))
    self.Maps.setItem(self.lmr,4,item)
    self.Maps.removeCellWidget(self.lmr,4)
    self.nDir = QtGui.QComboBox()
    self.mapsgen()
    self.dump()

def rmodec(self,a):
    item = QtGui.QTableWidgetItem()
    item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
    item.setText(self.rmode.itemText(a))
    self.Maps.setItem(self.lmr,3,item)
    self.Maps.removeCellWidget(self.lmr,3)
    self.rmode = QtGui.QComboBox()
    self.mapsgen()
    self.dump()

def rmodenc(self,a):
    item = QtGui.QTableWidgetItem()
    item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
    item.setText(self.rmoden.itemText(a))
    self.Maps.setItem(self.lmr,3,item)
    self.Maps.removeCellWidget(self.lmr,3)
    self.rmoden = QtGui.QComboBox()
    self.mapsgen()
    self.dump()

def Dimensionc(self,a):
    item = QtGui.QTableWidgetItem()
    item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
    item.setText(self.Dimension.itemText(a))
    self.Maps.setItem(self.lmr,2,item)
    if self.Dimension.itemText(a) == "Nether":
        if self.Maps.item(self.lmr,3).text() != "Normal" and self.Maps.item(self.lmr,3).text() != "Lighting" and self.Maps.item(self.lmr,3).text() != "Smooth Light":
            item = QtGui.QTableWidgetItem()
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
            item.setText("Normal")
            self.Maps.setItem(self.lmr,3,item)
    self.Maps.removeCellWidget(self.lmr,2)
    self.Dimension = QtGui.QComboBox()
    self.mapsgen()
    self.dump()

def worldc(self,a):
    item = QtGui.QTableWidgetItem()
    item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
    item.setText(self.world.itemText(a))
    self.Maps.removeCellWidget(self.lmr,1)
    self.Maps.setItem(self.lmr,1,item)
    self.world  = QtGui.QComboBox()
    self.world.currentIndexChanged.connect(self.worldc)
    self.mapsgen()
    self.newrowmap()
    self.dump()

def oncchangemap(self,a,b):
    if a > 0:
        try:
            if b==0 and self.Maps.item(a,0).text() in self.mapnames:
                self.warncell(a,0,"m0")
                item = QtGui.QTableWidgetItem()
                item.setText(self.backm[0][a-1])
                self.Maps.setItem(a,0,item)
        except: None

        try:
            try:
                int(str(self.Maps.item(a,6).text()))
            except AttributeError: None
        except ValueError:
            self.warncell(a,6,"m6")
            item = QtGui.QTableWidgetItem()
            item.setText(self.backm[6][a-1])
            self.Maps.setItem(a,6,item)

    self.newrowmap()
    self.mapsgen()
    self.dump()

def mapsgen(self):
    self.maps = []
    self.mapnames = []
    for i in range(1,self.Maps.rowCount()):
        try:
            if str(self.Maps.item(i,0).text()).replace(" ","")!="" and str(self.Maps.item(i,1).text()).replace(" ","")!="":
                self.maps.append((str(self.Maps.item(i,0).text()),str(self.Maps.item(i,1).text()),str(self.Maps.item(i,2).text()),str(self.Maps.item(i,3).text()),str(self.Maps.item(i,4).text()),str(self.Maps.item(i,5).text()),str(self.Maps.item(i,6).text())))
        except: None
        try:
            self.mapnames.append(str(self.Maps.item(i,0).text()))
        except AttributeError: None

def newrowmap(self):
    newrow = False
    try:
        if self.Maps.item(self.Maps.rowCount()-1,0).text().replace(" ","") != "":newrow = True
    except: None
    try:
        if self.Maps.item(self.Maps.rowCount()-1,1).text().replace(" ","") != "":newrow = True
    except: None
    if newrow:
        self.Maps.setRowCount(self.Maps.rowCount()+1)
        item = QtGui.QTableWidgetItem()
        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
        item.setText("")
        self.Maps.setItem(self.Worlds.rowCount()-1,1,item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
        item.setText("Overworld")
        self.Maps.setItem(self.Maps.rowCount()-1,2,item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
        item.setText("Normal")
        self.Maps.setItem(self.Maps.rowCount()-1,3,item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
        item.setText("Upper Left")
        self.Maps.setItem(self.Maps.rowCount()-1,4,item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
        item.setText("Png")
        self.Maps.setItem(self.Maps.rowCount()-1,5,item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
        item.setText("95")
        self.Maps.setItem(self.Maps.rowCount()-1,6,item)

    for i in range(1,self.Maps.rowCount()-2):
        removeroww = True
        try:
            if self.Maps.item(i,0).text().replace(" ","") != "": removeroww = False
        except: None
        try:
            if self.Maps.item(i,1).text().replace(" ","") != "": removeroww = False
        except: None
        if removeroww == True:
            self.Maps.removeRow(i)

def onchangemap(self,a,b,c=0,d=0):
    self.Maps.removeCellWidget(c,d)
    self.lmr = a
    if a != 0:
        if b == 1:
            self.world = QtGui.QComboBox()
            preworld = ""
            try:
                preworld = self.Maps.item(a,1).text()
            except: None
            self.world.addItem("")
            for i, j in self.worlds:
                self.world.addItem(i)
            k = 1
            for i, j in self.worlds:
                if str(i) == preworld:
                    self.world.setCurrentIndex(k)
                k+=1
            self.Maps.setCellWidget(a,b,self.world)
            self.world.currentIndexChanged.connect(self.worldc)
            self.world.showPopup()
        if b == 2:
            self.Dimension = QtGui.QComboBox()
            self.Dimension.addItem("Overworld")
            self.Dimension.addItem("Nether")
            self.Dimension.addItem("End")
            preDimension = ""
            try:
                preDimension = self.Maps.item(a,2).text()
            except: None
            if "Overworld" == preDimension:
                self.Dimension.setCurrentIndex(0)
            if "Nether" == preDimension:
                self.Dimension.setCurrentIndex(1)
            if "End" == preDimension:
                self.Dimension.setCurrentIndex(2)
            self.Maps.setCellWidget(a,b,self.Dimension)
            self.Dimension.currentIndexChanged.connect(self.Dimensionc)
            self.Dimension.showPopup()

        if b == 3:
            prermode = ""
            try:
                prermode = self.Maps.item(a,3).text()
            except: None
            if self.Maps.item(a,2).text() == "Nether":
                self.rmoden = QtGui.QComboBox()
                self.rmoden.addItem("Normal")
                self.rmoden.addItem("Lighting")
                self.rmoden.addItem("Smooth Light")
                if "Normal" == prermode:
                    self.rmoden.setCurrentIndex(0)
                if "Lighting" == prermode:
                    self.rmoden.setCurrentIndex(1)
                if "Smooth Light" == prermode:
                    self.rmoden.setCurrentIndex(2)
                self.Maps.setCellWidget(a,b,self.rmoden)
                self.rmoden.currentIndexChanged.connect(self.rmodenc)
                self.rmoden.showPopup()
            elif self.Maps.item(a,2).text() != "Nether":
                self.rmode = QtGui.QComboBox()
                self.rmode.addItem("Normal")
                self.rmode.addItem("Lighting")
                self.rmode.addItem("Smooth Light")
                self.rmode.addItem("Night")
                self.rmode.addItem("Smooth Night")
                self.rmode.addItem("Cave")
                if "Normal" == prermode:
                    self.rmode.setCurrentIndex(0)
                if "Lighting" == prermode:
                    self.rmode.setCurrentIndex(1)
                if "Smooth Light" == prermode:
                    self.rmode.setCurrentIndex(2)
                if "Night" == prermode:
                    self.rmode.setCurrentIndex(3)
                if "Smooth Night" == prermode:
                    self.rmode.setCurrentIndex(4)
                if "Cave" == prermode:
                    self.rmode.setCurrentIndex(5)
                self.Maps.setCellWidget(a,b,self.rmode)
                self.rmode.currentIndexChanged.connect(self.rmodec)
                self.rmode.showPopup()

        if b == 4:
            self.nDir = QtGui.QComboBox()
            self.nDir.addItem("Upper Left")
            self.nDir.addItem("Upper Right")
            self.nDir.addItem("Lower Left")
            self.nDir.addItem("Lower Right")
            prenDir = ""
            try:
                prenDir = self.Maps.item(a,4).text()
            except: None
            if "Upper Left" == prenDir:
                self.nDir.setCurrentIndex(0)
            if "Upper Right" == prenDir:
                self.nDir.setCurrentIndex(1)
            if "Lower Left" == prenDir:
                self.nDir.setCurrentIndex(2)
            if "Lower Right" == prenDir:
                self.nDir.setCurrentIndex(3)
            self.Maps.setCellWidget(a,b,self.nDir)
            self.nDir.currentIndexChanged.connect(self.nDirc)
            self.nDir.showPopup()

        if b == 5:
            preimgfor = ""
            self.imgfor = QtGui.QComboBox()
            self.imgfor.addItem("Png")
            self.imgfor.addItem("Jpg")
            self.imgfor.addItem("Jpeg")
            try:
                preimgfor = self.Maps.item(a,5).text()
            except: None
            if "Png" == preimgfor:
                self.imgfor.setCurrentIndex(0)
            if "Jpg" == preimgfor:
                self.imgfor.setCurrentIndex(1)
            if "Jpeg" == preimgfor:
                self.imgfor.setCurrentIndex(2)
            self.Maps.setCellWidget(a,b,self.imgfor)
            self.imgfor.currentIndexChanged.connect(self.imgforc)
            self.imgfor.showPopup()