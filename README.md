# People Management API Python

## SetUp

### VirtualEnv
This isolated by itself all the installed packages

#### Activate
`$ source venv/bin/activate`
#### Deactivate
`(venv)$ deactivate`

### Dependencies/Packages
#### Install PipEnv Dependencies
`$ pip install`

#### Install requirements from a txt file
`$ pip install -r PATH`

#### Record pip dependencies into requirements.txt file
`$ pip freeze > requirements.txt`

### Database
#### Start Postgresql data base
`$ brew services start postgresql`

#### Stop Postgresql data base
`$ brew services stop postgresql`

### Running
#### We need define which file to run when running flask
`$ export FLASK_APP=run.py`

