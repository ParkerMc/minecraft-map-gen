#-------------------------------------------------------------------------------
# Name:        core
# Purpose:     the core of the program
#
# Author:      ParkerMc
#
# Created:     17/05/2016
# Copyright:   (c) ParkerMc 2016
# Licence:     MIT
#-------------------------------------------------------------------------------
import subprocess


def runcommand(out,command):
    f = open("over.log","w")
    f.close()
    proc = subprocess.Popen("ping %s" % ip, shell=True,
                            stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if line.strip() == "":
            pass
        else:
            log.append(line.strip())
        if not line: break
    proc.wait()
