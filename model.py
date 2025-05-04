from datetime import datetime, timedelta
import mysql.connector
import json
from flask import make_response, jsonify
import jwt
from config import dbconfig

class user_model():
    def __init__(self):
        self.con = mysql.connector.connect(host=dbconfig['host'],user=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True)

    def all_user_model(self, id):
        self.cur.execute(f"SELECT * FROM user_profile WHERE id={id}")
        user = self.cur.fetchone()
        if user:
            return make_response(jsonify(user), 200)
        else:
            return make_response({"message": "USER_NOT_FOUND"}, 404)
    
    def add_user_model(self,data):
        self.cur.execute(f"INSERT INTO user_profile(name, goals, workoutlevel, gender, birthdate, height, weight) VALUES('{data['name']}', '{data['goals']}', '{data['workoutlevel']}', '{data['gender']}', '{data['birthdate']}', '{data['height']}', '{data['weight']}')")
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)
