import json
from module.user import *
from module.booking import *
from module.client import *
from module.vendor import *
from module.vehicle import *
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

    
    # # ******************************
    #         # VEHICLE 
    # # ******************************

    def v_list(self):
        data = vehicleModule(self.arg)
        req  = vehicleModule.listValidate(data)

        return req
    
    def v_deactlist(self):
        data = vehicleModule(self.arg)
        req  = vehicleModule.deactivatelistValidate(data)
        return req

    def v_entry(self):
        data = vehicleModule(self.arg, self.req)
        req  = vehicleModule.entryValidate(data)

        return req

    def v_update(self):
        data = vehicleModule(self.arg, self.req, self.id)
        req  = vehicleModule.updateValidate(data)      
        return req
    
    def v_activate(self):
        data = vehicleModule(self.arg, self.req)
        req = vehicleModule.activateValidate(data)

        return req
    
    def v_deactivate(self):
        data = vehicleModule(self.arg, self.req)
        req  = vehicleModule.deactivateValidate(data)      
        return req
    
    def v_reqdeactivate(self):
        data = vehicleModule(self.arg, self.req)
        req  = vehicleModule.reqdeactivateValidate(data)
        return req
    
    def v_getimage(self):
        data = vehicleModule(self.arg, self.req)
        req  = vehicleModule.getimageValidate(data)
        return req

    def v_single(self):
        data        = vehicleModule(self.arg, self.req)
        res         = vehicleModule.getVehicle(data)
        return res




    # ******************************
    #           CLIENT             #
    # ******************************

    def c_single(self):
        data        = clientModule(self.arg, self.req)
        res         = clientModule.getClient(data)
        return res