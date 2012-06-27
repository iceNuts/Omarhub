import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
from login import *
from base import *
from home import *
from profile import *
from activate import *
from loginUsername import *
from content import *
from profile import *
from activitycreator import *
from activityshow import *

class MainHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.redirect("/auth/login")
			return
		else:
			self.redirect("/home")
			return

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", MainHandler),
			(r"/auth/login", LoginHandler),
			(r"/home", HomeHandler),
			(r"/auth/activate", ActivateHandler),
			(r"/auth/activate/([\S]+)",PasswdSettingHandler),
			(r"/auth/login/verify/username", LoginUsernameHandler),
			(r"/auth/login/forgetpasswd", ActivateHandler),
            (r"/content/provider/getevents", EventProvider),
            (r"/content/provider/getoffers", OfferProvider),
            (r"/content/provider/getneeds", NeedProvider),
            (r"/content/provider/getrecentall", RecentallProvider),
			(r"/profile/([\d]+)",ProfileHandler),
			(r"/profile/editMyProfile", ProfileEditHandler),
			(r"/auth/logout", LogoutHandler),
			(r"/create", CreateHandler),
			(r"/event/create", EventCreateHandler),
			(r"/offer/create", OfferCreateHandler),
			(r"/need/create", NeedCreateHandler),
			(r"/event/([\d]+)", EventShowHandler),
			(r"/offer/([\d]+)", OfferShowHandler),
			(r"/need/([\d]+)", NeedShowHandler)
			]
		settings = dict(
			template_path=os.path.join(os.path.dirname(__file__), "template"),
			static_path=os.path.join(os.path.dirname(__file__), "static"),
			login_url="/auth/login",
			cookie_secret="94s2ss5swv18xdwsdfeewrdde9xtacsxse//vr0",
			debug = True
		)
		tornado.web.Application.__init__(self ,handlers, **settings)
		

def main():
	tornado.options.parse_command_line()
  	http_server = tornado.httpserver.HTTPServer(Application())
 	http_server.listen(8888)
 	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()







