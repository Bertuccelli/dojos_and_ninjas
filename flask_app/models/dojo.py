from flask_app.config.mysqlconnection import  connectToMySQL
from flask_app import DATABASE

class Dojo:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * "
        query += "FROM dojos;"
        result = connectToMySQL(DATABASE).query_db(query)
        list_dojos = []

        for row in result:
            list_dojos.append(cls(row))
        return list_dojos


    @classmethod
    def get_dojo_id(cls, data):
        query = "SELECT * "
        query += "FROM dojos;"
        query += "WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result


    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos(name)"
        query += "VALUES(%(name)s );"

        id_new_dojo = connectToMySQL(DATABASE).query_db(query, data)
        print(id_new_dojo)
        return id_new_dojo


    @classmethod
    def single_dojo(cls, data):
        query = "SELECT * "
        query += "FROM dojos;"
        query += "WHERE name = %(name)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result


