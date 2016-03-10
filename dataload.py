import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class DataLoader():

	def load_courses(self, user):
		self.course_list = [{'name':x.name,'key':x.key.urlsafe()} for x in db_defs.Course.query(ancestor=ndb.Key(db_defs.Course, user.app.config.get('default-group'))).fetch()]
		return self.course_list

	def load_users(self, user):
		self.user_list = [{'first_name':x.first_name,'last_name':x.last_name,'courses':x.courses,'key':x.key.urlsafe()} for x in db_defs.User.query(ancestor=ndb.Key(db_defs.User, user.app.config.get('default-group'))).fetch()]
		return self.user_list

