pyinstaller main.py --windowed --onefile
xcopy assets dist\assets\ /E
xcopy img dist\img\ /E
xcopy music dist\music\ /E
xcopy sound dist\sound\ /E 