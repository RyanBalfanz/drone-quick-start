install:
	pip install -r requirements.txt

test:
	forego run -e .test.env python -Wall manage.py test
