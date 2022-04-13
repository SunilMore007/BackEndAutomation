import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Trading invitation'
msg['From'] = 'Sunil Team'
msg['To'] = 'sunilmore.testing@gmail.com'
msg.set_content("Test Mail from Python community")

with open("EmailTemplate.txt") as template:
    data=template.read()
    msg.set_content(data)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("sunilmore.testing@gmail.com", "Sunil@123")
server.send_message(msg)
server.quit()
print("Email Sent")