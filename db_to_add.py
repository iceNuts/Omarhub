import tornado.database
from tornado.options import define, options
import unicodedata
from copy import copy

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="localhost:3306", help="imp host")
define("mysql_database", default="imp", help="imp db")
define("mysql_user", default="root", help="imp db user")
define("mysql_password", default="alpine", help="imp db passwd")

class dbmgr:

	def create_db_connection(self):
		self.db = tornado.database.Connection(
			host=options.mysql_host, database=options.mysql_database,
            		user=options.mysql_user, password=options.mysql_password)
	
	def drop_db_connection(self):
		self.db.close()
		
	def get_tags(tag_domain):
		self.create_db_connection()
		if not tag_domain:
			return None
		tags=self.db.get("SELECT name,followed From Tags WHERE tag_domain=%s",''.join(tag_domain))
		self.drop_db_connection()
		if not tags:
			print "Ooops"
			return None
		return tags
		
	def check_tag_followed(mail,name,tag_domain):
		self.create_db_connection()
		
		tag_id = self.db.get("select tag_id from Tags where name=%s and tag_domain=%s",''.join(name),''.join(tag_domain)) 
		tagfollowed=self.db.execute_rowcount("select * from UserTag where mail=%s and tag_id=%s",''.join(mail),int(tag_id["tag_id"]))
		return tagfollowed

	def get_user_profile_info_by_id(self, user_id, mode):
		"""Profile to fetch info, 0 all 1 part"""
		self.create_db_connection()
		if not user_id:
			return None
		if mode == 0:
				result = self.db.query("SELECT * FROM Users WHERE user_id = %s",user_id)
		elif mode == 1:
				result = self.db.query("SELECT user_id,first_name,last_name,avatar,location FROM Users WHERE user_id = %s", user_id)#untest
		self.drop_db_connection()
		print result
		if not result:
			print "Ooops"
			return None
		return result
		
