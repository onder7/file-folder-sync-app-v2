import os
from pathlib import Path

project_root = Path(__file__).parent

pyinstaller_args = [
    str(Path(project_root, 'run.py')),
    '--onefile',
    '--windowed',
    '--name=FileSyncApp',
    '--hidden-import=tkcalendar',
    '--hidden-import=python-dateutil',
    '--hidden-import=tkcalendar',
    '--hidden-import=python-dateutil',
    '--hidden-import=babel',
    '--hidden-import=babel_numbers',
    '--manifest=manifest.xml',
]


from PyInstaller.__main__ import run

run(pyinstaller_args)
print('Executable dosya başarıyla oluşturuldu!')