from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from Registration_System.website.data_models import Authority
from website import db
from Registration_System.website.data_models import Appointments

Verification = Blueprint('Verification',__name__)

@Verification.route('/', methods =['GET','POST'])
@login_required
def verify():
    if request.method == 'POST':
        Applicantid = request.form.get('applicantid')
        Appointmentid = request.form.get('appointmentid')
        Officerid = request.form.get('officerid')
        if len(Applicantid) < 10:
            flash('Applicant Id has maximum of 10 characters.',category='error')
        elif len(Appointmentid) < 10:
            flash('Appointment Id has maximum of 10 characters.', category='error')
        elif len(Officerid) < 5 :
            flash('Officer Id has maximum of 5 characters.',category='error')
        else:
            v_officer = Authority.query.filter_by(officerid = Officerid).first()
            v_applicant = Appointments.query.filter_by(applicantid = Applicantid).first()
            v_appointment = Appointments.query.filter_by(appointmentid = Appointmentid).first()
            if v_applicant and v_officer and v_appointment :
                flash('Verification successful!',category='success')
            else:
                flash('Verification failed.',category='error')
    return render_template("Verification.html" , user=current_user)
