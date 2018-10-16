import re
import urllib2
from bs4 import BeautifulSoup
import json
from smtplib import SMTP_SSL as SMTP  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
import ssl


def urlify(s):
    s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '+', s)
    return s

def imdb_search(ID) :
    base_url = 'https://www.imdb.com/title/'+ID+'/'
    r = urllib2.urlopen(base_url)
    soup = BeautifulSoup(r,'html5lib')
    
    for element in soup.find_all('div',{'class':'seasons-and-year-nav'}):
        x = element.find_all('div')[2]
        url = x.find('a').get('href')
    final_url = "https://www.imdb.com" + url         
    return final_url


def omdb_search(name):
    base_url = 'http://www.omdbapi.com/?apikey=869dbe88&&type=series&t='
    omdb_url = base_url + name + '&plot=full'
    json_obj = urllib2.urlopen(omdb_url)
    data = json.load(json_obj)
    response = data['Response']

    if response == u'True': # comparing unicode and bool values.
        imdbID = data['imdbID']
        return imdbID
    else:
        return -1


def sendmail(email_id, email_body):
    SMTPserver = 'smtp.gmail.com'
    USERNAME = config.FROM_EMAIL
    sender = config.FROM_EMAIL
    destination = email_id
    text_subtype = 'plain'
    content = email_body

    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject']= 'SERIOHOLIC: Status of your favourite TV Shows.'
        msg['From'] = config.FROM_EMAIL

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USERNAME, config.PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
            print('Please Check your Inbox!\n')
        finally:
            conn.quit()
    except:
        print("Failed to send email; %s" % "CUSTOM_ERROR")