FROM python:3.9

RUN apt-get update -y && \
    apt-get upgrade -y && \
    # Python dev
    apt-get install -y python3-pip build-essential gcc python3-dev musl-dev libssl-dev cargo \
    # PostgreSQL
    libpq-dev \
    # Misc
    libffi-dev \
    # scipy
    libblas3 liblapack3 liblapack-dev libblas-dev gfortran \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt \
    && rm -rf /root/.pip

COPY ./wait_postgres.sh /wait_postgres.sh
COPY ./entrypoint.sh /entrypoint
COPY ./django_migrate.sh /django_migrate

RUN chmod +x /django_migrate
