import webapp2
import base_page
import user_ctrl
from google.appengine.ext import ndb
import db_defs

class NewUser(user_ctrl.User):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}

	def render(self, page, template_values={}):
		user_ctrl.User.render(self, page, self.template_values)

	def post(self):
		action = self.request.get('action')
		if action == 'add_user':
			k = ndb.Key(db_defs.User, self.app.config.get('default-group'))
			new_user = db_defs.User(parent=k)
			new_user.first_name = self.request.get('first_name')
			new_user.last_name = self.request.get('last_name')
			new_user.email = self.request.get('user_email')
			new_user.user_tel = self.request.get('user_tel')
			new_user.user_gen = self.request.get('user_gen')
			new_user.courses = [ndb.Key(urlsafe=x) for x in self.request.get_all('user_courses[]')]
			new_user.put()

			self.template_values = {'message': 'User added'}
			self.render('base.html', self.template_values)
		else:
			redirect('/')