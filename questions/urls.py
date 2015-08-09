from django.conf.urls import patterns, url
from questions import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^questions$', views.questions, name='questions'),
    url(r'^questions/add-question/$', views.add_question, name='add_question'),
    url(r'^start-game$', views.start_game, name='start_game'),
]