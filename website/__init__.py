from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "Passport Automation System.db"

def create_application():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'EADF1500AILA1165PAS1BE3CSEA5S3Y'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///D:\College\Python\miniproject(OOAD)\Passport Automation System\Registration_System\website\{DB_NAME}'
    db.init_app(app)

    from website.Login import Login
    from website.Verification import Verification
    from Registration_System.website.Appointment import Appointment

    app.register_blueprint(Login,url_prefix='/')
    app.register_blueprint(Verification,url_prefix='/')

    from Registration_System.website.data_models import Authority
    login_manager = LoginManager()
    login_manager.login_view = 'Login.Signin'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Authority.query.get(int(id))

    return app
