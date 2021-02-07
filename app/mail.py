import smtplib

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login('chelsiewebsite@gmail.com', 'mtbwazdmldkfnulz')

# Send text message through SMS gateway of destination number

message = MIMEMultipart("alternative")
message["Subject"] = "[WARNING] Article Expiring Soon"
message['From'] = "noreply@bestbefore.tech"
# message["To"] = receiver_email
msg = """Dear user,

This is a kind reminder that one of your articles is expiring soon.

To check the article, please log in on best-before.tech

Cheers,
Best Before Team
"""
text = MIMEText(msg, "plain")
message.attach(text)
server.sendmail('noreply@bestbefore.tech', 'chelsiengmk@gmail.com', message.as_string())
