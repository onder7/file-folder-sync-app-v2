# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\py\\28102024fcopy\\run.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['tkcalendar', 'python-dateutil', 'tkcalendar', 'python-dateutil', 'babel', 'babel_numbers'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='FileSyncApp',
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
    manifest='manifest.xml',
)