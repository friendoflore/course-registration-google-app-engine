import webapp2

config = {'default-group': 'base-data'}

application = webapp2.WSGIApplication([
	('/newuser', 'new_user.NewUser'),
	('/join', 'join.Join'),
	('/edit', 'edit.Edit'),
	('/view', 'view.View'),
	('/', 'user_ctrl.User'),
], debug=True, config=config)

