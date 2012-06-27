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
		tagdict=dict()
		tagdict["Work Field"]=self.dbManager.get_tags("work_field")
		for i in tagdict["Work Field"]:
			name=i["name"]
			followed=i["followed"]
			my_follow=self.dbManager.check_tag_followed(mail,name,"work_field")
			i=[name,followed,my_follow]
		tagdict["Location"]=self.dbManager.get_tags("location")
		for i in tagdict["Location"]:
			name=i["name"]
			followed=i["followed"]
			my_follow=self.dbManager.check_tag_followed(mail,name,"location")
			i=[name,followed,my_follow]
		tagdict["Target Population"]=self.dbManager.get_tags("target")
		for i in tagdict["Target Population"]:
			name=i["name"]
			followed=i["followed"]
			my_follow=self.dbManager.check_tag_followed(mail,name,"target")
			i=[name,followed,my_follow]
		tagdict["Free Tags"]=self.dbManager.get_tags("freetag")
		for i in tagdict["Free Tags"]:
		for i in tagdict["Free Tags"]:
			name=i["name"]
			followed=i["followed"]
			my_follow=self.dbManager.check_tag_followed(mail,name,"freetag")
			i=[name,followed,my_follow]
		
		self.render("tags.html",user_id=user_id,tagdict=tagdict)
