scribe: python scribe.py
worker: celery worker --app=worker --pool=eventlet
web: gunicorn -w 4 web.web_eye:app