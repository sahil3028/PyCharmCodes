import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(message_html):
    host = "smtp.gmail.com"
    port = 465

    username = "sahil12345rock@gmail.com"
    password = "jvaw gzws pcvf mblm"
    receiver = "sahil12345rock@gmail.com"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "🗞️ Your Daily News Digest"
    msg["From"] = username
    msg["To"] = receiver

    msg.attach(MIMEText(message_html, "html"))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())