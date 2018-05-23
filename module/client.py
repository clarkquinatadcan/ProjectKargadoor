from .api_settings import *
from .api import *


ClientObj     = ClientEndPoint()

url_entry         = ClientObj.client_entry()
url_update        = ClientObj.client_update()
url_activelist    = ClientObj.client_list()
url_inactivelist  = ClientObj.client_inactivelist()



class clientModule(object):
    def __init__(self,arg,req=None,pre=None):
        self.arg = arg
        self.req = req
        self.pre = pre

    def entryValidate(self):
        http_req = httpreq(url_entry, self.arg, self.req)
        data     = httpreq.send_data(http_req)
        
        return data

    def updateValidate(self):
        http_req = httpreq(url_update, self.arg, self.req)
        data     = httpreq.send_data(http_req)
        
        return data
    
    def activeValidate(self):
        http_req = httpreq(url_activelist, self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data

    def inactiveValidate(self):
        http_req = httpreq(url_inactivelist, self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data

    def activateValidate(self):
        id = self.req
        http_req = httpreq(ClientObj.client_activate(id), self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data

    def deactivateValidate(self):
        id = self.req
        http_req = httpreq(ClientObj.client_deactivate(id), self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data

    def singlesearchValidate(self):
        id = self.req
        http_req = httpreq(ClientObj.client_single(id), self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data
    
    def singleprofileValidate(self):
        id = self.req
        http_req = httpreq(ClientObj.client_profile(id), self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data