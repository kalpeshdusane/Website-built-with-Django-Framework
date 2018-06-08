from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Question(models.Model):

	user = models.ForeignKey(User, default=1)
	title = models.CharField(max_length=250)
	topic = models.CharField(max_length=100)
	upload_time = models.DateTimeField()
	question_content = models.TextField()
	number_of_views = models.IntegerField(default=0)

	def get_absolute_url(self):
		return reverse('forum:question_detail', kwargs={'question_id':self.pk})

	def __str__(self):
		return self.title

class Answer(models.Model):

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	user = models.ForeignKey(User, default=1)
	answer_content = models.TextField()
	upload_time = models.DateTimeField() 

	def __str__(self):
		return self.answer_content