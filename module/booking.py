from .api_settings import *
from .api import *

BookingObj       = BookingEndpoint()

url_entry        = BookingObj.booking_entry()
url_activelist   = BookingObj.booking_activelist()
url_list_current = BookingObj.booking_currentlist()
url_list_future  = BookingObj.booking_futurelist()
url_inactivelist = BookingObj.booking_inactivelist()
url_update       = BookingObj.booking_update()



class bookingModule(object):
    def __init__(self,arg,req=None,pre=None):
        self.arg = arg
        self.req = req
        self.pre = pre

    def entryValidate(self):
        http_req = httpreq(url_entry, self.arg, self.req)
        data     = httpreq.send_data(http_req)

        return data

    def activelistValidate(self):
        http_req = httpreq(url_activelist, self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data

    def currentlistValidate(self):
        http_req = httpreq(url_list_current, self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data
    
    def futureValidate(self):
        http_req = httpreq(url_list_future, self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data
    
    def inactivelistValidate(self):
        http_req = httpreq(url_inactivelist, self.arg)
        data     = httpreq.getData_LIST(http_req)
        return data

    def bookingDetails(self):
        id = self.req
        http_req = httpreq(BookingObj.booking_single_search(id), self.arg)
        data     = httpreq.getData_LIST(http_req)
        return data

    def bookingActivation(self):
        id = self.req
        http_req = httpreq(BookingObj.booking_activate(id), self.arg)
        data     = httpreq.getData_LIST(http_req)
        return data

