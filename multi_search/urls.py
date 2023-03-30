from django.urls import path
from .views import search_names


urlpatterns = [
    path('search/', search_names, name='search_names'),
]