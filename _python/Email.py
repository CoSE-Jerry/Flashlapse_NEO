import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendtest():

    fromaddr = "notification_noreply@flashlapseinnovations.com"
    toaddr = "xmiao8@wisc.edu"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "FLASHLAPSE NOTIFICATION"
    body = "imaging complete"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("AKIAJOQJ7F74CE65JXIA", "Ar6L9IIFT/CxuaGMwM2BNHuT+FkSbpjkYWnCTAG05Rr+")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)