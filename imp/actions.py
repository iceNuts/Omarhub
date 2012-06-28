import tornado.web
import tornado.auth
from base import *
from core.db import *

class FollowPeopleActionHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def post(self, user_id):
		if not self.current_user:
			self.write('0')
		self.dbManager.follow_people_action(self.current_user, user_id)
		self.write('1')

class UnfollwPeopleActionHandler(BaseHandler):
	def initialize(self):	
		self.dbManager = dbmgr()
	def post(self, user_id):
		if not self.current_user:
			self.write('0')
		self.dbManager.unfollow_people_action(self.current_user, user_id)
		self.write('1')