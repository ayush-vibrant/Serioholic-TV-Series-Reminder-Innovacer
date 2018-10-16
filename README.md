# Serioholic: TV-Series Reminder -Innovacer

## This is a project for HackerCamp'19 by Innovaccer: SDE-Intern (Platform)
Please find the problem statement [here](https://www.innovaccer.com/media/hackercamp/SDE-Intern-Assignment.pdf).

# Getting started with the service
1. Install python 2.7.12 from [here] (https://www.python.org/downloads/release/python-2712/)
2. Clone the repository using `git clone -b master https://github.com/ayush-vibrant/Serioholic-TV-Series-Reminder-Innovacer`.
3. Install python-dotenv from [here](https://github.com/theskumar/python-dotenv)
4. For security reasons file with details of database and sender's account credentials is not commited on git. So create a file `.env` in the root folder with the following contents,
```
FROM_EMAIL = 'MY_EMAIL'
PASSWORD = 'MY_EMAIL_PASSWORD'  
host="MY_HOST"
user="MY_USER"     
password="MY_PASSWORD"  

```
5. Run `main.py` to start the project <br />

# Prerequisites
* All the scipts that I have created were tested successfully on **Linux** based OSes with **Python 2.7.12** installed on the system.

## Description
* Aforementioned script requires email address and list of favourite TV series for multiple users as input. The prompt is as follows: <br />
Email address: abc.123@xyz.com <br />
TV Series: Game of thrones, suits, friends, black mirror, gotham <br />
* The script (database.py) stores the input data in `series` table in MySQLdb named `mydatabase`. <br />
* A single email is sent to the input email address with all the
appropriate response for every TV series. The content of the mail 
depends on the following use cases:
1. Exact date is mentioned for next episode.
2. Only year is mentioned for next season.
3. All the seasons are finished and no further details are available. <br />

> Below picture shows the sample e-mail response genereated by the `utility.py`. <br />
<img src="https://github.com/ayush-vibrant/Serioholic-TV-Series-Reminder-Innovacer/blob/master/Images/email_response.png"  />


