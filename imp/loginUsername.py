import tornado.web
import tornado.auth
from base import *
from core.db import *

class LoginUsernameHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def post(self):
		mail = self.get_arguments("username")
		"""return 0 not good"""
		self.write(unicode(self.dbManager.check_user_exist(mail)))
