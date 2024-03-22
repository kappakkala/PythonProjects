include .env

PIP	= .\venv\Scripts\pip
PYTHON = .\venv\Scripts\python

create:
	virtualenv --python ${PYTHON_PATH} venv

load:
	.\venv\Scripts\activate
	$(PIP) install -r requirements.txt

publish:load
	$(PYTHON) inactivity_publisher.py

subscribe:load
	$(PYTHON) inactivity_subscriber.py