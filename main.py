
import os
from Database import Database as db
import Helpers as helper
from Datavalidation import validateUsers;
from dotenv import load_dotenv;
from os.path import join, dirname

"""
    main method for the execution

    database initialization
    json read
"""
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("USERNAME")
DATABASE_PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
DB = os.environ.get("DB")

print(SECRET_KEY)

def main():
    dbClients = db(SECRET_KEY, DATABASE_PASSWORD, HOST, DB);
    # connect to database
    dbClients.connect();
    data = helper.JsonRead();
    #catch the errors if any duting the json read
    validateUsers(data,dbClients.insertIntoSqlTable);
    # close the connection
    dbClients.closeConnection();
    

if __name__ == "__main__":
    main()

