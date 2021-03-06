import tornado.web
import tornado.auth
from base import *
from core.db import *

class HomeHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self):
		if not self.current_user:
			self.redirect("/auth/login")
			return 
		mail=self.current_user
		userlist=self.dbManager.get_user_profile_info(mail,0)
		user=userlist[0]
		user_id=user["user_id"]
		avatar=user["avatar"]
		self.render("home.html",user_id=user_id,my_user_id=user_id,my_avatar=avatar)
		
	def post(self):
		pass
