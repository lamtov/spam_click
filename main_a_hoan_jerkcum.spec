# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/Lam/Documents/TOVANLAM_MMO/PYTHON_AUTO_CLICK/main_a_hoan_jerkcum.py'],
             pathex=['C:/Users/Lam/.conda/envs/minimal_example/python.exe', 'C:\\Users\\Lam\\Documents\\TOVANLAM_MMO\\PYTHON_AUTO_CLICK'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main_a_hoan_jerkcum',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
