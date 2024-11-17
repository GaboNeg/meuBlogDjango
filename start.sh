#!/bin/bash

# Rodar as migrations
python manage.py makemigrations --noinput
python manage.py migrate --noinput


# Iniciar o servidor Gunicorn (ou qualquer outro servidor)
gunicorn meuBlog.wsgi:application
