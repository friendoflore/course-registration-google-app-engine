import webapp2
import os
import jinja2 

# This controls loads the Jinja template and renders the page
class BaseHandler(webapp2.RequestHandler):

	def get_course_name(self, k):
		name = k.get()
		return name

	@webapp2.cached_property
	def jinja2(self):
		env = jinja2.Environment(
		loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
		extensions=['jinja2.ext.autoescape'],
		autoescape=True
		)

		env.globals['get_course_name'] = self.get_course_name
		env.add_extension('jinja2.ext.loopcontrols')
		return env

	def render(self, template, template_variables={}):
		template = self.jinja2.get_template(template)
		self.response.write(template.render(template_variables))
