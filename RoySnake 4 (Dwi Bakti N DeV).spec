# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\User\\Documents\\Game Py Creat By Me\\Python Roy Snake (Dwi Bakti N Dev)\\RoySnake Revolution Project By (Dwi Bakti N Dev)\\RoySnake 4 Playfrom (Dwi Bakti N Dev)\\RoySnake 4 (Dwi Bakti N DeV).py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\User\\Documents\\Game Py Creat By Me\\Python Roy Snake (Dwi Bakti N Dev)\\RoySnake Revolution Project By (Dwi Bakti N Dev)\\RoySnake 4 Playfrom (Dwi Bakti N Dev)\\Roysnake4.ico', '.ico'), ('C:\\Users\\User\\Documents\\Game Py Creat By Me\\Python Roy Snake (Dwi Bakti N Dev)\\RoySnake Revolution Project By (Dwi Bakti N Dev)\\RoySnake 4 Playfrom (Dwi Bakti N Dev)\\RoyKun.jpg', '.jpg'), ('C:\\Users\\User\\Documents\\Game Py Creat By Me\\Python Roy Snake (Dwi Bakti N Dev)\\RoySnake Revolution Project By (Dwi Bakti N Dev)\\RoySnake 4 Playfrom (Dwi Bakti N Dev)', 'RoySnake 4 Playfrom (Dwi Bakti N Dev)/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='RoySnake 4 (Dwi Bakti N DeV)',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\User\\Documents\\Game Py Creat By Me\\Python Roy Snake (Dwi Bakti N Dev)\\RoySnake Revolution Project By (Dwi Bakti N Dev)\\RoySnake 4 Playfrom (Dwi Bakti N Dev)\\Roysnake4.ico'],
)
