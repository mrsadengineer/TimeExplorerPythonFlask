# Time Explorer Python and Flask Web App  
## Introduction - the project's aim  
App to explore the datetime library for the programming language of Python.  Virtual playground for explorer through datetime. Provides a simple datatime web api.   

## Technologies
Project is created with:  

Python  3.8.6
Flask   

## Project status
The project is in the beginning. 
Setting up working enviroment. (in progress)  
Structuring presentation layer....   

## Sources
https://code.visualstudio.com/docs/python/tutorial-flask

https://flask.palletsprojects.com/en/1.0.x/cli/

https://github.com/microsoft/python-sample-vscode-flask-tutorial



## Scope of functionalities
User functions
* show current time and date for now
* how many days between two dates
* how much time between two dates
* personalized data and time 

system function
* web ui based app for interactive with python and flask knowledge
* deploy with Docker ()
* documented with github  
* build through github actions
* explore datetime 






### Dev Setup and Launch
#### Setup
##### Session System Level - Software installtion  - 
Install Python  
Install pip  
install virtual environment  
##### Presentation Level      
Create Project App root folder   
Create virutal enviromenet    
    python -m venv <env>  
Use pip to install flask in the new virtual enviroment  
    pip install flask
##### Application Level  - Setup work enviroment -
Set Up Editor (VSCODE)
-Create code snippets
-setup debugger  

Data/Code/Application Structure  
-Python  
-Flask  
--Templates folder
---Html files  
--Static Content folder  
---data.json files   


#### For Windows Launch
##### To create virtual environment
python -m venv env

##### Running app option
There are bascially two ways to start a flask app. Within the code using app.run() or through the flask cmd line lagnauge `flask run`  
Depending on your intentions, you would want use the best approche when you ask yourself, "should I use app.run() or flask run?"  

But before running the flask app, make scure the virtual enviroment is running. You can do it manuely or by seting up the python interperter. To manuely activate virtual enviroment by typing in the command line:
  
'env\scripts\activate'  
  
##### Selecting Python Interperter in VSCODE
For Development in VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:

Activate virtual enviroment by:
use Terminal: Create New Integrated Terminal     

##### Running by Command Line 
When in the virtual virtual enviroment

python -m flask run

##### Install Flask
###### Windows
pip install flask

#### Command time commans
To quit session  

`ctrl + c` to exit



#### Intializing Project Workspace and Github
echo "# TimeExplorerPythonFlask" >> README.md

git init


git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/msadengineer/TimeExplorerPythonFlask.git

git push -u origin main

  
## Other information
### todo
Document Setting up VSCODE Project debugger configuration for python  
Creating code snippet documentation  
Create dockerfile  
### Placement for Future README Sub sections  
Table of contents  
Illustrations  
Examples of use  