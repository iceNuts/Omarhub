import tornado.web
import tornado.auth
from base import *

class HomeHandler(BaseHandler):
	def get(self):
		self.render("home.html")