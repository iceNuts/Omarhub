#coding:utf-8
import tornado.web
import re
import sendmail
import time
from random import choice
from base import *
from core.db import *

xmyUri = ''

class ActivateHandler(BaseHandler):
	webaddress="http://127.0.0.1:8888/auth/activate/"
	def initialize(self):
		self.dbManager = dbmgr()
	def genLink(self,email):
		strtime=time.strftime('%s%h%a%j%w%d%W',time.localtime(time.time()))
		emailparts=email.split("@")
		ename=emailparts[0]
		ehost=emailparts[1].split(".")[0]
		link=''
		for i in range(8):
			link=link+choice('abcdefghijklmnopqrstuvwxyz%!')
		link=link+ename
		for i in range(7):
			link=link+choice('abcdefghijklmnopqrstuvwxyz%!')
		link=link+strtime
		for i in range(11):
			link=link+choice('$%!')
		link=link+strtime
		for i in range(6):
			link=link+choice('abcdefghijklmnopqrstuvwxyz%!')
		
		return link
    
	def get(self):
		global xmyUri 
		xmyUri = "%s"%(self.request.uri)
		print xmyUri
		if self.current_user:
			self.redirect("/home")
			return
		else:
			self.render("firstlogin.html")

	def post(self):
		global xmyUri 
		email=self.get_argument("user_email")
		"""check if user exists"""
		if (not self.dbManager.check_user_exist(email)) or (self.dbManager.check_user_activated(email) and xmyUri != "/auth/login/forgetpasswd"):
			"""Show no users"""
			print "forgetpassword"
			xmyUri = ''
			self.redirect("/")
			return
		link=self.genLink(email)
		print "activate"
		message="Please click "+self.webaddress+link+" to activate your account"
		#db.insert(link,email,date)
		self.dbManager.set_activate_events(email,link)
		sendmail.send_mail(email,"Activate your account",message)
		xmyUri = ''
		self.redirect("/")
        
class PasswdSettingHandler(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self,activate_id):
		if self.current_user:
			self.redirect("/home")
			return
		if self.dbManager.check_activation_expired(activate_id):
			"""Expired"""
			self.redirect("/")
		self.render("setpassword.html")
		
	def post(self,activate_id):
		passwd=self.get_argument("user_passwd")
		mail = self.dbManager.get_activate_account(activate_id)
		if not mail:
			"""Expired"""
			return
		self.dbManager.update_user_password(mail, passwd)
		self.set_secure_cookie("user", ''.join(mail))
		"""Need mail account to redirect"""
		self.redirect('/home/'+''.join(mail))
		self.write(passwd)

