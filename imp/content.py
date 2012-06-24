import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import json
from base import *
from core.db import *

#Return json 

class EventProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	
	def post(self):
		if not self.current_user:
			return None
		cursor = self.get_arguments("cursor")
		id = self.current_user
		print id
		list = self.dbManager.get_event_list(id, cursor)
		self.write(json.dumps(list))


class OfferProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()

	def post(self):
		if not self.current_user:
			return None
		cursor = self.get_arguments("cursor")
		id = self.current_user
		#print id
		list = self.dbManager.get_offer_list(id, cursor)
		self.write(json.dumps(list))


class NeedProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	
	def post(self):
		if not self.current_user:
			return None
		cursor = self.get_arguments("cursor")
		id = self.current_user
		#print id
		list = self.dbManager.get_need_list(id, cursor)
		self.write(json.dumps(list))

class RecentallProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	#Only for test TODO
	def get(self):
		if not self.current_user:
			return None
		id = self.current_user
		cursor = self.get_arguments("cursor")
		print id
		list = self.dbManager.get_need_list(id, cursor)
		self.write(json.dumps(list))
	def post(self):
		if not self.current_user:
			return None
		cursor = self.get_arguments("cursor")
		id = self.current_user
		#print id
		list = self.dbManager.get_recent_all_list(id, cursor)
		self.write(json.dumps(list))
	









