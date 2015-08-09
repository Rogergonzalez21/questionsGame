from django.conf.urls import patterns, url
from questions import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]