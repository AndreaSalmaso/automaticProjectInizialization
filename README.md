Hi there!👋 Here you can find the files that allows you to automate the creation of a new repository (both local and remote) when starting a new project. Here what it does:
1. creates a new pubblic repo in your GitHub account
2. in the path you previously setted, creates a folder with the repo's name and jumps in it
3. initiates a loca repo in the folder
4. connect the local repo with the remote one
5. creates a blank README file
6. makes the first push
7. opens Visual Code Studio in the project folder (if you don't have it, just follow the instruction below)

### Setup
 1. clone the repo
 2. open a cmd window and type in 
	```bash 
	pip install selenium
	 ```
 3. open *create.bat*: add your GitHub username and the default folder for your projects
	```bash 
	@REM your GitHub username (type it as it is, without quotes and with no space after the '=' sign)
	set  GitHub_username=
		
	@REM path of the default folder where you want to save your projects (no quotes and space here either)
	set  projectsPATH=
	 ```
    If you don't have/use Visual Code Studio, just delete the last line
    ```bash
    code .
    ```
4. open *initialize.py* and add your GitHub password
	```python
	PASSWORD = ""
	```
5. add the folder _automaticProjectInitialization_ to PATH  

### How to use it   

open a cmd window, wherever you want, and type in
```bash
create <name-of-the-folder-you-want-to-create>
```
example: ```create newProject```
