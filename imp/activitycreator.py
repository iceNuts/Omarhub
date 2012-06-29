import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import json
from base import *
from core.db import *
from copy import copy

#Create New activity
#Insert into tables: Recent_Events & corresponding table

class CreateHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self):
		if not self.current_user:
			self.redirect("/")
		mail=self.current_user
		userlist=self.dbManager.get_user_profile_info(mail,0)
		user=userlist[0]
		user_id=user["user_id"]
		avatar=user["avatar"]
		self.render("create.html", user_id=user_id,my_user_id=user_id,my_avatar=avatar)

class EventCreateHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self):
		pass #show template
	def post(self):
		if not self.current_user:
			self.redirect("/")
		info = dict()
		info['title'] = self.get_argument("title")
		info['description'] = self.get_argument("description")
		info['location'] = self.get_argument("location")
		info['work_field'] = self.get_argument("work_field")
		info['target_population'] = self.get_argument("target_population")
		info['start_date'] = self.get_argument("start_date")
		info['end_date'] = self.get_argument("end_date")	
						
		id = self.dbManager.create_new_activity(self.current_user,info, 0)
		self.redirect("/event/"+ str(id))
		

class OfferCreateHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self):
		pass #show template
	def post(self):
		if not self.current_user:
			self.redirect("/")
		info = dict()
		info['title'] = self.get_argument("title")
		info['description'] = self.get_argument("description")
		info['location'] = self.get_argument("location")
		info['target_population'] = self.get_argument("target_population")
		
		id = self.dbManager.create_new_activity(self.current_user,info, 1)
		self.redirect("/offer/"+ str(id))



class NeedCreateHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self):
		pass #show template
	def post(self):
		if not self.current_user:
			self.redirect("/")
		info = dict()
		info['title'] = self.get_argument("title")
		info['description'] = self.get_argument("description")
		info['location'] = self.get_argument("location")
		info['target_population'] = self.get_argument("target_population")
		
		id = self.dbManager.create_new_activity(self.current_user,info, 2)
		self.redirect("/need/"+str(id))

