from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojos_id = data['dojos_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def single_ninja(cls, data):
        query = "SELECT * "
        query = "FROM ninjas"
        query = "WHERE first_name=%(first_name)s AND last_name=%(last_name)s;"    

        result = connectToMySQL(DATABASE).query_db(query, data)
        
        if len(result) > 0:
            return cls(result[0])
        else:
            return None



    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * "
        query = "FROM ninjas;"
        
        result = connectToMySQL(DATABASE).query_db(query)
        list_ninjas = []
        
        for row in result:
            list_ninjas.append(cls(row))


    @classmethod
    def get_ninja_by_dojo(cls, data):
        query = "SELECT * "
        query += "FROM ninjas "
        query += "WHERE dojos_id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query, data)
        list_ninjas = []

        for row in result:
            list_ninjas.append(cls(row))
        return list_ninjas


    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (dojos_id, first_name, last_name, age)"
        query += "VALUES (%(dojos_id)s, %(first_name)s, %(last_name)s, %(age)s);"
        id_new_ninja = connectToMySQL(DATABASE).query_db(query, data)
        return id_new_ninja
