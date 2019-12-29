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

# 报错处理方法 可能是 pyinstaller版本太低了
pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
python -m pip install --upgrade pip


