from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search_names, name='search_names'),
    path('ajax/', views.ajax_view, name='ajax'),
    path('index/', views.index, name='index')
]