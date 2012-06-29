import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import json
from base import *
from core.db import *
from copy import copy

#Return json 

class EventProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	
	def post(self):
		if not self.current_user:
			return None
		cursor = self.get_arguments("cursor")
		mode = self.get_arguments("mode")
		mail = self.current_user
		id = self.current_user
		list = self.dbManager.get_event_list(id, cursor, mode)
		userlist_me=self.dbManager.get_user_profile_info(mail,0)
		user_me=userlist_me[0]
		my_user_id=user_me["user_id"]
		i = 0
		if not list:
			return list()
		for item in list:
			item['my_user_id'] = my_user_id
			list[i] = item
			i = i + 1
		for item in list:
			m_mail = item['mail']
			tmp_list = self.dbManager.get_user_profile_info(m_mail, 1)
			tmp_list[0]["is_followed"] = str(self.dbManager.check_if_followed(mail, m_mail))
			item['author'] = copy(tmp_list[0])
		self.write(json.dumps(list))


class OfferProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()

	def post(self):
		if not self.current_user:
			return None
		cursor = self.get_arguments("cursor")
		mode = self.get_arguments("mode")
		id = self.current_user
		#print id
		list = self.dbManager.get_offer_list(id, cursor, mode)
		i = 0
		mail=self.current_user
		userlist_me=self.dbManager.get_user_profile_info(mail,0)
		user_me=userlist_me[0]
		my_user_id=user_me["user_id"]	
		if not list:
			return list()
		for item in list:
			item['my_user_id'] = my_user_id
			list[i] = item
			i = i + 1
		for item in list:
			m_mail = item['mail']
			tmp_list = self.dbManager.get_user_profile_info(m_mail, 1)
			tmp_list[0]["is_followed"] = str(self.dbManager.check_if_followed(mail, m_mail))
			item['author'] = copy(tmp_list[0])
		self.write(json.dumps(list))


class NeedProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	
	def post(self):
		if not self.current_user:
			return None
		cursor = self.get_arguments("cursor")
		mode = self.get_arguments("mode")
		id = self.current_user
		#print id/
		list = self.dbManager.get_need_list(id, cursor, mode)
		i = 0
		mail=self.current_user
		userlist_me=self.dbManager.get_user_profile_info(mail,0)
		user_me=userlist_me[0]
		my_user_id=user_me["user_id"]	
		if not list:
			return list()
		for item in list:
			item['my_user_id'] = my_user_id
			list[i] = item
			i = i + 1
		for item in list:
			m_mail = item['mail']
			tmp_list = self.dbManager.get_user_profile_info(m_mail, 1)
			tmp_list[0]["is_followed"] = str(self.dbManager.check_if_followed(mail, m_mail))
			item['author'] = copy(tmp_list[0])
		self.write(json.dumps(list))

class RecentallProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def post(self):
		if not self.current_user:
			return None
		cursor = self.get_arguments("cursor") 
				
		mode = self.get_arguments("mode")
		id = self.current_user
		#print id
		list = self.dbManager.get_recent_all_list(id, cursor, mode)
		i = 0
		mail=self.current_user
		userlist_me=self.dbManager.get_user_profile_info(mail,0)
		user_me=userlist_me[0]
		my_user_id=user_me["user_id"]	
		if not list:
			return list()
		for item in list:
			item['my_user_id'] = my_user_id
			list[i] = item
			i = i + 1
		self.write(json.dumps(list))
	
class PeopleProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
	def post(self):
		if not self.current_user:
			return None
		cursor = self.get_arguments("cursor")
		list = self.dbManager.get_all_users(self.current_user,cursor)
		i = 0
		mail=self.current_user
		userlist_me=self.dbManager.get_user_profile_info(mail,0)
		user_me=userlist_me[0]
		my_user_id=user_me["user_id"]	
		if not list:
			return list()
		for item in list:
			item['_type'] = "People"
			item['my_user_id'] = my_user_id
			list[i] = item
			i = i + 1
		self.write(json.dumps(list))









