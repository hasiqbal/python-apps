import smtplib
import ssl

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'hasaniqbal6901@gmail.com'
    password = 'flprgpbrrkspyvws'

    reciever = "hasaniqbal6901@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
        print('Email sent!')


