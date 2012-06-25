import tornado.web
import tornado.auth
from base import *

class ProfileHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		if not self.current_user:
			self.redirect("/auth/login")
		mail=self.current_user
		user=self.dbManager.get_user_profile_info(mail)
		followers=self.dbManager.get_follower(mail)
		following=self.dbManager.get_following(mail)
		self.render("profile.html",user=user,followers=followers,following=following)
