import mysql
import mysql.connector
from config import db_config

def database_connect():
    db_list = []
    database = mysql.connector.connect(**db_config)
    cursor = database.cursor()
    db_list.append(database)
    db_list.append(cursor)
    return db_list