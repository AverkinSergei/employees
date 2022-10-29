#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

/wait_postgres.sh

python manage.py collectstatic --noinput

gunicorn app.wsgi:application --bind 0.0.0.0:8000
