#!/bin/bash
cd webapp/
echo "Please visit this URL : http://127.0.0.1:8000/ after server runs"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

