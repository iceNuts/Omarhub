import tornado.web
import tornado.auth
from core.db import *
from base import *
from core.db import *

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
			"name":user["first_name"]+" "+user["last_name"],
			"age":user["age"],
			"gender":user["gender"],
			"mail":user["mail"],
			"target_population":user["target_population"],
			"location":user["location"],
			"work_field":user["work_field"],
			"language":user["language"],
			#"avatar":user["avatar"]
		}
		user_contact={
			"street":user["street"],
			"city":user["city"],
			"state":user["state"],
			"post_code":user["post_code"],
			"country":user["country"],
			"mobile":user["mobile"],
			"mobile_code":user["mobile_code"],
			"skype":user["skype"]
		}
		user_basic["gender"]=self.get_strgender(user_basic["gender"])
		organization["_type"]=self. get_str_orgtype(organization["_type"])
		organization["org_id"]=None
		
		follower_count=self.dbManager.get_follower_count(mail)
		following_count=self.dbManager.get_following_count(mail)
		self.render("profile.html",
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
		
		
		




