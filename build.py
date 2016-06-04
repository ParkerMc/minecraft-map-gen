from distutils.core import setup
import py2exe, sys, os

Mydata_files = [('', ['os']),('assets',['assets/splach.png','assets/icon.ico']),('ui',['ui/main.ui'])]
sys.argv.append('py2exe')

setup(
    data_files = Mydata_files,
    options = {'py2exe': {'bundle_files': 1, 'compressed': True,"dll_excludes":['w9xpopen.exe']}},
    windows = [{"icon_resources": [(1, "assets/icon.ico")],'script': 'start.pyw'}],
    zipfile = None,
)

