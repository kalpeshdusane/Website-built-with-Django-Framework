from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from forum.models import Question, Answer
from .forms import QuestionForm, AnswerForm
import datetime
from django.core.urlresolvers import reverse


# Create your views here.
def home(request):
	if not request.user.is_authenticated():
		return render(request, 'accounts/login.html')
	return render(request, 'forum/home.html')

def tutorial(request):
	if not request.user.is_authenticated():
		return render(request, 'accounts/login.html')
	return render(request, 'forum/tutorial.html')
		
def question_detail(request, question_id):
	if not request.user.is_authenticated():
		return render(request, 'accounts/login.html')
	try:
		question = Question.objects.get(pk=question_id)
		question.number_of_views = question.number_of_views + 1
		question.save()
	except Question.DoesNotExist:
		raise Http404("Question Does Not Exist in the database.")

	return render(request, 'forum/question.html', {'question' : question})

def forum_list(request):
	if not request.user.is_authenticated():
		return render(request, 'accounts/login.html')
	all_questions = Question.objects.all().order_by("-upload_time")
	context = {'all_questions' : all_questions}
	return render(request, 'forum/forum.html' , context)

def create_question(request):
	if not request.user.is_authenticated():
		return render(request, 'accounts/login.html')
	form = QuestionForm(request.POST or None)
	if form.is_valid():
		question = form.save(commit=False)
		question.user = request.user
		question.upload_time = datetime.datetime.now()
		question.save()
		return render(request, 'forum/question.html', {'question': question})
	context = {
		"form": form,
	}
	return render(request, 'forum/question_form.html', context)

def create_answer(request, question_id):
	if not request.user.is_authenticated():
		return render(request, 'accounts/login.html')
	form = AnswerForm(request.POST or None)
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question Does Not Exist in the database.")
	if form.is_valid():		
		answer = form.save(commit=False)
		answer.question = question
		answer.user = request.user
		answer.upload_time = datetime.datetime.now()
		answer.save()
		# return render(request, 'forum/question.html', {'question': question})
		return render(request, 'forum/question.html', {'question': question})
	context = {
		"form": form,
	}
	return render(request, 'forum/answer_form.html', context)