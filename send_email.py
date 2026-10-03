import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "Your Email"
    password = "Keep App passwords id from manage your google account"

    receiver = "Reciever Email"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
