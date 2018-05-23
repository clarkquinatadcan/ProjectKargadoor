import json

from module.vehicle import *
from module.api_settings import *

class vehicle_controller(object):
    def __init__(self,arg,req=None,id=None):
        self.arg = arg
        self.req = req
        self.id = id

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
    
    def get_imageurl(self):
        data = vehicleModule(self)
        req  = vehicleModule.geturlValidate(data)
        return req

    def v_single(self):
        data        = vehicleModule(self.arg, self.req)
        res         = vehicleModule.singleValidate(data)
        return res

    def v_search(self):
        data        = vehicleModule(self.arg, self.req)
        res         = vehicleModule.searchValidate(data)
        return res

    def v_asapsearch(self):
        data        = vehicleModule(self.arg, self.req)
        res         = vehicleModule.asapsearchValidate(data)
        return res

    def v_type(self):
        data        = vehicleModule(self)
        res         = vehicleModule.v_typelistValidate(data)
        return res

    def v_type_create(self):
        data        = vehicleModule(self)
        res         = vehicleModule.v_typeCreateValidate(data)
        return res

    def v_type_update(self):
        data        = vehicleModule(self)
        res         = vehicleModule.v_typeUpdateValidate(data)
        return res

    def v_type_activate(self):
        data        = vehicleModule(self)
        res         = vehicleModule.v_typeActivateValidate(data)
        return res

    def v_type_deactivate(self):
        data        = vehicleModule(self)
        res         = vehicleModule.v_typeDeactivateValidate(data)
        return res
