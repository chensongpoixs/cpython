#!/bin/bash

#先 ：
pip search openpyxl
#然后：
pip install openpyxl
#应该没问题了，如果还有欢迎留言

# 
pip install xlrd

# exe tools

pip install pyinstaller
# 打包 exe文件的命令
pyinstaller --onefile --nowindowed --icon="computer_three.ico" guess_exe.py
