from django.urls import include, path
from . import views
from .views import HomePageView 

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('scraper', HomePageView.as_view(), name='Scraper'), # homepage
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]