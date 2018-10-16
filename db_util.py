import mysql.connector
import os

db = mysql.connector.connect(
    host=os.getenv('host'), #server address where database is running
    user=os.getenv('user'),      #username to access database
    password=os.getenv('password'),   #password to access database
    port="3306",     #port no of server
    # database="mydatabase" #database name 
) 