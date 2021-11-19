# yahoo_rss_fetcher
Scrape yahoo rss finance feeds

Application contains:
REST API service to get pageable rss_feeds from postgres db
SCRAPER service to fetch data from yahoo finance rss feeds and put items to postgres db

Some of main services used to build solution:
  * django
  * celery
  * rest_framework
  * rabbitmq
  * postgres
  * docker


# To run Application install docker and run commands
```
docker-compose build
docker-compose up
```
