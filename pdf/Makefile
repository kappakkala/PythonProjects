include .env

PIP	= .\venv\Scripts\pip3
PYTHON = .\venv\Scripts\python

create:
	virtualenv --python ${PYTHON_PATH} venv

activate:
	.\venv\Scripts\activate

load:activate
	$(PIP) install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt