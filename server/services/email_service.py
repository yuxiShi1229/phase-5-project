from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def init_mail(app):
    mail.init_app(app)

def send_email(recipient, subject, body):
    msg = Message(subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[recipient])
    msg.body = body
    mail.send(msg)

def send_class_invitation(student_email, classroom_name):
    subject = f"Invitation to join {classroom_name}"
    body = f"You have been invited to join the classroom: {classroom_name}. Please log in to your account to access it."
    send_email(student_email, subject, body)

def send_class_reminder(student_email, classroom_name, start_time):
    subject = f"Reminder: Upcoming class for {classroom_name}"
    body = f"This is a reminder that your class {classroom_name} is starting at {start_time}. Don't forget to join!"
    send_email(student_email, subject, body)