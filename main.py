import smtplib
import yaml
import csv

class AcceptTokenNotRecognisedException(Exception):
    pass

def login():
    server.ehlo()
    server.login(username, password)

def wrapup():
    server.close()

def send(to, body, subject='Shambles Audition'):
    msg = """\From: %s\nTo: %s\nSubject: %s\n%s\n""" % (fromaddr, to, subject, body)
    server.sendmail(fromaddr, to, msg)

def sendAccept(person):
    fname = person[NAME].partition(' ')[0]
    send(person[EMAIL], acceptMsg.format(fname))

def sendReject(person):
    fname = person[NAME].partition(' ')[0]
    send(person[EMAIL], rejectMsg.format(fname))

with open('config.yaml') as f:
    cfg = yaml.load(f)


with open('accept.txt') as f:
    acceptMsg = f.read()

with open('reject.txt') as f:
    rejectMsg = f.read()

data = []
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

del data[0]

print (data)

fromaddr = cfg['username']

username = cfg['username']
password = cfg['password']

NAME = 0
EMAIL = 1
ACCEPT = 2

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

login()

for person in data:
    if person[ACCEPT] == 'Y':
        sendAccept(person)
    elif person[ACCEPT] == 'N':
        sendReject(person)
    else:
        raise AcceptTokenNotRecognisedException
    print ('Email sent! to {0}'.format(person[NAME]))
wrapup()
