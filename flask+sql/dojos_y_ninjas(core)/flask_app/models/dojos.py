from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def muestra_dojos(cls):
        query = "SELECT * FROM dojos"
        result = connectToMySQL('dojos_ninjas').query_db(query)
        dojos = []
        for d in result:
            dojos.append(cls(d))
        return dojos
    
    @classmethod
    def guardar_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        result = connectToMySQL('dojos_ninjas').query_db(query, data)
        return result
    
    @classmethod
    def muestra_ninjas_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE ninjas.dojo_id = %(id)s"
        result = connectToMySQL('dojos_ninjas').query_db(query, data)
        print(result)
        if len(result) >= 1:
            dojo = cls(result[0])
            for d in result:
                dj = {
                    'id': d['ninjas.id'],
                    'first_name' : d['first_name'],
                    'last_name' : d['last_name'],
                    'age' : d['age'],
                    'created_at' : d['created_at'],
                    'updated_at' : d['updated_at']
                }
                
                ninja = Ninja(dj)
                dojo.ninjas.append(ninja)
                print(dojo)
            return dojo