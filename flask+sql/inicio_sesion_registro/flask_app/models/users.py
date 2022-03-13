from pickle import TRUE
from flask_app.config.mysqlconection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        nuevoId = connectToMySQL('registro').query_db(query, data)
        return nuevoId
    
    @classmethod
    def validate_info(cls, data):
        
        is_valid = True
        
        if len(data['first_name']) < 3:
            flash('The name must be at least 4 characters', 'register')
            is_valid = False
            return is_valid
            
        if len(data['last_name']) <3:
            flash("The last name must be at least 4 characters", 'register')
            is_valid = False
            
        
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email", 'register')
            is_valid = False
            
        
        if len(data['password']) < 6:
            flash("The password must be at least 6 characters", 'register')
            is_valid = False
            
        
        if data['password'] != data['confirm']:
            flash('Passwords do not match', 'register')
            is_valid = False
        
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('registro').query_db(query, data)
        if len(result) >= 1:
            flash("Email already exists", 'register')
            is_valid = False
        
        return is_valid
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('registro').query_db(query, data)
        rlt = result[0]
        user = cls(rlt)
        return user
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('registro').query_db(query, data)
        
        if len(result) < 1:
            return False
        else:
            rst= result[0]
            is_valid = cls(rst)
        
            return is_valid