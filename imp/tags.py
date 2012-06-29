import tornado.web
import tornado.auth
from core.db import *
from base import *
from core.db import *

class TagHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		if not self.current_user:
			self.redirect("/auth/login")
		mail=self.current_user
		userlist=self.dbManager.get_user_profile_info(mail,0)
		user=userlist[0]
		user_id=user["user_id"]
		avatar=user["avatar"]
		tagdict=dict()
		tagdict["Work Field"]=self.dbManager.get_tags("work_field")
		#print type(tagdict["Work Field"])
		for i in range(len(tagdict["Work Field"])):
			tid=tagdict["Work Field"][i]["tag_id"]
			print type(i)
			name=tagdict["Work Field"][i]["name"]
			followed=tagdict["Work Field"][i]["followed"]
			my_follow=self.dbManager.check_tag_followed(mail,name,"work_field")
			tagdict["Work Field"][i]=[tid,name,followed,my_follow]
			#print i
			
		tagdict["Location"]=self.dbManager.get_tags("location")
		for i in range(len(tagdict["Location"])):
			tid=tagdict["Location"][i]["tag_id"]
			name=tagdict["Location"][i]["name"]
			followed=tagdict["Location"][i]["followed"]
			my_follow=self.dbManager.check_tag_followed(mail,name,"location")
			tagdict["Location"][i]=[tid,name,followed,my_follow]
			
		tagdict["Target Population"]=self.dbManager.get_tags("target")
		for i in range(len(tagdict["Target Population"])):
			tid=tagdict["Target Population"][i]["tag_id"]
			name=tagdict["Target Population"][i]["name"]
			followed=tagdict["Target Population"][i]["followed"]
			my_follow=self.dbManager.check_tag_followed(mail,name,"target")
			tagdict["Target Population"][i]=[tid,name,followed,my_follow]
			
		tagdict["Free Tags"]=self.dbManager.get_tags("freetag")
		for i in range(len(tagdict["Free Tags"])):
			tid=tagdict["Free Tags"][i]["tag_id"]
			name=tagdict["Free Tags"][i]["name"]
			followed=tagdict["Free Tags"][i]["followed"]
			my_follow=self.dbManager.check_tag_followed(mail,name,"freetag")
			tagdict["Free Tags"][i]=[tid,name,followed,my_follow]
			
		self.render("tags.html",user_id=user_id,tagdict=tagdict,my_user_id=user_id,my_avatar=avatar)

class TagFollowHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def post(self,tag_id):
		if not self.current_user:
			self.redirect("/auth/login")
		mail=self.current_user
		success=self.dbManager.set_follow_tags(tag_id,mail,0)
		self.write("1")
		#if success==1 :
		#	self.write("1")
		#else :
		#	self.write("0")
		
class TagUnfollowHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def post(self,tag_id):
		if not self.current_user:
			self.redirect("/auth/login")
		mail=self.current_user
		success=self.dbManager.set_follow_tags(tag_id,mail,1)
		self.write("1")
		#if success==1 :
		#	self.write("1")
		#else :
		#	self.write("0")
