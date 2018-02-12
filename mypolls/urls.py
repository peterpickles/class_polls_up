from django.conf.urls import url
from mypolls import views

urlpatterns = [
    # Matches /polls
    url(r'^$', views.index, name='index'),
    #matches /polls/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #matches /polls/5/results
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    url(r'^(?P<question_id>[0-9]+)/vote/process$', views.process_vote, name='process_vote')

]