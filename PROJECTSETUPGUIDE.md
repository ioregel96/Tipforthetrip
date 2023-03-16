# TipForTheTriTip Django Project Setup

### Create a directory to hold the cloned repository and project-related files 
Open a terminal and navigate to to the newly created directory.
If you use '~', it points to your home directory
(Ex for creating directory):
```shell
cd ~
mkdir TFTT-Backend
cd Backend
```
  
### Create a virtual environment
Having a venv is useful because all project dependecies stay within that environment and will avoid issues with other projects
(Ex using python3): 
```shell
python3 -m venv .venv
```

#### Activate the virtual environment
(Ex using linux):
```shell
. .venv/bin/activate
```
(Ex using Windows):
```ps
& .venv/Scripts/activate
```

To deactivate your venv:
```ps
deactivate
```

### Install the dependencies for the project
```shell
pip install -r requirements.txt
```

Note: Use the following command if you install any python packages and need to update the requirements.txt file:
```shell
pip freeze > requirements.txt
```

### Start the django api
```shell
python manage.py runserver
```


