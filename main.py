# coding: utf-8
import urllib2
from bs4 import BeautifulSoup
import re
import json
import datetime
import database
import utility as ut

omdb_apikey = '869dbe88'

def main():
    print("----------------------Hackercamp'19----------------------")
    print "\n"
    print("SERIOHOLIC: Quench your thirst of binge watching.")
    print(2*"\n")

    EMAIL_REGEX_PATTERN = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    email_id = raw_input(('Email address: '))
    while not EMAIL_REGEX_PATTERN.match(email_id):
        print('Incorrect email address entered, please try again!\n')
        email_id = raw_input(('Email address: '))
    tvSeriesString = raw_input(('TV Series: '))
    for_template = tvSeriesString 
    print '\n' 

    try:
        database.add_to_db(email_id,tvSeriesString)
        print 'Your preferences has been recoded in Database.\n'
    except:
        print 'Failed to add preferences in Database.\n'

    li = [ut.urlify(x.strip()) for x in tvSeriesString.split(',')]
    # for i in range(len(li)):
    message = []
    shows_name = [x.strip() for x in for_template.split(',')]
    for i in li:
        # ID = omdb_search(li[i])
        ID = ut.omdb_search(i)
        #numberOfSeasons = find_season(ID).text
        if(ID == -1):
            print 'No search results found!'
        else:
            imdb_url = ut.imdb_search(ID)
            # print imdb_url
            response = urllib2.urlopen(imdb_url)
            html = response.read()
            soup = BeautifulSoup(html,'html5lib')
            airdate_box = []
            airdate_box_formatted = []
            for i in soup.find_all('div',attrs={'class':'airdate'}):
                a = str(i.text).replace("\n","").strip().replace(".","")
                airdate_box.append(a)
            # print "First scrape"
            # print airdate_box

            # TODO: Apply filter to increase the processing speed
            airdate_box[:] = [item for item in airdate_box if item != '']
            # print "After removing empty entries"
            #print airdate_box

            today_date = datetime.datetime.now()
            # print today_date
            for i in airdate_box:
                if(len(i) == 4):
                    dt = datetime.datetime.strptime(i, "%Y").strftime("%Y")
                elif (len(i) == 8 ):
                    dt = datetime.datetime.strptime(i,"%b %Y").strftime("%Y-%m")
                else:
                    dt = datetime.datetime.strptime(i,"%d %b %Y").strftime("%Y-%m-%d")
                airdate_box_formatted.append(dt)

            #print "Formatted list"
            #print airdate_box_formatted
            #print '\n'
            
            
            if(len(airdate_box_formatted) == 0):
                res = "No information available for this show as of now."
                message.append(res)
                #print res
            flag = 4
            for i in airdate_box_formatted:
                if(len(i) == 10):
                    dt_obj = datetime.datetime.strptime(i,"%Y-%m-%d")
                    if(dt_obj > today_date):
                        next_air = dt_obj 
                        flag = 1
                        break
                elif(len(i) == 7):
                    dt_obj = datetime.datetime.strptime(i,"%Y-%m")
                    if(dt_obj > today_date):
                        next_air = dt_obj
                        flag = 2
                        break
                elif(len(i) == 4):
                    dt_obj = datetime.datetime.strptime(i,"%Y")
                    if(dt_obj > today_date):
                        next_air = dt_obj
                        flag = 3
                        break
                else:
                    pass
            # print flag
            if(flag == 4):
                res = "The show has finished streaming all its episodes."
                message.append(res)
                #print res
            elif(flag == 1):
                next_air = str(next_air)
                res = "The next episode airs on " + next_air[0:10] + "."
                message.append(res)
                #print res
            elif(flag == 2):
                next_air = str(next_air)
                res = "The next season begins in " + next_air[0:7] + "."
                message.append(res)
                #print res
            elif(flag == 3):
                next_air = str(next_air)
                res = "The next season begins in " + next_air[0:4] + "."
                message.append(res)
                #print res
            else:
                pass
    
    email_body = ''
    for i in range(len(message)):
        email_body += 'Tv series name: ' + str(shows_name[i].title()) + '\n' + "Status: " + str(message[i]) + '\n' + '\n'
    print email_body
    ut.sendmail(email_id, email_body)
            

if __name__ == '__main__':
    main()