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

class EventCreateHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self):
		pass #show template
	def post(self):
		if not self.current_user:
			self.redirect("/")
		info = dict()
		info['title'] = self.get_arguments("title")
		info['description'] = self.get_arguments("description")
		info['location'] = self.get_arguments("location")
		info['work_field'] = self.get_arguments("work_field")
		info['target_population'] = self.get_arguments("target_population")
		info['start_date'] = self.get_arguments("start_date")
		info['end_date'] = self.get_arguments("end_date")		
		
		self.dbManager.create_new_activity(self.current_user,info, 0)
		

class OfferCreateHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self):
		pass #show template
	def post(self):
		if not self.current_user:
			self.redirect("/")
		info = dict()
		info['title'] = self.get_arguments("title")
		info['description'] = self.get_arguments("description")
		info['location'] = self.get_arguments("location")
		info['work_field'] = self.get_arguments("work_field")
		info['target_population'] = self.get_arguments("target_population")
		
		self.dbManager.create_new_activity(self.current_user,info, 1)

class NeedCreateHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self):
		pass #show template
	def post(self):
		if not self.current_user:
			self.redirect("/")
		info = dict()
		info['title'] = self.get_arguments("title")
		info['description'] = self.get_arguments("description")
		info['location'] = self.get_arguments("location")
		info['work_field'] = self.get_arguments("work_field")
		info['target_population'] = self.get_arguments("target_population")
		
		self.dbManager.create_new_activity(self.current_user,info, 2)

