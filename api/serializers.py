# serializers.py
from rest_framework import serializers
from .models import NewsItem

class NewsItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsItem
        fields = ('id','link','title', 'description', 'pubDate')
