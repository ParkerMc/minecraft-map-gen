#-------------------------------------------------------------------------------
# Name:        setup
# Purpose:
#
# Author:      ParkerMc
#
# Created:     02/05/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     GNU
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#Config:
var = "0.12.109"
windows32 = "http://overviewer.org/builds/win32/8/overviewer-0.12.109.zip"
windows64 = "http://overviewer.org/builds/win64/7/overviewer-0.12.109.zip"
linux = "http://overviewer.org/builds/src/7/overviewer-0.12.109.tar.gz"
#-------------------------------------------------------------------------------
import urllib, zipfile, tarfile, os, shutil;
cwd = os.getcwd()

def main():
    #remove old if any
    print "removeing old"
    if os.path.exists("32bit"):
        shutil.rmtree("32bit")
    if os.path.exists("64bit"):
        shutil.rmtree("64bit")
    if os.path.exists("linux"):
        shutil.rmtree("linux")
    #make folders to use
    if not os.path.exists("temp"):
        os.makedirs("temp")
    if not os.path.exists("linux"):
        os.makedirs("linux")
    if not os.path.exists("32bit"):
        os.makedirs("32bit")
    if not os.path.exists("64bit"):
        os.makedirs("64bit")
    #download files
    if not os.path.isfile("temp/32-"+var+".zip"):
        print "Downloading Windows 32 bit Overviwer"
        urllib.urlretrieve(windows32,"temp/32-"+var+".zip")
    if not os.path.isfile("temp/64-"+var+".zip"):
        print "Downloading Windows 64 bit Overviwer"
        urllib.urlretrieve(windows64,"temp/64-"+var+".zip")
    if not os.path.isfile("temp/l-"+var+".zip"):
        print "Downloading Linux Overviwer"
        urllib.urlretrieve(linux,"temp/l-"+var+".tar.gz")
    #extrat
    print "extringing"
    with zipfile.ZipFile("temp/32-"+var+".zip", "r") as z:
        z.extractall("32bit/")
    with zipfile.ZipFile("temp/64-"+var+".zip", "r") as z:
        z.extractall("64bit/")
    tar = tarfile.open("temp/l-"+var+".tar.gz", "r:gz")
    tar.extractall("linux")
    tar.close()
    lfrom = os.listdir("linux")[0]
    for i in os.listdir("linux/"+lfrom):
        if not os.path.isfile("linux/"+lfrom+"/"+i):
            shutil.copytree("linux/"+lfrom+"/"+i,"linux/"+i)
        if os.path.isfile("linux/"+lfrom+"/"+i):
            shutil.copy("linux/"+lfrom+"/"+i,"linux/"+i)
    shutil.rmtree("linux/"+lfrom)

if __name__ == '__main__':
    main()
