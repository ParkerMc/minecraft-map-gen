#-------------------------------------------------------------------------------
# Name:        Main
# Purpose:     To handle the main gui
#
# Author:      ParkerMc
#
# Created:     21/05/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     MIT
#-------------------------------------------------------------------------------
import sys, os
from PyQt4 import QtCore, QtGui, uic
global temp
temp = 'plp'

form_class = uic.loadUiType("ui/main.ui")[0]

class Main(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        self.lmr = 0
        self.worlds = []
        self.maps = []
        self.filep = ""
        global temp
        temp = self
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.outputb.clicked.connect(self.outputbf)
        self.packb.clicked.connect(self.packbf)
        self.actionOpen.triggered.connect(self.actionOpenf)
        self.Worlds.cellDoubleClicked.connect(self.path)
        self.Worlds.cellClicked.connect(self.path)
        self.Worlds.cellEntered.connect(self.path)
        self.Worlds.cellChanged.connect(self.onchangeworld)
        self.Maps.cellChanged.connect(self.oncchangemap)
        self.Maps.currentCellChanged.connect(self.onchangemap)
        self.Maps.cellClicked.connect(self.onchangemap)
        self.Maps.cellEntered.connect(self.onchangemap)
        self.Maps.cellDoubleClicked.connect(self.onchangemap)
        self.imgfor.setVisible(False)
        self.Dimension.setVisible(False)
        self.World.setVisible(False)
        self.rmode.setVisible(False)
        self.rmoden.setVisible(False)
        self.nDir.setVisible(False)
        self.World.currentIndexChanged.connect(self.worldc)
        self.Dimension.currentIndexChanged.connect(self.Dimensionc)
        self.nDir.currentIndexChanged.connect(self.nDirc)
        self.imgfor.currentIndexChanged.connect(self.imgforc)
        self.rmode.currentIndexChanged.connect(self.rmodec)
        self.rmoden.currentIndexChanged.connect(self.rmodenc)

    def imgforc(self,a):
        self.imgfor.setVisible(False)
        item = QtGui.QTableWidgetItem()
        item.setText(self.imgfor.itemText(a))
        self.Maps.setItem(self.lmr,5,item)
        self.worldsgen()

    def nDirc(self,a):
        self.nDir.setVisible(False)
        item = QtGui.QTableWidgetItem()
        item.setText(self.nDir.itemText(a))
        self.Maps.setItem(self.lmr,4,item)
        self.worldsgen()

    def rmodec(self,a):
        self.rmode.setVisible(False)
        item = QtGui.QTableWidgetItem()
        item.setText(self.rmode.itemText(a))
        self.Maps.setItem(self.lmr,3,item)
        self.worldsgen()

    def rmodenc(self,a):
        self.rmoden.setVisible(False)
        item = QtGui.QTableWidgetItem()
        item.setText(self.rmoden.itemText(a))
        self.Maps.setItem(self.lmr,3,item)
        self.worldsgen()

    def Dimensionc(self,a):
        self.Dimension.setVisible(False)
        item = QtGui.QTableWidgetItem()
        item.setText(self.Dimension.itemText(a))
        self.Maps.setItem(self.lmr,2,item)
        if self.Dimension.itemText(a) == "Nether":
            if self.Maps.item(self.lmr,3).text() != "Normal" and self.Maps.item(self.lmr,3).text() != "Lighting" and self.Maps.item(self.lmr,3).text() != "Smooth Light":
                item = QtGui.QTableWidgetItem()
                item.setText("Normal")
                self.Maps.setItem(self.lmr,3,item)
        self.worldsgen()

    def worldc(self,a):
        self.World.setVisible(False)
        item = QtGui.QTableWidgetItem()
        item.setText(self.World.itemText(a))
        self.Maps.setItem(self.lmr,1,item)
        self.worldsgen()

    def oncchangemap(self,a,b):
        if a == 0:
            item = QtGui.QTableWidgetItem()
            if b == 0:
                item.setText("Name")
                self.Maps.setItem(0,0,item)
            if b == 1:
                item.setText("World")
                self.Maps.setItem(0,1,item)
            if b == 2:
                item.setText("Dimension")
                self.Maps.setItem(0,2,item)
            if b == 3:
                item.setText("Rendermode")
                self.Maps.setItem(0,3,item)
            if b == 4:
                item.setText("North Direction")
                self.Maps.setItem(0,4,item)
            if b == 5:
                item.setText("Image Format")
                self.Maps.setItem(0,5,item)
            if b == 6:
                item.setText("Image Quality")
                self.Maps.setItem(0,6,item)

        self.worldsgen()

    def worldsgen(self):
        for i in range(1,self.Maps.rowCount()):
            try:
                if str(self.Maps.item(i,0).text()).replace(" ","")!="" and str(self.Maps.item(i,1).text()).replace(" ","")!="":
                    self.maps.append((str(self.Maps.item(i,0).text()),str(self.Maps.item(i,1).text()),str(self.Maps.item(i,2).text()),str(self.Maps.item(i,3).text()),str(self.Maps.item(i,4).text()),str(self.Maps.item(i,5).text()),str(self.Maps.item(i,6).text())))
            except: None

    def onchangemap(self,a,b,c=0,d=0):
        self.lmr = a
        self.imgfor.setVisible(False)
        self.Dimension.setVisible(False)
        self.World.setVisible(False)
        self.rmode.setVisible(False)
        self.rmoden.setVisible(False)
        self.nDir.setVisible(False)
        if a != 0:
            if b == 1:
                preworld = ""
                try:
                    preworld = self.Maps.item(a,1).text()
                except: None
                self.World.clear()
                self.World.addItem("")
                for i, j in self.worlds:
                    self.World.addItem(i)
                k = 1
                for i, j in self.worlds:
                    if str(i) == preworld:
                        self.World.setCurrentIndex(k)
                    k+=1
                self.World.setVisible(True)
            if b == 2:
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
                self.Dimension.setVisible(True)

            if b == 3:
                prermode = ""
                try:
                    prermode = self.Maps.item(a,3).text()
                except: None
                if self.Maps.item(a,2).text() == "Nether":
                    if "Normal" == prermode:
                        self.rmoden.setCurrentIndex(0)
                    if "Lighting" == prermode:
                        self.rmoden.setCurrentIndex(1)
                    if "Smooth Light" == prermode:
                        self.rmoden.setCurrentIndex(2)
                    self.rmoden.setVisible(True)
                elif self.Maps.item(a,2).text() != "Nether":
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
                    self.rmode.setVisible(True)

            if b == 4:
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
                self.nDir.setVisible(True)

            if b == 5:
                preimgfor = ""
                try:
                    preimgfor = self.Maps.item(a,5).text()
                except: None
                if "Png" == preimgfor:
                    self.imgfor.setCurrentIndex(0)
                if "Jpg" == preimgfor:
                    self.imgfor.setCurrentIndex(1)
                if "Jpeg" == preimgfor:
                    self.imgfor.setCurrentIndex(2)
                self.imgfor.setVisible(True)

    def onchangeworld(self,a,b):
        self.worlds = []

        for i in range(1,self.Worlds.rowCount()):
            try:
                if str(self.Worlds.item(i,0).text()).replace(" ","")!="" and str(self.Worlds.item(i,1).text()).replace(" ","")!="":
                    self.worlds.append((str(self.Worlds.item(i,0).text()),str(self.Worlds.item(i,1).text())))
            except: None
        try:
            if self.Worlds.item(self.Worlds.rowCount()-1,0).text().replace(" ","") != "":self.Worlds.setRowCount(self.Worlds.rowCount()+1)
        except: None
        try:
            if self.Worlds.item(self.Worlds.rowCount()-1,1).text().replace(" ","") != "":self.Worlds.setRowCount(self.Worlds.rowCount()+1)
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

        if a == 0:
            if b == 0:
                item = QtGui.QTableWidgetItem()
                item.setText("Name")
                self.Worlds.setItem(0,0,item)
            if b == 1:
                item2 = QtGui.QTableWidgetItem()
                item2.setText("Path")
                self.Worlds.setItem(0,1,item2)

    def path(self,a,b):
        if a > 0 and b == 1:
            back = ""
            item = QtGui.QTableWidgetItem()
            try:
                item.setText(str(QtGui.QFileDialog.getOpenFileName(directory=self.Worlds.item(a,b).text(),filter="Minecraft World (level.dat)"))+"")
                back = Worlds.item(a,b).text()
            except:
                item.setText(str(QtGui.QFileDialog.getOpenFileName(filter="Minecraft World (level.dat)")))
            if item.text() == "":
                item.setText = back
            self.Worlds.setItem(a,b,item)

    def actionOpenf(self):
        print QtGui.QFileDialog.getOpenFileName(filter="Config File (*.cfg)")

    def outputbf(self):
        self.outputt.setText(QtGui.QFileDialog.getExistingDirectory(directory=temp.outputt.text()))

    def packbf(self):
        self.packt.setText(QtGui.QFileDialog.getOpenFileName(directory=temp.packt.text(),filter="Texture Pack (*.zip; *.jar)"))

    def save(self):
        if self.filep == "":
            self.filep = QtGui.QFileDialog.getSaveFileName(filter="Config File (*.cfg)")
            output = "#Made with a generator by ParkerMc\n"
            output += "#"+self.outputt.text()+"\n"+ "#"+self.packt.text()+"\n#"+str(self.processes.value())+"\n#"+str(self.worlds).replace("[","").replace("]","")+"\n \n"
            for i, j in self.worlds:
                object += 'worlds["'+j+'"] = "'+ k +'"\n'
##		for i, j, k, l, m, n, o, p in configa[4]:
##		  if l == 0:
##		      l = "normal"
##		  if l == 1:
##		      l = "lighting"
##		  if l == 2:
##		      l = "smooth_lighting"
##		  if l == 3:
##		      l = "night"
##		  if l == 4:
##		      l = "smooth_night"
##		  if l == 5:
##		      l = "nether"
##		  if l == 6:
##		      l = "nether_lighting"
##		  if l == 7:
##		      l = "nether_smooth_lighting"
##		  if l == 8:
##		      l = "cave"
##		  if k == 0:
##		      k = "overworld"
##		  if k == 1:
##		      k = "nether"
##		  if k == 2:
##		      k = "end"
##		  if m == 0:
##		      m = "upper-left"
##		  if m == 1:
##		      m = "upper-right"
##		  if m == 2:
##		      m = "lower-left"
##		  if m == 3:
##		      m = "lower-right"
##		  if o == 3:
##		      o = "png"
##		  if o == 1:
##		      o = "jpg"
##		  if o == 2:
##		      o = "jpeg"
##
##		  output += 'renders["'+str(i)+'"] = {\n    "world": "world'+str(j)+'",\n    "title": "'+str(i)+'",\n    "rendermode": "'+str(l)+'",\n    "dimension": "'+str(k)+'",\n    "northdirection" : "'+str(m)+'",\n    "imgformat" : "'+str(o)+'",\n    "imgquality" : "'+str(p)+'",\n } \n \n'
##		output += 'outputdir = "'+configa[0].replace("\\","/")+'"'
##		f = open(configa[2].replace("\\","/"),"w")
##		f.write(output)
##		f.close()

app = QtGui.QApplication(sys.argv)
myWindow = Main()
myWindow.show()
app.exec_()