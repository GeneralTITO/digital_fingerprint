import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.relogio import actual_time
import threading

def send_email_async(to):
    def send_email_inner():
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'email'
        smtp_password = 'chave'

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  

        server.login(smtp_username, smtp_password)

        subject = 'Registro de presença'
        body = f'Sua presença foi confirmada em {actual_time()}'
        from_address = 'ddigitalfingerprint@gmail.com'
        to_address = to

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(from_address, to_address, msg.as_string())

        server.quit()

    email_thread = threading.Thread(target=send_email_inner)
    email_thread.start()
