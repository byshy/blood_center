make sure when using cmd to be inside you project directory                                    |
|---|
- cmd -> heroku login
- pip install gunicorn
- pip install django-heroku
- make sure requirements.txt is available
- cmd -> heroku create <app_name>
- check using heroku open
- add STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
- create Procfile with no extension and put this in it: web: gunicorn <app_name>.wsgi
- add new host and make local variables (secret key and debug boolean) use secrets.token_hex(24) to generate a new secret key
- git push heroku master
- again check using heroku open
- check if a database is created or not (using cmd -> heroku addons)
- cmd -> heroku run python manage.py migrate
- cmd -> heroku run python manage.py createsuperuser