from src.models.userModel import userModel
from src.entities.responseEntity import responseEntity
from src.controllers.responseController import responseController
from src.entities.userEntity import userEntity

class userController(responseController):

    def get_users(self):
        _message = None
        _status = self.interruption
        _data= None
        try:
            _model = userModel()
            _data = _model.get_users()
            print(_data)
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
            print('error: '+ str(e))
        return responseEntity(_status,_message,_data).toJSON()
    
    def add_users(self,request):
        _message = None
        _status = self.interruption
        _data= None
        try:
            _entity = userEntity()
            _entity.requestToClass(request)
            _model = userModel()
            _data = _model.add_users(_entity)
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
            print('error: '+ str(e))
        return responseEntity(_status,_message,_data).toJSON()

    def update_users(self,request):
        _message = None
        _status = self.interruption
        _data= None
        try:
            _entity = userEntity()
            _entity.requestToClass(request)
            _model = userModel()
            _data = _model.update_users(_entity)
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
            print('error: '+ str(e))
        return responseEntity(_status,_message,_data).toJSON()

    
    def delete_users(self,index):
        _message = None
        _status = self.interruption
        _cod = None
        try:
            _model = userModel()
            _cod = _model.delete_users(index)
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
            print('error: '+ str(e))
        return responseEntity(_status,_message,_cod).toJSON()

    def get_users_by_id(self,index):
        _message = None
        _status = self.interruption
        _entity = None
        try:
            _model = userModel()
            _entity = _model.get_users_by_id(index)
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
            print('error: '+ str(e))
        return responseEntity(_status,_message,_entity).toJSON()
