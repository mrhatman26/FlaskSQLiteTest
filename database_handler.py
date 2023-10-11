import sqlite3
import os

def database_start():
    db = sqlite3.connect('local_test.db')
    with open(".\db_commands.sql", "r") as sql_file:
        sql_script = sql_file.read()
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()
    sql_file.close()
    db.close()

def database_read():
    db = sqlite3.connect('local_test.db')
    items = []
    cursor = db.cursor()
    cursor.execute("SELECT * FROM table_staff")
    for item in cursor.fetchall():
        items.append(item)
    db.close()
    return items