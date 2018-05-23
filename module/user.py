import json, jwt

from .api_settings import *
from .api import *

UserObj   = UserEndpoint()

url_login = UserObj.user_login()

class userModule(object):
    def __init__(self,arg):
        self.arg = arg

    def loginValidate(self):
        log    = json.dumps(self.arg)

        http_req = httpreq(url_login, log)
        data     = httpreq.getData_POST(http_req)
        decode   = jwt.decode(data, verify=False)

        return data