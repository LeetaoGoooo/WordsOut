# -*- mode: python ; coding: utf-8 -*-
"""
This hits most of the major notes required for
building a stand alone version of your Gooey application.
"""


import os
import platform
import gooey
gooey_root = os.path.dirname(gooey.__file__)

from PyInstaller.building.api import EXE, PYZ, COLLECT
from PyInstaller.building.build_main import Analysis
from PyInstaller.building.datastruct import Tree
from PyInstaller.building.osx import BUNDLE

block_cipher = None

a = Analysis(['app.py'],
             pathex=['app.py'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             )
pyz = PYZ(a.pure)

options = [('u', None, 'OPTION'), ('v', None, 'OPTION'), ('w', None, 'OPTION')]


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          options,
          name='WordsOut',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon=os.path.join(gooey_root, 'logo.ico'))

info_plist = {'addition_prop': 'additional_value'}
app = BUNDLE(exe,
             name='WordsOut.app',
             bundle_identifier=None,
             info_plist=info_plist
            )