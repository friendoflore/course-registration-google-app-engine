from google.appengine.ext import ndb

class User(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	user_tel = ndb.StringProperty(required=True)
	user_gen = ndb.StringProperty(required=True)
	courses = ndb.KeyProperty(repeated=True)

class Course(ndb.Model):
	name = ndb.StringProperty(required=True)