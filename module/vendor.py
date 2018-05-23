from .api_settings import *
from .api import *

VendorObj        = VendorEndpoint()

url_register     = VendorObj.vendor_registration()
url_list         = VendorObj.vendor_list()
url_inactivelist = VendorObj.vendor_inactivelist()
url_activate     = VendorObj.vendor_activate()
url_deactivate   = VendorObj.vendor_deactivate()

class vendorModule(object):
    def __init__(self,arg,req=None,pre=None):
        self.arg = arg
        self.req = req
        self.pre = pre

    def registerValidate(self):
        http_req = httpreq(url_register, self.arg)
        data     = httpreq.send_data(http_req)
        
        return data

    def updateValidate(self):
        id = self.pre
        http_req = httpreq(VendorObj.vendor_update(id), self.arg, self.req)
        data     = httpreq.send_data(http_req)

        return data

    def profileValidate(self):
        id = self.req
        http_req = httpreq(VendorObj.vendor_profile(id), self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data

    def listValidate(self):
        http_req = httpreq(url_list, self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data

    def inactivelistValidate(self):
        http_req = httpreq(url_inactivelist, self.arg)
        data     = httpreq.getData_LIST(http_req)


        return data

    def activateValidate(self):
        http_req = httpreq(url_activate, self.arg, self.req)
        data     = httpreq.send_data(http_req)

        return data
        

    def deactivateValidate(self):
        http_req = httpreq(url_deactivate, self.arg, self.req)
        data     = httpreq.send_data(http_req)

        return data    
