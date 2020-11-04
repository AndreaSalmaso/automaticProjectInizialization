@echo off
title create

@REM your GitHub username (type it as it is, without quotes and with no space after the '=' sign)
set  GitHub_username=
@REM EXAMPLE --> GitHub_username=AndreaSalmaso
    
@REM path of the default folder where you want to save your projects (no quotes and space here either)
set  projectsPATH=
@REM EXAMPLE --> projectsPATH=C:\user\Desktop

initialize.py %1 %GitHub_username%
cd %projectsPATH%
mkdir %1
cd %1
git init
git remote add origin https://github.com/%GitHub_username%/%1.git
echo > README.md
git add .
git commit -m "Initial commit"
git push -u origin master
code .