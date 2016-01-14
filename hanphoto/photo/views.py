from google.appengine.api import users

from django.views.generic import TemplateView


class BaseView(TemplateView):
	template_name = None

	def get_context_data(self, **kwargs):

		context = super(BaseView, self).get_context_data(**kwargs)

		# create login/logout url
		if users.get_current_user():
			url = users.create_logout_url(self.request.get_full_path())
			url_linktext = 'Logout'
			context['user_login'] = users.get_current_user().nickname()
			context['is_user_admin'] = users.is_current_user_admin()
		else:
			url = users.create_login_url(self.request.get_full_path())
			url_linktext = 'Login'

		context['url'] = url
		context['url_linktext'] = url_linktext

		return context

class IndexView(BaseView):
	template_name = "photo/index.html"

	def get_context_data(self, **kwargs):

		context = super(IndexView, self).get_context_data(**kwargs)

		return context


class PhotoView(BaseView):
	template_name = "photo/photo.html"

	def get_context_data(self, **kwargs):
		context = super(PhotoView, self).get_context_data(**kwargs)

		return context