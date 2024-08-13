from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['DEBUG'] = True

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.articles import articles_bp
    from app.routes.comments import comments_bp
    from app.routes.category import categories_bp
    from app.routes.users import users_bp
    app.register_blueprint(articles_bp, url_prefix='/articles')
    app.register_blueprint(comments_bp, url_prefix='/comments')
    app.register_blueprint(categories_bp, url_prefix='/category')
    app.register_blueprint(users_bp, url_prefix='/users')

    return app
