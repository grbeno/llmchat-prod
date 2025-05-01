#!/bin/sh

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Daphne server..."
gunicorn web: daphne -b 0.0.0.0 -p 8080 config.asgi:application
