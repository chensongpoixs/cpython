@echo off
RPM jupyter 工具的启动脚本
setlocal

cd /d %~dp0

start ipython notebook

RPM if "%1" == "" pause


