import mysql.connector

db = mysql.connector.connect(
    host="localhost", #server address where database is running
    user="root",      #username to access database
    password="123",   #password to access database
    port="3306",      #port no of server
    # database="mydatabase" #database name 
    )