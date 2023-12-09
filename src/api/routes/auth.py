import re
from flask import Blueprint, jsonify,request
from typing import Dict
import validators
import phonenumbers
from werkzeug.security import generate_password_hash
from src.api.models.User import User


auth = Blueprint("auth",__name__,url_prefix="/api/auth")

@auth.post("/sign-up")
def sign_up():
    
    first_name = request.get_json().get('firstName', None)
    last_name = request.get_json().get('lastName', None)
    username = request.get_json().get('username', None)
    password = request.get_json().get('password', None)
    email = request.get_json().get('email', None)
    phone_number  = request.get_json().get('phoneNumber', None)

    if not username or not first_name or not last_name or not password or not email:
        return jsonify({
            'error': True,
            'message': "all values needed"
        }), 400

    if len(username) < 2:
        return jsonify({
            'error': True,
            'message': "username length is less than 2"
        }), 400
        
    if len(password) < 5:
        return jsonify({
            'error': True,
            'message': "password length is less than 5"
        }), 400
        
    if not validators.email(email):
        return jsonify({
            'error':True,
            'message':"invalid email"
        }), 400
    
    my_number = phonenumbers.parse("+234"+phone_number)
        
    if not phonenumbers.is_valid_number(my_number):
        return jsonify({
            'error':True,
            'message':"invalid phonenumber"
        }), 400
        
    if User.get_user_by_email(email):
        return jsonify({
            'error': True,
            'message': "email already exists"
        }), 400
    
    if User.get_user_by_username(username):
        return jsonify({
            'error': True,
            'message': "username already exists"
        }), 400
        
    password_hash = generate_password_hash(password)
    
    if User.create_user({
        'first_name': first_name,
        'username': username,
        'last_name': last_name,
        'password_hash': password_hash,
        'email': email,
        'phone_number': phone_number
    }) :
        return jsonify({
            'error': False,
            'message': "user created successfully"
        }), 201
        
    
    return jsonify({
        'error': True,
        'message': "something went wrong"
    }), 500
    
    
    #     if Admin.get_admin_by_email(email):
    #         return jsonify({
    #             'error': True,
    #             'message': "email already exists"
    #         }), 400
        
    
    # return jsonify({
    #     'error': True,
    #     'message': "bingo",
    #     'data': phonenumbers.is_valid_number(my_number)
    # }),200