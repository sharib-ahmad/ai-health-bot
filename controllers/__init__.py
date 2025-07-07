from .auth_route import auth_bp
from .bot_route import bot_bp


def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(bot_bp)
