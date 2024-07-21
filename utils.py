import time
import random
import subprocess
from bs4 import BeautifulSoup
from email.message import EmailMessage
import ssl
import smtplib
import config


def random_sleep() -> None:
    time.sleep(random.randint(1, 3))


def get_soup(URL) -> BeautifulSoup:
    curl = open('curl.sh', 'r').read().replace('{{url}}', URL)
    html = subprocess.run(curl,
                          shell=True,
                          capture_output=True,
                          text=True).stdout
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def notify(subjectMessage: str, bodyMessage: str) -> None:
    emailSender = config.EMAIL_SENDER
    emailPassword = config.EMAIL_PASSWORD
    emailReceptor = emailSender
    emailSubject = subjectMessage
    emailBody = bodyMessage

    em = EmailMessage()
    em["From"] = emailSender
    em["To"] = emailReceptor
    em["Subject"] = emailSubject
    em.set_content(emailBody)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as msg:
        msg.login(emailSender, emailPassword)
        msg.sendmail(emailSender, emailReceptor, em.as_string())
    print("Email sent successfully")
