run:
	flask run

format:
	isort -rc app migrations
	black .

lint:
	black --check .
	flake8 .

test:
	python app/tests.py