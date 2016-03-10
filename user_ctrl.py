import webapp2
import base_page
import db_defs
from dataload import DataLoader

class User(base_page.BaseHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}

	def render(self, page, template_values):
		d = DataLoader()
		self.template_values['courses'] = d.load_courses(self)
		self.template_values['users'] = d.load_users(self)
		base_page.BaseHandler.render(self, page, self.template_values)

	def get(self):
		self.template_values['message'] = self.request.get('message')
		self.render('base.html', self.template_values)