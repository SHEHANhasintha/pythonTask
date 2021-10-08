import os
from mysql.connector import (connection);
from mysql.connector import (errorcode)
from dotenv import load_dotenv;
from os.path import join, dirname

"""
    SqlClass Handler
    This class deals with the sql classes that handles transection and establish connection with DB
"""

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("USERNAME")
DATABASE_PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
DB = os.environ.get("DB")

class Database(object):
    cursor = None;
    conn = None;
    def __init__(self,
                user=SECRET_KEY,
                password=DATABASE_PASSWORD,
                host=HOST,
                database=DB):
        self.user = user;
        self.password = password;
        self.host = host;
        self.database = database;

    # Establish the connection to the database
    def connect(self):
        # handle emergency failure
        try:
            cnx = connection.MySQLConnection(user=self.user,
                                            password=self.password,
                                            host=self.host,
                                            database=self.database)
            self.cursor = cnx.cursor();
            self.conn = cnx
            return cnx
        # if error what to do
        except errorcode as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)       

    # table insertion query
    def insertIntoSqlTable(self,indexNumber, firstName, lastName, location, age):
        # error handling incase of occur
        try:
            # insert statement
            mySql_insert_query = """INSERT INTO userData (firstName, lastName, age, loc, indexNumber) 
                                    VALUES (%s, %s, %s, %s, %s) """
            # ready recode
            record = (firstName, lastName, age, location, indexNumber)
            # tranfer to sql
            self.cursor.execute(mySql_insert_query, record)
            # commit 
            self.conn.commit()
            # intertion status successful feedback
            print("Record inserted successfully into clients table")
            # close the cursor
        except Exception as err:
            print("tranfer failed due to " + str(err))

    # close database connection
    def closeConnection(self):
        if self.conn.is_connected():
            self.cursor.close();
            self.conn.close()
            print("MySQL connection is closed")    



