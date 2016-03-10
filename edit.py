import webapp2
import base_page
import user_ctrl
from google.appengine.ext import ndb
from dataload import DataLoader
import db_defs

class Edit(base_page.BaseHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}

	def render(self, page, template_values={}):
		base_page.BaseHandler.render(self, page, template_values)

	def get(self):
		action = self.request.get('action')
		if action == "edit_user":
			user_key = ndb.Key(urlsafe=self.request.get('user_key'))
			user = user_key.get()

			d = DataLoader()


			self.template_values['course_list'] = d.load_courses(self)
			self.template_values['first_name'] = user.first_name
			self.template_values['last_name'] = user.last_name
			self.template_values['email'] = user.email
			self.template_values['user_tel'] = user.user_tel
			self.template_values['user_gen'] = user.user_gen
			self.template_values['courses'] = user.courses

			self.template_values['ukey'] = user_key.urlsafe()

		self.render('edit.html', self.template_values)

	def post(self):
		user_key = ndb.Key(urlsafe=self.request.get('user_key'))
		user = user_key.get()

		# Change the user's information
		same = True

		for c, v in vars(user).iteritems():
			if user.first_name == self.request.get('first_name'):
				pass
			else:
				same = False
				break
			if user.last_name == self.request.get('last_name'):
				pass
			else:
				same = False
				break
			if user.email == self.request.get('email'):
				pass
			else:
				same = False
				break
			if user.user_tel == self.request.get('user_tel'):
				pass
			else:
				same = False
				break
			if user.user_gen == self.request.get('gender'):
				pass
			else:
				same = False
				break
			if user.courses == [ndb.Key(urlsafe=x) for x in self.request.get_all('user_courses[]')]:
				pass
			else:
				same = False
				break

		user.first_name = self.request.get('first_name')
		user.last_name = self.request.get('last_name')
		user.email = self.request.get('email')
		user.user_tel = self.request.get('user_tel')
		user.user_gen = self.request.get('gender')
		user.courses = [ndb.Key(urlsafe=x) for x in self.request.get_all('user_courses[]')]
		
		if same:
			response_message = 'User ' + user.first_name + ' ' + user.last_name + ' not edited.'
		else:
			response_message = 'User ' + user.first_name + ' ' + user.last_name + ' edited.'

		user.put()

		self.template_values = {'message': response_message}

		self.redirect('/?message=' + self.template_values['message'])



