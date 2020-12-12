from django.urls import path, include
from .views import *
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    
    path('', SearchData.as_view(), name='search'),
    path('<int:page>/', SearchData.as_view(), name='search_pagination'),
]