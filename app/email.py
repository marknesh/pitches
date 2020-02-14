from . import mail
from flask_mail import Message
from flask import render_template


def email_sender(subject,template,to,**kwargs):
    sender_mail='mikeknowles.dez@gmail.com'

    email=Message(subject,sender=sender_mail,recipients=[to])
    email.body=render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)