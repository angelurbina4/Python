from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_usuarios').query_db(query)
        #llega una lista a traves de results 
        #[
        #    { una lista }
        #]
        users = [] #convierto los objetos  para que sean de la clase usuario
        for u in results:
            users.append(cls(u))
        return users 
    
    @classmethod
    def guardar(cls, data):
        #data = {"first_name" = "v"...}
        query = "INSERT INTO users (first_name, last_name, email) VAlUE (%(first_name)s, %(last_name)s, %(email)s)" #names del html
        result = connectToMySQL('esquema_usuarios').query_db(query, data)
        return result
    
    @classmethod
    def borrar(cls, data):
        #data = {"id": "1"}
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios').query_db(query, data)
        return result
    
    @classmethod
    def mostrar(cls, data):
        #data = {"id": "1"}
        query = "SELECT * FROM users WHERE id = %(id)s" #Aqui regresa una lista con solo un valor que fue el que pedi
        result = connectToMySQL('esquema_usuarios').query_db(query, data)
        user =result[0] # porque es la unica posicion 
        user = cls(user) # lo obligo a que sea clase usuario
        return user
    
    @classmethod
    def actualizar(cls,data):
        # lista en diccionario con toda la data
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        result = connectToMySQL('esquema_usuarios').query_db(query, data)
        return result