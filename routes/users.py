from flask import Blueprint, jsonify, request

users = Blueprint('users', __name__)

@users.route('/', methods=['GET'])
def get_users():
    return jsonify({"users": ["user1", "user2", "user3"]})

@users.route('/', methods=['POST'])
def create_user():
    data = request.json
    return jsonify({"status": "User created", "user": data}), 201