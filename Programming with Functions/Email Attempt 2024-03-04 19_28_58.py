import smtplib
from email.message import EmailMessage

subject = input("Without spaces, what would you like your subject header to be?")
sender = input("What is your email address?")

with open(subject) as email_file:
    msg = EmailMessage()
    msg.set_content(email_file.read())

msg['Subject'] = subject
msg['From'] = sender
msg['To'] = "bbn4779@gmail.com"

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
