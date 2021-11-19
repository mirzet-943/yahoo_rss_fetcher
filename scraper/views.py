from django.shortcuts import render
from django.views import generic
from api.models import NewsItem
# Create your views here.
class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles' 
    # assign "News" object list to the object "articles"
    # pass news objects as queryset for listview
    def get_queryset(self):
        return NewsItem.objects.all()