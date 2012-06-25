import tornado.web
import tornado.auth
from core.db import *
from base import *

class ProfileHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get_strgender(self,gid):
		if gid==0 :
			return "Male"
		else:
			return "Female"
			
	def get_str_orgtype(self,otid):
		if otid==0 :
			return "Private sector"
		elif otid==1 :
			return "Government Agency"
		else:
			return "Multilateral Organization"
		
	def get(self):
		if not self.current_user:
			self.redirect("/auth/login")
		mail=self.current_user
		userlist=self.dbManager.get_user_profile_info(mail)
		user=userlist[0]
		organizationlist=self.dbManager.get_user_organization(mail)
		organization=organizationlist[0]
		user_basic={
			"first_name":"",
			"last_name":"",
			"age":0,
			"gender":0,
			"mail":"",
			"target_population":"",
			"location":"",
			"work_field":"",
			"language":"",
			"avatar":""
		}
		user_contact={
			"street":"",
			"city":"",
			"state":"",
			"post_code":"",
			"country":"",
			"mobile":"",
			"mobile_code":"",
			"skype":""
		}
		user_basic.update(user)
		user_contact.update(user)
		user_basic["gender"]=self.get_strgender(user_basic["gender"])
		organzation["_type"]=self. get_str_orgtype(organzation["_type"])
		
		follower_count=self.dbManager.get_follower_count(mail)
		following_count=self.dbManager.get_following_count(mail)
		self.render("profile.html",
			user=user,
			follower_count=follower_count,
			following_count=following_count,
			user_basic=user_basic,
			user_contact=user_contact,
			organization=organization
		)


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
		
		
		




