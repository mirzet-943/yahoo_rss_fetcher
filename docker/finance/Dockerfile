FROM python:3.8-slim

RUN mkdir -p /app/finance
RUN mkdir -p /app/api

RUN apt-get update && apt-get install --yes --no-install-recommends \
        wait-for-it

RUN pip3 install --user \
        django-createsuperuserwithpassword \
        psycopg2-binary


COPY api/ /app/api/
COPY finance/ /app/finance/
COPY . /app/


WORKDIR /app/
RUN sh -c "pip install --upgrade pip && pip install -r requirements.txt"
# RUN django-admin startproject yahoo

# WORKDIR /app/finance
# RUN echo 'DATABASES = {"default": {"ENGINE": "django.db.backends.postgresql", "NAME": "postgres", "USER": "postgres","PASSWORD": "mys3cr3tp455", "HOST": "postgres", "PORT": 5432}}' >> yahoo/settings.py
# RUN echo 'ALLOWED_HOSTS = ["*"]' >> yahoo/settings.py
# RUN echo 'INSTALLED_APPS += ("rest_framework", )' >> yahoo/settings.py
# RUN echo 'INSTALLED_APPS += ("django_createsuperuserwithpassword", )' >> yahoo/settings.py
