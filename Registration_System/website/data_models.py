from website import db 
#from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Registrations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicantid = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(64))
    dob = db.Column(db.String(11))
    gender = db.Column(db.String(6))
    birthplace = db.Column(db.String(160))
    fathername = db.Column(db.String(160))
    address1 = db.Column(db.String(320))
    address2 = db.Column(db.String(320))
    district = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))
    pincode = db.Column(db.BigInteger)
    mobile = db.Column(db.BigInteger)
    emailid = db.Column(db.String(160))
    qualification = db.Column(db.String(160))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(160), unique=True)
    password = db.Column(db.String(160))
    details = db.relationship('Registrations')

class Appointments(db.Model):
    appointmentid = db.Column(db.BigInteger,primary_key= True)
    applicantid = db.Column(db.BigInteger, unique = True)
    appointmentdate = db.Column(db.String(11))
    appointmenttime = db.Column(db.String(25))
    registration_user_id = db.Column(db.Integer, db.ForeignKey('registrations.id'))

class Authority(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    officerid = db.Column(db.BigInteger, unique = True)
    designation = db.Column(db.String(200))
    name = db.Column(db.String(150))
    password = db.Column(db.String(160))
