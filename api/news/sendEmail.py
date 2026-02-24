import smtplib, ssl

def send_email(mssg):
    host="smtp.gmail.com"
    port=465

    username="sahil12345rock@gmail.com"
    password= "jvaw gzws pcvf mblm"

    receiver="sahil12345rock@gmail.com"

    context= ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,mssg)
#send_email("yooo twin")