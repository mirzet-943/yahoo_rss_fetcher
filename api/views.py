from django.http.response import HttpResponse
from django.shortcuts import render
from .paginations import CustomPagination
from rest_framework import viewsets
from .serializers import NewsItemSerializer
from .models import NewsItem
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound

class NewsItemViewSet(viewsets.ModelViewSet):
    queryset = NewsItem.objects.all().order_by('pubDate')
    serializer_class = NewsItemSerializer
    pagination = CustomPagination
    #disable post methods
    http_method_names = ['get', 'head']

    def get_object(self):
        return get_object_or_404(NewsItem, id=self.request.query_params.get("id"))

    def get_queryset(self):
        symbols = ["AAPL","TWTR","GC=F","INTC"]
        if (self.request.query_params.get("symbol") in symbols):
            result =  NewsItem.objects.filter(symbol=self.request.query_params.get("symbol")).order_by('-pubDate')
            return result
        else:
            return NewsItem.objects.none()