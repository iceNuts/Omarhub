import tornado.web
import tornado.auth
from core.db import *
from base import *
from core.db import *

class ProfileHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	
	#def sub_dict_minus(self,dict_ori,somekey):
	#	dict_res={}
	#	for k in dict_ori:
	#		if k!=somekey:
	#			dict_res.update({k:dict_ori[k]})
	#	return dict_res
			
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
		userlist_me=self.dbManager.get_user_profile_info(mail,0)
		user_me=userlist_me[0]
		my_user_id=str(user_me["user_id"])
		my_avatar=user_me["avatar"]
		
		userlist=self.dbManager.get_user_profile_info_by_id(user_id,0)
		user=userlist[0]
		user_mail=user["mail"]
		user_name=" ".join([user["first_name"],user["last_name"]])
		
		organizationlist=self.dbManager.get_user_organization(user_mail)
		organization=organizationlist[0]
		
		user_basic={
			"name":user_name,
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
		
		follower_count=self.dbManager.get_follower_count(user_mail)
		following_count=self.dbManager.get_following_count(user_mail)
		is_followed=self.dbManager.check_if_followed(mail,user_mail)
		follower_list=self.dbManager.get_follower_brief_list(user_mail,8)
		following_list=self.dbManager.get_following_brief_list(user_mail,8)
		
		print type(user_basic)
		self.render("profile.html",
			my_user_id=my_user_id,
			user_id=user_id,
			user_name=user_name,
			is_followed=is_followed,
			follower_count=follower_count,
			following_count=following_count,
			follower_list=follower_list,
			following_list=following_list,
			user_basic=user_basic,
			user_contact=user_contact,
			organization=org_info,
			my_avatar=my_avatar,
			avatar=avatar
		)


class ProfileEditHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def sub_dict_minus(self,dict_ori,somekey):
		dict_res={}
		for k in dict_ori:
			if k!=somekey:
				dict_res.update({k:dict_ori[k]})
		return dict_res
	
	def get(self):
		if not self.current_user:
			self.redirect("/auth/login")
		mail=self.current_user
		userlist=self.dbManager.get_user_profile_info(mail,0)
		user=userlist[0]
		organizationlist=self.dbManager.get_user_organization(mail)
		organization=organizationlist[0]
		user_id=user["user_id"]
		user_name=" ".join([user["first_name"],user["last_name"]])
		avatar=user["avatar"]
		
		user=self.sub_dict_minus(user,"user_id")
		user=self.sub_dict_minus(user,"avatar")
		user=self.sub_dict_minus(user,"mail")
		user=self.sub_dict_minus(user,"passwd")
		user=self.sub_dict_minus(user,"register_date")
		user=self.sub_dict_minus(user,"org_id")
		
		print type(user)
		organization=self.sub_dict_minus(organization,"org_id")
		
		follower_count=self.dbManager.get_follower_count(mail)
		following_count=self.dbManager.get_following_count(mail)
		is_followed=0
		follower_list=self.dbManager.get_follower_brief_list(mail,8)
		
		self.render("profile_edit.html",
			user_all_info=user,
			user_name=user_name,
			organization=organization,
			is_followed=is_followed,
			follower_count=follower_count,
			following_count=following_count,
			follower_list=follower_list,
			user_id=user_id,
			my_user_id=user_id,
			my_avatar=avatar,
			avatar=avatar
		)
		
class ProfileEditUserHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
			
	def post(self):
		if not self.current_user:
			self.redirect("/auth/login")
		mail = self.current_user
		userlist=self.dbManager.get_user_profile_info(mail,0)
		user=userlist[0]
		user_id=user["user_id"]
		#fetch input data
		#user can't change the mail
		updatedict=dict()
		
		#updatedict["user_id"]=self.get_arguments("user_id")
		updatedict["first_name"] = self.get_arguments("first_name")
		updatedict["last_name"] = self.get_arguments("last_name")
		updatedict["age"] = self.get_arguments("age")
		updatedict["gender"]=self.get_arguments("gender")
		updatedict["location"] = self.get_arguments("location")
		updatedict["target_population"] = self.get_arguments("target_population")
		updatedict["work_field"] = self.get_arguments("work_field")
		updatedict["language"] = self.get_arguments("language")
		updatedict["street"]=self.get_arguments("street")
		updatedict["city"]=self.get_arguments("city")
		updatedict["post_code"]=self.get_arguments("post_code")
		updatedict["country"] = self.get_arguments("country")
		updatedict["mobile"] =self.get_arguments("mobile")
		updatedict["mobile_code"]=self.get_arguments("mobile_code")
		updatedict["skype"] = self.get_arguments("skype")
		self.dbManager.set_user_profile_info(mail,updatedict)
		
		self.redirect("/profile/"+str(user_id))
		
class ProfileEditOrgHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
			
	def post(self):
		if not self.current_user:
			self.redirect("/auth/login")
		mail = self.current_user
		userlist=self.dbManager.get_user_profile_info(mail,0)
		user=userlist[0]
		user_id=user["user_id"]
		#updatedict["user_id:"]=self.getarguments("user_id")
		updatedict["first_name"] = self.get_arguments("first_name")
		updatedict["last_name"] = self.get_arguments("last_name")
		updatedict["age"] = self.get_arguments("age")
		updatedict["gender"]=self.get_arguments("gender")
		updatedict["location"] = self.get_arguments("location")
		updatedict["target_population"] = self.get_arguments("target_population")
		updatedict["work_field"] = self.get_arguments("work_field")
		updatedict["language"] = self.get_arguments("language")
		updatedict["street"]=self.get_arguments("street")
		updatedict["city"]=self.get_arguments("city")
		updatedict["post_code"]=self.get_arguments("post_code")
		updatedict["country"] = self.get_arguments("country")
		updatedict["mobile"] =self.get_arguments("mobile")
		updatedict["mobile_code"]=self.get_arguments("mobile_code")
		updatedict["skype"] = self.get_arguments("skype")
		#self.dbManager.set_org_profile_info(mail,updatedict)
		
		self.redirect("/profile/"+str(user_id))
		
class ProfileInnovationHandler(BaseHandler):
	pass

