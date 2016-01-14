from django.conf.urls import patterns, url

from photo import views

urlpatterns = patterns('',
	# index
	url(r'^$', views.IndexView.as_view()),
	# Photo
	url(r'^photo/$', views.PhotoView.as_view()),
)