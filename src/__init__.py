from flask import Flask,jsonify
from flask_cors import CORS
from src.config import SECRET_KEY
from src.api.routes.auth import auth

def create_app():

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        # JWT_SECRET_KEY=JWT_SECRET_KEY,
        # JWT_ACCESS_TOKEN_EXPIRES=JWT_ACCESS_TOKEN_EXPIRES,
        # JWT_REFRESH_TOKEN_EXPIRES=JWT_REFRESH_TOKEN_EXPIRES,
        # JWT_TOKEN_LOCATION=JWT_TOKEN_LOCATION,
        # JWT_QUERY_STRING_NAME=JWT_QUERY_STRING_NAME
    )

    CORS(app, supports_credentials=True, resources={
        r"/*": {
            "origins": {
                "*",
            }
        }
    })
    
    app.register_blueprint(auth)


    @app.errorhandler(404)
    def handle_404(e):
        return jsonify({
            'error':True,
            'message':"Not Found"
        })

    return app