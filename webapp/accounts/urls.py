from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [

		# account/login/
		url(r'^login/$', views.login_user, name='login_user' ),

		# account/register/
		url(r'^register/$', views.register, name='register' ),

		# account/logout/
		url(r'^logout/$', views.logout_user, name='logout_user'),
	]

