from django.shortcuts import render
from django.views import View
import requests
import json
import jwt


class ApiConstant:
	def __init__(self):
            self.base       ='http://10.0.1.220'
        #     self.base       ='http://10.0.1.36'  #Live Server
        #     self.base       ='http://10.0.1.126'
        #     self.base       ='http://10.0.1.231'
        #     self.base       ='http://10.0.1.36'
        #     self.port	    = 2000       #Live Server Port
            self.api        ='api'
            self.version    ='v1.0'
        #     self.url        ="{base}:{port}/{api}/{ver}".format(base=self.base, port=self.port,api=self.api, ver=self.version) #Live Server IP
            self.url        ="{base}/{api}/{ver}".format(base=self.base,api=self.api, ver=self.version)

class UserEndpoint(ApiConstant):
	def user_login(self):
            self.endpoint = 'user/login' 
            return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

class VendorEndpoint(ApiConstant):
        def vendor_registration(self):
                self.endpoint = 'new/vendor'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vendor_update(self,ven_id = 0):
                self.ven_id = ven_id
                self.endpoint = 'vendor/update/'
                return "{url}/{endpoint}/{v_id}".format(url=self.url,endpoint=self.endpoint,v_id=self.ven_id)

        def vendor_list(self):
                self.endpoint = 'vendor/list'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)
        def vendor_inactivelist(self):
                self.endpoint = 'vendor/list/inactive'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vendor_profile(self,ven_id = 0):
                self.ven_id = ven_id
                self.endpoint = 'vendor/list/'
                return "{url}/{endpoint}/{v_id}".format(url=self.url,endpoint=self.endpoint,v_id=self.ven_id)

        def vendor_deactivate(self):
                self.endpoint = 'vendor/deactivate'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vendor_activate(self):
                self.endpoint = 'vendor/activate'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

class VehicleEndpoint(ApiConstant):
        def vehicle_list(self):
                self.endpoint = 'vehicle/list'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)
        
        def vehicle_deactivatelist(self):
                self.endpoint = 'vehicle/deactivate/list'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vehicle_entry(self):
                self.endpoint = 'new/vehicle/entry'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vehicle_update(self,v_id = 0):
                self.ven_id = v_id
                self.endpoint = 'vehicle/update/'
                return "{url}/{endpoint}/{v_id}".format(url=self.url,endpoint=self.endpoint,v_id=self.ven_id)

        def vehicle_reqdeactivate(self):
                self.endpoint = 'vehicle/req/deactivate'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vehicle_deactivate(self):
                self.endpoint = 'vehicle/app/deactivate'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vehicle_activate(self):
                self.endpoint = 'vehicle/activate'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vehicle_getimage(self, img=""):
                self.img = img
                self.endpoint = 'vehicle/get_image'
                return "{url}/{endpoint}/{image}".format(url=self.url,endpoint=self.endpoint,image=self.img)

        def vehicle_single(self, vcl_id = 0):
                self.vehicle_id = vcl_id
                self.endpoint = 'vehicle/single/search'
                return "{url}/{endpoint}/{vcl_id}".format(url=self.url,endpoint=self.endpoint,vcl_id=self.vehicle_id)

        def vehicle_search(self):
                self.endpoint = 'vehicle/search'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vehicle_asapsearch(self):
                self.endpoint = 'vehicle/asap/search'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vehicle_type_list(self):
                self.endpoint = 'vehicle_type/list'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vehicle_type_create(self):
                self.endpoint = 'vehicle_type/create'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)


        def vehicle_type_update(self):
                self.endpoint = 'vehicle_type/update'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)  

        def vehicle_type_activate(self):
                self.endpoint = 'vehicle_type/activate'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def vehicle_type_deactivate(self):
                self.endpoint = 'vehicle_type/deactivate'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint) 

class ClientEndPoint(ApiConstant):
        # client list
        def client_list(self):
                self.endpoint = 'client/active/list'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)
        
        def client_inactivelist(self):
                self.endpoint = 'client/inactive/list'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def client_single(self,client_id = 0):
                self.client_id = client_id
                self.endpoint = 'client/single/search'
                return "{url}/{endpoint}/{c_id}".format(url=self.url,endpoint=self.endpoint,c_id=self.client_id)

        def client_profile(self,client_id = 0):
                self.client_id = client_id
                self.endpoint = 'client/profile/search'
                return "{url}/{endpoint}/{c_id}".format(url=self.url,endpoint=self.endpoint,c_id=self.client_id)

        def client_activate(self,client_id = 0):
                self.client_id = client_id
                self.endpoint = 'client/activate'
                return "{url}/{endpoint}/{c_id}".format(url=self.url,endpoint=self.endpoint,c_id=self.client_id)

        def client_deactivate(self,client_id = 0):
                self.client_id = client_id
                self.endpoint = 'client/deactivate'
                return "{url}/{endpoint}/{c_id}".format(url=self.url,endpoint=self.endpoint,c_id=self.client_id)

        def client_entry(self):
                self.endpoint = 'client/entry'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def client_update(self):
                self.endpoint = 'client/update'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)


class BookingEndpoint(ApiConstant):
        def booking_entry(self):
                self.endpoint = 'booking/entry'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def booking_activelist(self):
                self.endpoint = 'booking/active/list'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def booking_currentlist(self):
                self.endpoint = 'booking/active/list/current'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def booking_futurelist(self):
                self.endpoint = 'booking/active/list/future'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)


        def booking_inactivelist(self):
                self.endpoint = 'booking/inactive/list'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def booking_update(self):
                self.endpoint = 'booking/update'
                return "{url}/{endpoint}".format(url=self.url,endpoint=self.endpoint)

        def booking_activate(self, booking_id = 0):
                self.id = booking_id
                self.endpoint = 'booking/activate'
                return "{url}/{endpoint}/{id}".format(url=self.url,endpoint=self.endpoint,id=self.id)

        def booking_deactivate(self, booking_id = 0):
                self.id = booking_id
                self.endpoint = 'booking/deactivate'
                return "{url}/{endpoint}/{id}".format(url=self.url,endpoint=self.endpoint,id=self.id)

        def booking_delete(self, booking_id = 0):
                self.id = booking_id
                self.endpoint = 'booking/delete'
                return "{url}/{endpoint}/{id}".format(url=self.url,endpoint=self.endpoint,id=self.id)

        def booking_single_search(self, booking_id = 0):
                self.id = booking_id
                self.endpoint = 'booking/search'
                return "{url}/{endpoint}/{id}".format(url=self.url,endpoint=self.endpoint,id=self.id)
