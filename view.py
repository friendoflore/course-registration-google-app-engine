import webapp2
import base_page
import user_ctrl
from google.appengine.ext import ndb
from dataload import DataLoader
import db_defs

class View(base_page.BaseHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}

	def get(self):
		action = self.request.get('action')
		if action == "view_user":
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

		self.render('view.html', self.template_values)