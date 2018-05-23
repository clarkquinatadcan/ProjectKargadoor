import json

from module.vendor import *
from module.api_settings import *

class vendor_controller(object):
    def __init__(self,arg,req=None,id=None):
        self.arg = arg
        self.req = req
        self.id  = id
        
    # # ******************************
    #         # VENDOR 
    # # ******************************
    def get_list(self):
        vendor_list = vendorModule(self.arg)
        res         = vendorModule.listValidate(vendor_list)
        return res
    
    def inactive_list(self):
        vendor_list = vendorModule(self.arg)
        res         = vendorModule.inactivelistValidate(vendor_list)
        return res


    def single_list(self):
        vendor_list = vendorModule(self.arg,self.req)
        res         = vendorModule.profileValidate(vendor_list)
        return res

    def addvendor(self):
        data        = vendorModule(self.arg)
        send_req    = vendorModule.registerValidate(data)

        return send_req
    

    def updatevendor(self):
        data        = vendorModule(self.arg,self.req,self.id)
        send_update = vendorModule.updateValidate(data)
        print(send_update)
        return send_update

    def deactivate(self):
        data = vendorModule(self.arg, self.req)
        deactivate_req = vendorModule.deactivateValidate(data)

        return deactivate_req
    
    def activate(self):
        data = vendorModule(self.arg, self.req)
        activate_req = vendorModule.activateValidate(data)

        return activate_req
