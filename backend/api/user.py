from flask import Blueprint, jsonify, request
user_bp = Blueprint("user", __name__)

@user_bp.get("/user/list")
def get_user_list():
    pass

@user_bp.post("/user/add")
def add_user():
    pass