from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title','topic','question_content']

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['answer_content']
