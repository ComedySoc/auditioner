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

def getFname(person):
    return person[NAME].partition(' ')[0]

def sendAccept(person):
    fname = getFname(person)
    send(person[EMAIL], acceptMsg.format(fname))

def sendReject(person):
    fname = getFname(person)
    send(person[EMAIL], rejectMsg.format(fname))

def sendCallback(person):
    fname = getFname(person)
    send(person[EMAIL], callbackMsg.format(fname))

with open('config.yaml') as f:
    cfg = yaml.load(f)

with open('accept.txt') as f:
    acceptMsg = f.read()

with open('reject.txt') as f:
    rejectMsg = f.read()

with open('callback.txt') as f:
    callbackMsg = f.read()

data = []
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

del data[0]

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
        print ('Acceptance sent to {0}'.format(person[NAME]))
    elif person[ACCEPT] == 'N':
        sendReject(person)
        print ('Rejection sent to {0}'.format(person[NAME]))
    elif person[ACCEPT] == 'C':
        sendCallback(person)
        print ('Callback sent to {0}'.format(person[NAME]))
    else:
        raise AcceptTokenNotRecognisedException
wrapup()
