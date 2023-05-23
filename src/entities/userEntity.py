import json
from collections import namedtuple
 
class userEntity:

    def __init__(self,codigo=None,user_nickname=None,user_password=None,user_name=None,user_lastname=None,user_edad=None,user_genero=None,user_pais=None,user_mail=None):
        self.codigo = codigo
        self.user_nickname = user_nickname
        self.user_password = user_password
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.user_edad = user_edad
        self.user_genero = user_genero
        self.user_pais = user_pais
        self.user_mail = user_mail

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
    
    def requestToClass(self,request):
        data = request.get_json() 
        data = json.dumps(data)
        values = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        self.codigo = values.codigo
        self.user_nickname = values.user_nickname
        self.user_password = values.user_password
        self.user_name = values.user_name
        self.user_lastname = values.user_lastname
        self.user_edad = values.user_edad
        self.user_genero = values.user_genero
        self.user_pais = values.user_pais
        self.user_mail = values.user_mail