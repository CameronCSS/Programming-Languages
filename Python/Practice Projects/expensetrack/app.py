from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Config
    app.config.from_object("config.Config")  # Load config from a separate file
    
    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Register blueprints
    from routes.auth import auth_bp
    from routes.expenses import expenses_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(expenses_bp)
    
    return app
