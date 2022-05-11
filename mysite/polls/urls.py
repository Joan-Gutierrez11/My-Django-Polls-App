from django.contrib import admin
from django.urls import path
from polls import views 

urlpatterns = [
    path('', views.home_polls, name='poll')
]