from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('start.py', base=base, targetName = 'Map-gen.exe')
]

setup(name='Minecraft Map Gen',
      version = '0.1',
      description = 'A Minecraft Map Gen By ParkerMc',
      options = dict(build_exe = buildOptions),
      executables = executables)
