run:
	flask run

format:
	isort -rc .
	black .

lint:
	black --check .
	flake8 .