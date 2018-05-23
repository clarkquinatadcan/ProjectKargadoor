from .api_settings import *
from .api import *

VehicleObj          = VehicleEndpoint()

url_list            = VehicleObj.vehicle_list()
url_deactivatelist  = VehicleObj.vehicle_deactivatelist()
url_entry           = VehicleObj.vehicle_entry()
url_reqdeactivate   = VehicleObj.vehicle_reqdeactivate()
url_deactivate      = VehicleObj.vehicle_deactivate()
url_activate        = VehicleObj.vehicle_activate()
url_single          = VehicleObj.vehicle_single()
url_search          = VehicleObj.vehicle_search()
url_asapsearch      = VehicleObj.vehicle_asapsearch()
url_vehicle_type    = VehicleObj.vehicle_type_list()

url_vehicle_type_create        = VehicleObj.vehicle_type_create()
url_vehicle_type_update        = VehicleObj.vehicle_type_update()
url_vehicle_type_activate      = VehicleObj.vehicle_type_activate()
url_vehicle_type_deactivate    = VehicleObj.vehicle_type_deactivate()

class vehicleModule(object):
    def __init__(self,arg=None,req=None,pre=None):
        self.arg = arg
        self.req = req
        self.pre = pre

    def listValidate(self):
        http_req = httpreq(url_list, self.arg)
        data     = httpreq.getData_LIST(http_req)
        
        return data

    def deactivatelistValidate(self):
        http_req = httpreq(url_deactivatelist, self.arg)
        data     = httpreq.getData_LIST(http_req)

        return data

    def entryValidate(self):
        http_req = httpreq(url_entry,self.arg,self.req)
        data     = httpreq.send_data(http_req)

        return data

    def reqdeactivateValidate(self):
        http_req = httpreq(url_reqdeactivate,self.arg,self.req)
        data     = httpreq.send_data(http_req)

        return data

    def activateValidate(self):
        http_req = httpreq(url_activate,self.arg,self.req)
        data     = httpreq.send_data(http_req)
        return data
        
        
        

    def deactivateValidate(self):
        http_req = httpreq(url_deactivate,self.arg,self.req)
        data     = httpreq.send_data(http_req)

        return data

    def updateValidate(self):
        id = self.pre
        http_req = httpreq(VehicleObj.vehicle_update(id),self.arg,self.req)
        data     = httpreq.send_data(http_req)

        return data

    def getimageValidate(self):
        image    = self.arg
        http_req = httpreq(VehicleObj.vehicle_getimage(image),self.req)
        data     = httpreq.getData_LIST(http_req)

        return data

    def geturlValidate(self):
        url = VehicleObj.vehicle_getimage()

        return url
    
    def singleValidate(self):
        id       = self.req
        http_req = httpreq(VehicleObj.vehicle_single(id), self.arg)
        data     = httpreq.getData_LIST(http_req)
        return data

    def searchValidate(self):
        print(url_search," = ",self.arg," = ",self.req)
        http_req = httpreq(url_search,self.arg,self.req)
        data     = httpreq.send_data(http_req)

        return data

    def asapsearchValidate(self):
        http_req = httpreq(url_asapsearch,self.arg,self.req)
        data     = httpreq.send_data(http_req)

        return data

    def v_typelistValidate(self):
        http_req = httpreq(url_vehicle_type)
        data     = httpreq.get_LIST(http_req)        
        return data

    def v_typeCreateValidate(self):
        http_req = httpreq(url_vehicle_type_create)
        data     = httpreq.get_LIST(http_req)        
        return data

    def v_typeUpdateValidate(self):
        http_req = httpreq(url_vehicle_type_update)
        data     = httpreq.get_LIST(http_req)        
        return data

    def v_typeActivateValidate(self):
        http_req = httpreq(url_vehicle_type_activate)
        data     = httpreq.get_LIST(http_req)        
        return data

    def v_typeDeactivateValidate(self):
        http_req = httpreq(url_vehicle_type_deactivate)
        data     = httpreq.get_LIST(http_req)        
        return data