import tornado.web
import tornado.auth
from core.db import *
from base import *
from core.db import *

class AdminCreateUserHandler(BaseHandler):
	def get(self):
		self.render("create_user.html")
	def post(self):
		mail=''.join(self.get_arguments("email_address"))
		user_info=dict()
		user_info["first_name"]=''.join(self.get_arguments("first_name"))
		user_info["last_name"]=''.join(self.get_arguments("last_name"))
		role=self.get_argument("roles")
		print role
		if ''.join(role)=="admin":
			user_info["passwd"]=''.join(self.get_arguments("password"))
			result=self.dbManager.create_new_admin(mail,user_info)
		else :
			result=self.dbManager.create_new_user(mail,user_info)
		
		if result :
			self.write("Success")
		else :
			self.write("failed")
		#self.redirect("/admin/createuser")

#class AdminUserHandler(BaseHandler):
#	def get(self):
#		self.render("admin_users.html",user_id=0)
