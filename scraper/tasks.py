# scraping/tasks.py
import uuid
import _thread
from bs4.element import ResultSet
from django.db.models.fields import UUIDField
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from api.models import NewsItem
from celery import Celery

app = Celery('scraper')

@app.task
def scrape(symbol):
    article_list = []
    try:
        print('Starting the scraping tool: '+ symbol)
        headers = {
                    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", 
                    'Accept-Language': 'en-US,en;q=0.9,hr-HR;q=0.8,hr;q=0.7', 
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
                    }
        link = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=' + symbol + '&region=US&lang=en-US'
        print (link)
        r = requests.get(link, headers= headers)
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.find_all('item')
        lastGuidAdded = NewsItem.objects.filter(symbol=symbol).order_by('-pubDate').first()
        print(lastGuidAdded)
        if (lastGuidAdded):
            try:
                indexInArticles = [ x.find('guid').text for x in articles].index(str(lastGuidAdded.guid))
                if (indexInArticles > 0):
                    print(indexInArticles)
                    articles = articles[:indexInArticles - 1]
                elif (indexInArticles == 0):
                    articles = None
            except Exception as e:
                print("Item does not exists")
                print (e)
        if (articles is None):
            print ("No new articles for symbol: " + symbol)
            return
        print("Total count articles from symbol: ", symbol, len(articles))
        for a in articles:
            title = a.find('title').text
            print('Scrapping article' + title)
            link = a.find('link').text
            guid = a.find('guid').text
            description = a.find('description').text
            published_wrong = a.find('pubDate').text
            published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
            article = {
                'title': title,
                'link': link,
                'description': description,
                'published': published,
                'symbol': symbol,
                'guid': guid
            }
            article_list.append(article)
        return save(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
   

#Start threads to scrape all symbols :)
@app.task
def start_scraping():
   _thread.start_new_thread( scrape, ("AAPL",) )
   _thread.start_new_thread( scrape, ("TWTR", ) )
   _thread.start_new_thread( scrape, ("GC=F", ) )
   _thread.start_new_thread( scrape, ("INTC", ) )


@app.task
def save(article_list):
    print('starting')
    for article in article_list:
        try:
            NewsItem.objects.create(
                title = article['title'],
                description = "test",
                link = article['link'],
                pubDate = article['published'],
                id = uuid.uuid4(),
                symbol = article['symbol'],
                guid = article['guid'],
            )
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished ')

    