import os
import datetime
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def mail():

    # Set csv location
    os.chdir('ReadFromCSV')
    folderpath = os.getcwd()
    filepath = os.path.join(folderpath, 'BugData.csv')

    # Global config
    emailfrom = "orelmishakim@gmail.com"
    emailto = "orel.amedi@gmail.com"
    fileToSend = filepath
    filename = 'BugData.csv'
    username = os.environ.get('MAIL_USERNAME')
    password = os.environ.get('MAIL_PASSWORD')

    # Time
    now = datetime.datetime.now()
    nowFormat = now.strftime("Date: %d/%m/%Y \nTime: %H:%M")

    # Message config
    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = "Auto generated CSV"
    body = f'The CSV generated on {nowFormat}'
    msg.attach(MIMEText(body, 'plain'))


    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=filename)
    msg.attach(attachment)

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username, password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()
    print('Mailed!')


if __name__ == '__main__':
    mail()