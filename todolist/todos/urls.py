from django.urls import path, include
from django.conf.urls import url
from . import views

#Redirects to todos/views.py
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    path('add/', views.add, name='add'),
]