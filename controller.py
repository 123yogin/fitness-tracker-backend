from flask import request
from app import app
from model import user_model

@app.route('/')
def home():
    return "Server is running on port 4000 with me as the controller!"

obj = user_model()

@app.route("/user/<id>", methods=["GET"])
def all_users(id):
    return obj.all_user_model(id)

@app.route("/user/add", methods=["POST"])
def add_user():
    return obj.add_user_model(request.form)
