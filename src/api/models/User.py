from . import db
from typing import Dict
from src.modules.Serializer import Serializer
from datetime import datetime
# from bson.objectid import ObjectId


users = db.users

class User:

    @staticmethod
    def create_user(new_user: Dict) -> bool:
        db_response = users.insert_one({
            'first_name':new_user['first_name'],
            'last_name':new_user['last_name'],
            'password':new_user['password_hash'],
            'email': new_user['email'],
            'phone_number':new_user['phone_number'],
            'username': new_user['username'],
            'created_at': datetime.now(),
            'updated_at': None,
        })

        return True if db_response.inserted_id else False
    
    @staticmethod
    def get_user_by_email(email:str,needed_attributes=['_id','email','password','first_name','last_name','username','phone_number','created_at','updated_at']) -> Dict:
        db_response = users.find_one({'email':email})
        return Serializer(needed_attributes).serialize(db_response) if db_response else {}
    
    @staticmethod
    def get_user_by_username(username:str,needed_attributes=['_id','email','password','first_name','last_name','username','phone_number','created_at','updated_at']) -> Dict:
        db_response = users.find_one({'username':username})
        return Serializer(needed_attributes).serialize(db_response) if db_response else {}