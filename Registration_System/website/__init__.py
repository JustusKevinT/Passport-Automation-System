from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "Passport Automation System.db"

def create_application():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'EADF1500AILA1165PAS1BE3CSEA5S3Y'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.join(path.abspath(path.dirname(__file__)), DB_NAME)}'
    db.init_app(app)

    from website.Registration import Registration
    from website.Login import Login
    from website.Appointment import Appointment
    app.register_blueprint(Registration,url_prefix='/')
    app.register_blueprint(Login,url_prefix='/')
    app.register_blueprint(Appointment,url_prefix='/')

    from website.data_models import User, Registrations
    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'Login.Signin'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('websiteapp/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database created")
