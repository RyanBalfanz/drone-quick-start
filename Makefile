install:
	pip install -r requirements.txt

test:
	forego run -e .test.env python manage.py test
