#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

/wait_postgres.sh

python manage.py migrate