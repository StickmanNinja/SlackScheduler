import MySQLdb
import os

# Setting database variables.
serverusername = os.getenv("serverusername")
serverpassword = os.getenv("serverpassword")
dbpassword = os.getenv("dbpassword")
dbname = os.getenv("dbname")


def verifySetup():
    # Makes sure table exists. If not, it creates one.
    conn = MySQLdb.connect(serverusername + ".mysql.pythonanywhere-services.com", serverusername, dbpassword, dbname)
    c = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS `users` (id int(11) NOT NULL auto_increment, email TEXT NOT NULL, password TEXT NOT NULL, slackid TEXT NOT NULL, primary key (id))"
    c.execute(sql)

def getPassword(email):
    # Gets password from user account.
    conn = MySQLdb.connect(serverusername + ".mysql.pythonanywhere-services.com", serverusername, dbpassword, dbname)
    c = conn.cursor()
    sql = "SELECT %d FROM users \
          WHERE email '%d'" % ("password", str(email))
    try:
       # Execute the SQL command
       c.execute(sql)
       # Fetch all the rows in a list of lists.
       results = c.fetchall()
       for row in results:
          password = row[0]
          # Now print fetched result
          return str(password)
    except:
       print ("Error: unable to fetch data")

def createUser(email, password, slackid):
    conn = MySQLdb.connect(serverusername + ".mysql.pythonanywhere-services.com", serverusername, dbpassword, dbname)
    c = conn.cursor()
    sql = "INSERT INTO `users`(email,password,slackid) VALUES (%d,%d,%d);" % (email, password, slackid)
    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()
