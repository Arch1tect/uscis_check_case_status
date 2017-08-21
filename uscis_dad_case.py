import requests
from bs4 import BeautifulSoup
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


def send_simple_message(subject, msg):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd1b6c36cfcee4a788c1d9794208e7583.mailgun.org/messages",
        auth=("api", "key-c5e95173a1f60ab411eff18031723799"),
        data={"from": "Excited User <uscis_dad_case.py@arch.tech>",
              "to": ["yo", "swtdavid@gmail.com"],
              "subject": subject,
              "text": msg})





payload = {
	'changeLocale': '',
	'appReceiptNum':'LIN1790258728',
	'initCaseSearch':'CHECK STATUS',
}
resp = requests.post('https://egov.uscis.gov/casestatus/mycasestatus.do', data=payload)
soup = BeautifulSoup(resp.text)

print soup.prettify()

res = soup.find("div", class_="rows text-center")

case_title = res.find("h1").get_text()

email_subject = "USCIS dad case - %s" % case_title
email_res = send_simple_message(email_subject, res)

print email_res.content