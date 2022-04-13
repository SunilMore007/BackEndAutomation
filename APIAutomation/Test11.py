import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Trading invitation'
msg['From'] = 'Sunil Team'
msg['To'] = 'sunilmore0057@gmail.com'
msg.set_content("Test Mail from Python community")

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("sunilmore.testing@gmail.com", "Sunil@123")
server.send_message(msg)
server.quit()