from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from forum.models import Question, Answer

app_name = 'forum'

urlpatterns = [

		# for home page
		url(r'^$', views.home, name='home' ),

		# for list of QA forum/
		url(r'^forum/$', views.forum_list , name = 'forum_list'),

		# for detailed Question
		url(r'^forum/(?P<question_id>\d+)/$', views.question_detail , name='question_detail' ),

		# for create question 
		url(r'^forum/add/$', views.create_question , name='create_question' ),

		# for create question 
		url(r'^forum/(?P<question_id>\d+)/answer/$', views.create_answer , name='create_answer' ),

		# for home page
		url(r'^tutorial/$', views.tutorial, name='tutorial' ),

	]

