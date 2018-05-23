import json

from module.user import *
from module.api_settings import *

class controller(object):
    def __init__(self,arg,req=None,id=None):
        self.arg = arg
        self.req = req
        self.id  = id
        
    def login(self):
        loginModule = userModule(self.arg)
        res         = userModule.loginValidate(loginModule)
        return res