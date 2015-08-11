from django.conf.urls import patterns, url
from questions import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^questions$', views.questions, name='questions'),
    url(r'^questions/add-question/$', views.add_question, name='add_question'),
    url(r'^questions/edit-question/(?P<question_id>\d+)/$', views.edit_question, name='edit_question'),
    url(r'^start-game/$', views.start_game, name='start_game'),
    url(r'^questions/question-detail/(?P<question_id>\d+)/$', views.question_detail, name='question_detail'),
]