# TO_DO_LIST

# Requirements
* Python 3.9.6
* Django 3.2.13
* djangorestframework 3.13.1
* celery 5.2.6
* django-celery-beat 2.2.1
* eventlet 0.33.0
* redis 4.2.2
* python-crontab 2.6.0

# About
This is a web application that allows users to add tasks and set tasks' categories, priorities, deadlines for them.
# How to run 
First of all you need to run redis server
After that you need to open terminal and proceed to project app
```
cd .../TO_DO_LIST/todoproject
```
Then run this command 
```
celery -A todoproject.celery beat
```
Then you need to run 
```
celery -A todoproject worker -l info -P eventlet
```
After that run a server
```
python manage.py runserver
```
Open the link in your browser 
```
http://127.0.0.1:8000/
```

# Requirements installation
To install Requirements you need to open a terminal and run  these commands 
```
pip install django

pip install djangorestframework

pip install celery

pip install redis

pip install django-celery-beat

pip install eventlet

pip install python-crontab
```