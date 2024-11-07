@echo off
REM Compiling Python script with PyInstaller
pyinstaller --onefile --windowed --icon=icon.ico --debug=all --upx-dir "C:\Users\olive\Downloads\upx-4.2.4-win64" --name="Zari" --add-data "files/fonts/Roboto/Roboto-Bold.ttf;files/fonts/Roboto" --clean mainwindow.py

echo Compilation complete.
pause
