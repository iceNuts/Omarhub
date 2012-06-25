import tornado.web
import tornado.auth
from core.db import *
from base import *

class ProfileHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		if not self.current_user:
			self.redirect("/auth/login")
		mail=self.current_user
		user=self.dbManager.get_user_profile_info(mail)
		followers=self.dbManager.get_follower_count(mail)
		following=self.dbManager.get_following_count(mail)
		self.render("profile.html",user=user,followers=followers,following=following)


class ProfileEditHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	
	def get(self):
		if not self.current_user:
			self.redirect("/auth/login")
		pass
			
	def post(self):
		if not self.current_user:
			return None
		mail = self.current_user
#fetch input data
#user can't change the mail
		first_name = self.get_arguments("first_name")
		last_name = self.get_arguments("last_name")
		age = self.get_arguments("age")
		location = self.get_arguments("location")
		target_population = self.get_arguments("target_population")
		work_field = self.get_arguments("work_field")
		language = self.get_arguments("language")
		country = self.get_arguments("country")
		skype = self.get_arguments("skype")
		
		
		




