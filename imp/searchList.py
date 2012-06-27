import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
import json
from base import *
from core.db import *


class SearchListProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def sub_dict(somedict,*somekeys):
		return dict([(k,somedict[k]) for k in somekeys if k in somedict])
		
	def get(self):
		keyWords=self.get_arguments("keywords")
		if keyWords==[]:
			list1=self.dbManager.search_default_list(" ")
		else:
			list1=self.dbManager.search_default_list(keyWords)
		print list1
		mes="Sorry, no item found!"
		itemCount=len(list1)
		print list1, itemCount
		self.render("searchresults.html", sList = list1, count = itemCount, mes = mes)
		
		
	"""def post(self):
		keyWords=self.get_arguments("keywords")
		self.set_header("Content-Type", "text/plain")
		listDefaults=self.dbManager.search_default_list(keyWords)
		if not listDefaults:
			self.write("Wrong!")
			return None
		self.write("Success!")"""		
		
class SearchEventListProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		keyWords=self.get_arguments("keywords")
		if keyWords==[]:
			list1=self.dbManager.search_event_list(" ")
		else:
			list1=self.dbManager.search_event_list(keyWords)
		mes="Sorry, no item found!"
		itemCount=len(list1)
		print list1, itemCount
		self.render("searchresults.html", sList = list1, count = itemCount, mes = mes)
		
		
class SearchOfferListProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		keyWords=self.get_arguments("keywords")
		if keyWords==[]:
			list1=self.dbManager.search_offer_list_list(" ")
		else:
			list1=self.dbManager.search_event_list(keyWords)
		mes="Sorry, no item found!"
		itemCount=len(list1)
		print list1, itemCount
		self.render("searchresults.html", sList = list1, count = itemCount, mes = mes)
		

class SearchNeedListProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		keyWords=self.get_arguments("keywords")
		if keyWords==[]:
			list1=self.dbManager.search_need_list(" ")
		else:
			list1=self.dbManager.search_need_list(keyWords)
		mes="Sorry, no item found!"
		itemCount=len(list1)
		self.render("searchresults.html", sList = list1, count = itemCount, mes = mes)
		
class SearchUserListProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		list1=self.dbManager.search_user_list("e")
		itemCount=len(list1)
		mes=None
		if list1==None:
			mes="Sorry, no items found!"
		self.render("searchresults.html", sList = list1, count = itemCount, mes = mes)
		
