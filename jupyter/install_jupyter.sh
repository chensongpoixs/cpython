#!/bin/bash

#在命令行下可用pip下载并安装

pip install jupyter

#安装完成后，在命令行下输入

jupyter notebook

#可启动浏览器，进入Web程序界面


#也可以通过安装ipython交互式计算和开发环境(增强的交互式Python shell)，分以下两步安装

pip install ipython

pip install “ipython[notebook]”

#然后启动应用

ipython notebook

#可以通过Upload上载本地文件，如果要直接打开本地的.ipynb文件，可以直接在命令行输入

jupyter notebook e:\1.ipynb
