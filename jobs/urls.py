from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.index),
    path('search/', views.search, name="search"),
]