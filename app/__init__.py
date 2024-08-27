from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from config import Config

db = SQLAlchemy()
ma = Marshmallow()  # This is fine as long as you’re not using SQLAlchemyAutoSchema directly from here
api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    
    with app.app_context():
        from . import routes
        db.create_all()

    return app
