import os
from flask_mail import Message
from utils.common import TokenGenerator
#from server import mail
from server import mail

# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)


# def send_email(to, subject, template, **kwargs):
#     app = current_app._get_current_object()
#     msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
#                   sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#     msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     thr = Thread(target=send_async_email, args=[app, msg])
#     thr.start()
#     return thr

def send_forgot_password_email(request, user):
    """
    It sends an email to the user with a link to reset their password

    :param request: The request object
    :param user: The user object of the user who requested the password reset
    """
    current_site = request.url_root
    mail_subject = "Reset your password"
    domain = os.environ.get("API_URL")
    uid = user.id
    token = TokenGenerator.encode_token(user)
    msg = Message(
        mail_subject, sender=os.environ.get("EMAIL_HOST_USER"), recipients=[user.email]
    )
    msg.html = f"Please click on the link to reset your password, {domain}/pages/auth/reset-password/{uid}/{token}"
    mail.send(msg)
