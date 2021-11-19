from django.shortcuts import render
from .paginations import CustomPagination
# Create your views here.
# views.py
from rest_framework import viewsets
from .serializers import NewsItemSerializer
from .models import NewsItem


class NewsItemViewSet(viewsets.ModelViewSet):
    queryset = NewsItem.objects.all().order_by('pubDate')
    serializer_class = NewsItemSerializer
    pagination = CustomPagination

    def get_object(self):
        return get_object_or_404(Note, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return NewsItem.objects.filter(symbol=self.request.query_params.get("symbol")).order_by('-pubDate')
