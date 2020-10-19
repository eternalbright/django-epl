#!/usr/bin/env sh

export DJANGO_SUPERUSER_EMAIL=root@example.com
export DJANGO_SUPERUSER_USERNAME=root
export DJANGO_SUPERUSER_PASSWORD=qwerty1234

./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser --no-input

./manage.py runserver 0.0.0.0:"${PORT}"