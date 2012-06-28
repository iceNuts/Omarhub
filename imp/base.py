import tornado.web
import tornado.auth

class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
        	return self.get_secure_cookie("user")
        	
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get_current_user_id(self):
		if not self.current_user:
			self.redirect("/auth/login")
		mail=self.current_user
		userlist_me=self.dbManager.get_user_profile_info(mail,0)
		user_me=userlist_me[0]
		my_user_id=str(user_me["user_id"])
		return my_user_id
		
	def get_user_info(self,mail):
		resultlist=self.dbManager.get_user_profile_info(mail,0)
		result=resultlist[0]
		user_info=dict()
		user_info["user_id"]=result["user_id"]
		user_info["user_name"]=' '.join([result["first_name"],result["last_name"]])
		user_info["avatar"]=result["avatar"]
		
