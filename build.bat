@echo off
REM Compiling Python script with PyInstaller
pyinstaller --onefile --windowed --icon=icon.ico --add-data "files/fonts/Roboto/Roboto-Bold.ttf;files/fonts/Roboto" mainwindow.py

echo Compilation complete.
pause
