import uuid
from django.db import models

# models.py
class NewsItem(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.CharField(max_length=500)
    pubDate = models.DateTimeField()
    symbol = models.CharField(max_length=50)
    guid =  models.UUIDField(default=uuid.uuid4, null= True)
    def __str__(self):
        return self.title
