import webapp2
import base_page
import db_defs
from dataload import DataLoader

class User(base_page.BaseHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}

	def render(self, page, template_values):
		#self.template_values = {'action':'new_user'}
		#self.template_values['courses'] = [{'name':x.name,'key':x.key.urlsafe()} for x in db_defs.Course.query().fetch()]
		d = DataLoader()
		self.template_values['courses'] = d.load_courses()
		self.template_values['users'] = d.load_users()
		base_page.BaseHandler.render(self, page, self.template_values)

	def get(self):
		self.render('base.html', self.template_values)