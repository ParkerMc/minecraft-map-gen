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
        self.worlds = []
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

    def onchangeworld(self,a,b):
        self.worlds = []
        for i in range(1,self.Worlds.rowCount()):
            try:
                if str(self.Worlds.item(i,0).text()).replace(" ","")!="" and str(self.Worlds.item(i,1).text()).replace(" ","")!="":
                    self.worlds.append((str(self.Worlds.item(i,0).text()),str(self.Worlds.item(i,1).text())))
            except: None
        print self.worlds
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
            for i, j in configa[3]:
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