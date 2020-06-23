virtualenv:
	python3 -m venv venv 
	source venv/bin/activate

install:
	python -m pip install -r requirements.txt 
