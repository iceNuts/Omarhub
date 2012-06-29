import tornado.database
from tornado.options import define, options
import unicodedata
from copy import copy
from operator import itemgetter, attrgetter
import urllib, hashlib

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
		
	def set_activate_events(self, mail, _id):
		"""Insert or update an activation events"""
		self.create_db_connection()
		number = self.db.get("SELECT _id FROM Activate_Events WHERE mail=%s", ''.join(mail))
		if number:
			self.db.execute("UPDATE Activate_Events SET _id=%s,create_time=%s WHERE mail=%s", ''.join(_id), "1", ''.join(mail))
		else:
			self.db.execute("INSERT INTO Activate_Events (mail,_id,create_time) VALUES(%s,%s,%s)", ''.join(mail),''.join(_id),'1')
		self.drop_db_connection()
	
	def get_activate_account(self, _id):
		"""Return mail address or None"""
		self.create_db_connection()
		date = self.db.get("SELECT create_time FROM Activate_Events WHERE _id=%s", ''.join(_id))
		if cmp(unicodedata.normalize('NFKD', date.create_time).encode('ascii','ignore'), "1") == 0:
			self.db.execute("UPDATE Activate_Events SET create_time=%s WHERE _id=%s", "0",''.join(_id))
			_mail = self.db.get("SELECT mail FROM Activate_Events WHERE _id=%s", ''.join(_id))
			self.drop_db_connection()
			return unicodedata.normalize('NFKD', _mail.mail).encode('ascii','ignore')
		else:
			self.drop_db_connection()
			return None
			
	def update_user_password(self, mail, passwd):
		"""Update user's password"""
		self.create_db_connection()
		self.db.execute("UPDATE Users SET passwd=%s WHERE mail=%s", ''.join(passwd), ''.join(mail))
		self.drop_db_connection()
	
	def check_user_exist(self, mail):
		"""Check if user exists"""
		self.create_db_connection()
		u = self.db.query("SELECT mail FROM Users WHERE mail=%s", ''.join(mail))
		self.drop_db_connection()
		if u:
			return 1
		else:
			return 0
			
	def check_user_activated(self, mail):
		"""Check if user activated"""
		self.create_db_connection()
		u = self.db.get("SELECT passwd FROM Users WHERE mail=%s", ''.join(mail))
		self.drop_db_connection()
		if not u.passwd:
			return 0
		if ''.join(u.passwd) != '':
			return 1
		else:
			return 0
			
	def check_activation_expired(self, _id):
		"""Check if expired"""
		self.create_db_connection()
		date = self.db.get("SELECT create_time FROM Activate_Events WHERE _id=%s", ''.join(_id))
		self.drop_db_connection()
		if not date:
			return 1
		if cmp(unicodedata.normalize('NFKD', date.create_time).encode('ascii','ignore'), "1") == 0:
			return 0
		else:
			return 1
		
	def checkAuth(self,usr_name, passwd,mode):
		#mode 0 for fellow,1 for admin
		self.create_db_connection()
		result = self.db.get("SELECT passwd FROM Users WHERE mail = %s", ''.join(usr_name))
		self.drop_db_connection()
		password = unicodedata.normalize('NFKD', result.passwd).encode('ascii','ignore')
		if not password or cmp(password, ''.join(passwd)) != 0:
			return 0
		elif cmp(password, ''.join(passwd)) == 0:
			return 1;
	
	def get_certain_activity(self, id, mode):
		"""Provide certain info to watch"""
	# 0 event 1 offer 2 need
		self.create_db_connection()
		if mode == 0:
			result = self.db.query("SELECT id,mail,title,location,description,work_field,target_population,start_date,end_date FROM Events WHERE id=%s", int(id))
		elif mode == 1:
			result = self.db.query("SELECT id,mail,title,location,description,target_population FROM Offers WHERE id=%s", int(id))
		elif mode == 2:
			result = self.db.query("SELECT id, mail,title,location,description,target_population FROM Needs WHERE id=%s", int(id))
		self.drop_db_connection()
		return result

	def get_event_list(self, mail, cursor, mode):
		"""for event provider,return dictionary, 0 personal, 1 recent, 2 most followed"""
		self.create_db_connection()
		if not cursor:
			return None
		strCursor = unicodedata.normalize('NFKD', cursor[0]).encode('ascii','ignore')
		if int(''.join(mode)) == 0:
				result = self.db.query("SELECT id, mail,title,location,description,work_field,target_population,start_date,end_date FROM Events WHERE mail = %s LIMIT %s,20", mail, int(strCursor))
		elif int(''.join(mode)) == 1:
				result = self.db.query("select id, mail,title,location,description,work_field,target_population,start_date,end_date FROM Events order by time DESC LIMIT %s,20", int(strCursor))
		elif int(''.join(mode)) == 2:
				result = self.db.query("select id, mail,title,location,description,work_field,target_population,start_date,end_date FROM Events order by followed DESC LIMIT %s,20", int(strCursor))
		self.drop_db_connection()
		print result
		if not result:
			print "Ooops"
			return None
		return result
        
	def get_offer_list(self,mail, cursor, mode):
		"""for offer provider,return dictionary, 0 personal, 1 recent, 2 most followed"""
		self.create_db_connection()
		if not cursor:
			return None
		strCursor = unicodedata.normalize('NFKD', cursor[0]).encode('ascii','ignore')
		if int(''.join(mode)) == 0:
			result = self.db.query("SELECT id, mail,title,location,description,target_population FROM Offers WHERE mail = %s LIMIT %s,20", mail, int(strCursor))
		elif int(''.join(mode)) == 1:
			result = self.db.query("SELECT id, mail,title,location,description,target_population FROM Offers order by time DESC LIMIT %s,20", int(strCursor))
		elif int(''.join(mode)) == 2:
			result = self.db.query("SELECT id, mail,title,location,description,target_population FROM Offers order by followed DESC LIMIT %s,20", int(strCursor))
		self.drop_db_connection()
		print result
		if not result:
			print "Ooops"
			return None
		return result
    
	def get_need_list(self,mail, cursor, mode):
		"""for need provider,return dictionary, 0 personal, 1 recent, 2 most followed"""
		self.create_db_connection()
		if not cursor:
			return None
		strCursor = unicodedata.normalize('NFKD', cursor[0]).encode('ascii','ignore')
		if int(''.join(mode)) == 0:
			result = self.db.query("SELECT id, mail,title,location,description,target_population FROM Needs WHERE mail = %s LIMIT %s,20", mail, int(strCursor))
		elif int(''.join(mode)) == 1:
			result = self.db.query("SELECT id, mail,title,location,description,target_population FROM Needs order by time DESC LIMIT %s,20", int(strCursor))
		elif int(''.join(mode)) == 2:
			result = self.db.query("SELECT id, mail,title,location,description,target_population FROM Needs order by followed DESC LIMIT %s,20", int(strCursor))
		self.drop_db_connection()
		print result
		if not result:
			print "Ooops"
			return None
		return result
		
	def get_recent_all_list(self,mail, cursor, mode):
		"""for all recent events provider,return dictionary, mode = 1 most recent 2 most followed"""
		self.create_db_connection()
		if not cursor:
			return None
		strCursor = unicodedata.normalize('NFKD', cursor[0]).encode('ascii','ignore')
		if int(''.join(mode)) == 0: # most recent
			result = self.db.query("SELECT _type,typeId,_from,_to FROM Recent_Events where _type <> 'Follow' order by _date DESC LIMIT %s,20", int(strCursor))
		elif int(''.join(mode)) == 1: # most followed
			result = self.db.query("SELECT _type,typeId,_from,_to FROM Recent_Events where _type <> 'Follow' order by followed DESC LIMIT %s,20", int(strCursor))
		elif int(''.join(mode)) == 2: # myself
			result = self.db.query("SELECT _type,typeId,_from,_to, _date FROM Recent_Events where mail_from = %s order by _date DESC LIMIT %s,20", mail,int(strCursor))	
		i = 0
		for item in result:
			type = unicodedata.normalize('NFKD', item['_type']).encode('ascii','ignore') # judge which table
			typeId = item['typeId'] # get id in that table
			author_mail = item['_from'] # get author's mail address
			if cmp(type,'Needs') == 0:
				need_item = self.db.query("SELECT id, mail,title,location,description,target_population FROM Needs where id=%s", int(typeId))
				item = dict(item.items() + need_item[0].items())
				author_item = self.get_user_profile_info(author_mail, 1)
				#Get if followed
				flag = self.db.query("select * from Follow_Status where mail_from=%s and mail_to=%s", mail, author_mail)
				number = self.get_follower_count(author_mail)
				if flag:
					author_item[0]['is_followed'] = '1'
				else:
					author_item[0]['is_followed'] = '0'
				#Get if followed
				print author_item
				item['author'] = copy(author_item[0])
			elif cmp(type,'Offers') == 0:
				offer_item = self.db.query("SELECT id, mail,title,location,description,target_population FROM Offers WHERE id = %s ", int(typeId))
				item = dict(item.items() + offer_item[0].items())
				author_item = self.get_user_profile_info(author_mail, 1)
				#Get if followed
				flag = self.db.query("select * from Follow_Status where mail_from=%s and mail_to=%s", mail, author_mail)
				number = self.get_follower_count(author_mail)
				if flag:
					author_item[0]['is_followed'] = '1'
				else:
					author_item[0]['is_followed'] = '0'
				#Get if followed
				item['author'] = copy(author_item[0])
			elif cmp(type,'Events') == 0:
				event_item = self.db.query("SELECT id, mail,title,location,description,work_field,target_population,start_date,end_date FROM Events WHERE id=%s", int(typeId))
				item = dict(item.items() + event_item[0].items())
				author_item = self.get_user_profile_info(author_mail, 1)
				#Get if followed
				flag = self.db.query("select * from Follow_Status where mail_from=%s and mail_to=%s", mail, author_mail)
				number = self.get_follower_count(author_mail)
				if flag:
					author_item[0]['is_followed'] = '1'
				else:
					author_item[0]['is_followed'] = '0'
				#Get if followed
				item['author'] = copy(author_item[0])
			elif cmp(type,'Follow') == 0:
				mail_from_item = self.get_user_profile_info(item[_from], 1)
				mail_to = self.get_user_profile_info(item[_to], 1)
				item = dict(item.items() + mail_from[0].items() + mail_to[0].itmes())
				item['_date'] = str(item['_date'])
			result[i] = item
			i = i + 1
									
		self.drop_db_connection()
		#####Todo#######
		print result
		if not result:
			print "Ooops"
			return None
		return result
	
	def get_user_profile_info(self, mail, mode):
		"""Profile to fetch info, 0 all 1 part"""
		self.create_db_connection()
		if not mail:
			return None
		if mode == 0:
				result = self.db.query("SELECT * FROM Users WHERE mail = %s", mail)
		elif mode == 1:
				result = self.db.query("SELECT user_id,first_name,last_name,avatar,location FROM Users WHERE mail = %s", mail)
		self.drop_db_connection()
		print result
		if not result:
			print "Ooops"
			return None
		return result
	
	def check_if_followed(self, mail_from, mail_to):
		#Get if followed
		flag = self.db.query("select * from Follow_Status where mail_from=%s and mail_to=%s", mail_from, mail_to)
		if flag:
			return 1
		else:
			return 0
		#Get if followed
		
	def get_user_profile_info_by_id(self, user_id, mode):
		"""Profile to fetch info, 0 all 1 part"""
		self.create_db_connection()
		if not user_id:
			return None
		if mode == 0:
				result = self.db.query("SELECT * FROM Users WHERE user_id = %s",user_id)
		elif mode == 1:
				result = self.db.query("SELECT user_id,first_name,last_name,avatar,location FROM Users WHERE user_id = %s", user_id)
				
		self.drop_db_connection()
		print result
		if not result:
			print "Ooops"
			return None
		return result

	def get_all_users(self, mail,cursor):
		"""Return all people info sorted by time"""
		if not cursor:
			return None
		self.create_db_connection()
		strCursor = unicodedata.normalize('NFKD', cursor[0]).encode('ascii','ignore')	
		mylist = self.db.query("select user_id, first_name, last_name, avatar, location from Users where passwd <> '' order by register_date desc limit %s,20", int(strCursor))
		i = 0
		result = list(mylist)
		for item in mylist:
			m_mail = self.db.query("select mail from Users where user_id=%s", item['user_id'])
			flag = self.db.query("select * from Follow_Status where mail_from=%s and mail_to=%s", mail, m_mail[0]['mail'])
			number = self.get_follower_count(m_mail)
			if flag:
				item['is_followed'] = '1'
			else:
				item['is_followed'] = '0'
			item['follower_number'] = number
			x = dict()
			x["author"] = item
			result[i] = x
			i = i + 1
		self.drop_db_connection()
		return result
	
	def follow_people_action(self, mail, user_id):
		"""Add a follow event in Follow_Status"""
		self.create_db_connection()
		id = unicodedata.normalize('NFKD', user_id).encode('ascii','ignore')
		m_mail = self.db.query("select mail from Users where user_id=%s", int(id))
		flag = self.check_if_followed(mail, m_mail[0]['mail'])
		if not flag and cmp(mail,m_mail[0]['mail']) != 0:
			self.db.execute("insert into Follow_Status (mail_from,mail_to) values(%s, %s)", mail, m_mail[0]['mail'])
			self.db.execute("insert into Recent_Events (_type, _from, _to) values (%s,%s,%s)", "Follow", mail, m_mail['0']['mail'])
		self.drop_db_connection()
	
	def unfollow_people_action(self, mail, user_id):
		"""Unfollow peoplem, simply delete a row"""
		self.create_db_connection()
		id = unicodedata.normalize('NFKD', user_id).encode('ascii','ignore')
		m_mail = self.db.query("select mail from Users where user_id=%s", int(id))
		flag = self.check_if_followed(mail, m_mail[0]['mail'])
		if flag:
			self.db.execute("delete from Follow_Status where mail_from=%s and mail_to=%s", mail, m_mail[0]['mail'])
		self.drop_db_connection()
	
	def get_user_organization(self, mail):
		"""Return organization info"""
		self.create_db_connection()
		if not mail:
			return None
		org_id = self.db.get("SELECT org_id FROM Users Where mail=%s", mail)
  		print org_id
		result = self.db.query("SELECT * FROM Organization WHERE org_id=%s", int(org_id['org_id']))
		self.drop_db_connection()
		print result
		if not result:
			print "Ooops"
			return None
		return result

	def set_user_profile_info(self, mail, info):
		"""Set profile Info"""
		self.create_db_connection()
		for item in info:
			sqlstatement=' '.join(["update Users set",item])
			entry = self.db.execute(sqlstatement+"=%s where mail=%s", ''.join(info[item]),mail)
		self.drop_db_connection()
		print entry
			
	def get_follower_count(self, mail):
		"""Get the number of followers"""
		self.create_db_connection()
		if not mail:
			return None
		print type(mail)
		if type(mail) is str:
			result = self.db.query("select * from Follow_Status where mail_to=%s", ''.join(mail))
		elif type(mail) is list:
			result = self.db.query("select * from Follow_Status where mail_to=%s", mail[0]['mail'])
		elif type(mail) is unicode:
			result = self.db.query("select * from Follow_Status where mail_to=%s", mail)
		self.drop_db_connection()
		return len(result)
			
	def get_following_count(self, mail):
		"""Get the number of following"""
		self.create_db_connection()
		if not mail:
			return None
		result = self.db.query("select * from Follow_Status where mail_from=%s", ''.join(mail))
		self.drop_db_connection()
		return len(result)
		
	def get_follower_brief_list(self, mail,num):
		"""Get the a brief list of followers"""
		self.create_db_connection()
		if not mail:
			return None
		result = self.db.query("select u.user_id,u.first_name,u.last_name,u.avatar from Follow_Status f,Users u where f.mail_to=%s and f.mail_from=u.mail limit 0,%s", mail,num)
		self.drop_db_connection()
		return result

	def create_new_activity(self, mail, info, mode):
		"""Insert into tables for new record"""
		self.create_db_connection()
		if mode == 0: # Event
			entry = self.db.execute("insert into Events (mail, title, description, location, work_field, target_population, start_date, end_date) values (%s, %s, %s, %s, %s, %s, %s, %s)", mail, info['title'], info['description'], info['location'], info['work_field'], info['target_population'], info['start_date'], info['end_date'])
			self.db.execute("insert into Recent_Events (_type, typeId, _from) values (%s,%s,%s)", "Events", entry, mail)
		elif mode == 1: # offer
			entry = self.db.execute("insert into Offers (mail, title, description, location, target_population) values (%s, %s, %s, %s, %s)", mail, info['title'], info['description'], info['location'], info['target_population'])
			self.db.execute("insert into Recent_Events (_type, typeId, _from) values (%s,%s,%s)", "Offers", entry, mail)
		elif mode == 2: # need
			entry = self.db.execute("insert into Needs (mail, title, description, location, target_population) values (%s, %s, %s, %s, %s)", mail, info['title'], info['description'], info['location'], info['target_population'])
			self.db.execute("insert into Recent_Events (_type, typeId, _from) values (%s,%s,%s)", "Needs", entry, mail)
		self.drop_db_connection()
		return entry
			
	def create_new_user(self, mail, info):
		"""Create a unique id"""
		self.create_db_connection()
		
		email = mail
		default = "http://ww2.sinaimg.cn/large/675f2d7fjw1due79vjemjj.jpg"
		size = 100
		
		gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
		gravatar_url += urllib.urlencode({'d':default, 's':str(size)})

		exist=self.db.execute_rowcount("select * from Users where mail=%s",mail)
		if exist :
			return 0
		self.db.execute("insert into Users (mail) values (%s)", mail)
		for item in info:
			sqlstatement=' '.join(["update Users set",item])
			entry = self.db.execute(sqlstatement+"=%s where mail=%s", ''.join(info[item]),mail)
		self.db.execute("update Users set avatar=%s where mail=%s", gravatar_url, mail)
		self.drop_db_connection()
		return 1
		
	def create_new_admin(self, mail, info):
		"""Create a unique id"""
		self.create_db_connection()
		exist=self.db.execute_rowcount("select * from Admins where mail=%s",mail)
		if exist :
			print "This is illogical"
			return 0
		self.db.execute("insert into Admins (mail) values (%s)", mail)
		for item in info:
			sqlstatement=' '.join(["update Admins set",item])
			entry = self.db.execute(sqlstatement+"=%s where mail=%s", ''.join(info[item]),mail)
		self.drop_db_connection()
		return 1


	def delete_a_user(mail):
		"""Lack of Update Users"""
		create_db_connection(self)
		result = self.db.execute("DELETE FROM Users WHERE mail=%s", mail)
		drop_db_connection(self)					
		if result:
			return 1
		else:
			return 0

	def insert_user_avatar(user_id ,avatar):
		"""Use avatar's name to remember a url for resource"""
		create_db_connection(self)
		result = self.db.execute("UPDATE Users SET avatar = %s WHERE user_id = %s", "/resources/avatars/"+avatar ,user_id)
		drop_db_connection(self)
		if result:
			return 1
		return 0
		
	
	def insert_user_orgnization(_id, name, acronym, found_date, site_url, _type, numberOfemployees, phoneNumber, country_code):
		"""Insert the organization info to an user"""
		create_db_connection(self)
		number = (self.db.excute("SELECT COUNT(*) FROM Orgnization", None)) + 1
		usr = self.db.excute("UPDATE Users SET org_id = %s WHERE user_id = %s", number, _id)
		org = self.db.excute("INSERT INTO Organization (org_id, name, acronym, found_date, site_url, _type, numberOfemployees, phoneNumber, country_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", number, name, acronym, found_date, site_url, _type, numberOfemployees, phoneNumber, country_code)
		drop_db_connection(self)
		if org:
			return 1
		return 0
	
	def update_active_users(_id):
		"""Update active users list, replace the outdated with the latest"""
		create_db_connection(self)
		result = self.db.execute("UPDATE Active_Users SET time = %s WHERE user_id = %s", UTC_TIMESTAMP(), _id)
		if not result:
			result = self.db.excute("INSERT INTO Active_Uers (user_id, time) VALUES (%s, UTC_TIMESTAMP())", _id)
		drop_db_connection(self)
		if result:
			return 1
		return 0
	def update_follow_status(_from, _to, status):
		create_db_connection(self)
		if status:
			result = self.db.excute("INSERT INTO Follow_Status (mail_from, mail_to, time) VALUES (%s, %s,UTC_TIMESTAMP())", _from, _to)
		else:
			result = self.db.execute("DELETE FROM Follow_Status WHERE mail_from=%s and mail_to=%s", _from, _to)
		drop_db_connection(self)
		if result:
			return 1
		else:	
			return 0

	def update_recent_events(_type, _from, _to):
		create_db_connection(self)
		number = self.db.execute("SELECT COUNT(*) FROM Recent_Events")
		result = self.db.execute("INSERT INTO Recent_Events (id, _type, _date, _from, _to) VALUES(%s, %s, UTC_TIMESTAMP(),%s,%s)", number+1,_type,_from,_to)
		drop_db_connection(self)
		if result:
			return 1
		else:
			return 0
		
	def get_tags(self,tag_domain):
		self.create_db_connection()
		if not tag_domain:
			return None
		tags=self.db.query("SELECT tag_id,name,followed From Tags WHERE tag_domain=%s",''.join(tag_domain))
		self.drop_db_connection()
		if not tags:
			print "Ooops"
			return None
		return tags
		
	def set_follow_tags(self,tag_id,mail,mode):
		#mode 0 for follow,mode 1 for unfollow
		self.create_db_connection()
		if not mail or not tag_id:
			return 0
		tagfollowed=self.db.execute_rowcount("select * from UserTag where user_mail=%s and tag_id=%s",''.join(mail),tag_id)
		if mode != tagfollowed:
			return 0
		if mode==0 :
			result=self.db.execute("INSERT INTO UserTag (tag_id,user_mail) VALUES(%s,%s)",tag_id,''.join(mail))
		else:
			result=self.db.execute("DELETE FROM UserTag WHERE user_mail=%s and tag_id=%s",''.join(mail),tag_id)
		
		return 1
		
	def check_tag_followed(self,mail,name,tag_domain):
		self.create_db_connection()
		
		tag_id = self.db.get("select tag_id from Tags where name=%s and tag_domain=%s",''.join(name),''.join(tag_domain)) 
		if not tag_id:
			return 0
		tagfollowed=self.db.execute_rowcount("select * from UserTag where user_mail=%s and tag_id=%s",''.join(mail),int(tag_id["tag_id"]))
		return tagfollowed
		    
	def search_default_list(self,keywords):
		self.create_db_connection()
		resultE = self.search_event_list(keywords)
		resultO = self.search_offer_list(keywords)
		resultN = self.search_need_list(keywords)
		result = resultE + resultO + resultN
		result1 = sorted(result, key = attrgetter('time'), reverse = True)
		return result1
	
	def search_event_list(self,keywords):
		self.create_db_connection()
		if not keywords:
			return None
		result = self.db.query("SELECT u.first_name, u.last_name, e.id, e.title, e.description, e.time FROM Events e, Users u WHERE e.mail=u.mail && (e.title LIKE '%%"+keywords+"%%' OR e.description LIKE '%%"+keywords+"%%' OR u.first_name LIKE '%%"+keywords+"%%' OR u.last_name LIKE '%%"+keywords+"%%' )" )
		self.drop_db_connection()
		return result
		
	def search_offer_list(self,keywords):
		self.create_db_connection()
		if not keywords:
			return None
		result = self.db.query("SELECT u.first_name, u.last_name, o.id, o.title, o.description, o.time FROM Offers o, Users u WHERE o.mail=u.mail && (o.title LIKE '%%"+keywords+"%%' OR o.description LIKE '%%"+keywords+"%%' OR u.first_name LIKE '%%"+keywords+"%%' OR u.last_name LIKE '%%"+keywords+"%%' )" )
		self.drop_db_connection()
		return result
        
	def search_need_list(self,keywords):
		self.create_db_connection()
		if not keywords:
			return None
		result = self.db.query("SELECT u.first_name, u.last_name, n.id, n.title, n.description, n.time FROM Needs n, Users u WHERE n.mail=u.mail && (n.title LIKE '%%"+keywords+"%%' OR n.description LIKE '%%"+keywords+"%%' OR u.first_name LIKE '%%"+keywords+"%%' OR u.last_name LIKE '%%"+keywords+"%%' )" )
		self.drop_db_connection()
		return result
	
	def search_user_list(self,keywords):
		self.create_db_connection()
		if not keywords:
			return None
		resultE = self.db.query("SELECT u.first_name, u.last_name, e.id, e.title, e.description, e.time FROM Events e, Users u WHERE e.mail=u.mail && (u.first_name LIKE '%%"+keywords+"%%' OR u.last_name LIKE '%%"+keywords+"%%' )" )
		resultO = self.db.query("SELECT u.first_name, u.last_name, o.id, o.title, o.description, o.time FROM Offers o, Users u WHERE o.mail=u.mail && (u.first_name LIKE '%%"+keywords+"%%' OR u.last_name LIKE '%%"+keywords+"%%' )" )
		resultN = self.db.query("SELECT u.first_name, u.last_name, n.id, n.title, n.description, n.time FROM Needs n, Users u WHERE n.mail=u.mail && (u.first_name LIKE '%%"+keywords+"%%' OR u.last_name LIKE '%%"+keywords+"%%' )" )
		result = resultE + resultO + resultN
		result1 = sorted(result, key = attrgetter('time'), reverse = True)
		self.drop_db_connection()
		return result1
		
			









			








		
