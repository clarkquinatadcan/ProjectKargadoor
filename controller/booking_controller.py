import json

from module.booking import *
from module.api_settings import *

class booking_controller(object):
    def __init__(self,arg,req=None,id=None):
        self.arg = arg
        self.req = req
        self.id  = id
        
    
    def b_entry(self):
        data = bookingModule(self.arg, self.req)
        req = bookingModule.entryValidate(data)
        return req

    def b_activelist(self):
        data = bookingModule(self.arg)
        req = bookingModule.activelistValidate(data)

        return req

    def b_currentlist(self):
        data = bookingModule(self.arg)
        req = bookingModule.currentlistValidate(data)

        return req

    def b_futurelist(self):
        data = bookingModule(self.arg)
        req = bookingModule.futureValidate(data)

        return req

    def b_inactivelist(self):
        data = bookingModule(self.arg)
        req = bookingModule.inactivelistValidate(data)

        return req

    
    def booking_single(self):
        data = bookingModule(self.arg, self.req)
        req  = bookingModule.bookingDetails(data)
        return req