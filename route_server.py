from routes import Mapper  
from routes import middleware  
import webob.dec  
from wsgiref.simple_server import make_server  
  
class controller(object):  
    def __init__(self):  
        self.i = 1  
    def __call__(self):  
        print self.i  
    def search(self):  
        return "do search()"  
    def show(self):  
        return "do show()"  
    def index(self):  
        return "do index()"  
    def update(self):  
        return "do update()"  
    def delete(self):  
        return "do delete()"  
    def create(self):  
        return "do create()"  
    def create_many(self):  
        return "do create_many()"  
    def update_many(self):  
        return "do update_many()"  
    def list_many(self):  
        return "do list_many()"  
    def delete_many(self):  
        return "do delete_many()"  
class appclass(object):  
  
    def __init__(self):  
        a = controller()  
        map = Mapper()
        map.connect('/images',controller=a,  
                   action='search',  
                   conditions={'method':['GET']})  
        
        self.route = middleware.RoutesMiddleware(self.dispatch,map)  
 
    @webob.dec.wsgify  
    def __call__(self,req):  
        return self.route  
 
    @staticmethod  
    @webob.dec.wsgify  
    def dispatch(req):  
        match = req.environ['wsgiorg.routing_args'][1]  
        print "route match result is:",match  
        if not match:  
            return "fake url"  
  
        controller = match['controller']  
        action = match['action']  
        if hasattr(controller,action):  
            func = getattr(controller,action)  
            ret = func()  
            return ret  
        else:  
            return "has no action:%s" %action  
  
  
if __name__=="__main__":  
    app = appclass()  
    server = make_server('',8088,app)
    server.serve_forever()
