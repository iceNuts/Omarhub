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
		list = self.dbManager.get_certain_activity(id, 0)
		self.render('show_one.html', list=list)

class OfferShowHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self, id):
		if not self.current_user:
			self.redirect("/")
		list = self.dbManager.get_certain_activity(id, 1)
		self.render('show_one.html', list=list)

class NeedShowHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self, id):
		if not self.current_user:
			self.redirect("/")
		list = self.dbManager.get_certain_activity(id, 2)
		self.render('show_one.html', list=list)
