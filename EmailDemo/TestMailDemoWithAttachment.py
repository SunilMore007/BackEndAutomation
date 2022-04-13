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


with open("result.xlsx", "rb") as f:
    filedata=f.read()
    print("file data in binary", filedata)
    file_name=f.name
    print("file name is ", file_name)
    msg.add_attachment(filedata,maintype="application", subtype="xlsx", filename=file_name)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("sunilmore.testing@gmail.com", "Sunil@123")
server.send_message(msg)
server.quit()
print("Email Sent")