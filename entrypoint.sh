#!/bin/sh

echo "Psql started"

#python manage.py migrate
python main.py
exec "$@"