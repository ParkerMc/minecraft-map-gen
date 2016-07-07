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
import sys, os, subprocess, platform, warn, close, mapstm, worldstm
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import QThread

form_class = uic.loadUiType("ui/main.ui")[0]

class Main(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        self.forceClose = False
        self.lmr = 0
        self.worlds = []
        self.worldnames = []
        self.maps = []
        self.mapnames = []
        self.backm = []
        self.backw = []
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
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+S"), self, self.savekey)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+R"), self, self.runkey)
        self.dump()

    def runkey(self,no="no"):
        if no == "no":
            self.srun()

    def savekey(self,no="no"):
        if no == "no":
            self.save()

    def dump(self):
        self.backm = []
        self.backw = []
        for i in range(1,self.Worlds.rowCount()):
            try: self.backw.append(str(self.Worlds.item(i,0).text()))
            except: self.backw.append("")
        for i in range(1,self.Maps.rowCount()-1):
            try: self.backm.append((self.Maps.item(i,0).text()))
            except: self.backm.append("")

    def srun(self):
        self.save()
        try:
            if str(self.outputt.text()).replace(" ","") == "" or not os.path.exists(str(self.outputt.text())):
                self.warn("You must provide a valid output path.")
                return False
        except:
            self.warn("You must provide a valid output path.")
            return False
        try:
            if str(self.Worlds.item(1,0).text()).replace(" ","")=="" or str(self.Worlds.item(1,1).text()).replace(" ","")=="":
                self.warn("You must have at least 1 world.")
                return False
        except:
            self.warn("You must have at least 1 world.")
            return False
        try:
            if str(self.Maps.item(1,0).text()).replace(" ","")=="" or str(self.Maps.item(1,1).text()).replace(" ","")=="":
                self.warn("You must have at least 1 map.")
                return False
        except:
            self.warn("You must have at least 1 map.")
            return False
        global fileo
        fileo = self.filep
        run()
        self.tabWidget.setFixedWidth(0)
        self.run.setFixedWidth(0)
        self.output.setFixedWidth(781)
        self.cancel.setFixedWidth(91)

    def imgforc(self,a):
        mapstm.imgforc(self,a)

    def nDirc(self,a):
        mapstm.nDirc(self,a)

    def rmodec(self,a):
        mapstm.rmodec(self,a)

    def rmodenc(self,a):
        mapstm.rmodenc(self,a)

    def Dimensionc(self,a):
        mapstm.Dimensionc(self,a)

    def worldc(self,a):
        mapstm.worldc(self,a)

    def oncchangemap(self,a,b):
        mapstm.oncchangemap(self,a,b)

    def mapsgen(self):
        mapstm.mapsgen(self)

    def newrowmap(self):
        mapstm.newrowmap(self)

    def onchangemap(self,a,b,c=0,d=0):
        mapstm.onchangemap(self,a,b,c,d)

    def onchangeworld(self,a,b):
        worldstm.onchangeworld(self,a,b)

    def path(self,a,b):
        worldstm.path(self,a,b)

    def actionOpenf(self):
        ofile = QtGui.QFileDialog.getOpenFileName(filter="Config File (*.cfg)")
        try:
            f = open(ofile,"r")
        except: return
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

    def genOut(self):
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
            output += '\ntexturepath = "'+str(self.packt.text()).replace("\\","/")+'"'
        return output

    def save(self):
        if self.filep == "":
            try:
                self.filep = QtGui.QFileDialog.getSaveFileName(filter="Config File (*.cfg)")
            except: return False
        output = self.genOut()
        f = open(str(self.filep).replace("\\","/"),"w")
        f.write(output)
        f.close()
        return True
    def warncell(self, a, b, i):
        print str(a)+"-"+str(b)+"-"+str(i)
    def warn(self, i):
        self.wdialog = warn.warn(i)
        self.wdialog.exec_()


    def closeEvent(self, event):
        closen = True
        if self.filep == "":
        	if str(self.outputt.text()).strip() != "" or str(self.packt.text()).strip() != "" or str(self.processes.value()).strip() != "1" or len(self.worlds) != 0 or len(self.maps) != 0:
        		closen = False
        else:
            f = open(self.filep,"r")
            lines = f.readlines()
            f.close()
            "\n#"+str(self.maps).replace("[","").replace("]","").replace("(","").replace(")","").replace("'","")+"\n \n"
            if lines[2].strip() != "#"+str(self.outputt.text()).strip() or lines[3].strip() != "#"+str(self.packt.text()).strip() or lines[4].strip() != "#"+str(self.processes.value()).strip() or lines[5].strip() != "#"+str(self.worlds).replace("[","").replace("]","").replace("(","").replace(")","").replace("'","").strip() or lines[6].strip() != "#"+str(self.maps).replace("[","").replace("]","").replace("(","").replace(")","").replace("'","").strip():
                closen = False

        if closen:
            stopn()
        else:
            self.cdialog = close.close(self)
            self.cdialog.exec_()
            if not self.forceClose:
                event.ignore()


class Worker(QThread):

    def go(self):
        self.go = True

    def run(self):
        self.go = False
        global go
        global sel
        while go == False:
            None
        global fileo
        global stop
        if not stop:
            if platform.system() == "Windows" and platform.architecture() == "32Bit":
                proc = subprocess.Popen("32bit\\overviewer.exe --config="+str(fileo), shell=True, stdout=subprocess.PIPE)
                print "32bit\\overviewer.exe --config="+fileo
            if platform.system() == "Windows" and platform.architecture() == "64Bit":
                proc = subprocess.Popen("64bit\\overviewer.exe --config="+str(fileo), shell=True, stdout=subprocess.PIPE)
            if platform.system() == "Linux":
                proc = subprocess.Popen("overviewer.py --config="+str(fileo), shell=True, stdout=subprocess.PIPE)
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

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = Main()
    myWindow.show()
    app.exec_()
    thread.terminate()