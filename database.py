import db_util

def add_to_db(email_id, tvSeriesString):
    cur = db_util.db.cursor()

    try:
        cur.execute('CREATE DATABASE IF NOT EXISTS mydatabase;')
        #print('----DB created----')
    except:
        print('----Error in creating database!!----')

    db_util.db.commit() 

    try:
        q4 = 'USE mydatabase;'
        cur.execute(q4)
        #print('----Using mydatabase----')
    except:
        print('----Error in creating database!!----')


    q2 = 'create table IF NOT EXISTS series (email varchar(100) default NULL, tv varchar(255) default NULL);'
    cur.execute(q2)
    db_util.db.commit()

    q3 = "INSERT INTO series (email, tv) VALUES (%s, %s)"
    cur.execute(q3,(email_id, tvSeriesString))  
    db_util.db.commit()
    #print '----Entries recorded in DB----'

    # Close the connection
    db_util.db.close()