import tornado.web
import tornado.auth
from core.db import *
from base import *
from core.db import *

class ProfileHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	
	def sub_dict_minus(self,dict_ori,somekey):
		dict_res={}
		for k in dict_ori:
			if k!=somekey:
				dict_res.update({k:dict_ori[k]})
		return dict_res
			
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
		
	def get(self,user_id):
		if not self.current_user:
			self.redirect("/auth/login")
		mail=self.current_user
		userlist=self.dbManager.get_user_profile_info(mail,0)
		user=userlist[0]
		organizationlist=self.dbManager.get_user_organization(mail)
		organization=organizationlist[0]
		user_id=user["user_id"]
		user_basic={
			"name":" ".join([user["first_name"],user["last_name"]]),
			"age":user["age"],
			"gender":user["gender"],
			"mail":user["mail"],
			"target population":user["target_population"],
			"location":user["location"],
			"work field":user["work_field"],
			"language":user["language"]
		}
		user_contact={
			"street":user["street"],
			"city":user["city"],
			"state":user["state"],
			"country":user["country"],
			"postcode":user["post_code"],
			"mobile":user["mobile"],
			"mobile code":user["mobile_code"],
			"skype":user["skype"]
		}
		org_info={
			"name":organization["name"],
			"acronym":organization["acronym"],
			"type":organization["_type"],
			"found date":organization["found_date"],
			"website":organization["site_url"],
			"employee number":organization["numberOfemployees"],
			"phone":organization["phoneNumber"],
			"country code":organization["country_code"]
		}
		user_basic["gender"]=self.get_strgender(user_basic["gender"])
		org_info["type"]=self. get_str_orgtype(org_info["type"])
		
		avatar=user["avatar"]
		
		follower_count=self.dbManager.get_follower_count(mail)
		following_count=self.dbManager.get_following_count(mail)
		self.render("profile.html",
			user_id=user_id,
			follower_count=follower_count,
			following_count=following_count,
			user_basic=user_basic,
			user_contact=user_contact,
			organization=org_info,
			avatar=avatar
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
		
		
		




