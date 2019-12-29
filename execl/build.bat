@echo off

setlocal

setlocal enabledelayedexpansion


cd /d %~dp0


pyinstaller --onefile --nowindowed  .\cexecl.py

if "%1" == "" pause