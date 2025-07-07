from flask import Flask
from models import db, csrf, login_manager
from models.model import create_admin
from controllers import register_blueprints
from logging.handlers import RotatingFileHandler
import logging
import os

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = f'{os.urandom(24)}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    
    login_manager.login_view = 'auth_bp.login'

    
    register_blueprints(app)

    with app.app_context():
        db.create_all()
        create_admin(app)

    if not os.path.exists("logs"):
        os.mkdir("logs")

    file_handler = RotatingFileHandler("logs/app.log", maxBytes=10240, backupCount=3)
    file_handler.setFormatter(
        logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
    )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info("🚀 App started and logging is set up.")

    return app

from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()