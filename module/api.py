import requests
import json

class httpreq(object):
    def __init__(self, url, arg=None, token=None):
        self.url        = url
        self.arg        = arg
        self.token      = token

    def getData_POST(self):
        self.headers = {
            'Content-Type'      :   "application/json",
            'Cache-Controller'  :   "no-cache"
        }
        response = requests.request("POST", self.url, data=self.arg, headers=self.headers)
        return response.text
        
    def send_data(self):
        self.headers = {
            'Authorization'     : "Bearer {token}".format(token=self.token),
            'Content-Type'      : "application/json",
        }
        response = requests.request("POST", self.url, data=self.arg, headers=self.headers)

        return response.text
        
    
    def getData_LIST(self):
        self.headers = {
            'Authorization'     : "Bearer {token}".format(token=self.arg),
        }
        response = requests.request("GET", self.url, headers=self.headers)

        return response.text

    def get_LIST(self):
        response = requests.request("GET", self.url)
        return response.text