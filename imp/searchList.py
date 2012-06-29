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
			keywords=str(keyWords[0]).split(" ")
			list1=[]
			for i in keywords:
				list2=self.dbManager.search_default_list(i)
				list3=[a for a in list2 if a not in list1]
				list1+=list3
		print list1
		itemcount=len(list1)
		self.render("searchresults.html", sList=list1,count=itemcount,key=keyWords)
		
class SearchAllListProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def sub_dict(somedict,*somekeys):
		return dict([(k,somedict[k]) for k in somekeys if k in somedict])
		
	def get(self):
		keyWords=self.get_arguments("keywords")
		if keyWords==[]:
			list1=self.dbManager.search_default_list(" ")
		else:
			keywords=str(keyWords[0]).split(" ")
			list1=[]
			for i in keywords:
				list2=self.dbManager.search_default_list(i)
				list3=[a for a in list2 if a not in list1]
				list1+=list3
		list1=json.dumps(list1)
		self.write(list1)
		
class SearchEventListProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		keyWords=self.get_arguments("keywords")
		if keyWords==[]:
			list1=self.dbManager.search_event_list(" ")
		else:
			keywords=str(keyWords[0]).split(" ")
			list1=[]
			for i in keywords:
				list2=self.dbManager.search_event_list(i)
				list3=[a for a in list2 if a not in list1]
				list1+=list3
		list1=json.dumps(list1)
		self.write(list1)
		
		
class SearchOfferListProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		keyWords=self.get_arguments("keywords")
		if keyWords==[]:
			list1=self.dbManager.search_offer_list(" ")
		else:
			keywords=str(keyWords[0]).split(" ")
			list1=[]
			for i in keywords:
				list2=self.dbManager.search_offer_list(i)
				list3=[a for a in list2 if a not in list1]
				list1+=list3
		list1=json.dumps(list1)
		self.write(list1)
		

class SearchNeedListProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		keyWords=self.get_arguments("keywords")
		if keyWords==[]:
			list1=self.dbManager.search_need_list(" ")
		else:
			keywords=str(keyWords[0]).split(" ")
			list1=[]
			for i in keywords:
				list2=self.dbManager.search_need_list(i)
				list3=[a for a in list2 if a not in list1]
				list1+=list3
		list1=json.dumps(list1)
		self.write(list1)
		
class SearchUserListProvider(BaseHandler):
	def initialize(self):
		self.dbManager = dbmgr()
		
	def get(self):
		keyWords=self.get_arguments("keywords")
		if keyWords==[]:
			list1=self.dbManager.search_user_list(" ")
		else:
			keywords=str(keyWords[0]).split(" ")
			list1=[]
			for i in keywords:
				list2=self.dbManager.search_user_list(i)
				list3=[a for a in list2 if a not in list1]
				list1+=list3
		list1=json.dumps(list1)
		self.write(list1)
		
