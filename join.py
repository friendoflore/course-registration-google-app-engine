import webapp2
import base_page
import user_ctrl
from google.appengine.ext import ndb
import db_defs

class Join(user_ctrl.User):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}

	def render(self, page, template_values={}):
	 	user_ctrl.User.render(self, page, self.template_values)

	def post(self):
		action = self.request.get('action')
		if action == 'add_course':
			k = ndb.Key(db_defs.Course, self.app.config.get('default-group'))
			new_course = db_defs.Course(parent=k)
			new_course.name = self.request.get('course_name')
			new_course.put()

			self.template_values = {'message': 'Course added'}
			self.render('base.html', self.template_values)
		else:
			redirect('/')