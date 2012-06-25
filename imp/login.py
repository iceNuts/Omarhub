import tornado.web
import tornado.auth
from base import *
from core.db import *

errorcode = ''

class LoginHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		global errorcode
	def get(self):
	        """Cookie judge if auth"""
		if self.current_user:
			self.redirect("/home")
			return
		"""Show template for login"""
		global errorcode
		print errorcode
		self.render("login.html", errorcode=errorcode)	
		errorcode = ''
		
	def post(self):
		global errorcode
		"""Check username & passwd"""
		passwd = self.get_arguments("u_passwd")
		usr_mail = self.get_arguments("u_mail")
							
		if self.dbManager.checkAuth(usr_mail, passwd):
			self.errorcode = ''
			self.set_secure_cookie("user", ''.join(usr_mail))
			self.redirect("/home/"+''.join(usr_mail))
			return
		else:
			errorcode = '1'
			self.redirect("/")
			return

class LogoutHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def get(self):
		if self.current_user:
			self.clear_all_cookies()
		self.redirect("/")
				




		
