import tornado.web
import tornado.auth
from base import *
from core.db import *

class FollowActionHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def post(self):
		if not self.current_user:
			self.write('0')
		user_id = self.get_argument("user_id")
		self.dbManager.follow_action(self.current_user, user_id)
		self.write('1')
