import tornado.web
import tornado.auth
from base import *

class HomeHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self):
		if not self.current_user:
			self.redirect("/auth/login")
		mail=self.current_user
		
		self.render("home.html")
		
	def post(self):
		pass
