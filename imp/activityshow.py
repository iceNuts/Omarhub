import tornado.web
import tornado.auth
import json
from base import *
from core.db import *

class EventShowHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self, id):
		if not self.current_user:
			self.redirect("/")
		list = self.get_certain_activity(id, 0)
		self.write(json.dumps(list))

class OfferShowHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self, id):
		if not self.current_user:
			self.redirect("/")
		list = self.get_certain_activity(id, 1)
		self.write(json.dumps(list))

class NeedShowHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self, id):
		if not self.current_user:
			self.redirect("/")
		list = self.get_certain_activity(id, 2)
		self.write(json.dumps(list))