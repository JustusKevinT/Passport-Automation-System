from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from website.data_models import Registrations
from website import db


Registration = Blueprint('Registration',__name__)

@Registration.route('/', methods =['GET','POST'])
@login_required
def add():
    if request.method == 'POST':
        applicantid = request.form.get('applicantid')
        name = request.form.get('name')
        dob = request.form.get('dob')
        gender = request.form.get('gender')
        birthplace = request.form.get('birthplace')
        fathername = request.form.get('fathername')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        district = request.form.get('district')
        state = request.form.get('state')
        country = request.form.get('country')
        pincode = request.form.get('pincode')
        mobile = request.form.get('mobile')
        emailid = request.form.get('emailid')
        qualification = request.form.get('qualification')
        if len(applicantid) < 10:
            flash('Applicant Id has maximum of 10 characters.',category='error')
        elif len(name) < 1:
            flash('Name must be greater than 1 character.', category='error')
        elif len(gender) < 1 :
            flash('Gender must be specified.',category='error')
        elif len(fathername) < 1:
            flash('Father name must be greater than 1 character.',category='error')
        elif len(birthplace) < 1:
            flash('Birthplace must be greater than 1 character.',category='error')
        elif len(address1) < 1:
            flash('Address1 must be greater than 1 character.',category='error')
        elif len(district) < 1:
            flash('District must be greater than 1 character.',category='error')
        elif len(state) < 1:
            flash('State must be greater than 1 character.',category='error')
        elif len(country) < 1:
            flash('Country must be greater than 1 character.',category='error')
        elif len(pincode) < 1:
            flash('Pincode must be greater than 1 character.',category='error')
        elif len(mobile) < 1:
            flash('Mobile number must be greater than 1 character.',category='error')
        elif len(emailid) < 1:
            flash('Email Id must be greater than 1 character.',category='error')
        elif len(qualification) < 1:
            flash('Qualification must be greater than 1 character.',category='error')
        elif len(dob) < 1:
            flash('DOB must be specified.',category='error')
        else:
            new_registration = Registrations(applicantid=applicantid,name=name,dob=dob,gender=gender,birthplace=birthplace,fathername=fathername,address1=address1,address2=address2,district=district,state=state,country=country,pincode=pincode,mobile=mobile,emailid=emailid,qualification=qualification)
            db.session.add(new_registration)
            db.session.commit()
            flash('Registration successful!',category='success')
    return render_template("registration.html" , user=current_user)
