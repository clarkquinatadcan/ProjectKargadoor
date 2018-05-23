import json

from module.client import *
from module.api_settings import *

class client_controller(object):
    def __init__(self,arg,req=None,id=None):
        self.arg = arg
        self.req = req
        self.id = id
    
    def client_entry(self):
        data    = clientModule(self.arg,self.req)
        req     = clientModule.entryValidate(data)
        return req

    def client_update(self):
        data    = clientModule(self.arg,self.req)
        req     = clientModule.updateValidate(data)
        return req    

    def client_activelist(self):
        data    = clientModule(self.arg)
        req     = clientModule.activeValidate(data)
        return req

    def client_inactivelist(self):
        data    = clientModule(self.arg)
        req     = clientModule.inactiveValidate(data)
        return req
    
    def client_activate(self):
        data    = clientModule(self.arg)
        req     = clientModule.activateValidate(data)
        return req

    def client_deactivate(self):
        data    = clientModule(self.arg)
        req     = clientModule.deactivateValidate(data)
        return req  

    def client_single(self):
        data    = clientModule(self.arg,self.req)
        req     = clientModule.singlesearchValidate(data)
        return req

    def client_profile(self):
        data    = clientModule(self.arg,self.req)
        req     = clientModule.singleprofileValidate(data)
        return req