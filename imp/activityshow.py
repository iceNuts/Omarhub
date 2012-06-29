import tornado.web
import tornado.auth
import json
from base import *
from core.db import *

class EventShowHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self, id):
		my_user_id=self.get_current_user_id()
		userlist=self.dbManager.get_user_profile_info_by_id(my_user_id,0)
		userme=userlist[0]
		avatar=userme["avatar"]
		list = self.dbManager.get_certain_activity(id, 0)
		mail=list[0]["mail"]
		user_dict=self.get_user_info(mail)
		print list
		self.render('show_one.html', 
			list=list ,my_user_id=my_user_id,
			user_id=user_dict["user_id"],
			user_name=user_dict["user_name"],
			avatar=user_dict["avatar"],
			my_avatar=avatar
		)

class OfferShowHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self, id):
		my_user_id=self.get_current_user_id()
		userlist=self.dbManager.get_user_profile_info_by_id(my_user_id,0)
		userme=userlist[0]
		avatar=userme["avatar"]
		list = self.dbManager.get_certain_activity(id, 1)
		mail=list[0]["mail"]
		user_dict=self.get_user_info(mail)
		self.render('show_one.html', 
			list=list ,my_user_id=my_user_id,
			user_id=user_dict["user_id"],
			user_name=user_dict["user_name"],
			avatar=user_dict["avatar"],
			my_avatar=avatar
		)

class NeedShowHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self, id):
		my_user_id=self.get_current_user_id()
		userlist=self.dbManager.get_user_profile_info_by_id(my_user_id,0)
		userme=userlist[0]
		avatar=userme["avatar"]
		list = self.dbManager.get_certain_activity(id, 2)
		mail=list[0]["mail"]
		user_dict=self.get_user_info(mail)
		self.render('show_one.html', 
			list=list ,my_user_id=my_user_id,
			user_id=user_dict["user_id"],
			user_name=user_dict["user_name"],
			avatar=user_dict["avatar"],
			my_avatar=avatar
		)
