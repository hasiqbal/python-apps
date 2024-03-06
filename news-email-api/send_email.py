import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(email):
    host = 'smtp.gmail.com'
    port = 465
    username = 'hasaniqbal6901@gmail.com'
    password = 'flprgpbrrkspyvws'


    reciever = "hasaniqbal6901@gmail.com"
    context = ssl.create_default_context()

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = reciever
    msg['Subject'] = 'Tesla News'
    
    msg.attach(MIMEText(email, 'plain'))

    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, msg.as_string())
        print('Email sent!')
