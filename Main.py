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
import sys, os, subprocess
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import QThread, pyqtSignal

f = open("os","r")
global osc
osc = f.readline()
f.close()

form_class = uic.loadUiType("ui/main.ui")[0]

class Main(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        self.lmr = 0
        self.worlds = []
        self.worldnames = []
        self.maps = []
        self.mapnames = []
        self.backm = [[],[],[],[],[],[],[]]
        self.backw = [[],[]]
        self.worldpaths = []
        self.filep = ""
        global sel
        sel = self
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.world = QtGui.QComboBox()
        self.Dimension = QtGui.QComboBox()
        self.Dimension.addItem("Overworld")
        self.Dimension.addItem("Nether")
        self.Dimension.addItem("End")
        self.rmode = QtGui.QComboBox()
        self.rmode.addItem("Normal")
        self.rmode.addItem("Lighting")
        self.rmode.addItem("Smooth Light")
        self.rmode.addItem("Night")
        self.rmode.addItem("Smooth Night")
        self.rmode.addItem("Cave")
        self.rmoden = QtGui.QComboBox()
        self.rmoden.addItem("Normal")
        self.rmoden.addItem("Lighting")
        self.rmoden.addItem("Smooth Light")
        self.nDir = QtGui.QComboBox()
        self.nDir.addItem("Upper Left")
        self.nDir.addItem("Upper Right")
        self.nDir.addItem("Lower Left")
        self.nDir.addItem("Lower Right")
        self.imgfor = QtGui.QComboBox()
        self.imgfor.addItem("Png")
        self.imgfor.addItem("Jpg")
        self.imgfor.addItem("Jpeg")
        self.outputb.clicked.connect(self.outputbf)
        self.packb.clicked.connect(self.packbf)
        self.actionOpen.triggered.connect(self.actionOpenf)
        self.actionSave.triggered.connect(self.save)
        self.actionRun.triggered.connect(self.srun)
        self.Worlds.cellDoubleClicked.connect(self.path)
        self.Worlds.cellClicked.connect(self.path)
        self.Worlds.cellEntered.connect(self.path)
        self.Worlds.cellChanged.connect(self.onchangeworld)
        self.Maps.cellChanged.connect(self.oncchangemap)
        self.Maps.currentCellChanged.connect(self.onchangemap)
        self.Maps.cellClicked.connect(self.onchangemap)
        self.Maps.cellEntered.connect(self.onchangemap)
        self.Maps.cellDoubleClicked.connect(self.onchangemap)
        self.Dimension.currentIndexChanged.connect(self.Dimensionc)
        self.nDir.currentIndexChanged.connect(self.nDirc)
        self.imgfor.currentIndexChanged.connect(self.imgforc)
        self.rmode.currentIndexChanged.connect(self.rmodec)
        self.rmoden.currentIndexChanged.connect(self.rmodenc)
        self.run.clicked.connect(self.srun)
        self.dump()

    def dump(self):
        self.backm = [[],[],[],[],[],[],[]]
        self.backw = [[],[]]
        for i in range(1,self.Worlds.rowCount()):
            try: self.backw[0].append(str(self.Worlds.item(i,0).text()))
            except: self.backw[0].append("")
            try: self.backw[1].append(str(self.Worlds.item(i,1).text()))
            except: self.backw[1].append("")
        for i in range(1,self.Maps.rowCount()-1):
            try: self.backm[0].append((self.Maps.item(i,0).text()))
            except: self.backm[0].append("")
            try: self.backm[1].append(str(self.Maps.item(i,1).text()))
            except: self.backm[1].append("")
            try: self.backm[2].append(str(self.Maps.item(i,2).text()))
            except: self.backm[2].append("")
            try: self.backm[3].append(str(self.Maps.item(i,3).text()))
            except: self.backm[3].append("")
            try: self.backm[4].append(str(self.Maps.item(i,4).text()))
            except: self.backm[4].append("")
            try: self.backm[5].append(str(self.Maps.item(i,5).text()))
            except: self.backm[5].append("")
            try: self.backm[6].append(str(self.Maps.item(i,6).text()))
            except: self.backm[6].append("")

    def srun(self):
        if self.save():
            global fileo
            fileo = self.filep
            run()
            self.tabWidget.setFixedWidth(0)
            self.run.setFixedWidth(0)
            self.output.setFixedWidth(781)
            self.cancel.setFixedWidth(91)

    def imgforc(self,a):
        item = QtGui.QTableWidgetItem()
        item.setText(self.imgfor.itemText(a))
        self.Maps.setItem(self.lmr,5,item)
        self.Maps.removeCellWidget(self.lmr,5)
        self.imgfor = QtGui.QComboBox()
        self.mapsgen()
        self.dump()

    def nDirc(self,a):
        item = QtGui.QTableWidgetItem()
        item.setText(self.nDir.itemText(a))
        self.Maps.setItem(self.lmr,4,item)
        self.Maps.removeCellWidget(self.lmr,4)
        self.nDir = QtGui.QComboBox()
        self.mapsgen()
        self.dump()

    def rmodec(self,a):
        item = QtGui.QTableWidgetItem()
        item.setText(self.rmode.itemText(a))
        self.Maps.setItem(self.lmr,3,item)
        self.Maps.removeCellWidget(self.lmr,3)
        self.rmode = QtGui.QComboBox()
        self.mapsgen()
        self.dump()

    def rmodenc(self,a):
        item = QtGui.QTableWidgetItem()
        item.setText(self.rmoden.itemText(a))
        self.Maps.setItem(self.lmr,3,item)
        self.Maps.removeCellWidget(self.lmr,3)
        self.rmoden = QtGui.QComboBox()
        self.mapsgen()
        self.dump()

    def Dimensionc(self,a):
        item = QtGui.QTableWidgetItem()
        item.setText(self.Dimension.itemText(a))
        self.Maps.setItem(self.lmr,2,item)
        if self.Dimension.itemText(a) == "Nether":
            if self.Maps.item(self.lmr,3).text() != "Normal" and self.Maps.item(self.lmr,3).text() != "Lighting" and self.Maps.item(self.lmr,3).text() != "Smooth Light":
                item = QtGui.QTableWidgetItem()
                item.setText("Normal")
                self.Maps.setItem(self.lmr,3,item)
        self.Maps.removeCellWidget(self.lmr,2)
        self.Dimension = QtGui.QComboBox()
        self.mapsgen()
        self.dump()

    def worldc(self,a):
        item = QtGui.QTableWidgetItem()
        item.setText(self.world.itemText(a))
        self.Maps.removeCellWidget(self.lmr,1)
        self.Maps.setItem(self.lmr,1,item)
        self.world  = QtGui.QComboBox()
        self.world.currentIndexChanged.connect(self.worldc)
        self.mapsgen()
        self.newrowmap()
        self.dump()

    def oncchangemap(self,a,b):
        good = True
        if a > 0:
            #if True:
            try:
                if b==0 and self.Maps.item(a,0).text() in self.mapnames:
                    self.warncell(a,0,"m0")
                    item = QtGui.QTableWidgetItem()
                    item.setText(self.backm[0][a-1])
                    self.Maps.setItem(a,0,item)
            except: None

            try:
                if self.Maps.item(a,1).text() not in [""]+self.worldnames and b==1:
                    self.warncell(a,1,"m1")
                    item = QtGui.QTableWidgetItem()
                    item.setText(self.backm[1][a-1])
                    self.Maps.setItem(a,1,item)

            except: None

            try:
                if self.Maps.item(a,2).text() not in ["Overworld","Nether","End"] and b==2:
                    self.warncell(a,2,"m2")
                    item = QtGui.QTableWidgetItem()
                    item.setText(self.backm[2][a-1])
                    self.Maps.setItem(a,2,item)

            except: None

            try:
                if self.Maps.item(a,3).text() not in ["Normal","Lighting","Smooth Light","Night","Smooth Night","Cave"] and b==3 :
                    self.warncell(a,3,"m3")
                    item = QtGui.QTableWidgetItem()
                    item.setText(self.backm[3][a-1])
                    self.Maps.setItem(a,3,item)

            except: None

            try:
                if self.Maps.item(a,4).text() not in ["Upper Left","Upper Right","Lower Left","Lower Right"] and b== 4:
                    self.warncell(a,4,"m4")
                    item = QtGui.QTableWidgetItem()
                    item.setText(self.backm[4][a-1])
                    self.Maps.setItem(a,4,item)

            except: None

            try:
                if self.Maps.item(a,5).text() not in ["Png","Jpg","Jpeg"] and b==5:
                    self.warncell(a,5,"m5")
                    item = QtGui.QTableWidgetItem()
                    item.setText(self.backm[5][a-1])
                    self.Maps.setItem(a,5,item)

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
            item.setText("Overworld")
            self.Maps.setItem(self.Maps.rowCount()-1,2,item)
            item = QtGui.QTableWidgetItem()
            item.setText("Normal")
            self.Maps.setItem(self.Maps.rowCount()-1,3,item)
            item = QtGui.QTableWidgetItem()
            item.setText("Upper Left")
            self.Maps.setItem(self.Maps.rowCount()-1,4,item)
            item = QtGui.QTableWidgetItem()
            item.setText("Png")
            self.Maps.setItem(self.Maps.rowCount()-1,5,item)
            item = QtGui.QTableWidgetItem()
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

    def onchangeworld(self,a,b):
        if a > 0:
            try:
                if b==0 and self.Worlds.item(a,0).text() in self.worldnames:
                    self.warncell(a,0,"w0")
                    item = QtGui.QTableWidgetItem()
                    item.setText(self.backw[0][a-1])
                    self.Words.setItem(a,0,item)
            except: None

            try:
                if b==0 and self.Worlds.item(a,1).text() in self.worldpaths or os.path.exists(self.Worlds.item(a,1).text()) != True:
                    self.warncell(a,1,"w1")
                    item = QtGui.QTableWidgetItem()
                    item.setText(self.backw[1][a-1])
                    self.Words.setItem(a,1,item)
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
        self.dump()

    def path(self,a,b):
        if a > 0 and b == 1:
            back = ""
            item = QtGui.QTableWidgetItem()
            dire = ""
            try:
                dire = self.Worlds.item(a,b)
            except: None
            if dire == "":
                item.setText(str(QtGui.QFileDialog.getOpenFileName(directory=dire.text(),filter="Minecraft World (level.dat)"))+"")
            elif dire != "":
                item.setText(str(QtGui.QFileDialog.getOpenFileName(filter="Minecraft World (level.dat)")))
            self.Worlds.setItem(a,b,item)

    def actionOpenf(self):
        ofile = QtGui.QFileDialog.getOpenFileName(filter="Config File (*.cfg)")
        f = open(ofile,"r")
        while self.Maps.rowCount() > 2:
            self.Maps.removeRow(self.Maps.rowCount()-1)
        while self.Worlds.rowCount() > 2:
            self.Worlds.removeRow(self.Worlds.rowCount()-1)
        rawfile = f.readlines()
        f.close()
        self.outputt.setText(str(rawfile[2]).replace("#","").replace("\n","").strip())
        self.packt.setText(str(rawfile[3]).replace("#","").replace("\n","").strip())
        self.processes.setValue(int(str(rawfile[4]).replace("#","").replace("\n","").strip()))
        j = 0
        k = 1
        for i in str(rawfile[5]).replace("#","").replace("\n","").split(","):
            item = QtGui.QTableWidgetItem()
            item.setText(i.strip())
            self.Worlds.setItem(k,j,item)
            if j >= 1:
                j = -1
                k += 1
            j+=1
        j = 0
        k = 1
        for i in str(rawfile[6]).replace("#","").replace("\n","").split(","):
            item = QtGui.QTableWidgetItem()
            item.setText(i.strip())
            self.Maps.setItem(k,j,item)
            if j >= 6:
                j = -1
                k += 1
            j+=1
        item = QtGui.QTableWidgetItem()
        item.setText("Overworld")
        self.Maps.setItem(self.Maps.rowCount()-1,2,item)
        item = QtGui.QTableWidgetItem()
        item.setText("Normal")
        self.Maps.setItem(self.Maps.rowCount()-1,3,item)
        item = QtGui.QTableWidgetItem()
        item.setText("Upper Left")
        self.Maps.setItem(self.Maps.rowCount()-1,4,item)
        item = QtGui.QTableWidgetItem()
        item.setText("Png")
        self.Maps.setItem(self.Maps.rowCount()-1,5,item)
        item = QtGui.QTableWidgetItem()
        item.setText("95")
        self.Maps.setItem(self.Maps.rowCount()-1,6,item)
        self.dump()
        self.filep = ofile

    def outputbf(self):
        self.outputt.setText(QtGui.QFileDialog.getExistingDirectory(directory=self.outputt.text()))

    def packbf(self):
        self.packt.setText(QtGui.QFileDialog.getOpenFileName(directory=self.packt.text(),filter="Texture Pack (*.zip; *.jar)"))

    def save(self):
        if str(self.outputt.text()).replace(" ","") == "" or not os.path.exists(str(self.outputt.text())):
            self.warn("You must provide a valid output path.")
            return False
        if str(self.Worlds.item(1,0).text()).replace(" ","")=="" or str(self.Worlds.item(1,1).text()).replace(" ","")=="":
            self.warn("You must have at least 1 world.")
            return False
        if str(self.Maps.item(1,0).text()).replace(" ","")=="" or str(self.Maps.item(1,1).text()).replace(" ","")=="":
            self.warn("You must have at least 1 map.")
            return False
        if self.filep == "":
            try:
                self.filep = QtGui.QFileDialog.getSaveFileName(filter="Config File (*.cfg)")
            except: return False
        output = "#Made with a generator by ParkerMc\n####Do NOT edit####\n"
        output += "#"+self.outputt.text()+"\n"+ "#"+self.packt.text()+"\n#"+str(self.processes.value())+"\n#"+str(self.worlds).replace("[","").replace("]","").replace("(","").replace(")","").replace("'","")+"\n#"+str(self.maps).replace("[","").replace("]","").replace("(","").replace(")","").replace("'","")+"\n \n"
        for i, j in self.worlds:
            output += 'worlds["world_'+i+'"] = "'+ j.replace("level.dat","") +'"\n'
        for i, j, k, l, m, n, o in self.maps:
            output += 'renders["'+str(i)+'"] = {\n    "world": "world_'+str(j)+'",\n    "title": "'+str(i)+'",\n    "rendermode": "'
            if str(k) == "Nether":
                output += str(l).replace("Normal","normal").replace("lighting","lighting").replace("Smooth Light","smooth_lighting")
            elif str(k) != "Nether":
                output += str(l).replace("Normal","normal").replace("lighting","lighting").replace("Smooth Light","smooth_lighting").replace("Night","night").replace("Smooth Night","smooth_night").replace("Cave","cave")

            output += '",\n    "dimension": "'+str(k).replace("Overworld","overworld").replace("Nether","nether").replace("End","end")+'",\n    "northdirection" : "'+str(m).replace("Upper Left","upper-left").replace("Upper Right","upper-right").replace("Lower Left","lower-left").replace("Lower Right","lower-right")+'",\n    "imgformat" : "'+str(n).replace("Png","png").replace("Jpg","jpg").replace("Jpeg","jpeg")+'",\n    "imgquality" : "'+str(o)+'",\n } \n \n'
        output += 'outputdir = "'+str(self.outputt.text()).replace("\\","/")+'"'
        if str(self.packt.text()).replace("","") != "":
            output += '"\ntexturepath = "'+str(self.packt.text()).replace("\\","/")+'"'
        f = open(str(self.filep).replace("\\","/"),"w")
        f.write(output)
        f.close()
        return True
    def warncell(self, a, b, i):
        print str(a)+"-"+str(b)+"-"+str(i)
    def warn(self, i):
        print i

    def closeEvent(self, event):
        stopn()
##        if can_exit:
##            event.accept() # let the window close
##        else:
##            event.ignore()


class Worker(QThread):

    def go(self):
        self.go = True

    def run(self):
        self.go = False
        global go
        global sel
        while go == False:
            None
        global osc
        global fileo
        global stop
        if not stop:
            if osc == "win32":
                proc = subprocess.Popen("32bit\\overviewer.exe --config="+str(fileo), shell=True, stdout=subprocess.PIPE)
                print "32bit\\overviewer.exe --config="+fileo
            if osc == "win64":
                proc = subprocess.Popen("64bit\\overviewer.exe --config="+str(fileo), shell=True, stdout=subprocess.PIPE)
            if osc == "linux":
                proc = subprocess.Popen("./linux/overviewer.py --config="+str(fileo), shell=True, stdout=subprocess.PIPE)
            while True:
                line = proc.stdout.readline()
                if line.strip() == "":
                    pass
                else:
                    print line.strip()
                    sel.output.append(line.strip())
                if not line: break
                if stop: break
            proc.wait()

def slot(arg='finished'): print(arg)
thread = Worker()
thread.start()
global stop
stop = False
global go
go = False
def run():
    global go
    go = True
def stopn():
    global stop
    run()
    stop = True
##
##app = QtGui.QApplication(sys.argv)
##myWindow = Main()
##myWindow.show()
##app.exec_()
##thread.terminate()

