## Django template: https://github.com/wsvincent/djangox

## Installations
- conda install -c conda-forge bootstrap
- pip install django-allauth
- pip install django-crispy-forms
- pip install django-debug-toolbar

## Set up new user
- python manage.py makemigrations users
- python manage.py migrate
- python manage.py createsuperuser
  - user:admin
  - email: admin@example.com
  - password:admin
- python manage.py runserver
- go to: http://127.0.0.1:8000.
