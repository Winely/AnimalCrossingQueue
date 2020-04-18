# AnimalCrossingQueue

This project is to create a queueing application for gamers to land others' islands one by one.

## Install
Prerequisite: Python 3.6+; venv activated recommended
```
pip install -r requirements.txt
$ export FLASK_APP=src/app.py
$ flask run
```

## DB Migration

1. Modify DB Table Schema in `models` folder
2. run `python manage.py db migrate -m "changelog"` to commit database changes
3. run `python manage.py db upgrade` to sync to Database

## Project Structure

- `manage.py`     
  For Database Migration
- `migrations`     
  Database Version Control
- `src\models`     
  Database Models
- `src\routes`     
  App routes, like controllers
- `src\service`     
  App services, provide for route to use
- `src\utils`     
  Common utility functions

