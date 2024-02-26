include .env

PIP	= .\venv\Scripts\pip
PYTHON = .\venv\Scripts\python

create:
	virtualenv --python ${PYTHON_PATH} venv

activate:
	.\venv\Scripts\activate

load:activate
	$(PIP) install -r requirements.txt
	
run:activate
	${PYTHON} main.py > output.txt
	
