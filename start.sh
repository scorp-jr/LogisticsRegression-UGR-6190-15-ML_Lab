#!/bin/bash
# Use the PORT variable Render provides, default to 8000 locally
export PORT=${PORT:-8000}
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:$PORT
