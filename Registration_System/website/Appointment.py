from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .data_models import Appointments

Appointment = Blueprint('Appointment',__name__)

@Appointment.route('/Appointment',methods=['GET','POST'])
@login_required
def getappointment():
    if request.method == 'POST':
        appointmentid = request.form.get('appointmentid')
        applicantid = request.form.get('applicantid')
        appointmentdate = request.form.get('appointmentdate')
        appointmenttime = request.form.get('appointmenttime')
        if len(applicantid) < 10:
            flash('Applicant Id has maximum of 10 characters.',category='error')
        elif len(appointmentid) < 10:
             flash("Appointment Id has maximum of 10 characters.",category='error')
        elif len(appointmenttime) < 1:
             flash('Time must be specified.',category='error')
        elif len(appointmentdate) < 1:
             flash('Date must be specified.',category='error')
        else:
             new_appointment = Appointments(appointmentid=appointmentid,applicantid=applicantid,appointmentdate=appointmentdate,appointmenttime=appointmenttime)
             db.session.add(new_appointment)
             db.session.commit()
             flash('Appointment successful!',category='success')
    return render_template("appointment.html", user = current_user)
