import smtplib
import yaml

def login():
    server.ehlo()
    server.login(username, password)

def wrapup():
    server.close()

def send(body, subject='Shambles Auditions'):
    msg = """\
    From: %s
    To: %s  
    Subject: %s

    %s
    """ % (fromaddr, toaddr, subject, body)
    server.sendmail(fromaddr, toaddr, msg)

with open('config.yaml') as f:
    cfg = yaml.load(f)

print (cfg)

fromaddr = cfg['username']
toaddr = 'qumarthjash@gmail.com'

body = 'hello world!'

username = cfg['username']
password = cfg['password']

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

login()

send(body)

print ('Email sent!')
wrapup()
