import json
from collections import namedtuple
 
class userEntity:

    def __init__(self,codigo=None,user_name=None,user_mail=None,user_password=None):
        self.codigo = codigo
        self.user_name = user_name
        self.user_mail = user_mail
        self.user_password = user_password

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
    
    def requestToClass(self,request):
        data = request.get_json() 
        data = json.dumps(data)
        values = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        self.codigo = values.codigo
        self.user_name = values.user_name
        self.user_mail = values.user_mail
        self.user_password = values.user_password