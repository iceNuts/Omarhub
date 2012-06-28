import tornado.web
import tornado.auth
from core.db import *
from base import *
from core.db import *

class AdminUserHandler(BaseHandler):
	def get(self):
		self.render("admin_users.html",user_id=0)
