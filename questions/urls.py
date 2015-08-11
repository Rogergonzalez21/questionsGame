from django.conf.urls import patterns, url
from questions import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^questions$', views.questions, name='questions'),
    url(r'^questions/add-question/$', views.add_question, name='add_question'),
    url(r'^questions/edit-question/(?P<question_id>\d+)/$', views.edit_question, name='edit_question'),
    url(r'^questions/delete-question/(?P<question_id>\d+)/$', views.delete_question, name='delete_question'),
    url(r'^start-game$', views.start_game, name='start_game'),
    url(r'^start-game/(?P<dificulty_id>\d+)/$', views.game, name='game'),
    url(r'^start-game/(?P<dificulty_id>\d+)/(?P<question_id>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^start-game/(?P<dificulty_id>\d+)/(?P<question_id>\d+)/right/$', views.right_question, name='right_question'),
    url(r'^start-game/(?P<dificulty_id>\d+)/(?P<question_id>\d+)/wrong/$', views.wrong_question, name='wrong_question'),
]