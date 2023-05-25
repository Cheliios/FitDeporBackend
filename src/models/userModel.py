from src.cn.data_base_connection import Database
from src.models.dbModel import dbModel
from src.entities.userEntity import userEntity

class userModel(dbModel):

    def __init__(self):
        dbModel.__init__(self)
        
    def get_users(self):
        _db = None
        _data = []
        try:
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()

            _sql = """SELECT u.user_dni, 
                    u.user_nickname,
                    u.user_password,
                    u.user_name,
                    u.user_lastname,
                    u.user_edad,
                    u.user_genero,
                    u.user_pais,
                    u.user_mail
                FROM    main.user_app u; """   

            _cur = _con_client.cursor()
            _cur.execute(_sql,)
            _rows = _cur.fetchall()
        
            for row in _rows:
                _entity  = userEntity()
                _entity.user_dni = row[0]
                _entity.user_nickname = row[1]
                _entity.user_password = row[2]
                _entity.user_name = row[3]
                _entity.user_lastname = row[4]
                _entity.user_edad = row[5]
                _entity.user_genero = row[6]
                _entity.user_pais = row[7]
                _entity.user_mail = row[8]
                _data.append(_entity)

            _cur.close()
        except(Exception) as e:
            print(str(e))
            #self.add_log(str(e),type(self).__name__)
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return _data
    


    def add_users(self,entity):
        _db = None
        _data = []
        try:
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()

            _sql = """insert into main.user_app(user_dni, user_nickname, user_password, user_name, user_lastname, user_edad, user_genero, user_pais, user_mail)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s); """   

            _cur = _con_client.cursor()
            _cur.execute(_sql,(entity.user_dni,entity.user_nickname,entity.user_password,entity.user_name,entity.user_lastname,entity.user_edad,entity.user_genero,entity.user_pais,entity.user_mail))
            _con_client.commit()
            _cur.close()
        except(Exception) as e:
            print(str(e))
            #self.add_log(str(e),type(self).__name__)
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return entity




    def update_users(self,entity):
        _db = None
        _data = []
        try:
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()

            _sql = """update main.user_app 
                    set user_nickname  = %s,
                    user_password = %s,
                    user_name = %s,
                    user_lastname = %s,
                    user_edad = %s,
                    user_genero = %s,
                    user_pais = %s,
                    user_mail = %s
                    
                    where user_dni = %s;"""   

            _cur = _con_client.cursor()
            _cur.execute(_sql,(entity.user_nickname,entity.user_password,entity.user_name,entity.user_lastname,entity.user_edad,entity.user_genero,entity.user_pais,entity.user_mail,entity.user_dni))
            _con_client.commit()
            _cur.close()
        except(Exception) as e:
            print(str(e))
            #self.add_log(str(e),type(self).__name__)
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return entity




    def delete_users(self,user_dni):
        _db = None
        try:
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()

            _sql = """DELETE FROM main.user_app
                    WHERE user_dni = %s;"""   

            _cur = _con_client.cursor()
            _cur.execute(_sql,(user_dni,))
            _con_client.commit()
            _cur.close()
        except(Exception) as e:
            print(str(e))
            #self.add_log(str(e),type(self).__name__)
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return user_dni


        
    
    def get_users_by_id(self,user_dni):
        _db = None
        _entity = None
        try:
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()

            _sql = """SELECT u.user_nickname,u.user_password,u.user_name,u.user_lastname,u.user_edad,u.user_genero,u.user_pais,u.user_mail
                        FROM    main.user_app u
                        WHERE u.user_dni = %s;"""   

            _cur = _con_client.cursor()
            _cur.execute(_sql,(user_dni,))
            _rows = _cur.fetchall()

            if(len(_rows) >= 0):
                _entity = userEntity()
                _entity.user_nickname = _rows[0][0]
                _entity.user_password = _rows[0][1]
                _entity.user_name = _rows[0][2]
                _entity.user_lastname = _rows[0][3]
                _entity.user_edad = _rows[0][4]
                _entity.user_genero = _rows[0][5]
                _entity.user_pais = _rows[0][6]
                _entity.user_mail = _rows[0][7]
                _entity.user_dni = _rows[0][8]

            _cur.close()
        except(Exception) as e:
            print(str(e))
            #self.add_log(str(e),type(self).__name__)
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return _entity

