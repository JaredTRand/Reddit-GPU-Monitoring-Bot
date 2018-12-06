import smtplib
import yagmail
import keyring
from twilio.rest import Client
carriers = {
    'att':    '@mms.att.net',
    'tmobile':' @tmomail.net',
    'verizon':  '@vtext.com',
    'sprint':   '@page.nextel.com'
}
auth = ('EMAIL@EMAIL.COM', 'PASSWORD')
to_number = '123-456-7890{}'.format(carriers['tmobile'])    

def send(message):    
    keyring.set_password('yagmail', auth[0], auth[1])
    yagmail.SMTP(auth[0]).send(auth[0], 'dealz', message)


def send2(message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    from email.mime.text import MIMEText
    msg = MIMEText(message)
    msg["Subject"] = "Dealios"
    msg["From"] = auth[0]
    msg["To"] = to_number
    server.send_message(msg)
    
def send4(msg):
    account_sid = 'AC541429baa3b35665a2038529b6b2ecb2'
    auth_token = 'bf00c1afbe3de377d83c57f8e1cc16e9'
    client = Client(account_sid, auth_token)
    numberTwilio = 'TWILIO_NUMBER'
    numberRecipient = 'NUMBER_RECIPIENT'

    message = client.messages \
        .create(body=msg, to=numberRecipient, from_=numberTwilio)
 
    print(message.sid)



