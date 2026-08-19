import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS


load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app =  Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.product import Product
    from app.controllers.product_controller import product_bp
    app.register_blueprint(product_bp)

    
   
    return app

