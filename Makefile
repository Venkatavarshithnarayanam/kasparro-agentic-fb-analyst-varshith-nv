setup:
	python -m pip install -r requirements.txt

run:
	python src/run.py

test:
	pytest -q
