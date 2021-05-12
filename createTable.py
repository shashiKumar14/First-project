import sqlite3
import datetime

db= "project14.db"

def getDb():
    connection = sqlite3.connect(db)
    return connection
def createTables():
    tables = "CREATE TABLE IF NOT EXISTS ProjectData(id INTEGER PRIMARY KEY AUTOINCREMENT,ship_name text, Cruise_line text, Age INTEGER , Tonnage REAL,  passengers REAL,  length REAL,  cabins REAL,  passenger_density REAL,   crew REAL, timestamp NOT NULL DEFAULT(datetime('now','localtime')))"
    db = getDb()
    cursor = db.cursor()
    cursor.execute(tables)
