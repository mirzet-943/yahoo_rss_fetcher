FROM python:3.8-slim

RUN apt-get update && apt-get install --yes --no-install-recommends \
        wait-for-it

COPY scraper/ /app/scraper/
COPY requirements.txt /app/requirements.txt
COPY docker/scraper/entrypoint.sh  /app/docker/scraper/
COPY . .
COPY finance/settings.py /app/scraper/settings.py

WORKDIR /

RUN sh -c "pip install --upgrade pip && pip install -r requirements.txt"
RUN sh -c "pip install psycopg2-binary"
RUN sh -c "pip install threaded"
